import unittest
import sys
import os

# Ensure project root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.probability.statistical_properties.utils import (
    SampleValidator,
    StatisticalCalculations,
    TestResultAnalyzer,
)
from data_science.probability.statistical_properties.config import TestConfiguration
from data_science.probability.statistical_properties.enums import TestInterpretation


class TestSampleValidator(unittest.TestCase):
    def test_ensure_list(self):
        self.assertEqual(SampleValidator.ensure_list(5.0), [5.0])
        self.assertEqual(SampleValidator.ensure_list([1.0, 2.0]), [1.0, 2.0])
        self.assertEqual(SampleValidator.ensure_list(None), [])

    def test_validate_sample_pairs_success(self):
        x, y = SampleValidator.validate_sample_pairs([1.0, 2.0], [3.0, 4.0])
        self.assertEqual(x, [1.0, 2.0])
        self.assertEqual(y, [3.0, 4.0])

    def test_validate_sample_pairs_mismatch_raises(self):
        with self.assertRaises(ValueError):
            SampleValidator.validate_sample_pairs([1.0], [1.0, 2.0])


class TestStatisticalCalculations(unittest.TestCase):
    def test_mean_and_variance(self):
        self.assertEqual(StatisticalCalculations.mean([]), 0.0)
        samples = [0.0, 2.0]
        self.assertAlmostEqual(StatisticalCalculations.mean(samples), 1.0)
        # population variance for [0,2] is 1.0
        self.assertAlmostEqual(StatisticalCalculations.variance(samples), 1.0)
        # variance with provided mean
        self.assertAlmostEqual(StatisticalCalculations.variance(samples, mean=1.0), 1.0)

    def test_standard_deviation(self):
        samples = [0.0, 2.0]
        self.assertAlmostEqual(StatisticalCalculations.standard_deviation(samples), 1.0)

    def test_covariance_and_correlation(self):
        x = [0.0, 2.0, 0.0, 2.0]
        y_same = [0.0, 2.0, 0.0, 2.0]
        y_neg = [2.0, 0.0, 2.0, 0.0]
        cov_xx = StatisticalCalculations.covariance(x, y_same)
        var_x = StatisticalCalculations.variance(x)
        self.assertAlmostEqual(cov_xx, var_x)
        corr_xx = StatisticalCalculations.correlation_coefficient(x, y_same)
        self.assertAlmostEqual(corr_xx, 1.0)
        corr_neg = StatisticalCalculations.correlation_coefficient(x, y_neg)
        self.assertAlmostEqual(corr_neg, -1.0)
        # zero variance scenario
        z = [1.0, 1.0, 1.0]
        self.assertEqual(StatisticalCalculations.correlation_coefficient(x[:3], z), 0.0)

    def test_confidence_interval_95(self):
        self.assertEqual(StatisticalCalculations.confidence_interval_95([]), 0.0)
        # For [0,2], mean=1, std=1, n=2 => margin = 1.96 * 1 / sqrt(2)
        samples = [0.0, 2.0]
        expected_margin = 1.96 * 1.0 / (2 ** 0.5)
        self.assertAlmostEqual(StatisticalCalculations.confidence_interval_95(samples), expected_margin)


class TestResultAnalyzerUtil(unittest.TestCase):
    def test_interpret_error(self):
        cfg = TestConfiguration(tolerance_excellent=0.01, tolerance_good=0.05, tolerance_acceptable=0.1)
        self.assertEqual(TestResultAnalyzer.interpret_error(0.005, cfg), TestInterpretation.EXCELLENT)
        self.assertEqual(TestResultAnalyzer.interpret_error(0.02, cfg), TestInterpretation.GOOD)
        self.assertEqual(TestResultAnalyzer.interpret_error(0.07, cfg), TestInterpretation.ACCEPTABLE)
        self.assertEqual(TestResultAnalyzer.interpret_error(0.2, cfg), TestInterpretation.POOR)

    def test_create_interpretation_result(self):
        cfg = TestConfiguration(tolerance_excellent=0.01, tolerance_good=0.05, tolerance_acceptable=0.1)
        result = TestResultAnalyzer.create_interpretation_result(cfg)
        self.assertIn('excellent', result)
        self.assertIn('good', result)
        self.assertIn('acceptable', result)
        self.assertIn('poor', result)
        self.assertEqual(result['excellent'], 'error < 0.01')
        self.assertEqual(result['good'], '0.01 <= error < 0.05')
        self.assertEqual(result['acceptable'], '0.05 <= error < 0.1')
        self.assertEqual(result['poor'], 'error >= 0.1')


class TestBaseConfigEnumsExceptions(unittest.TestCase):
    def test_statistical_property_default_config(self):
        from data_science.probability.statistical_properties.base import StatisticalProperty
        sp = StatisticalProperty()
        # Should have a TestConfiguration instance by default
        self.assertIsInstance(sp.config, TestConfiguration)
        # Default sample size should be positive integer
        self.assertIsInstance(sp.config.sample_size, int)
        self.assertGreater(sp.config.sample_size, 0)

    def test_config_dataclasses_instantiation(self):
        from data_science.probability.statistical_properties.config import (
            StatisticalAnalysis,
            AdditivityTestResult,
            LinearityTestResult,
            ConstantShiftTestResult,
            TransformationTestResult,
            VarianceTestResult,
        )
        # Minimal plausible StatisticalAnalysis
        sa = StatisticalAnalysis(sample_size=10, sample_standard_deviation=1.2, margin_of_error_95_percent=0.3)
        self.assertEqual(sa.sample_size, 10)
        # Instantiate result holders with simple values to ensure dataclasses are usable
        add_res = AdditivityTestResult(
            property='E(X+Y)=E(X)+E(Y)', theoretical_sum=3.0, empirical_sum=3.0,
            absolute_error=0.0, relative_error_percent=0.0, components={},
            statistical_analysis=sa, independence_analysis={}, test_passed=True,
            interpretation={'excellent': 'error < 0.01'}
        )
        self.assertTrue(add_res.test_passed)
        lin_res = LinearityTestResult(property='lin', theoretical=1.0, empirical=1.0, error=0.0,
                                      individual_means={'E[X]': 0.5}, scalar_multipliers={'a': 1})
        self.assertEqual(lin_res.error, 0.0)
        cshift_res = ConstantShiftTestResult(property='shift', constant_shift=1.0, theoretical_mean=2.0,
                                             theoretical_shifted_mean=3.0, empirical_shifted_mean=3.0,
                                             absolute_error=0.0, relative_error_percent=0.0, components={},
                                             statistical_analysis=sa, variance_analysis={}, test_passed=True,
                                             interpretation={})
        self.assertEqual(cshift_res.constant_shift, 1.0)
        transf_res = TransformationTestResult(transformation='square', e_gx=1.0, g_ex=0.0, difference=1.0,
                                              jensen_inequality_holds=True)
        self.assertTrue(transf_res.jensen_inequality_holds)
        var_res = VarianceTestResult(property='var', theoretical_variance=1.0, empirical_variance=1.0, error=0.0,
                                     additional_info={})
        self.assertEqual(var_res.error, 0.0)

    def test_enums_values(self):
        # Ensure enum members exist and have expected values
        self.assertEqual(TestInterpretation.EXCELLENT.value, 'excellent')
        self.assertEqual(TestInterpretation.GOOD.value, 'good')
        self.assertEqual(TestInterpretation.ACCEPTABLE.value, 'acceptable')
        self.assertEqual(TestInterpretation.POOR.value, 'poor')

    def test_exceptions_hierarchy_and_raising(self):
        from data_science.probability.statistical_properties.exceptions import (
            StatisticalTestError, InvalidSampleError, InsufficientDataError
        )
        # Subclass relationships
        self.assertTrue(issubclass(InvalidSampleError, StatisticalTestError))
        self.assertTrue(issubclass(InsufficientDataError, StatisticalTestError))
        # Raising and catching
        with self.assertRaises(InvalidSampleError):
            raise InvalidSampleError('invalid')
        with self.assertRaises(InsufficientDataError):
            raise InsufficientDataError('insufficient')


if __name__ == '__main__':
    unittest.main()
