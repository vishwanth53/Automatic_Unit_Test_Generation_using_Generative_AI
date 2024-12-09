
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
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to the `.env` file.

## Usage
1. Run tests and generate coverage:
   ```bash
   python test_runner.py
   ```
2. Parse coverage gaps:
   ```bash
   python coverage_parser.py
   ```
3. Generate prompts for untested code:
   ```bash
   python prompt_builder.py
   ```
4. Call AI to generate unit tests:
   ```bash
   python ai_caller.py
   ```
## Troubleshooting
Common Errors: If you encounter syntax errors or issues with test generation, ensure that your code is correctly formatted and that the AI model has access to all necessary context.

Improving Coverage: To enhance code coverage, consider refining the prompts provided to the AI model or manually adding tests for complex cases.   
   
