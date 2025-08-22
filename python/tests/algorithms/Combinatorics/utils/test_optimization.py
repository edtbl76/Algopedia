"""
Tests for optimization utilities in the Combinatorics module.
"""
import unittest

from algorithms.Combinatorics.utils.optimization import optimize_k


class TestOptimization(unittest.TestCase):
    """Test cases for optimization utilities."""

    def test_optimize_k_symmetry(self):
        """Test that optimize_k correctly applies the symmetry property."""
        test_cases = [
            # n, k, expected
            (10, 3, 3),     # k < n/2, should return k
            (10, 7, 3),     # k > n/2, should return n-k
            (10, 5, 5),     # k = n/2, should return k
            (11, 6, 5),     # k > n/2 for odd n
            (11, 5, 5),     # k < n/2 for odd n
            (0, 0, 0),      # Edge case: n=k=0
        ]
        
        for n, k, expected in test_cases:
            with self.subTest(n=n, k=k):
                result = optimize_k(n, k)
                self.assertEqual(result, expected)
    
    def test_optimize_k_boundary_cases(self):
        """Test optimize_k with boundary cases."""
        # Edge cases
        self.assertEqual(optimize_k(5, 0), 0)  # k=0
        self.assertEqual(optimize_k(5, 5), 0)  # k=n
        
        # Large numbers
        large_n = 1000
        self.assertEqual(optimize_k(large_n, 300), 300)  # k < n/2
        self.assertEqual(optimize_k(large_n, 700), 300)  # k > n/2
        self.assertEqual(optimize_k(large_n, 500), 500)  # k = n/2
    
    def test_optimize_k_mathematical_property(self):
        """Test that optimize_k preserves the mathematical property C(n,k) = C(n,n-k)."""
        # This test verifies the mathematical foundation of the optimization
        # We don't actually compute C(n,k) here, but verify that min(k, n-k) is returned
        
        for n in range(1, 20):  # Test with various n values
            for k in range(n + 1):  # Test all valid k values for each n
                result = optimize_k(n, k)
                # The result should be the minimum of k and n-k
                expected = min(k, n - k)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()