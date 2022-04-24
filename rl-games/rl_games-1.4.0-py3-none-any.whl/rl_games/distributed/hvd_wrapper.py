import torch
import horovod.torch as hvd
import os


class HorovodWrapper:
    def __init__(self):
        hvd.init()
        self.rank = hvd.rank()
        self.rank_size = hvd.size()
        print('Starting horovod with rank: {0}, size: {1}'.format(self.rank, self.rank_size))
        #self.device_name = 'cpu'
        self.device_name = 'cuda:' + str(self.rank)

    def update_algo_config(self, config):
        config['device'] = self.device_name
        if self.rank != 0:
            config['print_stats'] = False
            config['lr_schedule'] = None
        return config

    def setup_algo(self, algo):
        hvd.broadcast_parameters(algo.model.state_dict(), root_rank=0)
        hvd.broadcast_optimizer_state(algo.optimizer, root_rank=0)
        algo.optimizer = hvd.DistributedOptimizer(algo.optimizer, named_parameters=algo.model.named_parameters())

        self.sync_stats(algo)

        if algo.has_central_value:
            hvd.broadcast_parameters(algo.central_value_net.model.state_dict(), root_rank=0)
            hvd.broadcast_optimizer_state(algo.central_value_net.optimizer, root_rank=0)

            algo.central_value_net.optimizer = hvd.DistributedOptimizer(algo.central_value_net.optimizer, named_parameters=algo.central_value_net.model.named_parameters())

    # allreduce doesn't work in expected way. need to fix it in the future
    def sync_recursive(self, values, name):
        if isinstance(values, torch.Tensor):
            values.data = hvd.allreduce(values, name=name)
        else:
            for k, v in values.items():
                self.sync_recursive(v, name+'/'+k)

    def sync_stats(self, algo):
        stats_dict = algo.get_stats_weights(model_stats=False)
        #self.sync_recursive(stats_dict, 'stats')
        if algo.normalize_input:
            algo.model.running_mean_std.running_mean = hvd.allreduce(algo.model.running_mean_std.running_mean, 'normalize_input/running_mean')
            algo.model.running_mean_std.running_var = hvd.allreduce(algo.model.running_mean_std.running_var, 'normalize_input/running_var')
        if algo.normalize_value:
            algo.model.value_mean_std.running_mean = hvd.allreduce(algo.model.value_mean_std.running_mean, 'normalize_value/running_mean')
            algo.model.value_mean_std.running_var = hvd.allreduce(algo.model.value_mean_std.running_var, 'normalize_value/running_var')
        if algo.has_central_value:
            cv_net = algo.central_value_net
            if cv_net.normalize_input:
                cv_net.model.running_mean_std.running_mean = hvd.allreduce(cv_net.model.running_mean_std.running_mean, 'cval/normalize_input/running_mean')
                cv_net.model.running_mean_std.running_var = hvd.allreduce(cv_net.model.running_mean_std.running_var, 'cval/normalize_input/running_var')
            if cv_net.normalize_value:
                cv_net.model.value_mean_std.running_mean = hvd.allreduce(cv_net.model.value_mean_std.running_mean, 'cval/normalize_value/running_mean')
                cv_net.model.value_mean_std.running_var = hvd.allreduce(cv_net.model.value_mean_std.running_var, 'cval/normalize_value/running_var')
        algo.curr_frames = hvd.allreduce(torch.tensor(algo.curr_frames), average=False).item()

    def broadcast_value(self, val, name):
        hvd.broadcast_parameters({name: val}, root_rank=0)

    def is_root(self):
        return self.rank == 0

    def average_stats(self, stats_dict):
        res_dict = {}
        for k,v in stats_dict.items():
            res_dict[k] = self.metric_average(v, k)

    def average_value(self, val, name):
        avg_tensor = hvd.allreduce(val, name=name)
        return avg_tensor
