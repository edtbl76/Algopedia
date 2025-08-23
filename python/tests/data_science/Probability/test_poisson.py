import unittest
import sys
import os
import math
from itertools import islice

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.probability.discrete.Poisson import PoissonDistribution


class TestPoissonDistribution(unittest.TestCase):
    def test_init_valid_parameters(self):
        """Test initialization with valid lambda rate"""
        # Test with lambda=1
        p = PoissonDistribution(1.0)
        self.assertEqual(p.lambda_rate, 1.0)
        
        # Test with lambda=5.5
        p_large = PoissonDistribution(5.5)
        self.assertEqual(p_large.lambda_rate, 5.5)
        
        # Test with lambda=0.1
        p_small = PoissonDistribution(0.1)
        self.assertEqual(p_small.lambda_rate, 0.1)
    
    def test_init_invalid_parameters(self):
        """Test initialization with invalid lambda rate"""
        # Test with negative lambda
        with self.assertRaises(ValueError):
            PoissonDistribution(-1.0)
        
        # Test with zero lambda should raise ValueError per current validation
        with self.assertRaises(ValueError):
            PoissonDistribution(0.0)
    
    def test_pmf(self):
        """Test probability mass function"""
        # Simple case: lambda=1
        p = PoissonDistribution(1.0)
        
        # P(X=0) = e^(-1) * 1^0 / 0! = e^(-1) ≈ 0.3679
        self.assertAlmostEqual(p.pmf(0), math.exp(-1), places=4)
        
        # P(X=1) = e^(-1) * 1^1 / 1! = e^(-1) ≈ 0.3679
        self.assertAlmostEqual(p.pmf(1), math.exp(-1), places=4)
        
        # P(X=2) = e^(-1) * 1^2 / 2! = e^(-1) / 2 ≈ 0.1839
        self.assertAlmostEqual(p.pmf(2), math.exp(-1) / 2, places=4)
        
        # PMF at invalid values
        self.assertEqual(p.pmf(-1), 0)
        
        
        # Test with larger lambda
        p_large = PoissonDistribution(10.0)
        # The mode of Poisson(10) is at k=10 (or k=9 due to integer constraint)
        # So pmf should increase up to around k=10 and then decrease
        self.assertGreater(p_large.pmf(10), p_large.pmf(5))
        self.assertGreater(p_large.pmf(10), p_large.pmf(15))
    
    def test_mean(self):
        """Test mean calculation"""
        # Mean = lambda
        
        # lambda=1 -> mean = 1
        p = PoissonDistribution(1.0)
        self.assertEqual(p.mean, 1.0)
        
        # lambda=5.5 -> mean = 5.5
        p_large = PoissonDistribution(5.5)
        self.assertEqual(p_large.mean, 5.5)
        
        # Zero lambda is invalid per current implementation; no test here
    
    def test_variance(self):
        """Test variance calculation"""
        # Variance = lambda
        
        # lambda=1 -> variance = 1
        p = PoissonDistribution(1.0)
        self.assertEqual(p.variance, 1.0)
        
        # lambda=5.5 -> variance = 5.5
        p_large = PoissonDistribution(5.5)
        self.assertEqual(p_large.variance, 5.5)
        
        # Zero lambda is invalid per current implementation; no test here
    
    def test_cdf(self):
        """Test cumulative distribution function"""
        # Simple case: lambda=1
        p = PoissonDistribution(1.0)
        
        # F(0) = P(X=0) = e^(-1) ≈ 0.3679
        self.assertAlmostEqual(p.cdf(0), math.exp(-1), places=4)
        
        # F(1) = P(X=0) + P(X=1) = e^(-1) + e^(-1) = 2*e^(-1) ≈ 0.7358
        self.assertAlmostEqual(p.cdf(1), 2 * math.exp(-1), places=4)
        
        # CDF at invalid values
        self.assertEqual(p.cdf(-1), 0.0)
    
    def test_sample_single(self):
        """Test sampling a single value"""
        # With lambda=1, should return a non-negative integer
        p = PoissonDistribution(1.0)
        sample = p.sample()
        self.assertIsInstance(sample, int)
        self.assertGreaterEqual(sample, 0)
    
    def test_sample_multiple(self):
        """Test sampling multiple values"""
        p = PoissonDistribution(3.0)
        samples = p.sample(1000)
        
        # Check that we got the right number of samples
        self.assertEqual(len(samples), 1000)
        
        # Check that all samples are non-negative integers
        for sample in samples:
            self.assertIsInstance(sample, int)
            self.assertGreaterEqual(sample, 0)
        
        # Check that the mean is approximately lambda
        # Allow for some random variation
        mean = sum(samples) / len(samples)
        self.assertGreater(mean, 2.8)
        self.assertLess(mean, 3.2)
        
        # Check that the variance is approximately lambda
        variance = sum((x - mean) ** 2 for x in samples) / len(samples)
        self.assertGreater(variance, 2.7)
        self.assertLess(variance, 3.3)
    
    def test_support(self):
        """Test the support method"""
        # Support should be {0, 1, 2, ...} but we can only check a finite portion
        p = PoissonDistribution(1.0)
        first_twenty = list(islice(p.support(), 20))
        
        # Check that the first few values are as expected
        self.assertEqual(first_twenty[:5], [0, 1, 2, 3, 4])
        
        # Ensure we retrieved exactly 20 items from the infinite iterator
        self.assertEqual(len(first_twenty), 20)
    
    def test_standard_deviation(self):
        """Test standard deviation calculation"""
        # Standard deviation = sqrt(variance) = sqrt(lambda)
        
        # lambda=1 -> std = 1
        p = PoissonDistribution(1.0)
        self.assertEqual(p.standard_deviation, 1.0)
        
        # lambda=4 -> std = 2
        p2 = PoissonDistribution(4.0)
        self.assertEqual(p2.standard_deviation, 2.0)
        
        # lambda=2.25 -> std = 1.5
        p3 = PoissonDistribution(2.25)
        self.assertEqual(p3.standard_deviation, 1.5)
    
    def test_equality(self):
        """Test equality comparison"""
        p1 = PoissonDistribution(1.0)
        p2 = PoissonDistribution(1.0)
        p3 = PoissonDistribution(2.0)
        
        # Same lambda should be equal
        self.assertEqual(p1, p2)
        
        # Different lambda should not be equal
        self.assertNotEqual(p1, p3)
        
        # Different types should not be equal
        self.assertNotEqual(p1, "not a distribution")
    
    def test_hash(self):
        """Test hash function"""
        p1 = PoissonDistribution(1.0)
        p2 = PoissonDistribution(1.0)
        
        # Same lambda should have same hash
        self.assertEqual(hash(p1), hash(p2))
        
        # Can be used as dictionary key
        d = {p1: "test"}
        self.assertEqual(d[p2], "test")
    
    def test_generate_single_sample(self):
        """Test the internal _generate_single_sample method"""
        # This is an internal method, but we can test it indirectly
        p = PoissonDistribution(1.0)
        
        # Generate many samples and check they're reasonable
        samples = [p._generate_single_sample() for _ in range(1000)]
        
        # All samples should be non-negative integers
        for sample in samples:
            self.assertIsInstance(sample, int)
            self.assertGreaterEqual(sample, 0)
        
        # Mean should be approximately lambda
        mean = sum(samples) / len(samples)
        self.assertGreater(mean, 0.9)
        self.assertLess(mean, 1.1)


if __name__ == '__main__':
    unittest.main()