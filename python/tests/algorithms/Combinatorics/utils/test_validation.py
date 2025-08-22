"""
Tests for validation utilities in the Combinatorics module.
"""
import unittest

from algorithms.Combinatorics.utils.validation import validate_inputs


class TestValidation(unittest.TestCase):
    """Test cases for validation utilities."""

    def test_valid_inputs(self):
        """Test that valid inputs don't raise exceptions."""
        # Test cases where n >= k >= 0
        test_cases = [
            (0, 0),  # Edge case: n=k=0
            (5, 0),  # Edge case: k=0
            (5, 5),  # Edge case: n=k
            (10, 5),  # Normal case: n>k>0
        ]
        
        for n, k in test_cases:
            with self.subTest(n=n, k=k):
                # Should not raise any exception
                validate_inputs(n, k)
    
    def test_negative_n(self):
        """Test that negative n raises ValueError."""
        with self.assertRaises(ValueError) as context:
            validate_inputs(-1, 0)
        
        self.assertEqual(str(context.exception), "n must be non-negative")
    
    def test_negative_k(self):
        """Test that negative k raises ValueError."""
        with self.assertRaises(ValueError) as context:
            validate_inputs(5, -1)
        
        self.assertEqual(str(context.exception), "k must be non-negative")
    
    def test_k_greater_than_n(self):
        """Test that k > n raises ValueError."""
        with self.assertRaises(ValueError) as context:
            validate_inputs(5, 6)
        
        self.assertEqual(str(context.exception), "k cannot be greater than n")


if __name__ == "__main__":
    unittest.main()