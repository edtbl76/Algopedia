import unittest
import sys
import os

# Add the parent directory to the path so we can import the test modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the test modules
from tests.search.test_naive_pattern_search import TestNaivePatternSearch
from tests.search.test_naive_pattern_search_v2 import TestNaivePatternSearchV2, TestCharsMatch as TestCharsMatchV2
from tests.search.test_naive_pattern_search_v3 import TestNaivePatternSearchV3, TestCharsMatch as TestCharsMatchV3, TestHelperFunctions
from tests.search.test_linear_search import TestLinearSearch

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add the test cases
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestNaivePatternSearch))
    test_suite.addTest(loader.loadTestsFromTestCase(TestNaivePatternSearchV2))
    test_suite.addTest(loader.loadTestsFromTestCase(TestCharsMatchV2))
    test_suite.addTest(loader.loadTestsFromTestCase(TestNaivePatternSearchV3))
    test_suite.addTest(loader.loadTestsFromTestCase(TestCharsMatchV3))
    test_suite.addTest(loader.loadTestsFromTestCase(TestHelperFunctions))
    test_suite.addTest(loader.loadTestsFromTestCase(TestLinearSearch))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print a summary
    print(f"\nRan {result.testsRun} tests")
    if result.wasSuccessful():
        print("All search tests passed!")
    else:
        print(f"Failed tests: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        sys.exit(1)