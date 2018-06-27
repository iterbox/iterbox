import numpy as np
from functools import reduce
from ..structures import Tensor
from ..structures import is_tensor

def test_is_tensor():
    array = np.arange(24).reshape(2,3,4)
    tensor = Tensor(array=array)
    result = is_tensor(tensor)
    assert result

def test_tensor():
    true_shape = (2, 3, 4)
    n_elements = reduce(lambda x, y: x * y, true_shape)
    array_3d = np.arange(n_elements).reshape(true_shape)

    tensor = Tensor(array=array_3d)
    assert isinstance(tensor, Tensor)

    shape = tensor.shape
    assert (shape == true_shape)

    order = tensor.order
    assert (order == len(true_shape))

    size = tensor.size
    assert (size == n_elements)

    tensor_copy = tensor.copy()
    assert (tensor != tensor_copy)

    frob_norm = tensor.frob_norm
