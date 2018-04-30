import numpy as np
from ..structures import Tensor
from ..structures import is_tensor

def test_is_tensor():
    array = np.arange(24).reshape(2,3,4)
    tensor = Tensor(array=array)
    result = is_tensor(tensor)
    result_2 = is_tensor(array)
    assert result
    assert result_2

