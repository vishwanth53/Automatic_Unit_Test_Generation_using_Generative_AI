import openai
import os

def setup_openai_key():
    """ Load the OpenAI API key from environment variables. """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key is not set in the environment variables.")
    openai.api_key = api_key

def clean_generated_tests(generated_tests, function_name):
    """
    Cleans the generated output by removing non-Python text, Markdown syntax,
    and ensuring the function is imported.
    Adds necessary imports for pytest-based test cases.
    """
    lines = generated_tests.splitlines()
    valid_lines = []
    inside_function = False

    for line in lines:
        stripped_line = line.strip()
        # Skip Markdown syntax (e.g., triple backticks)
        if stripped_line.startswith("```"):
            continue

        if stripped_line.startswith("def test_"):  # Start of a test case
            inside_function = True
            valid_lines.append(line)
        elif inside_function and stripped_line == "":  # Empty line within a function
            valid_lines.append("    pass")  # Add a placeholder body if missing
            inside_function = False
        elif inside_function:
            valid_lines.append(line)  # Add valid lines within the function body
        elif stripped_line.startswith("assert") or stripped_line == "":
            valid_lines.append(line)  # Add assertion or empty lines as is

    # Add necessary imports at the beginning
    import_statements = f"import pytest\nfrom example import {function_name}\n\n"
    return import_statements + "\n".join(valid_lines)




def generate_unit_tests(function_name, function_description):
    """ Generate unit tests for a given function using the OpenAI Codex model. """
    setup_openai_key()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Chat-based model
            messages=[
                {"role": "system", "content": "You are an expert Python developer and unit test generator."},
                {"role": "user", "content": f"Write unit tests in Python using pytest for the following function:\n{function_description}"}
            ],
            max_tokens=500,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        # Extract raw output
        raw_tests = response['choices'][0]['message']['content'].strip()
        
        # Clean the raw output
        cleaned_tests = clean_generated_tests(raw_tests, function_name)
        return cleaned_tests
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if _name_ == "_main_":
    functions = [
        {
            "name": "add",
            "description": """
def add(a, b):
    \"\"\"
    Add two numbers.
    - Test normal cases with integers and floats.
- Test edge cases with invalid input types, such as strings, lists, or None.
- Ensure invalid input cases raise a TypeError.
    \"\"\"
    return a + b
"""
        },
        {
            "name": "subtract",
            "description": """
def subtract(a, b):
    \"\"\"
    Subtract one number from another.
    \"\"\"
    return a - b
"""
        },
        {
            "name": "multiply",
            "description": """
def multiply(a, b):
    \"\"\"
    Multiply two numbers.
    \"\"\"
    return a * b
Please generate pytest unit tests for this function, including cases where:
- ⁠Both inputs are valid integers or floats.
- ⁠One or both inputs are invalid types (e.g., string, list, None) to ensure the function raises a TypeError.    
"""
        },
        {
            "name": "divide",
            "description": """
def divide(a, b):
    \"\"\"
    Divide one number by another. Raises ValueError if dividing by zero.
    \"\"\"
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
"""
        },{
            "name": "modulus",
            "description": """
def modulus(a, b):
    \"\"\"
    Calculate the remainder of dividing a by b.

    Parameters:
    a (int or float): The dividend.
    b (int or float): The divisor.
    - b is zero, which should raise a ValueError with the message "Cannot divide by zero."
- Either a or b is of an invalid type (e.g., string, list), which should raise a TypeError with the message "Inputs must be int or float."

Additionally, provide pytest unit tests covering:
- Standard cases with integers and floats.
- Edge cases such as division by zero.
- Invalid input types to ensure proper exception handling.
- Invalid input types to ensure proper exception handling.
- For floating-point comparisons, use pytest.approx to account for precision issues.

    Returns:
    int or float: The remainder when a is divided by b.

    Raises:
    ValueError: If b is zero.
    TypeError: If a or b is not an int or float.
"""
        }
    ]

    for func in functions:
        tests = generate_unit_tests(func["name"], func["description"])
        if tests:
            print(f"Generated Unit Tests for {func['name']}:\n")
            print(tests)
            with open(f"test_{func['name']}.py", "w") as f:
                f.write(tests)
            print(f"Test cases saved to 'test_{func['name']}.py'")
        else:
            print(f"Failed to generate unit tests for {func['name']}.")



