import unittest
import sys
import os
from typing import Optional, Sequence, Union, Any

# Ensure project root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.probability.random_variable import RandomVariable
from data_science.probability.statistical_properties.expectation import ExpectationOperator
from data_science.probability.statistical_properties.variance import VarianceOperator
from data_science.probability.statistical_properties.config import TestConfiguration


class MockRandomVariable(RandomVariable[float]):
    def __init__(self, mean_value: float, variance_value: float, samples: Sequence[float]):
        self._mean = mean_value
        self._variance = variance_value
        self._samples = list(samples)

    @property
    def mean(self) -> float:
        return self._mean

    @property
    def variance(self) -> float:
        return self._variance

    def cdf(self, value: float) -> float:
        # Minimal implementation for abstract base; not used in tests
        return 0.0

    def sample(self, size: Optional[int] = None) -> Union[float, Sequence[float]]:
        if size is None:
            return self._samples[0]
        # Repeat pattern to match requested size
        if len(self._samples) >= size:
            return self._samples[:size]
        result = []
        idx = 0
        while len(result) < size:
            result.append(self._samples[idx % len(self._samples)])
            idx += 1
        return result


class TestExpectationOperator(unittest.TestCase):
    def setUp(self) -> None:
        # Use a smaller sample size for faster tests; patterns repeat to fill size
        self.config = TestConfiguration(sample_size=1000)
        self.exp = ExpectationOperator(config=self.config)

    def test_additivity_property(self):
        # X has mean 2, Y has mean 3. Use non-constant samples to ensure non-zero margin of error.
        x_samples = [1.0, 3.0]  # mean 2
        y_samples = [2.0, 4.0]  # mean 3
        rv_x = MockRandomVariable(mean_value=2.0, variance_value=1.0, samples=x_samples)
        rv_y = MockRandomVariable(mean_value=3.0, variance_value=1.0, samples=y_samples)

        def joint_sampler(n: int):
            return rv_x.sample(n), rv_y.sample(n)

        result = self.exp.additivity(rv_x, rv_y, joint_sampler)
        self.assertAlmostEqual(result.theoretical_sum, 5.0, places=6)
        self.assertAlmostEqual(result.empirical_sum, 5.0, places=6)
        self.assertGreater(result.statistical_analysis.margin_of_error_95_percent, 0.0)
        self.assertTrue(result.test_passed)
        # Independence analysis: correlation should be positive but small pattern repeats; not asserting exact value
        self.assertIn('likely_independent', result.independence_analysis)
        self.assertEqual(result.property, 'E(X + Y) = E(X) + E(Y)')

    def test_linearity_property(self):
        x_samples = [1.0, 3.0]
        y_samples = [2.0, 4.0]
        rv_x = MockRandomVariable(mean_value=2.0, variance_value=1.0, samples=x_samples)
        rv_y = MockRandomVariable(mean_value=3.0, variance_value=1.0, samples=y_samples)

        a, b = 2.0, -1.0

        def joint_sampler(n: int):
            return rv_x.sample(n), rv_y.sample(n)

        result = self.exp.linearity(rv_x, rv_y, a, b, joint_sampler)
        theoretical = a * rv_x.mean + b * rv_y.mean
        self.assertAlmostEqual(result.theoretical, theoretical, places=6)
        self.assertAlmostEqual(result.empirical, theoretical, places=6)
        self.assertLess(result.error, 1e-9)
        self.assertEqual(result.property, 'E[aX + bY] = aE[X] + bE[Y]')

    def test_constant_shift(self):
        samples = [1.0, 3.0]  # mean 2, variance 1
        rv = MockRandomVariable(mean_value=2.0, variance_value=1.0, samples=samples)
        a = 5.0
        result = self.exp.constant_shift(rv, a)
        self.assertAlmostEqual(result.theoretical_mean, 2.0)
        self.assertAlmostEqual(result.theoretical_shifted_mean, 7.0)
        self.assertAlmostEqual(result.empirical_shifted_mean, 7.0)
        # Zero absolute error; margin should be > 0 because original samples non-constant
        self.assertEqual(result.absolute_error, 0.0)
        self.assertGreater(result.statistical_analysis.margin_of_error_95_percent, 0.0)
        self.assertTrue(result.test_passed)
        self.assertTrue(result.variance_analysis['variance_preserved'])

    def test_transformation_properties_with_convex_function(self):
        # Symmetric samples around 0
        samples = [-1.0, 0.0, 1.0]
        rv = MockRandomVariable(mean_value=0.0, variance_value=2/3, samples=samples)
        square = lambda x: x * x
        result = self.exp.transformation_properties(rv, square, 'square')
        self.assertEqual(result.transformation, 'square')
        # E[X^2] >= (E[X])^2 by Jensen for convex square
        self.assertGreaterEqual(result.e_gx, result.g_ex)
        # is_convex_approx should classify square as convex -> flag True
        self.assertTrue(result.jensen_inequality_holds)


class TestVarianceOperator(unittest.TestCase):
    def setUp(self) -> None:
        self.config = TestConfiguration(sample_size=1000)
        self.var_op = VarianceOperator(config=self.config)

    def test_scaling_property(self):
        base_samples = [0.0, 2.0]  # mean 1, variance 1 (population)
        rv = MockRandomVariable(mean_value=1.0, variance_value=1.0, samples=base_samples)
        a, b = 3.0, 5.0
        result = self.var_op.scaling_property(rv, a, b)
        self.assertEqual(result.property, 'Var[aX + b] = a²Var[X]')
        self.assertAlmostEqual(result.theoretical_variance, a * a * rv.variance)
        self.assertAlmostEqual(result.empirical_variance, 9.0, places=6)
        self.assertLess(result.error, 1e-9)
        self.assertIn('note', result.additional_info)

    def test_sum_property_with_positive_covariance(self):
        x_samples = [0.0, 2.0]
        # Perfect positive correlation: y = x
        y_samples = [0.0, 2.0]
        rv_x = MockRandomVariable(mean_value=1.0, variance_value=1.0, samples=x_samples)
        rv_y = MockRandomVariable(mean_value=1.0, variance_value=1.0, samples=y_samples)

        def joint_sampler(n: int):
            return rv_x.sample(n), rv_y.sample(n)

        result = self.var_op.sum_property(rv_x, rv_y, joint_sampler)
        self.assertEqual(result.property, 'Var[X + Y] = Var[X] + Var[Y] + 2Cov[X,Y]')
        # With VarX=VarY=1 and Cov=1 (identical sequences), theoretical variance should be 4
        self.assertAlmostEqual(result.theoretical_variance, 4.0, places=6)
        self.assertAlmostEqual(result.empirical_variance, 4.0, places=6)
        self.assertLess(result.error, 1e-9)
        self.assertFalse(result.additional_info['independence_assumption'])

    def test_constant_shift_invariance(self):
        samples = [0.0, 2.0]
        rv = MockRandomVariable(mean_value=1.0, variance_value=1.0, samples=samples)
        a = 10.0
        result = self.var_op.constant_shift_invariance(rv, a)
        self.assertEqual(result.property, 'Var[X + a] = Var[X]')
        self.assertAlmostEqual(result.theoretical_variance, 1.0)
        self.assertAlmostEqual(result.empirical_variance, 1.0)
        self.assertLess(result.error, 1e-9)
        self.assertTrue(result.additional_info['invariance_preserved'])
        self.assertAlmostEqual(result.additional_info['variance_preservation_ratio'], 1.0)


if __name__ == '__main__':
    unittest.main()
