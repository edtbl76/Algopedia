import unittest
import sys
import os

# Add the parent directory to the path so we can import the test modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the test modules
from tests.data_structures.test_hash_entry import TestHashEntry
from tests.data_structures.test_hash_function import TestHashFunction
from tests.data_structures.test_simple_addition_hash import TestSimpleAdditionHash
from tests.data_structures.test_hash_map import TestHashMap

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add the test cases
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestHashEntry))
    test_suite.addTest(loader.loadTestsFromTestCase(TestHashFunction))
    test_suite.addTest(loader.loadTestsFromTestCase(TestSimpleAdditionHash))
    test_suite.addTest(loader.loadTestsFromTestCase(TestHashMap))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print a summary
    print(f"\nRan {result.testsRun} tests")
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"Failed tests: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        sys.exit(1)
