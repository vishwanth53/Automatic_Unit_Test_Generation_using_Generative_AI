
# Automated Unit Test Generator using Generative AI

## Overview
This project automates the generation of unit tests using generative AI models like OpenAI's GPT. It improves code coverage, reduces manual effort, and increases software reliability.

## Features
Automated Test Generation: Utilizes AI models to generate unit tests for your codebase.
Code Coverage Analysis: Provides insights into code coverage to ensure comprehensive testing.
Framework Integration: Seamlessly integrates with popular testing frameworks like pytest.

## Components
1. `example.py`: Sample code to be tested.
2. `test_example.py`: Unit tests for `example.py`.
3. `test_runner.py`: Executes tests and generates coverage reports.
4. `coverage_parser.py`: Parses coverage reports to identify untested code.
5. `prompt_builder.py`: Builds prompts for AI models.
6. `ai_caller.py`: Interacts with OpenAI API to generate tests.

## Installation
1. Clone the repository.
    ```bash
    git clone https://github.com/vishwanth53/Automatic_Unit_Test_Generation_using_Generative_AI
    ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to the `.env` file.

## Usage
1. Prepare Your Code: Ensure your Python functions are defined in a module (e.g., example.py)
   
2. Run the AI Test Generator:
   ```bash
   python ai_caller.py
   ```
   This script will generate unit tests for the functions defined in your module and save them as test_<function_name>.py files.
   
3. Execute the Tests:
   ```bash
   pytest --cov=example --cov-report=term-missing
   ```
   This command should be called before and after calling the ai_caller function which helps in analysing the code coverage.

## Troubleshooting
Common Errors: If you encounter syntax errors or issues with test generation, ensure that your code is correctly formatted and that the AI model has access to all necessary context.

Improving Coverage: To enhance code coverage, consider refining the prompts provided to the AI model or manually adding tests for complex cases.   
   
