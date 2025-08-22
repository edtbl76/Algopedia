"""
Tests for combination functions in the Combinatorics module.
"""
import unittest

from algorithms.Combinatorics.combinations import (
    binomial_coefficient,
    BinomialMethod,
)


class TestCombinations(unittest.TestCase):
    """Test cases for combination functions."""

    def test_binomial_coefficient_small_values(self):
        """Test binomial_coefficient with small values."""
        test_cases = [
            # n, k, expected
            (5, 2, 10),      # C(5,2) = 10
            (5, 0, 1),       # C(5,0) = 1
            (5, 5, 1),       # C(5,5) = 1
            (0, 0, 1),       # C(0,0) = 1
            (10, 3, 120),    # C(10,3) = 120
            (10, 7, 120),    # C(10,7) = 120 (symmetry property)
        ]
        
        for n, k, expected in test_cases:
            with self.subTest(n=n, k=k):
                result = binomial_coefficient(n, k)
                self.assertEqual(result, expected)
    
    def test_binomial_coefficient_methods(self):
        """Test all methods of binomial_coefficient function."""
        # Test cases
        test_cases = [
            (5, 2, 10),
            (10, 5, 252),
            (20, 10, 184756),
        ]
        
        # Test each method
        for method in BinomialMethod:
            for n, k, expected in test_cases:
                with self.subTest(method=method.value, n=n, k=k):
                    result = binomial_coefficient(n, k, method)
                    self.assertEqual(result, expected)
    
    def test_binomial_coefficient_symmetry(self):
        """Test the symmetry property: C(n,k) = C(n,n-k)."""
        test_cases = [
            (10, 3),
            (15, 7),
            (20, 8),
        ]
        
        for n, k in test_cases:
            with self.subTest(n=n, k=k):
                result1 = binomial_coefficient(n, k)
                result2 = binomial_coefficient(n, n - k)
                self.assertEqual(result1, result2)
    
    def test_binomial_coefficient_pascal_identity(self):
        """Test Pascal's identity: C(n,k) = C(n-1,k-1) + C(n-1,k)."""
        test_cases = [
            (10, 5),
            (15, 7),
            (20, 10),
        ]
        
        for n, k in test_cases:
            with self.subTest(n=n, k=k):
                if k > 0 and k < n:  # Ensure valid inputs for the identity
                    result = binomial_coefficient(n, k)
                    expected = binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
                    self.assertEqual(result, expected)
    
    def test_binomial_coefficient_edge_cases(self):
        """Test edge cases for binomial_coefficient."""
        # C(n,0) = 1 for any n
        for n in range(10):
            self.assertEqual(binomial_coefficient(n, 0), 1)
        
        # C(n,n) = 1 for any n
        for n in range(10):
            self.assertEqual(binomial_coefficient(n, n), 1)
    
    def test_binomial_coefficient_large_values(self):
        """Test binomial_coefficient with larger values."""
        # C(30,15) = 155117520
        self.assertEqual(binomial_coefficient(30, 15), 155117520)
        
        # C(25,10) = 3268760
        self.assertEqual(binomial_coefficient(25, 10), 3268760)
        
        # Test with different methods for large values
        for method in BinomialMethod:
            with self.subTest(method=method.value):
                self.assertEqual(binomial_coefficient(25, 10, method), 3268760)


if __name__ == "__main__":
    unittest.main()