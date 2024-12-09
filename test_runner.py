
# test_runner.py - Runs tests and generates coverage reports

import subprocess

def run_tests():
    """Run tests using pytest and generate a coverage report."""
    result = subprocess.run(['pytest', '--cov=example', '--cov-report=xml'], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    run_tests()
