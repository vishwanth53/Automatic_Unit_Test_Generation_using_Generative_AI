# example.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# New function added (not covered by the tests)
def modulus(a, b):
    """Returns the remainder of a divided by b."""
    return a % b

