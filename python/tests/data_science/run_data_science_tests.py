import unittest
import sys
import os

# Add the parent directory to the path so we can import the test modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the test modules
from tests.data_science.test_addition_rule import TestAdditionRule
from tests.data_science.test_multiplication_rule import TestMultiplicationRule

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add the test cases
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestAdditionRule))
    test_suite.addTest(loader.loadTestsFromTestCase(TestMultiplicationRule))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print a summary
    print(f"\nRan {result.testsRun} tests")
    if result.wasSuccessful():
        print("All data science tests passed!")
    else:
        print(f"Failed tests: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        sys.exit(1)