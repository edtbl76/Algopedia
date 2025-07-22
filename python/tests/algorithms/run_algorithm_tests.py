import unittest
import sys
import os

# Add the parent directory to the path so we can import the test modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the test modules
from tests.algorithms.test_find_max import TestFindMax
from tests.algorithms.test_find_min import TestFindMin
from tests.algorithms.test_factorial import TestFactorial
from tests.algorithms.test_fibonacci import TestFibonacci
from tests.algorithms.test_flatten_list import TestFlattenList
from tests.algorithms.test_iteration_recursion_comparison import TestIterationRecursionComparison
from tests.algorithms.test_multiplication import TestMultiplication
from tests.algorithms.test_palindrome import TestPalindrome
from tests.algorithms.test_power_set import TestPowerSet
from tests.algorithms.test_sum_digits import TestSumDigits

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add the test cases
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestFindMax))
    test_suite.addTest(loader.loadTestsFromTestCase(TestFindMin))
    test_suite.addTest(loader.loadTestsFromTestCase(TestFactorial))
    test_suite.addTest(loader.loadTestsFromTestCase(TestFibonacci))
    test_suite.addTest(loader.loadTestsFromTestCase(TestFlattenList))
    test_suite.addTest(loader.loadTestsFromTestCase(TestIterationRecursionComparison))
    test_suite.addTest(loader.loadTestsFromTestCase(TestMultiplication))
    test_suite.addTest(loader.loadTestsFromTestCase(TestPalindrome))
    test_suite.addTest(loader.loadTestsFromTestCase(TestPowerSet))
    test_suite.addTest(loader.loadTestsFromTestCase(TestSumDigits))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print a summary
    print(f"\nRan {result.testsRun} tests")
    if result.wasSuccessful():
        print("All algorithm tests passed!")
    else:
        print(f"Failed tests: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        sys.exit(1)
