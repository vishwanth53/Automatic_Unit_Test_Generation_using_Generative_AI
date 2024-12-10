import pytest
from example import multiply



def test_multiply_valid_inputs():
    assert multiply(2, 3) == 6
    assert multiply(0, 5.5) == 0
    assert multiply(-4, 8) == -32
    assert multiply(-2.5, 4) == -10.0
    pass
def test_multiply_invalid_inputs():
    with pytest.raises(TypeError):
        multiply('a', 3)
    with pytest.raises(TypeError):
        multiply(2, 'b')
    with pytest.raises(TypeError):
        multiply('x', 'y')
    with pytest.raises(TypeError):
        multiply(None, 5)
    with pytest.raises(TypeError):
        multiply([1, 2, 3], 4)
    pass