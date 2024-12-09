# ai_caller.py
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt):
    """Call the OpenAI API to generate a unit test based on the provided prompt."""
    try:
        # Use the ChatCompletion.create method for GPT-4 or GPT-3.5
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using GPT-4 model
            messages=[{"role": "user", "content": prompt}],  # The prompt is now in messages
            max_tokens=200,  # Limit the response length
            temperature=0.5,  # Controls the randomness of the response
        )
        
        # Extract the generated unit test from the response
        generated_test = response['choices'][0]['message']['content'].strip()
        return generated_test
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

# Example usage
if __name__ == "__main__":
    prompt = """Write a pytest unit test for the following function:

Function Name: add
Docstring: Adds two numbers.
Code:
def add(a, b):
    return a + b"""
    
    unit_test = call_openai(prompt)
    if unit_test:
        print("Generated Unit Test:")
        print(unit_test)




