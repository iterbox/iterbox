"""
This module contains methods for the most common operations within multilinear algebra and
classes for the tensors represented through various tensor decompositions
"""

from .structures import Tensor, super_diag_tensor
from .operations import mode_n_product, unfold, fold