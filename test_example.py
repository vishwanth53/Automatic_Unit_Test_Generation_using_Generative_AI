
# test_example.py - Unit tests for example.py
from example import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(10, 2) == 5
    try:
        divide(5, 0)
    except ValueError:
        assert True  # Pass if exception is raised
