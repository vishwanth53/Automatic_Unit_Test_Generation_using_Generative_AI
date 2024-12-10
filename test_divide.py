import pytest
from example import divide



def test_divide_valid_input():
    assert divide(10, 2) == 5
    assert divide(100, 5) == 20
    pass
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
    pass
def test_divide_negative_numbers():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5
    pass