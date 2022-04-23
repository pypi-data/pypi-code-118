
import imp
from yacs.config import CfgNode as CN
from alfred.utils.base_config import Config as BaseConfig
import socket
import numpy as np
import os


class Config(BaseConfig):
    @staticmethod
    def init(cfg):
        # input and output
        cfg.host = 'auto'
        cfg.port = 9999
        cfg.width = 1920
        cfg.height = 1080

        cfg.max_human = 5
        cfg.filter = True
        cfg.track = True
        cfg.block = True  # block visualization or not, True for visualize each frame, False in realtime applications
        cfg.rotate = False
        cfg.debug = False
        cfg.write = False
        cfg.out = './results'
        # scene:
        cfg.scene_module = "alfred.vis.mesh3d.o3dwrapper"
        cfg.scene = []

        cfg.extra = CN()
        cfg.range = CN()
        cfg.new_frames = 0

        # skel
        cfg.skel = CN()
        cfg.skel.joint_radius = 0.02
        cfg.body_model_template = "none"
        # camera
        cfg.camera = CN()
        cfg.camera.phi = 0
        cfg.camera.theta = -90 + 60
        cfg.camera.cx = 0.
        cfg.camera.cy = 0.
        cfg.camera.cz = 6.
        cfg.camera.set_camera = False
        cfg.camera.camera_pose = []
        # range
        cfg.range = CN()
        cfg.range.minr = [-100, -100, -10]
        cfg.range.maxr = [100,  100,  10]
        cfg.range.rate_inlier = 0.8
        cfg.range.min_conf = 0.1

        cfg.body_model = CN()
        cfg.body_model.module = 'alfred.vis.mesh3d.skelmodel.SkelModel'
        cfg.body_model.args = CN()
        cfg.body_model.args.body_type = "body25"
        cfg.body_model.args.joint_radius = 0.02
        return cfg

    @staticmethod
    def parse(cfg):
        if cfg.host == 'auto':
            # cfg.host = socket.gethostname()
            cfg.host = '127.0.0.1'
        if cfg.camera.set_camera:
            pass
        else:  # use default camera
            # theta, phi = cfg.camera.theta, cfg.camera.phi
            theta, phi = np.deg2rad(
                cfg.camera.theta), np.deg2rad(cfg.camera.phi)
            cx, cy, cz = cfg.camera.cx, cfg.camera.cy, cfg.camera.cz
            st, ct = np.sin(theta), np.cos(theta)
            sp, cp = np.sin(phi), np.cos(phi)
            dist = 6
            camera_pose = np.array([
                [cp, -st*sp, ct*sp, cx],
                [sp, st*cp, -ct*cp, cy],
                [0., ct, st, cz],
                [0.0, 0.0, 0.0, 1.0]])
            cfg.camera.camera_pose = camera_pose.tolist()


def get_default_visconfig():
    crt_dir = os.path.dirname(__file__)
    cfg = Config.load(
        filename=os.path.join(crt_dir, 'default_viscfg.yml'))
    return cfg


'''
Global Config of sketlon

'''


CONFIG = {}

CONFIG['smpl'] = {'nJoints': 24, 'kintree':
                  [
                      [0, 1],
                      [0, 2],
                      [0, 3],
                      [1, 4],
                      [2, 5],
                      [3, 6],
                      [4, 7],
                      [5, 8],
                      [6, 9],
                      [7, 10],
                      [8, 11],
                      [9, 12],
                      [9, 13],
                      [9, 14],
                      [12, 15],
                      [13, 16],
                      [14, 17],
                      [16, 18],
                      [17, 19],
                      [18, 20],
                      [19, 21],
                      [20, 22],
                      [21, 23],
                  ],
                  # order like: https://github.com/YeeCY/SMPLpp/blob/master/docs/media/kinematic_tree.png
                  'joint_names': [
                      'MidHip',            # 0
                      'LUpLeg',       # 1
                      'RUpLeg',      # 2
                      'spine',           # 3
                      'LLeg',         # 4
                      'RLeg',        # 5
                      'spine1',          # 6
                      'LFoot',        # 7
                      'RFoot',       # 8
                      'spine2',          # 9
                      'LToeBase',     # 10
                      'RToeBase',    # 11
                      'neck',            # 12
                      'LShoulder',    # 13
                      'RShoulder',   # 14
                      'head',            # 15
                      'LArm',         # 16
                      'RArm',        # 17
                      'LForeArm',     # 18
                      'RForeArm',    # 19
                      'LHand',        # 20
                      'RHand',       # 21
                      'LHandIndex1',  # 22
                      'RHandIndex1',  # 23
                  ]
                  }

CONFIG['body25'] = {'nJoints': 25, 'kintree':
                    [[1,  0],
                     [2,  1],
                        [3,  2],
                        [4,  3],
                        [5,  1],
                        [6,  5],
                        [7,  6],
                        [8,  1],
                        [9,  8],
                        [10,  9],
                        [11, 10],
                        [12,  8],
                        [13, 12],
                        [14, 13],
                        [15,  0],
                        [16,  0],
                        [17, 15],
                        [18, 16],
                        [19, 14],
                        [20, 19],
                        [21, 14],
                        [22, 11],
                        [23, 22],
                        [24, 11]],
                    'joint_names': [
                        "Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe", "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel"]}
CONFIG['body25']['kintree_order'] = [
    [1, 8],  # 躯干放在最前面
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 5],
    [5, 6],
    [6, 7],
    [8, 9],
    [8, 12],
    [9, 10],
    [10, 11],
    [12, 13],
    [13, 14],
    [1, 0],
    [0, 15],
    [0, 16],
    [15, 17],
    [16, 18],
    [11, 22],
    [11, 24],
    [22, 23],
    [14, 19],
    [19, 20],
    [14, 21]
]
CONFIG['body25']['colors'] = ['k', 'r', 'r', 'r', 'b', 'b', 'b', 'k', 'r',
                              'r', 'r', 'b', 'b', 'b', 'r', 'b', 'r', 'b', 'b', 'b', 'b', 'r', 'r', 'r']
CONFIG['body25']['skeleton'] = \
    {
    (0,  1): {'mean': 0.228, 'std': 0.046},  # Nose     ->Neck
    (1,  2): {'mean': 0.144, 'std': 0.029},  # Neck     ->RShoulder
    (2,  3): {'mean': 0.283, 'std': 0.057},  # RShoulder->RElbow
    (3,  4): {'mean': 0.258, 'std': 0.052},  # RElbow   ->RWrist
    (1,  5): {'mean': 0.145, 'std': 0.029},  # Neck     ->LShoulder
    (5,  6): {'mean': 0.281, 'std': 0.056},  # LShoulder->LElbow
    (6,  7): {'mean': 0.258, 'std': 0.052},  # LElbow   ->LWrist
    (1,  8): {'mean': 0.483, 'std': 0.097},  # Neck     ->MidHip
    (8,  9): {'mean': 0.106, 'std': 0.021},  # MidHip   ->RHip
    (9, 10): {'mean': 0.438, 'std': 0.088},  # RHip     ->RKnee
    (10, 11): {'mean': 0.406, 'std': 0.081},  # RKnee    ->RAnkle
    (8, 12): {'mean': 0.106, 'std': 0.021},  # MidHip   ->LHip
    (12, 13): {'mean': 0.438, 'std': 0.088},  # LHip     ->LKnee
    (13, 14): {'mean': 0.408, 'std': 0.082},  # LKnee    ->LAnkle
    (0, 15): {'mean': 0.043, 'std': 0.009},  # Nose     ->REye
    (0, 16): {'mean': 0.043, 'std': 0.009},  # Nose     ->LEye
    (15, 17): {'mean': 0.105, 'std': 0.021},  # REye     ->REar
    (16, 18): {'mean': 0.104, 'std': 0.021},  # LEye     ->LEar
    (14, 19): {'mean': 0.180, 'std': 0.036},  # LAnkle   ->LBigToe
    (19, 20): {'mean': 0.038, 'std': 0.008},  # LBigToe  ->LSmallToe
    (14, 21): {'mean': 0.044, 'std': 0.009},  # LAnkle   ->LHeel
    (11, 22): {'mean': 0.182, 'std': 0.036},  # RAnkle   ->RBigToe
    (22, 23): {'mean': 0.038, 'std': 0.008},  # RBigToe  ->RSmallToe
    (11, 24): {'mean': 0.044, 'std': 0.009},  # RAnkle   ->RHeel
}

CONFIG['body15'] = {'nJoints': 15, 'kintree':
                    [[1,  0],
                     [2,  1],
                        [3,  2],
                        [4,  3],
                        [5,  1],
                        [6,  5],
                        [7,  6],
                        [8,  1],
                        [9,  8],
                        [10,  9],
                        [11, 10],
                        [12,  8],
                        [13, 12],
                        [14, 13], ]}
CONFIG['body15']['joint_names'] = CONFIG['body25']['joint_names'][:15]
CONFIG['body15']['skeleton'] = {
    key: val for key, val in CONFIG['body25']['skeleton'].items() if key[0] < 15 and key[1] < 15}
CONFIG['body15']['kintree_order'] = CONFIG['body25']['kintree_order'][:14]
CONFIG['body15']['colors'] = CONFIG['body25']['colors'][:15]

CONFIG['panoptic'] = {
    'nJoints': 19,
    'joint_names': ['Neck', 'Nose', 'MidHip', 'LShoulder', 'LElbow', 'LWrist', 'LHip', 'LKnee', 'LAnkle', 'RShoulder', 'RElbow', 'RWrist', 'RHip', 'RKnee', 'RAnkle', 'LEye', 'LEar', 'REye', 'REar']
}

CONFIG['hand'] = {'kintree':
                  [[1,  0],
                   [2,  1],
                      [3,  2],
                      [4,  3],
                      [5,  0],
                      [6,  5],
                      [7,  6],
                      [8,  7],
                      [9,  0],
                      [10,  9],
                      [11, 10],
                      [12, 11],
                      [13,  0],
                      [14, 13],
                      [15, 14],
                      [16, 15],
                      [17,  0],
                      [18, 17],
                      [19, 18],
                      [20, 19]],
                  'colors': [
                      'k', 'k', 'k', 'k', 'r', 'r', 'r', 'r',
                      'g', 'g', 'g', 'g', 'b', 'b', 'b', 'b',
                      'y', 'y', 'y', 'y']
                  }

CONFIG['handl'] = CONFIG['hand']
CONFIG['handr'] = CONFIG['hand']

CONFIG['bodyhand'] = {'kintree':
                      [[1,  0],
                       [2,  1],
                          [3,  2],
                          [4,  3],
                          [5,  1],
                          [6,  5],
                          [7,  6],
                          [8,  1],
                          [9,  8],
                          [10,  9],
                          [11, 10],
                          [12,  8],
                          [13, 12],
                          [14, 13],
                          [15,  0],
                          [16,  0],
                          [17, 15],
                          [18, 16],
                          [19, 14],
                          [20, 19],
                          [21, 14],
                          [22, 11],
                          [23, 22],
                          [24, 11],
                          [26,  7],  # handl
                          [27, 26],
                          [28, 27],
                          [29, 28],
                          [30,  7],
                          [31, 30],
                          [32, 31],
                          [33, 32],
                          [34,  7],
                          [35, 34],
                          [36, 35],
                          [37, 36],
                          [38,  7],
                          [39, 38],
                          [40, 39],
                          [41, 40],
                          [42,  7],
                          [43, 42],
                          [44, 43],
                          [45, 44],
                          [47,  4],  # handr
                          [48, 47],
                          [49, 48],
                          [50, 49],
                          [51,  4],
                          [52, 51],
                          [53, 52],
                          [54, 53],
                          [55,  4],
                          [56, 55],
                          [57, 56],
                          [58, 57],
                          [59,  4],
                          [60, 59],
                          [61, 60],
                          [62, 61],
                          [63,  4],
                          [64, 63],
                          [65, 64],
                          [66, 65]
                       ],
                      'nJoints': 67,
                      'skeleton': {
                          (0,  1): {'mean': 0.251, 'std': 0.050},
                          (1,  2): {'mean': 0.169, 'std': 0.034},
                          (2,  3): {'mean': 0.292, 'std': 0.058},
                          (3,  4): {'mean': 0.275, 'std': 0.055},
                          (1,  5): {'mean': 0.169, 'std': 0.034},
                          (5,  6): {'mean': 0.295, 'std': 0.059},
                          (6,  7): {'mean': 0.278, 'std': 0.056},
                          (1,  8): {'mean': 0.566, 'std': 0.113},
                          (8,  9): {'mean': 0.110, 'std': 0.022},
                          (9, 10): {'mean': 0.398, 'std': 0.080},
                          (10, 11): {'mean': 0.402, 'std': 0.080},
                          (8, 12): {'mean': 0.111, 'std': 0.022},
                          (12, 13): {'mean': 0.395, 'std': 0.079},
                          (13, 14): {'mean': 0.403, 'std': 0.081},
                          (0, 15): {'mean': 0.053, 'std': 0.011},
                          (0, 16): {'mean': 0.056, 'std': 0.011},
                          (15, 17): {'mean': 0.107, 'std': 0.021},
                          (16, 18): {'mean': 0.107, 'std': 0.021},
                          (14, 19): {'mean': 0.180, 'std': 0.036},
                          (19, 20): {'mean': 0.055, 'std': 0.011},
                          (14, 21): {'mean': 0.065, 'std': 0.013},
                          (11, 22): {'mean': 0.169, 'std': 0.034},
                          (22, 23): {'mean': 0.052, 'std': 0.010},
                          (11, 24): {'mean': 0.061, 'std': 0.012},
                          (7, 26): {'mean': 0.045, 'std': 0.009},
                          (26, 27): {'mean': 0.042, 'std': 0.008},
                          (27, 28): {'mean': 0.035, 'std': 0.007},
                          (28, 29): {'mean': 0.029, 'std': 0.006},
                          (7, 30): {'mean': 0.102, 'std': 0.020},
                          (30, 31): {'mean': 0.040, 'std': 0.008},
                          (31, 32): {'mean': 0.026, 'std': 0.005},
                          (32, 33): {'mean': 0.023, 'std': 0.005},
                          (7, 34): {'mean': 0.101, 'std': 0.020},
                          (34, 35): {'mean': 0.043, 'std': 0.009},
                          (35, 36): {'mean': 0.029, 'std': 0.006},
                          (36, 37): {'mean': 0.024, 'std': 0.005},
                          (7, 38): {'mean': 0.097, 'std': 0.019},
                          (38, 39): {'mean': 0.041, 'std': 0.008},
                          (39, 40): {'mean': 0.027, 'std': 0.005},
                          (40, 41): {'mean': 0.024, 'std': 0.005},
                          (7, 42): {'mean': 0.095, 'std': 0.019},
                          (42, 43): {'mean': 0.033, 'std': 0.007},
                          (43, 44): {'mean': 0.020, 'std': 0.004},
                          (44, 45): {'mean': 0.018, 'std': 0.004},
                          (4, 47): {'mean': 0.043, 'std': 0.009},
                          (47, 48): {'mean': 0.041, 'std': 0.008},
                          (48, 49): {'mean': 0.034, 'std': 0.007},
                          (49, 50): {'mean': 0.028, 'std': 0.006},
                          (4, 51): {'mean': 0.101, 'std': 0.020},
                          (51, 52): {'mean': 0.041, 'std': 0.008},
                          (52, 53): {'mean': 0.026, 'std': 0.005},
                          (53, 54): {'mean': 0.024, 'std': 0.005},
                          (4, 55): {'mean': 0.100, 'std': 0.020},
                          (55, 56): {'mean': 0.044, 'std': 0.009},
                          (56, 57): {'mean': 0.029, 'std': 0.006},
                          (57, 58): {'mean': 0.023, 'std': 0.005},
                          (4, 59): {'mean': 0.096, 'std': 0.019},
                          (59, 60): {'mean': 0.040, 'std': 0.008},
                          (60, 61): {'mean': 0.028, 'std': 0.006},
                          (61, 62): {'mean': 0.023, 'std': 0.005},
                          (4, 63): {'mean': 0.094, 'std': 0.019},
                          (63, 64): {'mean': 0.032, 'std': 0.006},
                          (64, 65): {'mean': 0.020, 'std': 0.004},
                          (65, 66): {'mean': 0.018, 'std': 0.004},
                      }
                      }

CONFIG['bodyhandface'] = {'kintree':
                          [[1,  0],
                           [2,  1],
                              [3,  2],
                              [4,  3],
                              [5,  1],
                              [6,  5],
                              [7,  6],
                              [8,  1],
                              [9,  8],
                              [10,  9],
                              [11, 10],
                              [12,  8],
                              [13, 12],
                              [14, 13],
                              [15,  0],
                              [16,  0],
                              [17, 15],
                              [18, 16],
                              [19, 14],
                              [20, 19],
                              [21, 14],
                              [22, 11],
                              [23, 22],
                              [24, 11],
                              [26,  7],  # handl
                              [27, 26],
                              [28, 27],
                              [29, 28],
                              [30,  7],
                              [31, 30],
                              [32, 31],
                              [33, 32],
                              [34,  7],
                              [35, 34],
                              [36, 35],
                              [37, 36],
                              [38,  7],
                              [39, 38],
                              [40, 39],
                              [41, 40],
                              [42,  7],
                              [43, 42],
                              [44, 43],
                              [45, 44],
                              [47,  4],  # handr
                              [48, 47],
                              [49, 48],
                              [50, 49],
                              [51,  4],
                              [52, 51],
                              [53, 52],
                              [54, 53],
                              [55,  4],
                              [56, 55],
                              [57, 56],
                              [58, 57],
                              [59,  4],
                              [60, 59],
                              [61, 60],
                              [62, 61],
                              [63,  4],
                              [64, 63],
                              [65, 64],
                              [66, 65],
                              [67,  68],
                              [68,  69],
                              [69,  70],
                              [70,  71],
                              [72,  73],
                              [73,  74],
                              [74,  75],
                              [75,  76],
                              [77,  78],
                              [78,  79],
                              [79,  80],
                              [81,  82],
                              [82,  83],
                              [83,  84],
                              [84,  85],
                              [86,  87],
                              [87,  88],
                              [88,  89],
                              [89,  90],
                              [90,  91],
                              [91,  86],
                              [92,  93],
                              [93,  94],
                              [94,  95],
                              [95,  96],
                              [96,  97],
                              [97,  92],
                              [98,  99],
                              [99, 100],
                              [100, 101],
                              [101, 102],
                              [102, 103],
                              [103, 104],
                              [104, 105],
                              [105, 106],
                              [106, 107],
                              [107, 108],
                              [108, 109],
                              [109,  98],
                              [110, 111],
                              [111, 112],
                              [112, 113],
                              [113, 114],
                              [114, 115],
                              [115, 116],
                              [116, 117],
                              [117, 110]
                           ],
                          'nJoints': 118,
                          'skeleton': {
                              (0,  1): {'mean': 0.251, 'std': 0.050},
                              (1,  2): {'mean': 0.169, 'std': 0.034},
                              (2,  3): {'mean': 0.292, 'std': 0.058},
                              (3,  4): {'mean': 0.275, 'std': 0.055},
                              (1,  5): {'mean': 0.169, 'std': 0.034},
                              (5,  6): {'mean': 0.295, 'std': 0.059},
                              (6,  7): {'mean': 0.278, 'std': 0.056},
                              (1,  8): {'mean': 0.566, 'std': 0.113},
                              (8,  9): {'mean': 0.110, 'std': 0.022},
                              (9, 10): {'mean': 0.398, 'std': 0.080},
                              (10, 11): {'mean': 0.402, 'std': 0.080},
                              (8, 12): {'mean': 0.111, 'std': 0.022},
                              (12, 13): {'mean': 0.395, 'std': 0.079},
                              (13, 14): {'mean': 0.403, 'std': 0.081},
                              (0, 15): {'mean': 0.053, 'std': 0.011},
                              (0, 16): {'mean': 0.056, 'std': 0.011},
                              (15, 17): {'mean': 0.107, 'std': 0.021},
                              (16, 18): {'mean': 0.107, 'std': 0.021},
                              (14, 19): {'mean': 0.180, 'std': 0.036},
                              (19, 20): {'mean': 0.055, 'std': 0.011},
                              (14, 21): {'mean': 0.065, 'std': 0.013},
                              (11, 22): {'mean': 0.169, 'std': 0.034},
                              (22, 23): {'mean': 0.052, 'std': 0.010},
                              (11, 24): {'mean': 0.061, 'std': 0.012},
                              (7, 26): {'mean': 0.045, 'std': 0.009},
                              (26, 27): {'mean': 0.042, 'std': 0.008},
                              (27, 28): {'mean': 0.035, 'std': 0.007},
                              (28, 29): {'mean': 0.029, 'std': 0.006},
                              (7, 30): {'mean': 0.102, 'std': 0.020},
                              (30, 31): {'mean': 0.040, 'std': 0.008},
                              (31, 32): {'mean': 0.026, 'std': 0.005},
                              (32, 33): {'mean': 0.023, 'std': 0.005},
                              (7, 34): {'mean': 0.101, 'std': 0.020},
                              (34, 35): {'mean': 0.043, 'std': 0.009},
                              (35, 36): {'mean': 0.029, 'std': 0.006},
                              (36, 37): {'mean': 0.024, 'std': 0.005},
                              (7, 38): {'mean': 0.097, 'std': 0.019},
                              (38, 39): {'mean': 0.041, 'std': 0.008},
                              (39, 40): {'mean': 0.027, 'std': 0.005},
                              (40, 41): {'mean': 0.024, 'std': 0.005},
                              (7, 42): {'mean': 0.095, 'std': 0.019},
                              (42, 43): {'mean': 0.033, 'std': 0.007},
                              (43, 44): {'mean': 0.020, 'std': 0.004},
                              (44, 45): {'mean': 0.018, 'std': 0.004},
                              (4, 47): {'mean': 0.043, 'std': 0.009},
                              (47, 48): {'mean': 0.041, 'std': 0.008},
                              (48, 49): {'mean': 0.034, 'std': 0.007},
                              (49, 50): {'mean': 0.028, 'std': 0.006},
                              (4, 51): {'mean': 0.101, 'std': 0.020},
                              (51, 52): {'mean': 0.041, 'std': 0.008},
                              (52, 53): {'mean': 0.026, 'std': 0.005},
                              (53, 54): {'mean': 0.024, 'std': 0.005},
                              (4, 55): {'mean': 0.100, 'std': 0.020},
                              (55, 56): {'mean': 0.044, 'std': 0.009},
                              (56, 57): {'mean': 0.029, 'std': 0.006},
                              (57, 58): {'mean': 0.023, 'std': 0.005},
                              (4, 59): {'mean': 0.096, 'std': 0.019},
                              (59, 60): {'mean': 0.040, 'std': 0.008},
                              (60, 61): {'mean': 0.028, 'std': 0.006},
                              (61, 62): {'mean': 0.023, 'std': 0.005},
                              (4, 63): {'mean': 0.094, 'std': 0.019},
                              (63, 64): {'mean': 0.032, 'std': 0.006},
                              (64, 65): {'mean': 0.020, 'std': 0.004},
                              (65, 66): {'mean': 0.018, 'std': 0.004},
                              (67, 68): {'mean': 0.012, 'std': 0.002},
                              (68, 69): {'mean': 0.013, 'std': 0.003},
                              (69, 70): {'mean': 0.014, 'std': 0.003},
                              (70, 71): {'mean': 0.012, 'std': 0.002},
                              (72, 73): {'mean': 0.014, 'std': 0.003},
                              (73, 74): {'mean': 0.014, 'std': 0.003},
                              (74, 75): {'mean': 0.015, 'std': 0.003},
                              (75, 76): {'mean': 0.013, 'std': 0.003},
                              (77, 78): {'mean': 0.014, 'std': 0.003},
                              (78, 79): {'mean': 0.014, 'std': 0.003},
                              (79, 80): {'mean': 0.015, 'std': 0.003},
                              (81, 82): {'mean': 0.009, 'std': 0.002},
                              (82, 83): {'mean': 0.010, 'std': 0.002},
                              (83, 84): {'mean': 0.010, 'std': 0.002},
                              (84, 85): {'mean': 0.010, 'std': 0.002},
                              (86, 87): {'mean': 0.009, 'std': 0.002},
                              (87, 88): {'mean': 0.009, 'std': 0.002},
                              (88, 89): {'mean': 0.008, 'std': 0.002},
                              (89, 90): {'mean': 0.008, 'std': 0.002},
                              (90, 91): {'mean': 0.009, 'std': 0.002},
                              (86, 91): {'mean': 0.008, 'std': 0.002},
                              (92, 93): {'mean': 0.009, 'std': 0.002},
                              (93, 94): {'mean': 0.009, 'std': 0.002},
                              (94, 95): {'mean': 0.009, 'std': 0.002},
                              (95, 96): {'mean': 0.009, 'std': 0.002},
                              (96, 97): {'mean': 0.009, 'std': 0.002},
                              (92, 97): {'mean': 0.009, 'std': 0.002},
                              (98, 99): {'mean': 0.016, 'std': 0.003},
                              (99, 100): {'mean': 0.013, 'std': 0.003},
                              (100, 101): {'mean': 0.008, 'std': 0.002},
                              (101, 102): {'mean': 0.008, 'std': 0.002},
                              (102, 103): {'mean': 0.012, 'std': 0.002},
                              (103, 104): {'mean': 0.014, 'std': 0.003},
                              (104, 105): {'mean': 0.015, 'std': 0.003},
                              (105, 106): {'mean': 0.012, 'std': 0.002},
                              (106, 107): {'mean': 0.009, 'std': 0.002},
                              (107, 108): {'mean': 0.009, 'std': 0.002},
                              (108, 109): {'mean': 0.013, 'std': 0.003},
                              (98, 109): {'mean': 0.016, 'std': 0.003},
                              (110, 111): {'mean': 0.021, 'std': 0.004},
                              (111, 112): {'mean': 0.009, 'std': 0.002},
                              (112, 113): {'mean': 0.008, 'std': 0.002},
                              (113, 114): {'mean': 0.019, 'std': 0.004},
                              (114, 115): {'mean': 0.018, 'std': 0.004},
                              (115, 116): {'mean': 0.008, 'std': 0.002},
                              (116, 117): {'mean': 0.009, 'std': 0.002},
                              (110, 117): {'mean': 0.020, 'std': 0.004},
                          }
                          }

face_kintree_without_contour = [[0,  1],
                                [1,  2],
                                [2,  3],
                                [3,  4],
                                [5,  6],
                                [6,  7],
                                [7,  8],
                                [8,  9],
                                [10, 11],
                                [11, 12],
                                [12, 13],
                                [14, 15],
                                [15, 16],
                                [16, 17],
                                [17, 18],
                                [19, 20],
                                [20, 21],
                                [21, 22],
                                [22, 23],
                                [23, 24],
                                [24, 19],
                                [25, 26],
                                [26, 27],
                                [27, 28],
                                [28, 29],
                                [29, 30],
                                [30, 25],
                                [31, 32],
                                [32, 33],
                                [33, 34],
                                [34, 35],
                                [35, 36],
                                [36, 37],
                                [37, 38],
                                [38, 39],
                                [39, 40],
                                [40, 41],
                                [41, 42],
                                [42, 31],
                                [43, 44],
                                [44, 45],
                                [45, 46],
                                [46, 47],
                                [47, 48],
                                [48, 49],
                                [49, 50],
                                [50, 43]]

CONFIG['face'] = {'kintree': [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16],  # outline (ignored)
                              [17, 18], [18, 19], [19, 20], [
    20, 21],  # right eyebrow
    [22, 23], [23, 24], [24, 25], [
    25, 26],  # left eyebrow
    [27, 28], [28, 29], [29, 30],  # nose upper part
    [31, 32], [32, 33], [33, 34], [
    34, 35],  # nose lower part
    [36, 37], [37, 38], [38, 39], [39, 40], [
    40, 41], [41, 36],  # right eye
    [42, 43], [43, 44], [44, 45], [45, 46], [
    46, 47], [47, 42],  # left eye
    [48, 49], [49, 50], [50, 51], [51, 52], [52, 53], [53, 54], [54, 55], [
        55, 56], [56, 57], [57, 58], [58, 59], [59, 48],  # Lip outline
    [60, 61], [61, 62], [62, 63], [63, 64], [64, 65], [
    65, 66], [66, 67], [67, 60]  # Lip inner line
], 'colors': ['g' for _ in range(100)]}

CONFIG['h36m'] = {
    'kintree': [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [0, 7], [7, 8], [8, 9], [9, 10], [8, 11], [11, 12], [
        12, 13], [8, 14], [14, 15], [15, 16]],
    'color': ['r', 'r', 'r', 'g', 'g', 'g', 'k', 'k', 'k', 'k', 'g', 'g', 'g', 'r', 'r', 'r'],
    'joint_names': [
        'hip',  # 0
        'LHip',  # 1
        'LKnee',  # 2
        'LAnkle',  # 3
        'RHip',  # 4
        'RKnee',  # 5
        'RAnkle',  # 6
        'Spine (H36M)',  # 7
        'Neck',  # 8
        'Head (H36M)',  # 9
        'headtop',  # 10
        'LShoulder',  # 11
        'LElbow',  # 12
        'LWrist',  # 13
        'RShoulder',  # 14
        'RElbow',  # 15
        'RWrist',  # 16
    ],
    'nJoints': 17}

NJOINTS_BODY = 25
NJOINTS_HAND = 21
NJOINTS_FACE = 70
NLIMBS_BODY = len(CONFIG['body25']['kintree'])
NLIMBS_HAND = len(CONFIG['hand']['kintree'])
NLIMBS_FACE = len(CONFIG['face']['kintree'])


def getKintree(name='total'):
    if name == 'total':
        # order: body25, face, rhand, lhand
        kintree = CONFIG['body25']['kintree'] + CONFIG['hand']['kintree'] + \
            CONFIG['hand']['kintree'] + CONFIG['face']['kintree']
        kintree = np.array(kintree)
        kintree[NLIMBS_BODY:NLIMBS_BODY + NLIMBS_HAND] += NJOINTS_BODY
        kintree[NLIMBS_BODY + NLIMBS_HAND:NLIMBS_BODY +
                2*NLIMBS_HAND] += NJOINTS_BODY + NJOINTS_HAND
        kintree[NLIMBS_BODY + 2*NLIMBS_HAND:] += NJOINTS_BODY + 2*NJOINTS_HAND
    elif name == 'smplh':
        # order: body25, lhand, rhand
        kintree = CONFIG['body25']['kintree'] + \
            CONFIG['hand']['kintree'] + CONFIG['hand']['kintree']
        kintree = np.array(kintree)
        kintree[NLIMBS_BODY:NLIMBS_BODY + NLIMBS_HAND] += NJOINTS_BODY
        kintree[NLIMBS_BODY + NLIMBS_HAND:NLIMBS_BODY +
                2*NLIMBS_HAND] += NJOINTS_BODY + NJOINTS_HAND
    return kintree


CONFIG['total'] = {}
CONFIG['total']['kintree'] = getKintree('total')
CONFIG['total']['nJoints'] = 137

COCO17_IN_BODY25 = [0, 16, 15, 18, 17, 5, 2, 6, 3, 7, 4, 12, 9, 13, 10, 14, 11]

CONFIG['bodyhandface']['joint_names'] = CONFIG['body25']['joint_names']


def coco17tobody25(points2d):
    dim = 3
    if len(points2d.shape) == 2:
        points2d = points2d[None, :, :]
        dim = 2
    kpts = np.zeros((points2d.shape[0], 25, 3))
    kpts[:, COCO17_IN_BODY25, :2] = points2d[:, :, :2]
    kpts[:, COCO17_IN_BODY25, 2:3] = points2d[:, :, 2:3]
    kpts[:, 8, :2] = kpts[:, [9, 12], :2].mean(axis=1)
    kpts[:, 8, 2] = kpts[:, [9, 12], 2].min(axis=1)
    kpts[:, 1, :2] = kpts[:, [2, 5], :2].mean(axis=1)
    kpts[:, 1, 2] = kpts[:, [2, 5], 2].min(axis=1)
    if dim == 2:
        kpts = kpts[0]
    return kpts


for skeltype, config in CONFIG.items():
    if 'joint_names' in config.keys():
        torsoid = [config['joint_names'].index(name) if name in config['joint_names'] else None for name in [
            'LShoulder', 'RShoulder', 'LHip', 'RHip']]
        torsoid = [i for i in torsoid if i is not None]
        config['torso'] = torsoid
