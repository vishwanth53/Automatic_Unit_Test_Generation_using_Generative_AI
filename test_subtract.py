import pytest
from example import subtract



def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3
    pass
def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3
    pass
def test_subtract_mixed_numbers():
    assert subtract(5, -2) == 7
    pass
def test_subtract_zero():
    assert subtract(0, 5) == -5
    pass
def test_subtract_float_numbers():
    assert subtract(3.5, 2.5) == 1.0
    pass
def test_subtract_large_numbers():
    assert subtract(1000000, 999999) == 1
    pass