import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.multiplication import multiplication, multiplication_recursive, _validate_multiplication_inputs


class TestMultiplication(unittest.TestCase):

    def test_multiplication_positive_numbers(self):
        """Test multiplication with positive numbers"""
        self.assertEqual(multiplication(6, 4), 24)
        self.assertEqual(multiplication(5, 3), 15)
        self.assertEqual(multiplication(1, 10), 10)

    def test_multiplication_negative_multiplier(self):
        """Test multiplication with negative multiplier"""
        self.assertEqual(multiplication(5, -3), -15)
        self.assertEqual(multiplication(7, -2), -14)

    def test_multiplication_negative_multiplicand(self):
        """Test multiplication with negative multiplicand"""
        self.assertEqual(multiplication(-5, 3), -15)
        self.assertEqual(multiplication(-7, 2), -14)

    def test_multiplication_both_negative(self):
        """Test multiplication with both numbers negative"""
        self.assertEqual(multiplication(-5, -3), 15)
        self.assertEqual(multiplication(-7, -2), 14)

    def test_multiplication_with_zero(self):
        """Test multiplication with zero"""
        self.assertEqual(multiplication(5, 0), 0)
        self.assertEqual(multiplication(0, 5), 0)
        self.assertEqual(multiplication(0, 0), 0)

    def test_multiplication_large_numbers(self):
        """Test multiplication with large numbers"""
        self.assertEqual(multiplication(100, 100), 10000)
        self.assertEqual(multiplication(1000, 10), 10000)

    def test_multiplication_recursive_positive_numbers(self):
        """Test recursive multiplication with positive numbers"""
        self.assertEqual(multiplication_recursive(6, 4), 24)
        self.assertEqual(multiplication_recursive(5, 3), 15)
        self.assertEqual(multiplication_recursive(1, 10), 10)

    def test_multiplication_recursive_negative_multiplier(self):
        """Test recursive multiplication with negative multiplier"""
        self.assertEqual(multiplication_recursive(5, -3), -15)
        self.assertEqual(multiplication_recursive(7, -2), -14)

    def test_multiplication_recursive_negative_multiplicand(self):
        """Test recursive multiplication with negative multiplicand"""
        self.assertEqual(multiplication_recursive(-5, 3), -15)
        self.assertEqual(multiplication_recursive(-7, 2), -14)

    def test_multiplication_recursive_both_negative(self):
        """Test recursive multiplication with both numbers negative"""
        self.assertEqual(multiplication_recursive(-5, -3), 15)
        self.assertEqual(multiplication_recursive(-7, -2), 14)

    def test_multiplication_recursive_with_zero(self):
        """Test recursive multiplication with zero"""
        self.assertEqual(multiplication_recursive(5, 0), 0)
        self.assertEqual(multiplication_recursive(0, 5), 0)
        self.assertEqual(multiplication_recursive(0, 0), 0)

    def test_multiplication_recursive_large_numbers(self):
        """Test recursive multiplication with large numbers"""
        self.assertEqual(multiplication_recursive(100, 100), 10000)
        self.assertEqual(multiplication_recursive(1000, 10), 10000)

    def test_validate_multiplication_inputs(self):
        """Test the input validation helper function"""
        # Test with positive multiplier
        normalized_multiplicand, normalized_multiplier, is_negative = _validate_multiplication_inputs(5, 3)
        self.assertEqual(normalized_multiplicand, 5)
        self.assertEqual(normalized_multiplier, 3)
        self.assertFalse(is_negative)

        # Test with negative multiplier
        normalized_multiplicand, normalized_multiplier, is_negative = _validate_multiplication_inputs(5, -3)
        self.assertEqual(normalized_multiplicand, 5)
        self.assertEqual(normalized_multiplier, 3)
        self.assertTrue(is_negative)

    def test_both_implementations_equivalent(self):
        """Test that both implementations produce the same results"""
        test_cases = [
            (0, 0),
            (5, 3),
            (6, 4),
            (5, -3),
            (-5, 3),
            (-5, -3),
            (100, 100),
            (1000, 10)
        ]

        for multiplicand, multiplier in test_cases:
            iterative_result = multiplication(multiplicand, multiplier)
            recursive_result = multiplication_recursive(multiplicand, multiplier)
            self.assertEqual(iterative_result, recursive_result)


if __name__ == '__main__':
    unittest.main()