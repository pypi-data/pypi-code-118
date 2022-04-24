
from ai4water.backend import get_attributes

try:
    import torch
except ModuleNotFoundError:
    torch = None

LAYERS = {}

LOSSES = {}

OPTIMIZERS = {}

if torch is not None:
    LAYERS.update(get_attributes(torch, 'nn', case_sensitive=True))

    LOSSES.update({"MSE": torch.nn.MSELoss,
                   "mse": torch.nn.MSELoss,
                   "CROSSENTROPYLOSS": torch.nn.CrossEntropyLoss,
                   "L1Loss": torch.nn.L1Loss,
                   "NLLLoss": torch.nn.NLLLoss,
                   "HingeEmbeddingLoss": torch.nn.HingeEmbeddingLoss,
                   "MarginRankingLoss": torch.nn.MarginRankingLoss,
                   "TripletMarginLoss": torch.nn.TripletMarginLoss,
                   "KLDivLoss": torch.nn.KLDivLoss,

                   })
    OPTIMIZERS.update(get_attributes(torch, 'optim', case_sensitive=True))
