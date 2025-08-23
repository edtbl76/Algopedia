import unittest
import sys
import os
from abc import ABC, abstractmethod
from typing import List, Optional, Iterator

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.probability.random_variable import (
    RandomVariable,
    DiscreteRandomVariable,
    ContinuousRandomVariable,
    ParametricDistribution,
    expected_value,
    variance,
    covariance
)


# Create concrete implementations of abstract classes for testing
class TestDiscreteRandomVariable(DiscreteRandomVariable[int]):
    """Concrete implementation of DiscreteRandomVariable for testing"""
    
    def __init__(self, values: List[int], probabilities: List[float]):
        self._values = values
        self._probabilities = probabilities
        # Validate that probabilities sum to 1
        if abs(sum(probabilities) - 1.0) > 1e-10:
            raise ValueError("Probabilities must sum to 1")
        if len(values) != len(probabilities):
            raise ValueError("Values and probabilities must have the same length")
    
    def pmf(self, value: int) -> float:
        if value in self._values:
            index = self._values.index(value)
            return self._probabilities[index]
        return 0.0
    
    def support(self) -> Iterator[int]:
        return iter(self._values)
    
    @property
    def mean(self) -> float:
        return sum(v * p for v, p in zip(self._values, self._probabilities))
    
    @property
    def variance(self) -> float:
        mean_val = self.mean
        return sum(((v - mean_val) ** 2) * p for v, p in zip(self._values, self._probabilities))
    
    def cdf(self, value: int) -> float:
        return sum(p for v, p in zip(self._values, self._probabilities) if v <= value)
    
    def sample(self, size: Optional[int] = None):
        import random
        if size is None:
            # Sample a single value
            r = random.random()
            cumulative = 0.0
            for v, p in zip(self._values, self._probabilities):
                cumulative += p
                if r < cumulative:
                    return v
            return self._values[-1]  # Fallback
        else:
            # Sample multiple values
            return [self.sample() for _ in range(size)]


class TestContinuousRandomVariable(ContinuousRandomVariable[float]):
    """Concrete implementation of ContinuousRandomVariable for testing"""
    
    def __init__(self, pdf_func, cdf_func, mean_val, variance_val, quantile_func):
        self._pdf_func = pdf_func
        self._cdf_func = cdf_func
        self._mean_val = mean_val
        self._variance_val = variance_val
        self._quantile_func = quantile_func
    
    def pdf(self, value: float) -> float:
        return self._pdf_func(value)
    
    def cdf(self, value: float) -> float:
        return self._cdf_func(value)
    
    @property
    def mean(self) -> float:
        return self._mean_val
    
    @property
    def variance(self) -> float:
        return self._variance_val
    
    def quantile(self, p: float) -> float:
        return self._quantile_func(p)
    
    def sample(self, size: Optional[int] = None) -> List[float]:
        import random
        if size is None:
            # Sample a single value using inverse transform sampling
            u = random.random()
            return self.quantile(u)
        else:
            # Sample multiple values
            return [self.sample() for _ in range(size)]


class TestParametricDistribution(ParametricDistribution):
    """Concrete implementation of ParametricDistribution for testing"""
    
    def __init__(self, params):
        self._params = params
    
    def parameters(self):
        return self._params


class TestRandomVariable(unittest.TestCase):
    def test_random_variable_abstract_methods(self):
        """Test that RandomVariable is an abstract class with required methods"""
        # Verify that we can't instantiate RandomVariable directly
        with self.assertRaises(TypeError):
            RandomVariable()
        
        # Verify that mean, variance, cdf, and sample are abstract methods
        self.assertTrue(hasattr(RandomVariable, 'mean'))
        self.assertTrue(hasattr(RandomVariable, 'variance'))
        self.assertTrue(hasattr(RandomVariable, 'cdf'))
        self.assertTrue(hasattr(RandomVariable, 'sample'))
    
    def test_discrete_random_variable_abstract_methods(self):
        """Test that DiscreteRandomVariable is an abstract class with required methods"""
        # Verify that we can't instantiate DiscreteRandomVariable directly
        with self.assertRaises(TypeError):
            DiscreteRandomVariable()
        
        # Verify that pmf and support are abstract methods
        self.assertTrue(hasattr(DiscreteRandomVariable, 'pmf'))
        self.assertTrue(hasattr(DiscreteRandomVariable, 'support'))
    
    def test_continuous_random_variable_abstract_methods(self):
        """Test that ContinuousRandomVariable is an abstract class with required methods"""
        # Verify that we can't instantiate ContinuousRandomVariable directly
        with self.assertRaises(TypeError):
            ContinuousRandomVariable()
        
        # Verify that pdf and quantile are abstract methods
        self.assertTrue(hasattr(ContinuousRandomVariable, 'pdf'))
        self.assertTrue(hasattr(ContinuousRandomVariable, 'quantile'))
    
    def test_parametric_distribution_abstract_methods(self):
        """Test that ParametricDistribution is an abstract class with required methods"""
        # Verify that we can't instantiate ParametricDistribution directly
        with self.assertRaises(TypeError):
            ParametricDistribution()
        
        # Verify that parameters is an abstract method
        self.assertTrue(hasattr(ParametricDistribution, 'parameters'))
    
    def test_standard_deviation(self):
        """Test standard_deviation method of RandomVariable"""
        # Create a discrete random variable with known variance
        rv = TestDiscreteRandomVariable([1, 2, 3], [0.2, 0.3, 0.5])
        
        # Calculate expected variance and standard deviation
        expected_variance = 0.2 * (1 - 2.3)**2 + 0.3 * (2 - 2.3)**2 + 0.5 * (3 - 2.3)**2
        expected_std_dev = expected_variance ** 0.5
        
        # Test that standard_deviation returns the square root of variance
        self.assertAlmostEqual(rv.standard_deviation, expected_std_dev)
    
    def test_discrete_random_variable_implementation(self):
        """Test concrete implementation of DiscreteRandomVariable"""
        # Create a simple discrete random variable (a die roll)
        die = TestDiscreteRandomVariable([1, 2, 3, 4, 5, 6], [1/6] * 6)
        
        # Test PMF
        for i in range(1, 7):
            self.assertAlmostEqual(die.pmf(i), 1/6)
        self.assertEqual(die.pmf(0), 0)
        self.assertEqual(die.pmf(7), 0)
        
        # Test support
        self.assertEqual(list(die.support()), [1, 2, 3, 4, 5, 6])
        
        # Test mean
        self.assertAlmostEqual(die.mean, 3.5)
        
        # Test variance
        # Variance of uniform distribution on {1,2,3,4,5,6} is (6²-1)/12 = 35/12
        self.assertAlmostEqual(die.variance, 35/12)
        
        # Test CDF
        self.assertEqual(die.cdf(0), 0)
        self.assertAlmostEqual(die.cdf(1), 1/6)
        self.assertAlmostEqual(die.cdf(3), 3/6)
        self.assertEqual(die.cdf(6), 1)
        self.assertEqual(die.cdf(7), 1)
        
        # Test sampling
        sample = die.sample()
        self.assertIn(sample, [1, 2, 3, 4, 5, 6])
        
        samples = die.sample(1000)
        self.assertEqual(len(samples), 1000)
        for s in samples:
            self.assertIn(s, [1, 2, 3, 4, 5, 6])
    
    def test_continuous_random_variable_implementation(self):
        """Test concrete implementation of ContinuousRandomVariable"""
        # Create a simple continuous random variable (uniform on [0,1])
        def uniform_pdf(x):
            return 1.0 if 0 <= x <= 1 else 0.0
        
        def uniform_cdf(x):
            if x < 0:
                return 0.0
            elif x > 1:
                return 1.0
            else:
                return x
        
        def uniform_quantile(p):
            return p  # For uniform on [0,1], quantile = p
        
        uniform = TestContinuousRandomVariable(
            pdf_func=uniform_pdf,
            cdf_func=uniform_cdf,
            mean_val=0.5,
            variance_val=1/12,
            quantile_func=uniform_quantile
        )
        
        # Test PDF
        self.assertEqual(uniform.pdf(-0.1), 0.0)
        self.assertEqual(uniform.pdf(0.5), 1.0)
        self.assertEqual(uniform.pdf(1.1), 0.0)
        
        # Test CDF
        self.assertEqual(uniform.cdf(-0.1), 0.0)
        self.assertEqual(uniform.cdf(0.5), 0.5)
        self.assertEqual(uniform.cdf(1.1), 1.0)
        
        # Test mean and variance
        self.assertEqual(uniform.mean, 0.5)
        self.assertEqual(uniform.variance, 1/12)
        
        # Test quantile
        self.assertEqual(uniform.quantile(0.25), 0.25)
        self.assertEqual(uniform.quantile(0.75), 0.75)
        
        # Test sampling
        sample = uniform.sample()
        self.assertGreaterEqual(sample, 0.0)
        self.assertLessEqual(sample, 1.0)
        
        samples = uniform.sample(1000)
        self.assertEqual(len(samples), 1000)
        for s in samples:
            self.assertGreaterEqual(s, 0.0)
            self.assertLessEqual(s, 1.0)
    
    def test_parametric_distribution_implementation(self):
        """Test concrete implementation of ParametricDistribution"""
        params = {'mu': 0, 'sigma': 1}
        dist = TestParametricDistribution(params)
        
        # Test parameters method
        self.assertEqual(dist.parameters(), params)
    
    def test_expected_value_function(self):
        """Test the expected_value function"""
        # Create a discrete random variable with known mean
        rv = TestDiscreteRandomVariable([1, 2, 3], [0.2, 0.3, 0.5])
        
        # Test that expected_value returns the same as rv.mean()
        self.assertEqual(expected_value(rv), rv.mean)
    
    def test_variance_function(self):
        """Test the variance function"""
        # Create a discrete random variable with known variance
        rv = TestDiscreteRandomVariable([1, 2, 3], [0.2, 0.3, 0.5])
        
        # Test that variance function returns the same as rv.variance()
        self.assertEqual(variance(rv), rv.variance)
    
    def test_covariance_function(self):
        """Test the covariance function"""
        # Create two discrete random variables
        rv1 = TestDiscreteRandomVariable([1, 2], [0.5, 0.5])
        rv2 = TestDiscreteRandomVariable([10, 20], [0.5, 0.5])
        
        # Define a joint sampler that creates perfectly correlated samples
        def joint_sampler(size):
            import random
            if size is None:
                size = 1
            samples = []
            for _ in range(size):
                # Generate a random number to determine which pair to select
                if random.random() < 0.5:
                    samples.append(([1], [10]))
                else:
                    samples.append(([2], [20]))
            return samples[0] if size == 1 else samples
        
        # Calculate covariance
        cov = covariance(rv1, rv2, joint_sampler)
        
        # Currently covariance is not implemented and returns None
        self.assertIsNone(cov)


if __name__ == '__main__':
    unittest.main()