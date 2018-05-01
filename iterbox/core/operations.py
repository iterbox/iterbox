"""
Functions and operations for tensor algebra
"""

import numpy as np
import functools


def unfold(tensor, mode):
    """ Unfolds N-dimensional array into a 2D array.

    Parameters
    ----------
    tensor : np.ndarray
        N-dimensional array to be unfolded
    mode : int
        Specifies a mode along which a `tensor` will be unfolded

    Returns
    -------
    tensor_unfolded : np.ndarray
        Unfolded version of a `tensor` with a shape ``(tensor.shape[mode], -1)``
    """
    tensor_unfolded = np.reshape(np.moveaxis(tensor, mode, 0), (tensor.shape[mode], -1))
    return tensor_unfolded


def fold(matrix, mode, shape):
    """ Fold a 2D array into a N-dimensional array.

    Parameters
    ----------
    matrix : np.ndarray
        Unfolded version of a tensor
    mode : int
        A mode along which original tensor was unfolded into a `matrix`
    shape : tuple
        Shape of the original tensor before it was unfolded

    Returns
    -------
    original_tensor : np.ndarray
        N-dimensional array of the original shape

    Notes
    -----
    At the moment it reverts unfolding operation (`unfold`). Will be generalised in a future
    """
    full_shape = list(shape)
    mode_dim = full_shape.pop(mode)
    full_shape.insert(0, mode_dim)
    original_tensor = np.moveaxis(np.reshape(matrix, full_shape), 0, mode)
    return original_tensor


def mode_n_product(tensor, matrix, mode):
    """ Mode-n product of a N-dimensional array with a matrix.

    Parameters
    ----------
    tensor : np.ndarray
        N-dimensional array
    matrix : np.ndarray
        2D array
    mode : int
        Specifies mode along which a `tensor` is multiplied by a `matrix`. The size of a `tensor` along this `mode`
        should be equal to the number of columns of the `matrix`. That is: ``tensor.shape[mode] = matrix.shape[1]``

    Returns
    -------
    result : np.ndarray
        The result of the mode-n product of a `tensor` with a `matrix` along specified `mode`.
    """
    # TODO: Implement mode-n product with a vector
    # TODO: Add dimensionality check
    orig_shape = list(tensor.shape)
    new_shape = orig_shape
    new_shape[mode] = matrix.shape[0]
    result = fold(np.dot(matrix, unfold(tensor, mode)), mode, tuple(new_shape))
    return result

def calc_sum(a,b):
    return a+b