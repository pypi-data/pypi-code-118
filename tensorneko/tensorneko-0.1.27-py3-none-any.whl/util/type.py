from enum import Enum
from typing import Callable, Union, List, Tuple, TypeVar

import numpy as np
import torch
from torch import device, Size
from torch.nn import Module

ModuleFactory = Union[Callable[[], Module], Callable[[int], Module]]
"""The module builder type of ``() -> torch.nn.Module | (int) -> torch.nn.Module``"""


Device = device
"""Device type of :class:`torch.device`"""


Shape = Union[Size, List[int], Tuple[int, ...]]
"""Shape type. Normally is ``List[int]``, ``Tuple[int, ...]`` or :class:`torch.Size`"""


# Generic types
T = TypeVar('T')  # Any type
R = TypeVar('R')  # Return type
A = TypeVar("A", torch.Tensor, np.ndarray)  # Array type
P = TypeVar("P", int, float, str, bool)  # Primitive type
E = TypeVar("E", bound=Enum)
