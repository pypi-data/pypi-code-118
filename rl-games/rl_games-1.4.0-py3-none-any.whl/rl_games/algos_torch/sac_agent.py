from rl_games.algos_torch import torch_ext

from rl_games.algos_torch.running_mean_std import RunningMeanStd

from rl_games.common import vecenv
from rl_games.common import schedulers
from rl_games.common import experience
from rl_games.interfaces.base_algorithm import  BaseAlgorithm
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime
from rl_games.algos_torch import  model_builder
from torch import optim
import torch 
from torch import nn
import torch.nn.functional as F
import numpy as np
import time



class SACAgent(BaseAlgorithm):
    def __init__(self, base_name, params):
        self.config = config = params['config']
        print(config)
        # TODO: Get obs shape and self.network
        self.load_networks(params)
        self.base_init(base_name, config)
        self.num_seed_steps = config["num_seed_steps"]
        self.gamma = config["gamma"]
        self.critic_tau = config["critic_tau"]
        self.batch_size = config["batch_size"]
        self.init_alpha = config["init_alpha"]
        self.learnable_temperature = config["learnable_temperature"]
        self.replay_buffer_size = config["replay_buffer_size"]
        self.num_steps_per_episode = config.get("num_steps_per_episode", 1)
        self.normalize_input = config.get("normalize_input", False)

        self.max_env_steps = config.get("max_env_steps", 1000) # temporary, in future we will use other approach

        print(self.batch_size, self.num_actors, self.num_agents)

        self.num_frames_per_epoch = self.num_actors * self.num_steps_per_episode

        self.log_alpha = torch.tensor(np.log(self.init_alpha)).float().to(self.sac_device)
        self.log_alpha.requires_grad = True
        action_space = self.env_info['action_space']
        self.actions_num = action_space.shape[0]

        self.action_range = [
            float(self.env_info['action_space'].low.min()),
            float(self.env_info['action_space'].high.max())
        ]

        obs_shape = torch_ext.shape_whc_to_cwh(self.obs_shape)
        net_config = {
            'obs_dim': self.env_info["observation_space"].shape[0],
            'action_dim': self.env_info["action_space"].shape[0],
            'actions_num' : self.actions_num,
            'input_shape' : obs_shape,
            'normalize_input' : self.normalize_input,
            'normalize_input': self.normalize_input,
        } 
        self.model = self.network.build(net_config)
        self.model.to(self.sac_device)

        print("Number of Agents", self.num_actors, "Batch Size", self.batch_size)

        self.actor_optimizer = torch.optim.Adam(self.model.sac_network.actor.parameters(),
                                                lr=self.config['actor_lr'],
                                                betas=self.config.get("actor_betas", [0.9, 0.999]))

        self.critic_optimizer = torch.optim.Adam(self.model.sac_network.critic.parameters(),
                                                 lr=self.config["critic_lr"],
                                                 betas=self.config.get("critic_betas", [0.9, 0.999]))

        self.log_alpha_optimizer = torch.optim.Adam([self.log_alpha],
                                                    lr=self.config["alpha_lr"],
                                                    betas=self.config.get("alphas_betas", [0.9, 0.999]))

        self.replay_buffer = experience.VectorizedReplayBuffer(self.env_info['observation_space'].shape, 
        self.env_info['action_space'].shape, 
        self.replay_buffer_size, 
        self.sac_device)
        self.target_entropy_coef = config.get("target_entropy_coef", 0.5)
        self.target_entropy = self.target_entropy_coef * -self.env_info['action_space'].shape[0]
        print("Target entropy", self.target_entropy)
        self.step = 0
        self.algo_observer = config['features']['observer']


        # TODO: Is there a better way to get the maximum number of episodes?
        self.max_episodes = torch.ones(self.num_actors, device=self.sac_device)*self.num_steps_per_episode
        # self.episode_lengths = np.zeros(self.num_actors, dtype=int)

    def load_networks(self, params):
        builder = model_builder.ModelBuilder()
        self.config['network'] = builder.load(params)

    def base_init(self, base_name, config):
        self.env_config = config.get('env_config', {})
        self.num_actors = config.get('num_actors', 1)
        self.env_name = config['env_name']
        print("Env name:", self.env_name)

        self.env_info = config.get('env_info')
        if self.env_info is None:
            self.vec_env = vecenv.create_vec_env(self.env_name, self.num_actors, **self.env_config)
            self.env_info = self.vec_env.get_env_info()

        self.sac_device = config.get('device', 'cuda:0')
        #temporary:
        self.ppo_device = self.sac_device
        print('Env info:')
        print(self.env_info)

        self.rewards_shaper = config['reward_shaper']
        self.observation_space = self.env_info['observation_space']
        self.weight_decay = config.get('weight_decay', 0.0)
        #self.use_action_masks = config.get('use_action_masks', False)
        self.is_train = config.get('is_train', True)

        self.c_loss = nn.MSELoss()
        # self.c2_loss = nn.SmoothL1Loss()
        
        self.save_best_after = config.get('save_best_after', 500)
        self.print_stats = config.get('print_stats', True)
        self.rnn_states = None
        self.name = base_name

        self.max_epochs = self.config.get('max_epochs', 1e6)

        self.network = config['network']
        self.rewards_shaper = config['reward_shaper']
        self.num_agents = self.env_info.get('agents', 1)
        self.obs_shape = self.observation_space.shape

        self.games_to_track = self.config.get('games_to_track', 100)
        self.game_rewards = torch_ext.AverageMeter(1, self.games_to_track).to(self.sac_device)
        self.game_lengths = torch_ext.AverageMeter(1, self.games_to_track).to(self.sac_device)
        self.obs = None

        self.min_alpha = torch.tensor(np.log(1)).float().to(self.sac_device)
        
        self.frame = 0
        self.update_time = 0
        self.last_mean_rewards = -100500
        self.play_time = 0
        self.epoch_num = 0
        
        self.writer = SummaryWriter('runs/' + config['name'] + datetime.now().strftime("_%d-%H-%M-%S"))
        print("Run Directory:", config['name'] + datetime.now().strftime("_%d-%H-%M-%S"))
        
        self.is_tensor_obses = None
        self.is_rnn = False
        self.last_rnn_indices = None
        self.last_state_indices = None

    def init_tensors(self):
        if self.observation_space.dtype == np.uint8:
            torch_dtype = torch.uint8
        else:
            torch_dtype = torch.float32
        batch_size = self.num_agents * self.num_actors

        self.current_rewards = torch.zeros(batch_size, dtype=torch.float32, device=self.sac_device)
        self.current_lengths = torch.zeros(batch_size, dtype=torch.long, device=self.sac_device)

        self.dones = torch.zeros((batch_size,), dtype=torch.uint8, device=self.sac_device)
 
    @property
    def alpha(self):
        return self.log_alpha.exp()

    @property
    def device(self):
        return self.sac_device
    
    def get_full_state_weights(self):
        state = self.get_weights()

        state['steps'] = self.step
        state['actor_optimizer'] = self.actor_optimizer.state_dict()
        state['critic_optimizer'] = self.critic_optimizer.state_dict()
        state['log_alpha_optimizer'] = self.log_alpha_optimizer.state_dict()        

        return state

    def get_weights(self):
        state = {'actor': self.model.sac_network.actor.state_dict(),
         'critic': self.model.sac_network.critic.state_dict(), 
         'critic_target': self.model.sac_network.critic_target.state_dict()}
        return state

    def save(self, fn):
        state = self.get_full_state_weights()
        torch_ext.save_checkpoint(fn, state)

    def set_weights(self, weights):
        self.model.sac_network.actor.load_state_dict(weights['actor'])
        self.model.sac_network.critic.load_state_dict(weights['critic'])
        self.model.sac_network.critic_target.load_state_dict(weights['critic_target'])

        if self.normalize_input and 'running_mean_std' in weights:
            self.model.running_mean_std.load_state_dict(weights['running_mean_std'])

    def set_full_state_weights(self, weights):
        self.set_weights(weights)

        self.step = weights['step']
        self.actor_optimizer.load_state_dict(weights['actor_optimizer'])
        self.critic_optimizer.load_state_dict(weights['critic_optimizer'])
        self.log_alpha_optimizer.load_state_dict(weights['log_alpha_optimizer'])

    def restore(self, fn):
        checkpoint = torch_ext.load_checkpoint(fn)
        self.set_full_state_weights(checkpoint)

    def get_masked_action_values(self, obs, action_masks):
        assert False

    def set_eval(self):
        self.model.eval()

    def set_train(self):
        self.model.train()

    def update_critic(self, obs, action, reward, next_obs, not_done,step):
        with torch.no_grad():
            dist = self.model.actor(next_obs)
            next_action = dist.rsample()
            log_prob = dist.log_prob(next_action).sum(-1, keepdim=True)
            target_Q1, target_Q2 = self.model.critic_target(next_obs, next_action)
            target_V = torch.min(target_Q1, target_Q2) - self.alpha * log_prob

            target_Q = reward + (not_done * self.gamma * target_V)
            target_Q = target_Q.detach()

        # get current Q estimates
        current_Q1, current_Q2 = self.model.critic(obs, action)

        critic1_loss = self.c_loss(current_Q1, target_Q)
        critic2_loss = self.c_loss(current_Q2, target_Q)
        critic_loss = critic1_loss + critic2_loss 
        self.critic_optimizer.zero_grad(set_to_none=True)
        critic_loss.backward()
        self.critic_optimizer.step()

        return critic_loss.detach(), critic1_loss.detach(), critic2_loss.detach()

    def update_actor_and_alpha(self, obs, step):
        for p in self.model.sac_network.critic.parameters():
            p.requires_grad = False

        dist = self.model.actor(obs)
        action = dist.rsample()
        log_prob = dist.log_prob(action).sum(-1, keepdim=True)
        entropy = dist.entropy().sum(-1, keepdim=True).mean()
        actor_Q1, actor_Q2 = self.model.critic(obs, action)
        actor_Q = torch.min(actor_Q1, actor_Q2)
        
        actor_loss = (torch.max(self.alpha.detach(), self.min_alpha) * log_prob - actor_Q)
        actor_loss = actor_loss.mean()

        self.actor_optimizer.zero_grad(set_to_none=True)
        actor_loss.backward()
        self.actor_optimizer.step()

        for p in self.model.sac_network.critic.parameters():
            p.requires_grad = True

        if self.learnable_temperature:
            alpha_loss = (self.alpha *
                          (-log_prob - self.target_entropy).detach()).mean()
            self.log_alpha_optimizer.zero_grad(set_to_none=True)
            alpha_loss.backward()
            self.log_alpha_optimizer.step()
        else:
            alpha_loss = None

        return actor_loss.detach(), entropy.detach(), self.alpha.detach(), alpha_loss # TODO: maybe not self.alpha

    def soft_update_params(self, net, target_net, tau):
        for param, target_param in zip(net.parameters(), target_net.parameters()):
            target_param.data.copy_(tau * param.data +
                                    (1 - tau) * target_param.data)

    def update(self, step):
        obs, action, reward, next_obs, done = self.replay_buffer.sample(self.batch_size)
        not_done = ~done

        obs = self.preproc_obs(obs)
        next_obs = self.preproc_obs(next_obs)

        critic_loss, critic1_loss, critic2_loss = self.update_critic(obs, action, reward, next_obs, not_done, step)

        actor_loss, entropy, alpha, alpha_loss = self.update_actor_and_alpha(obs, step)

        actor_loss_info = actor_loss, entropy, alpha, alpha_loss
        self.soft_update_params(self.model.sac_network.critic, self.model.sac_network.critic_target,
                                     self.critic_tau)
        return actor_loss_info, critic1_loss, critic2_loss

    def preproc_obs(self, obs):
        if isinstance(obs, dict):
            obs = obs['obs']
        return obs

    def env_step(self, actions):
        if not self.is_tensor_obses:
            actions = actions.cpu().numpy()
        obs, rewards, dones, infos = self.vec_env.step(actions) # (obs_space) -> (n, obs_space)

        self.step += self.num_actors
        if self.is_tensor_obses:
            return obs, rewards, dones, infos
        else:
            return torch.from_numpy(obs).to(self.sac_device), torch.from_numpy(rewards).to(self.sac_device), torch.from_numpy(dones).to(self.sac_device), infos
    
    def env_reset(self):
        with torch.no_grad():
            obs = self.vec_env.reset()

        if self.is_tensor_obses is None:
            self.is_tensor_obses = torch.is_tensor(obs)
            print("Observations are tensors:", self.is_tensor_obses)
                
        if self.is_tensor_obses:
            return obs.to(self.sac_device)
        else:
            return torch.from_numpy(obs).to(self.sac_device)

    def act(self, obs, action_dim, sample=False):
        obs = self.preproc_obs(obs)
        dist = self.model.actor(obs)
        actions = dist.sample() if sample else dist.mean
        actions = actions.clamp(*self.action_range)
        assert actions.ndim == 2
        return actions

    def extract_actor_stats(self, actor_losses, entropies, alphas, alpha_losses, actor_loss_info):
        actor_loss, entropy, alpha, alpha_loss = actor_loss_info
        
        actor_losses.append(actor_loss)
        entropies.append(entropy)
        if alpha_losses is not None:
            alphas.append(alpha)
            alpha_losses.append(alpha_loss)

    def clear_stats(self):
        self.game_rewards.clear()
        self.game_lengths.clear()
        self.mean_rewards = self.last_mean_rewards = -100500
        self.algo_observer.after_clear_stats()

    def play_steps(self, random_exploration=False):
        total_time_start = time.time()
        total_update_time = 0
        total_time = 0
        step_time = 0.0
        actor_losses = []
        entropies = []
        alphas = []
        alpha_losses = []
        critic1_losses = []
        critic2_losses = []

        obs = self.obs
        for _ in range(self.num_steps_per_episode):
            self.set_eval()
            if random_exploration:
                action = torch.rand((self.num_actors, *self.env_info["action_space"].shape), device=self.sac_device) * 2 - 1
            else:
                with torch.no_grad():
                    action = self.act(obs.float(), self.env_info["action_space"].shape, sample=True)

            step_start = time.time()

            with torch.no_grad():
                next_obs, rewards, dones, infos = self.env_step(action)
            step_end = time.time()

            self.current_rewards += rewards
            self.current_lengths += 1

            total_time += step_end - step_start

            step_time += (step_end - step_start)

            all_done_indices = dones.nonzero(as_tuple=False)
            done_indices = all_done_indices[::self.num_agents]
            self.game_rewards.update(self.current_rewards[done_indices])
            self.game_lengths.update(self.current_lengths[done_indices])

            not_dones = 1.0 - dones.float()

            self.algo_observer.process_infos(infos, done_indices)

            no_timeouts = self.current_lengths != self.max_env_steps
            dones = dones * no_timeouts

            self.current_rewards = self.current_rewards * not_dones
            self.current_lengths = self.current_lengths * not_dones

            if isinstance(obs, dict):
                obs = obs['obs']
            if isinstance(next_obs, dict):    
                next_obs = next_obs['obs']

            rewards = self.rewards_shaper(rewards)

            self.replay_buffer.add(obs, action, torch.unsqueeze(rewards, 1), next_obs, torch.unsqueeze(dones, 1))

            self.obs = obs = next_obs.clone()

            if not random_exploration:
                self.set_train() 
                update_time_start = time.time()
                actor_loss_info, critic1_loss, critic2_loss = self.update(self.epoch_num)
                update_time_end = time.time()
                update_time = update_time_end - update_time_start

                self.extract_actor_stats(actor_losses, entropies, alphas, alpha_losses, actor_loss_info)
                critic1_losses.append(critic1_loss)
                critic2_losses.append(critic2_loss)
            else:
                update_time = 0

            total_update_time += update_time

        total_time_end = time.time()
        total_time = total_time_end - total_time_start
        play_time = total_time - total_update_time

        return step_time, play_time, total_update_time, total_time, actor_losses, entropies, alphas, alpha_losses, critic1_losses, critic2_losses

    def train_epoch(self):
        if self.epoch_num < self.num_seed_steps:
            step_time, play_time, total_update_time, total_time, actor_losses, entropies, alphas, alpha_losses, critic1_losses, critic2_losses = self.play_steps(random_exploration=True)
        else:
            step_time, play_time, total_update_time, total_time, actor_losses, entropies, alphas, alpha_losses, critic1_losses, critic2_losses = self.play_steps(random_exploration=False)

        return step_time, play_time, total_update_time, total_time, actor_losses, entropies, alphas, alpha_losses, critic1_losses, critic2_losses

    def train(self):
        self.init_tensors()
        self.algo_observer.after_init(self)
        self.last_mean_rewards = -100500
        total_time = 0
        # rep_count = 0
        self.frame = 0
        self.obs = self.env_reset()

        while True:
            self.epoch_num += 1
            step_time, play_time, update_time, epoch_total_time, actor_losses, entropies, alphas, alpha_losses, critic1_losses, critic2_losses = self.train_epoch()

            total_time += epoch_total_time

            scaled_time = epoch_total_time
            scaled_play_time = play_time
            curr_frames = self.num_frames_per_epoch
            self.frame += curr_frames
            frame = self.frame #TODO: Fix frame
            # print(frame)

            if self.print_stats:
                fps_step = curr_frames / scaled_play_time
                fps_total = curr_frames / scaled_time
                print(f'fps step: {fps_step:.1f} fps total: {fps_total:.1f}')

            self.writer.add_scalar('performance/step_inference_rl_update_fps', curr_frames / scaled_time, frame)
            self.writer.add_scalar('performance/step_inference_fps', curr_frames / scaled_play_time, frame)
            self.writer.add_scalar('performance/step_fps', curr_frames / step_time, frame)
            self.writer.add_scalar('performance/rl_update_time', update_time, frame)
            self.writer.add_scalar('performance/step_inference_time', play_time, frame)
            self.writer.add_scalar('performance/step_time', step_time, frame)

            if self.epoch_num >= self.num_seed_steps:
                self.writer.add_scalar('losses/a_loss', torch_ext.mean_list(actor_losses).item(), frame)
                self.writer.add_scalar('losses/c1_loss', torch_ext.mean_list(critic1_losses).item(), frame)
                self.writer.add_scalar('losses/c2_loss', torch_ext.mean_list(critic2_losses).item(), frame)
                self.writer.add_scalar('losses/entropy', torch_ext.mean_list(entropies).item(), frame)
                if alpha_losses[0] is not None:
                    self.writer.add_scalar('losses/alpha_loss', torch_ext.mean_list(alpha_losses).item(), frame)
                self.writer.add_scalar('info/alpha', torch_ext.mean_list(alphas).item(), frame)

            self.writer.add_scalar('info/epochs', self.epoch_num, frame)
            self.algo_observer.after_print_stats(frame, self.epoch_num, total_time)

            if self.game_rewards.current_size > 0:
                mean_rewards = self.game_rewards.get_mean()
                mean_lengths = self.game_lengths.get_mean()

                self.writer.add_scalar('rewards/step', mean_rewards, frame)
                # self.writer.add_scalar('rewards/iter', mean_rewards, epoch_num)
                self.writer.add_scalar('rewards/time', mean_rewards, total_time)
                self.writer.add_scalar('episode_lengths/step', mean_lengths, frame)
                # self.writer.add_scalar('episode_lengths/iter', mean_lengths, epoch_num)
                self.writer.add_scalar('episode_lengths/time', mean_lengths, total_time)

                if mean_rewards > self.last_mean_rewards and self.epoch_num >= self.save_best_after:
                    print('saving next best rewards: ', mean_rewards)
                    self.last_mean_rewards = mean_rewards
                    self.save("./nn/" + self.config['name'])
                    if self.last_mean_rewards > self.config.get('score_to_win', float('inf')):
                        print('Network won!')
                        self.save("./nn/" + self.config['name'] + 'ep=' + str(self.epoch_num) + 'rew=' + str(mean_rewards))
                        return self.last_mean_rewards, self.epoch_num

                if self.epoch_num > self.max_epochs:
                    self.save("./nn/" + 'last_' + self.config['name'] + 'ep=' + str(self.epoch_num) + 'rew=' + str(mean_rewards))
                    print('MAX EPOCHS NUM!')
                    return self.last_mean_rewards, self.epoch_num                               
                update_time = 0

    