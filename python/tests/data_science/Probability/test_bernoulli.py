import unittest
import sys
import os
import math
import random

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.Probability.Bernoulli import BernoulliDistribution


class TestBernoulliDistribution(unittest.TestCase):
    def test_initialization_valid_probability(self):
        """Test initialization with valid probability values"""
        # Test with probability 0
        dist_0 = BernoulliDistribution(0)
        self.assertEqual(dist_0.probability, 0)
        
        # Test with probability 0.5
        dist_half = BernoulliDistribution(0.5)
        self.assertEqual(dist_half.probability, 0.5)
        
        # Test with probability 1
        dist_1 = BernoulliDistribution(1)
        self.assertEqual(dist_1.probability, 1)
        
        # Test with probability 0.3
        dist_03 = BernoulliDistribution(0.3)
        self.assertEqual(dist_03.probability, 0.3)

    def test_initialization_invalid_probability(self):
        """Test initialization with invalid probability values"""
        # Test with probability less than 0
        with self.assertRaises(ValueError):
            BernoulliDistribution(-0.1)
        
        # Test with probability greater than 1
        with self.assertRaises(ValueError):
            BernoulliDistribution(1.1)
        
        # Test with non-numeric value
        with self.assertRaises(TypeError):
            BernoulliDistribution("0.5")

    def test_pmf_valid_inputs(self):
        """Test PMF calculation with valid inputs"""
        # Test with probability 0.7
        dist = BernoulliDistribution(0.7)
        
        # Test PMF for k=0
        self.assertAlmostEqual(dist.pmf(0), 0.3)
        
        # Test PMF for k=1
        self.assertAlmostEqual(dist.pmf(1), 0.7)
        
        # Test with probability 0
        dist_0 = BernoulliDistribution(0)
        self.assertEqual(dist_0.pmf(0), 1)
        self.assertEqual(dist_0.pmf(1), 0)
        
        # Test with probability 1
        dist_1 = BernoulliDistribution(1)
        self.assertEqual(dist_1.pmf(0), 0)
        self.assertEqual(dist_1.pmf(1), 1)

    def test_pmf_invalid_inputs(self):
        """Test PMF calculation with invalid inputs"""
        dist = BernoulliDistribution(0.5)
        
        # Test with k < 0
        with self.assertRaises(ValueError):
            dist.pmf(-1)
        
        # Test with k > 1
        with self.assertRaises(ValueError):
            dist.pmf(2)
        
        # Test with non-integer k
        with self.assertRaises(ValueError):
            dist.pmf(0.5)
        
        # Test with non-numeric k
        with self.assertRaises(ValueError):
            dist.pmf("0")

    def test_mean_property(self):
        """Test mean property calculation"""
        # Test with probability 0.6
        dist = BernoulliDistribution(0.6)
        self.assertEqual(dist.mean, 0.6)
        
        # Test with probability 0
        dist_0 = BernoulliDistribution(0)
        self.assertEqual(dist_0.mean, 0)
        
        # Test with probability 1
        dist_1 = BernoulliDistribution(1)
        self.assertEqual(dist_1.mean, 1)
        
        # Test with probability 0.25
        dist_025 = BernoulliDistribution(0.25)
        self.assertEqual(dist_025.mean, 0.25)

    def test_variance_property(self):
        """Test variance property calculation"""
        # Test with probability 0.6
        dist = BernoulliDistribution(0.6)
        self.assertAlmostEqual(dist.variance, 0.24)  # 0.6 * (1 - 0.6) = 0.24
        
        # Test with probability 0
        dist_0 = BernoulliDistribution(0)
        self.assertEqual(dist_0.variance, 0)  # 0 * (1 - 0) = 0
        
        # Test with probability 1
        dist_1 = BernoulliDistribution(1)
        self.assertEqual(dist_1.variance, 0)  # 1 * (1 - 1) = 0
        
        # Test with probability 0.5 (maximum variance)
        dist_05 = BernoulliDistribution(0.5)
        self.assertEqual(dist_05.variance, 0.25)  # 0.5 * (1 - 0.5) = 0.25

    def test_standard_deviation_property(self):
        """Test standard deviation property calculation"""
        # Test with probability 0.6
        dist = BernoulliDistribution(0.6)
        expected_std = math.sqrt(0.6 * 0.4)
        self.assertAlmostEqual(dist.standard_deviation, expected_std)
        
        # Test with probability 0
        dist_0 = BernoulliDistribution(0)
        self.assertEqual(dist_0.standard_deviation, 0)
        
        # Test with probability 1
        dist_1 = BernoulliDistribution(1)
        self.assertEqual(dist_1.standard_deviation, 0)
        
        # Test with probability 0.5 (maximum standard deviation)
        dist_05 = BernoulliDistribution(0.5)
        self.assertEqual(dist_05.standard_deviation, 0.5)  # sqrt(0.25) = 0.5

    def test_mathematical_properties(self):
        """Test mathematical properties of Bernoulli distribution"""
        # Test that variance is maximum when p = 0.5
        dist_05 = BernoulliDistribution(0.5)
        dist_04 = BernoulliDistribution(0.4)
        dist_06 = BernoulliDistribution(0.6)
        
        self.assertGreater(dist_05.variance, dist_04.variance)
        self.assertGreater(dist_05.variance, dist_06.variance)
        
        # Test that variance approaches 0 as p approaches 0 or 1
        dist_001 = BernoulliDistribution(0.01)
        dist_099 = BernoulliDistribution(0.99)
        
        self.assertLess(dist_001.variance, 0.01)
        self.assertLess(dist_099.variance, 0.01)
        
        # Test that standard deviation is sqrt(p * (1-p))
        dist = BernoulliDistribution(0.3)
        expected_std = math.sqrt(0.3 * 0.7)
        self.assertAlmostEqual(math.sqrt(dist.variance), expected_std)

    def test_pmf_sum_to_one(self):
        """Test that PMF values sum to 1 for any valid probability"""
        probabilities = [0, 0.25, 0.5, 0.75, 1]
        
        for p in probabilities:
            dist = BernoulliDistribution(p)
            pmf_sum = dist.pmf(0) + dist.pmf(1)
            self.assertAlmostEqual(pmf_sum, 1.0)
            
    def test_cdf_calculation(self):
        """Test CDF calculation for Bernoulli distribution"""
        # Test with probability 0.7
        dist = BernoulliDistribution(0.7)
        
        # Test CDF for k < 0
        self.assertEqual(dist.cdf(-1), 0.0)
        
        # Test CDF for k = 0
        self.assertAlmostEqual(dist.cdf(0), 0.3)  # P(X ≤ 0) = P(X = 0) = 1 - p
        
        # Test CDF for k = 1
        self.assertEqual(dist.cdf(1), 1.0)  # P(X ≤ 1) = P(X = 0) + P(X = 1) = 1
        
        # Test CDF for k > 1
        self.assertEqual(dist.cdf(2), 1.0)  # P(X ≤ 2) = 1 since X ≤ 1 always
        
        # Test with probability 0
        dist_0 = BernoulliDistribution(0)
        self.assertEqual(dist_0.cdf(-1), 0.0)
        self.assertEqual(dist_0.cdf(0), 1.0)
        self.assertEqual(dist_0.cdf(1), 1.0)
        
        # Test with probability 1
        dist_1 = BernoulliDistribution(1)
        self.assertEqual(dist_1.cdf(-1), 0.0)
        self.assertEqual(dist_1.cdf(0), 0.0)
        self.assertEqual(dist_1.cdf(1), 1.0)

    def test_sample_method(self):
        """Test sample method for Bernoulli distribution"""
        # Test with probability 1 (should always return 1)
        dist_1 = BernoulliDistribution(1)
        for i in range(10):
            random_value = random.random()
            self.assertEqual(dist_1.sample(random_value), 1)
        
        # Test with probability 0 (should always return 0)
        dist_0 = BernoulliDistribution(0)
        for i in range(10):
            random_value = random.random()
            self.assertEqual(dist_0.sample(random_value), 0)
        
        # Test with probability 0.5
        dist_half = BernoulliDistribution(0.5)
        # For random_value < 0.5, should return 1
        self.assertEqual(dist_half.sample(0.4), 1)
        # For random_value >= 0.5, should return 0
        self.assertEqual(dist_half.sample(0.5), 0)
        self.assertEqual(dist_half.sample(0.6), 0)
        
        # Test with invalid random values
        with self.assertRaises(ValueError):
            dist_half.sample(-0.1)  # Less than 0
        with self.assertRaises(ValueError):
            dist_half.sample(1.1)   # Greater than 1

    def test_equality_method(self):
        """Test equality method for Bernoulli distribution"""
        # Test equal distributions
        dist1 = BernoulliDistribution(0.7)
        dist2 = BernoulliDistribution(0.7)
        self.assertEqual(dist1, dist2)
        
        # Test nearly equal distributions (within epsilon)
        dist3 = BernoulliDistribution(0.7 + 1e-11)
        self.assertEqual(dist1, dist3)
        
        # Test unequal distributions
        dist4 = BernoulliDistribution(0.8)
        self.assertNotEqual(dist1, dist4)
        
        # Test equality with non-BernoulliDistribution object
        self.assertNotEqual(dist1, "not a distribution")
        self.assertNotEqual(dist1, 0.7)

    def test_hash_method(self):
        """Test hash method for Bernoulli distribution"""
        # Create distributions with the same probability
        dist1 = BernoulliDistribution(0.7)
        dist2 = BernoulliDistribution(0.7)
        
        # Their hashes should be equal
        self.assertEqual(hash(dist1), hash(dist2))
        
        # Create a distribution with different probability
        dist3 = BernoulliDistribution(0.8)
        
        # Its hash should be different
        self.assertNotEqual(hash(dist1), hash(dist3))
        
        # Test using distributions as dictionary keys
        dist_dict = {dist1: "dist1", dist3: "dist3"}
        
        # Should be able to retrieve values using equivalent distributions
        dist1_copy = BernoulliDistribution(0.7)
        self.assertEqual(dist_dict[dist1_copy], "dist1")


if __name__ == '__main__':
    unittest.main()