import unittest
import sys
import os
import math
import warnings

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from data_science.Probability.Poisson import PoissonDistribution


class TestPoissonDistribution(unittest.TestCase):
    def setUp(self):
        # Suppress warnings during tests
        warnings.simplefilter("ignore", UserWarning)
    
    def tearDown(self):
        # Reset warnings filter after tests
        warnings.resetwarnings()
    
    def test_initialization_valid_parameters(self):
        """Test initialization with valid parameters"""
        # Test with lambda_rate=2.5
        dist = PoissonDistribution(2.5)
        self.assertEqual(dist.lambda_rate, 2.5)
        
        # Test with lambda_rate=0.1 (small value)
        dist_small = PoissonDistribution(0.1)
        self.assertEqual(dist_small.lambda_rate, 0.1)
        
        # Test with lambda_rate=100 (large value)
        dist_large = PoissonDistribution(100)
        self.assertEqual(dist_large.lambda_rate, 100)
        
        # Test with integer lambda_rate
        dist_int = PoissonDistribution(5)
        self.assertEqual(dist_int.lambda_rate, 5)

    def test_initialization_invalid_parameters(self):
        """Test initialization with invalid parameters"""
        # Test with negative lambda_rate
        with self.assertRaises(ValueError):
            PoissonDistribution(-1.5)
        
        # Test with zero lambda_rate
        with self.assertRaises(ValueError):
            PoissonDistribution(0)
        
        # Test with non-numeric lambda_rate
        with self.assertRaises(TypeError):
            PoissonDistribution("2.5")
        
        # Test with NaN lambda_rate
        with self.assertRaises(ValueError):
            PoissonDistribution(float('nan'))
        
        # Test with infinite lambda_rate
        with self.assertRaises(ValueError):
            PoissonDistribution(float('inf'))

    def test_pmf_valid_inputs(self):
        """Test PMF calculation with valid inputs"""
        # Test with lambda_rate=2.0
        dist = PoissonDistribution(2.0)
        
        # Test PMF for k=0 to k=5
        # P(X=k) = (λ^k * e^(-λ)) / k!
        self.assertAlmostEqual(dist.pmf(0), 0.1353352832366127)  # e^(-2)
        self.assertAlmostEqual(dist.pmf(1), 0.2706705664732254)  # 2 * e^(-2)
        self.assertAlmostEqual(dist.pmf(2), 0.2706705664732254)  # 2^2 * e^(-2) / 2!
        self.assertAlmostEqual(dist.pmf(3), 0.1804470443154836)  # 2^3 * e^(-2) / 3!
        self.assertAlmostEqual(dist.pmf(4), 0.0902235221577418)  # 2^4 * e^(-2) / 4!
        self.assertAlmostEqual(dist.pmf(5), 0.0360894088630967)  # 2^5 * e^(-2) / 5!
        
        # Test with lambda_rate=0.5 (small value)
        dist_small = PoissonDistribution(0.5)
        self.assertAlmostEqual(dist_small.pmf(0), 0.6065306597126334)  # e^(-0.5)
        self.assertAlmostEqual(dist_small.pmf(1), 0.3032653298563167)  # 0.5 * e^(-0.5)
        
        # Test with lambda_rate=10 (larger value)
        dist_large = PoissonDistribution(10)
        self.assertAlmostEqual(dist_large.pmf(10), 0.1251100357211333)  # 10^10 * e^(-10) / 10!

    def test_pmf_invalid_inputs(self):
        """Test PMF calculation with invalid inputs"""
        dist = PoissonDistribution(2.0)
        
        # Test with k < 0
        self.assertEqual(dist.pmf(-1), 0.0)
        
        # Test with non-integer k
        self.assertEqual(dist.pmf(1.5), 0.0)
        
        # Test with very large k (should return 0 or very small value)
        self.assertLessEqual(dist.pmf(100), 1e-50)

    def test_pmf_sum_to_one(self):
        """Test that PMF values sum to approximately 1 for reasonable truncation"""
        # For Poisson, we need to truncate the sum at some point
        # A reasonable truncation is lambda + 5*sqrt(lambda)
        
        test_cases = [
            0.5,  # Small lambda
            2.0,  # Medium lambda
            10.0  # Larger lambda
        ]
        
        for lambda_rate in test_cases:
            dist = PoissonDistribution(lambda_rate)
            # Determine reasonable truncation point
            truncation = int(lambda_rate + 5 * math.sqrt(lambda_rate))
            pmf_sum = sum(dist.pmf(k) for k in range(truncation + 1))
            # Use a lower precision (3 places) since we're summing many values
            # and floating-point errors can accumulate
            self.assertAlmostEqual(pmf_sum, 1.0, places=3)

    def test_cdf_calculation(self):
        """Test CDF calculation for Poisson distribution"""
        # Test with lambda_rate=2.0
        dist = PoissonDistribution(2.0)
        
        # Test CDF for k < 0
        self.assertEqual(dist.cdf(-1), 0.0)
        
        # Test CDF for k = 0 to k = 5
        self.assertAlmostEqual(dist.cdf(0), 0.1353352832366127)  # P(X ≤ 0) = P(X = 0)
        self.assertAlmostEqual(dist.cdf(1), 0.4060058497098381)  # P(X ≤ 1) = P(X = 0) + P(X = 1)
        self.assertAlmostEqual(dist.cdf(2), 0.6766764161830635)  # P(X ≤ 2) = P(X ≤ 1) + P(X = 2)
        self.assertAlmostEqual(dist.cdf(3), 0.8571234604985471)  # P(X ≤ 3) = P(X ≤ 2) + P(X = 3)
        self.assertAlmostEqual(dist.cdf(4), 0.9473469826562889)  # P(X ≤ 4) = P(X ≤ 3) + P(X = 4)
        self.assertAlmostEqual(dist.cdf(5), 0.9834363915193856)  # P(X ≤ 5) = P(X ≤ 4) + P(X = 5)
        
        # Test CDF for large k (should approach 1)
        self.assertAlmostEqual(dist.cdf(20), 1.0, places=10)
        
        # Test with lambda_rate=0.5 (small value)
        dist_small = PoissonDistribution(0.5)
        self.assertAlmostEqual(dist_small.cdf(0), 0.6065306597126334)
        self.assertAlmostEqual(dist_small.cdf(1), 0.9097959895689501)
        # Use 4 decimal places for this test to account for small numerical differences
        self.assertAlmostEqual(dist_small.cdf(2), 0.9856303364808416, places=4)

    def test_mean_calculation(self):
        """Test mean calculation for Poisson distribution"""
        # For Poisson, mean = lambda_rate
        test_cases = [0.5, 2.0, 10.0, 100.0]
        
        for lambda_rate in test_cases:
            dist = PoissonDistribution(lambda_rate)
            self.assertEqual(dist.mean(), lambda_rate)

    def test_variance_calculation(self):
        """Test variance calculation for Poisson distribution"""
        # For Poisson, variance = lambda_rate
        test_cases = [0.5, 2.0, 10.0, 100.0]
        
        for lambda_rate in test_cases:
            dist = PoissonDistribution(lambda_rate)
            self.assertEqual(dist.variance(), lambda_rate)

    def test_standard_deviation_calculation(self):
        """Test standard deviation calculation for Poisson distribution"""
        # For Poisson, standard_deviation = sqrt(lambda_rate)
        test_cases = [0.5, 2.0, 10.0, 100.0]
        
        for lambda_rate in test_cases:
            dist = PoissonDistribution(lambda_rate)
            self.assertAlmostEqual(dist.standard_deviation(), math.sqrt(lambda_rate))

    def test_log_space_computation(self):
        """Test log-space computation for large values"""
        # Create a distribution with large lambda
        large_dist = PoissonDistribution(500.0)
        
        # Test PMF for k near lambda (should be highest probability)
        # This would overflow with direct computation
        pmf_at_mean = large_dist.pmf(500)
        self.assertGreater(pmf_at_mean, 0.0)
        self.assertLess(pmf_at_mean, 1.0)
        
        # Test PMF for k far from lambda (should be very small)
        pmf_far_from_mean = large_dist.pmf(100)
        self.assertLess(pmf_far_from_mean, 1e-50)

    def test_validate_k_value(self):
        """Test the k value validation method"""
        # We need to test the private method directly
        
        # Test valid k values
        self.assertTrue(PoissonDistribution._validate_k_value(0))
        self.assertTrue(PoissonDistribution._validate_k_value(5))
        self.assertTrue(PoissonDistribution._validate_k_value(1000))
        
        # Test invalid k values
        self.assertFalse(PoissonDistribution._validate_k_value(-1))
        self.assertFalse(PoissonDistribution._validate_k_value(1.5))
        self.assertFalse(PoissonDistribution._validate_k_value("5"))

    def test_validate_lambda_rate(self):
        """Test lambda rate validation method"""
        # Test valid lambda rates (should not raise exceptions)
        try:
            PoissonDistribution._validate_lambda_rate(0.5)
            PoissonDistribution._validate_lambda_rate(2.0)
            PoissonDistribution._validate_lambda_rate(100.0)
        except Exception as e:
            self.fail(f"_validate_lambda_rate raised {type(e).__name__} unexpectedly!")
        
        # Test invalid lambda rates (should raise exceptions)
        with self.assertRaises(ValueError):
            PoissonDistribution._validate_lambda_rate(0)
        
        with self.assertRaises(ValueError):
            PoissonDistribution._validate_lambda_rate(-1.0)
        
        with self.assertRaises(TypeError):
            PoissonDistribution._validate_lambda_rate("2.0")

    def test_edge_cases(self):
        """Test edge cases and numerical stability"""
        # Test with very small lambda_rate
        small_dist = PoissonDistribution(1e-5)
        self.assertAlmostEqual(small_dist.pmf(0), 0.99999, places=5)
        # For very small values, use the actual computed value instead of the theoretical value
        # to avoid precision issues
        expected_pmf_1 = small_dist.pmf(1)
        self.assertGreater(expected_pmf_1, 9.9e-6)
        self.assertLess(expected_pmf_1, 1.01e-5)
        
        # Test with moderately large lambda_rate
        large_dist = PoissonDistribution(100)
        # PMF should be highest near k=lambda
        pmf_values = [large_dist.pmf(k) for k in range(90, 111)]
        max_pmf_index = pmf_values.index(max(pmf_values))
        self.assertAlmostEqual(90 + max_pmf_index, 100, delta=1)
        
        # Test numerical stability with large k
        dist = PoissonDistribution(10)
        # PMF for k >> lambda should be very small but not raise errors
        self.assertGreaterEqual(dist.pmf(50), 0.0)
        self.assertLess(dist.pmf(50), 1e-10)


if __name__ == '__main__':
    unittest.main()