import unittest
import sys
import os

# Add the parent directory to the path so we can import the test modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the test modules
from tests.data_science.test_addition_rule import TestAdditionRule
from tests.data_science.test_multiplication_rule import TestMultiplicationRule
from tests.data_science.Probability.test_bernoulli import TestBernoulliDistribution
from tests.data_science.Probability.test_binomial import TestBinomialDistribution
from tests.data_science.Probability.test_poisson import TestPoissonDistribution
from tests.data_science.Probability.test_statistical_properties_utils import (
    TestSampleValidator,
    TestStatisticalCalculations,
    TestResultAnalyzerUtil,
    TestBaseConfigEnumsExceptions,
)
from tests.data_science.Probability.test_statistical_properties_expectation_variance import (
    TestExpectationOperator,
    TestVarianceOperator,
)

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add the test cases
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestAdditionRule))
    test_suite.addTest(loader.loadTestsFromTestCase(TestMultiplicationRule))
    test_suite.addTest(loader.loadTestsFromTestCase(TestBernoulliDistribution))
    test_suite.addTest(loader.loadTestsFromTestCase(TestBinomialDistribution))
    test_suite.addTest(loader.loadTestsFromTestCase(TestPoissonDistribution))
    # Add statistical_properties tests
    test_suite.addTest(loader.loadTestsFromTestCase(TestSampleValidator))
    test_suite.addTest(loader.loadTestsFromTestCase(TestStatisticalCalculations))
    test_suite.addTest(loader.loadTestsFromTestCase(TestResultAnalyzerUtil))
    test_suite.addTest(loader.loadTestsFromTestCase(TestBaseConfigEnumsExceptions))
    test_suite.addTest(loader.loadTestsFromTestCase(TestExpectationOperator))
    test_suite.addTest(loader.loadTestsFromTestCase(TestVarianceOperator))
    
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