import unittest
import sys
import os
import math

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.probability.discrete.Binomial import BinomialDistribution


class TestBinomialDistribution(unittest.TestCase):
    def test_init_valid_parameters(self):
        """Test initialization with valid parameters"""
        # Test with n=10, p=0.5
        b = BinomialDistribution(10, 0.5)
        self.assertEqual(b.trials, 10)
        self.assertEqual(b.probability, 0.5)
        
        # Test with n=1, p=0.5 (should be equivalent to Bernoulli)
        b_bern = BinomialDistribution(1, 0.5)
        self.assertEqual(b_bern.trials, 1)
        self.assertEqual(b_bern.probability, 0.5)
        
        # Test with extreme probabilities
        b_zero = BinomialDistribution(5, 0.0)
        self.assertEqual(b_zero.probability, 0.0)
        
        b_one = BinomialDistribution(5, 1.0)
        self.assertEqual(b_one.probability, 1.0)
    
    def test_init_invalid_parameters(self):
        """Test initialization with invalid parameters"""
        # Test with negative trials
        with self.assertRaises(ValueError):
            BinomialDistribution(-1, 0.5)
        
        # Test with zero trials
        with self.assertRaises(ValueError):
            BinomialDistribution(0, 0.5)
        
        # Test with negative probability
        with self.assertRaises(ValueError):
            BinomialDistribution(10, -0.1)
        
        # Test with probability > 1
        with self.assertRaises(ValueError):
            BinomialDistribution(10, 1.1)
    
    def test_pmf(self):
        """Test probability mass function"""
        # Simple case: n=2, p=0.5
        b = BinomialDistribution(2, 0.5)
        
        # P(X=0) = (2 choose 0) * 0.5^0 * 0.5^2 = 1 * 1 * 0.25 = 0.25
        self.assertAlmostEqual(b.pmf(0), 0.25)
        
        # P(X=1) = (2 choose 1) * 0.5^1 * 0.5^1 = 2 * 0.5 * 0.5 = 0.5
        self.assertAlmostEqual(b.pmf(1), 0.5)
        
        # P(X=2) = (2 choose 2) * 0.5^2 * 0.5^0 = 1 * 0.25 * 1 = 0.25
        self.assertAlmostEqual(b.pmf(2), 0.25)
        
        # PMF at invalid values
        self.assertEqual(b.pmf(-1), 0)
        self.assertEqual(b.pmf(3), 0)
        
        # Special case: p=0
        b_zero = BinomialDistribution(5, 0.0)
        self.assertEqual(b_zero.pmf(0), 1.0)  # All mass at 0
        self.assertEqual(b_zero.pmf(1), 0.0)
        
        # Special case: p=1
        b_one = BinomialDistribution(5, 1.0)
        self.assertEqual(b_one.pmf(5), 1.0)  # All mass at n
        self.assertEqual(b_one.pmf(4), 0.0)
    
    def test_mean(self):
        """Test mean calculation"""
        # Mean = n*p
        
        # n=10, p=0.5 -> mean = 5
        b = BinomialDistribution(10, 0.5)
        self.assertEqual(b.mean, 5.0)
        
        # n=20, p=0.3 -> mean = 6
        b2 = BinomialDistribution(20, 0.3)
        self.assertEqual(b2.mean, 6.0)
        
        # Special case: p=0 -> mean = 0
        b_zero = BinomialDistribution(5, 0.0)
        self.assertEqual(b_zero.mean, 0.0)
        
        # Special case: p=1 -> mean = n
        b_one = BinomialDistribution(5, 1.0)
        self.assertEqual(b_one.mean, 5.0)
    
    def test_variance(self):
        """Test variance calculation"""
        # Variance = n*p*(1-p)
        
        # n=10, p=0.5 -> variance = 10*0.5*0.5 = 2.5
        b = BinomialDistribution(10, 0.5)
        self.assertEqual(b.variance, 2.5)
        
        # n=20, p=0.3 -> variance = 20*0.3*0.7 = 4.2
        b2 = BinomialDistribution(20, 0.3)
        self.assertAlmostEqual(b2.variance, 4.2)
        
        # Special case: p=0 -> variance = 0
        b_zero = BinomialDistribution(5, 0.0)
        self.assertEqual(b_zero.variance, 0.0)
        
        # Special case: p=1 -> variance = 0
        b_one = BinomialDistribution(5, 1.0)
        self.assertEqual(b_one.variance, 0.0)
    
    def test_cdf(self):
        """Test cumulative distribution function"""
        # Simple case: n=2, p=0.5
        b = BinomialDistribution(2, 0.5)
        
        # F(0) = P(X=0) = 0.25
        self.assertAlmostEqual(b.cdf(0), 0.25)
        
        # F(1) = P(X=0) + P(X=1) = 0.25 + 0.5 = 0.75
        self.assertAlmostEqual(b.cdf(1), 0.75)
        
        # F(2) = P(X=0) + P(X=1) + P(X=2) = 0.25 + 0.5 + 0.25 = 1.0
        self.assertAlmostEqual(b.cdf(2), 1.0)
        
        # CDF at invalid values
        self.assertEqual(b.cdf(-1), 0.0)
        self.assertEqual(b.cdf(3), 1.0)
        
        # Special case: p=0
        b_zero = BinomialDistribution(5, 0.0)
        self.assertEqual(b_zero.cdf(0), 1.0)  # All mass at 0
        
        # Special case: p=1
        b_one = BinomialDistribution(5, 1.0)
        self.assertEqual(b_one.cdf(4), 0.0)  # No mass below n
        self.assertEqual(b_one.cdf(5), 1.0)  # All mass at n
    
    def test_sample_single(self):
        """Test sampling a single value"""
        # With p=0, should always return 0
        b_zero = BinomialDistribution(5, 0.0)
        self.assertEqual(b_zero.sample(), 0)
        
        # With p=1, should always return n
        b_one = BinomialDistribution(5, 1.0)
        self.assertEqual(b_one.sample(), 5)
        
        # With n=10, p=0.5, should return an integer between 0 and 10
        b = BinomialDistribution(10, 0.5)
        sample = b.sample()
        self.assertIsInstance(sample, int)
        self.assertGreaterEqual(sample, 0)
        self.assertLessEqual(sample, 10)
    
    def test_sample_multiple(self):
        """Test sampling multiple values"""
        b = BinomialDistribution(10, 0.5)
        samples = b.sample(1000)
        
        # Check that we got the right number of samples
        self.assertEqual(len(samples), 1000)
        
        # Check that all samples are integers between 0 and n
        for sample in samples:
            self.assertIsInstance(sample, int)
            self.assertGreaterEqual(sample, 0)
            self.assertLessEqual(sample, 10)
        
        # Check that the mean is approximately n*p
        # Allow for some random variation
        mean = sum(samples) / len(samples)
        self.assertGreater(mean, 4.7)
        self.assertLess(mean, 5.3)
    
    def test_support(self):
        """Test the support method"""
        # n=3, p=0.5 -> support = {0, 1, 2, 3}
        b = BinomialDistribution(3, 0.5)
        support = list(b.support())
        self.assertEqual(support, [0, 1, 2, 3])
        
        # Special case: p=0 -> support should still be {0, 1, ..., n}
        # even though all probability mass is at 0
        b_zero = BinomialDistribution(2, 0.0)
        support_zero = list(b_zero.support())
        self.assertEqual(support_zero, [0, 1, 2])
    
    def test_standard_deviation(self):
        """Test standard deviation calculation"""
        # Standard deviation = sqrt(variance) = sqrt(n*p*(1-p))
        
        # n=10, p=0.5 -> std = sqrt(2.5) = 1.5811...
        b = BinomialDistribution(10, 0.5)
        self.assertAlmostEqual(b.standard_deviation, math.sqrt(2.5))
        
        # n=20, p=0.3 -> std = sqrt(4.2) = 2.0494...
        b2 = BinomialDistribution(20, 0.3)
        self.assertAlmostEqual(b2.standard_deviation, math.sqrt(4.2))
    
    def test_equality(self):
        """Test equality comparison"""
        b1 = BinomialDistribution(10, 0.5)
        b2 = BinomialDistribution(10, 0.5)
        b3 = BinomialDistribution(10, 0.3)
        b4 = BinomialDistribution(5, 0.5)
        
        # Same parameters should be equal
        self.assertEqual(b1, b2)
        
        # Different probability should not be equal
        self.assertNotEqual(b1, b3)
        
        # Different trials should not be equal
        self.assertNotEqual(b1, b4)
        
        # Different types should not be equal
        self.assertNotEqual(b1, "not a distribution")
    
    def test_hash(self):
        """Test hash function"""
        b1 = BinomialDistribution(10, 0.5)
        b2 = BinomialDistribution(10, 0.5)
        
        # Same parameters should have same hash
        self.assertEqual(hash(b1), hash(b2))
        
        # Can be used as dictionary key
        d = {b1: "test"}
        self.assertEqual(d[b2], "test")


if __name__ == '__main__':
    unittest.main()