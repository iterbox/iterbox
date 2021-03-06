"""
Classes for different tensor representations
"""

import numpy as np
from .operations import unfold, fold, mode_n_product


class Tensor(object):
    """ This class describes multidimensional data.

    All its methods implement all common operation on a tensor alone

    Parameters
    ----------
    data : np.ndarray
        N-dimensional array
    _orig_shape : tuple
        Original shape of a tensor. Defined at the object creation for convenience during unfolding and folding.
        Can potentially cause a lot of problems in a future.
    """
    # TODO: add description for the tensor and the factor matrices/modes etc. (Through pandas integration???)
    # TODO: implement unfolding and folding to tensors of an arbitrary order

    def __init__(self, array) -> None:
        """

        Parameters
        ----------
        array : {np.ndarray, Tensor}
        """
        # TODO: covert data to a specific data type (int, float etc)
        if isinstance(array, Tensor):
            self.data = array.data
            self._orig_shape = array._orig_shape
        else:
            self.data = array
            self._orig_shape = array.shape

    def copy(self):
        """ Produces a copy of itself

        Returns
        -------
        Tensor
        """
        return Tensor(self)

    @property
    def frob_norm(self):
        """ Frobenious norm of a tensor

        Returns
        -------
        float
        """
        # return np.sqrt(np.sum(self.data ** 2))
        return np.linalg.norm(self.data)

    @property
    def shape(self):
        """ Sizes of all dimensions of a tensor

        Returns
        -------
        tuple
        """
        return self.data.shape

    @property
    def order(self):
        """ Order of a tensor

        Returns
        -------
        int
        """
        return self.data.ndim

    @property
    def size(self):
        """ Number of elements in a tensor

        Returns
        -------
        int
        """
        return self.data.size

    def unfold(self, mode, inplace=True):
        """ Perform mode-n unfolding to a matrix

        Parameters
        ----------
        mode : int
            Specifies a mode along which a `tensor` will be unfolded
        inplace : bool
            If True, then modifies itself.
            If False, then creates new object (copy)

        Returns
        ----------
        tensor : Tensor
            Unfolded version of a tensor
        """
        if inplace:
            tensor = self
        else:
            tensor = self.copy()
        tensor.data = unfold(self.data, mode)
        return tensor

    def fold(self, inplace=True):
        """ Fold to the original shape (undo self.unfold)

        Parameters
        ----------
        inplace : bool
            If True, then modifies itself.
            If False, then creates new object (copy)

        Returns
        ----------
        tensor : Tensor
            Tensor of original shape (self._orig_shape)
        """
        if inplace:
            tensor = self
        else:
            tensor = self.copy()
        mode = tensor._orig_shape.index(tensor.shape[0])
        tensor.data = fold(self.data, mode, self._orig_shape)
        return tensor

    def mode_n_product(self, matrix, mode, inplace=True):
        """ Mode-n product of a tensor with a matrix

        Parameters
        ----------
        matrix : {Tensor, np.ndarray}
            2D array
        mode : int
            Specifies mode along which a tensor is multiplied by a `matrix`
        inplace : bool
            If True, then modifies itself.
            If False, then creates new object (copy)

        Returns
        -------
        tensor : Tensor
            The result of the mode-n product of a tensor with a `matrix` along specified `mode`.

        Notes
        -------
        Remember that mode_n product changes the shape of the tensor. Presumably, it also changes the interpretation
        of that mode
        """
        # TODO: Think about the way to change mode_description
        if isinstance(matrix, np.ndarray):
            matrix = Tensor(matrix)
        if inplace:
            tensor = self
        else:
            tensor = self.copy()
        tensor.data = mode_n_product(tensor=tensor.data, matrix=matrix.data, mode=mode)
        tensor._orig_shape = tensor.shape
        return tensor


def super_diag_tensor(order, values=None):
    """ Super-diagonal tensor of the specified `order`.

    Parameters
    ----------
    order : int
        Desired order of the tensor
    values : np.ndarray
        Array of values on the super-diagonal of a tensor. By default contains only ones.
        Length of this vector defines the Kryskal rank of a tensor.

    Returns
    -------
    tensor : Tensor
    """
    rank = values.size
    shape = (rank,) * order
    if values is None:
        values = np.ones(rank)
    core = np.zeros(shape)
    core[np.diag_indices(rank, ndim=order)] = values
    tensor = Tensor(core)
    return tensor


def is_tensor(obj):
    return isinstance(obj, Tensor)