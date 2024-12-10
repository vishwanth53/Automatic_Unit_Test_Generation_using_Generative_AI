import pytest
from example import modulus



def test_modulus_standard_cases():
    assert modulus(10, 3) == 1
    assert modulus(15.5, 4) == 3.5
    assert modulus(20, 7.5) == 5
    pass
def test_modulus_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        modulus(10, 0)
    pass
def test_modulus_invalid_input_types():
    with pytest.raises(TypeError, match="Inputs must be int or float."):
        modulus("abc", 5)
    with pytest.raises(TypeError, match="Inputs must be int or float."):
        modulus(10, [3, 4])
    pass




