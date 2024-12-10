# example.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    """
    Divide one number by another. Raises ValueError if dividing by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def multiply(a, b):
    """
    Multiply two numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be int or float.")
    return a * b

# New function added (not covered by the tests)
def modulus(a, b):
    """
    Returns the remainder of a divided by b.
    Raises ValueError if dividing by zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be int or float.")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b

