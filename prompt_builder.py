
# prompt_builder.py - Builds prompts for the AI model based on uncovered code

def build_prompt(function_name, docstring, code_snippet):
    """Create a prompt for generating unit tests using AI."""
    return f"""
    Write a pytest unit test for the following function:
    
    Function Name: {function_name}
    Docstring: {docstring}
    Code:
    {code_snippet}
    """
# Example usage
function_name = "add"
docstring = "Adds two numbers."
code_snippet = """def add(a, b):
    return a + b"""

prompt = build_prompt(function_name, docstring, code_snippet)
print(prompt)

function_name = "multiply"
docstring = "Multiplies two numbers."
code_snippet = """def multiply(a, b):
    return a * b"""

prompt = build_prompt(function_name, docstring, code_snippet)
print(prompt)

# Test with a function without a docstring
function_name = "divide"
docstring = "No docstring provided"
code_snippet = """def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b"""

prompt = build_prompt(function_name, docstring, code_snippet)
print(prompt)


if __name__ == "__main__":
    prompt = build_prompt("add", "Adds two numbers", "def add(a, b): return a + b")
    print(prompt)
