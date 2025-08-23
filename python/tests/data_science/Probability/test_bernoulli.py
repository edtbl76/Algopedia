import unittest
import sys
import os
import math

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.probability.discrete.Bernoulli import BernoulliDistribution


class TestBernoulliDistribution(unittest.TestCase):
    def test_init_valid_probability(self):
        """Test initialization with valid probability values"""
        # Test with probability 0
        b0 = BernoulliDistribution(0.0)
        self.assertEqual(b0.probability, 0.0)
        
        # Test with probability 0.5
        b_half = BernoulliDistribution(0.5)
        self.assertEqual(b_half.probability, 0.5)
        
        # Test with probability 1
        b1 = BernoulliDistribution(1.0)
        self.assertEqual(b1.probability, 1.0)
    
    def test_init_invalid_probability(self):
        """Test initialization with invalid probability values"""
        # Test with negative probability
        with self.assertRaises(ValueError):
            BernoulliDistribution(-0.1)
        
        # Test with probability > 1
        with self.assertRaises(ValueError):
            BernoulliDistribution(1.1)
    
    def test_pmf(self):
        """Test probability mass function"""
        b = BernoulliDistribution(0.7)
        
        # PMF at k=0
        self.assertAlmostEqual(b.pmf(0), 0.3)
        
        # PMF at k=1
        self.assertAlmostEqual(b.pmf(1), 0.7)
        
        # PMF at invalid values
        self.assertEqual(b.pmf(2), 0)
        self.assertEqual(b.pmf(-1), 0)
    
    def test_mean(self):
        """Test mean calculation"""
        # Mean with p=0
        b0 = BernoulliDistribution(0.0)
        self.assertEqual(b0.mean, 0.0)
        
        # Mean with p=0.5
        b_half = BernoulliDistribution(0.5)
        self.assertEqual(b_half.mean, 0.5)
        
        # Mean with p=1
        b1 = BernoulliDistribution(1.0)
        self.assertEqual(b1.mean, 1.0)
    
    def test_variance(self):
        """Test variance calculation"""
        # Variance with p=0
        b0 = BernoulliDistribution(0.0)
        self.assertEqual(b0.variance, 0.0)
        
        # Variance with p=0.5 (should be 0.25)
        b_half = BernoulliDistribution(0.5)
        self.assertEqual(b_half.variance, 0.25)
        
        # Variance with p=1
        b1 = BernoulliDistribution(1.0)
        self.assertEqual(b1.variance, 0.0)
        
        # Variance with p=0.7 (should be 0.7 * 0.3 = 0.21)
        b = BernoulliDistribution(0.7)
        self.assertAlmostEqual(b.variance, 0.21)
    
    def test_cdf(self):
        """Test cumulative distribution function"""
        b = BernoulliDistribution(0.7)
        
        # CDF for values < 0
        self.assertEqual(b.cdf(-1), 0.0)
        
        # CDF for 0 <= values < 1
        self.assertAlmostEqual(b.cdf(0), 0.3)
        self.assertAlmostEqual(b.cdf(0.5), 0.3)  # Should still be F(0)
        
        # CDF for values >= 1
        self.assertEqual(b.cdf(1), 1.0)
        self.assertEqual(b.cdf(2), 1.0)
    
    def test_sample_single(self):
        """Test sampling a single value"""
        # With p=0, should always return 0
        b0 = BernoulliDistribution(0.0)
        self.assertEqual(b0.sample(), 0)
        
        # With p=1, should always return 1
        b1 = BernoulliDistribution(1.0)
        self.assertEqual(b1.sample(), 1)
        
        # With p=0.5, should return either 0 or 1
        b_half = BernoulliDistribution(0.5)
        sample = b_half.sample()
        self.assertIn(sample, [0, 1])
    
    def test_sample_multiple(self):
        """Test sampling multiple values"""
        b = BernoulliDistribution(0.7)
        samples = b.sample(1000)
        
        # Check that we got the right number of samples
        self.assertEqual(len(samples), 1000)
        
        # Check that all samples are either 0 or 1
        for sample in samples:
            self.assertIn(sample, [0, 1])
        
        # Check that the proportion of 1s is approximately 0.7
        # Allow for some random variation
        proportion_of_ones = sum(samples) / len(samples)
        self.assertGreater(proportion_of_ones, 0.65)
        self.assertLess(proportion_of_ones, 0.75)
    
    def test_support(self):
        """Test the support method"""
        b = BernoulliDistribution(0.7)
        support = list(b.support())
        
        # Support should be [0, 1]
        self.assertEqual(support, [0, 1])
    
    def test_standard_deviation(self):
        """Test standard deviation calculation"""
        # Standard deviation with p=0.5 (should be 0.5)
        b_half = BernoulliDistribution(0.5)
        self.assertEqual(b_half.standard_deviation, 0.5)
        
        # Standard deviation with p=0.7 (should be sqrt(0.21))
        b = BernoulliDistribution(0.7)
        self.assertAlmostEqual(b.standard_deviation, math.sqrt(0.21))
    
    def test_equality(self):
        """Test equality comparison"""
        b1 = BernoulliDistribution(0.7)
        b2 = BernoulliDistribution(0.7)
        b3 = BernoulliDistribution(0.5)
        
        # Same probability should be equal
        self.assertEqual(b1, b2)
        
        # Different probability should not be equal
        self.assertNotEqual(b1, b3)
        
        # Different types should not be equal
        self.assertNotEqual(b1, "not a distribution")
    
    def test_hash(self):
        """Test hash function"""
        b1 = BernoulliDistribution(0.7)
        b2 = BernoulliDistribution(0.7)
        
        # Same probability should have same hash
        self.assertEqual(hash(b1), hash(b2))
        
        # Can be used as dictionary key
        d = {b1: "test"}
        self.assertEqual(d[b2], "test")


if __name__ == '__main__':
    unittest.main()