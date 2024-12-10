import pytest
from example import add



def test_add_positive_numbers():
    assert add(2, 3) == 5
    pass
def test_add_negative_numbers():
    assert add(-2, -3) == -5
    pass
def test_add_mixed_numbers():
    assert add(2, -3) == -1
    pass
def test_add_zero():
    assert add(0, 0) == 0
    pass
def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
    pass