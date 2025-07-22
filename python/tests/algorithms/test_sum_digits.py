import unittest
import sys
import os
from typing import List

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.sum_digits import sum_digits_iterative, sum_digits_recursive


class TestSumDigits(unittest.TestCase):
    def test_sum_digits_iterative_zero(self) -> None:
        """Test iterative sum_digits of 0"""
        result: int = sum_digits_iterative(0)
        self.assertEqual(result, 0)

    def test_sum_digits_iterative_single_digit(self) -> None:
        """Test iterative sum_digits of single digit numbers"""
        self.assertEqual(sum_digits_iterative(1), 1)
        self.assertEqual(sum_digits_iterative(5), 5)
        self.assertEqual(sum_digits_iterative(9), 9)

    def test_sum_digits_iterative_two_digits(self) -> None:
        """Test iterative sum_digits of two digit numbers"""
        self.assertEqual(sum_digits_iterative(12), 3)  # 1 + 2
        self.assertEqual(sum_digits_iterative(23), 5)  # 2 + 3
        self.assertEqual(sum_digits_iterative(99), 18) # 9 + 9

    def test_sum_digits_iterative_three_digits(self) -> None:
        """Test iterative sum_digits of three digit numbers"""
        self.assertEqual(sum_digits_iterative(123), 6)   # 1 + 2 + 3
        self.assertEqual(sum_digits_iterative(456), 15)  # 4 + 5 + 6
        self.assertEqual(sum_digits_iterative(999), 27)  # 9 + 9 + 9

    def test_sum_digits_iterative_larger_numbers(self) -> None:
        """Test iterative sum_digits of larger numbers"""
        self.assertEqual(sum_digits_iterative(1234), 10)    # 1 + 2 + 3 + 4
        self.assertEqual(sum_digits_iterative(56789), 35)   # 5 + 6 + 7 + 8 + 9
        self.assertEqual(sum_digits_iterative(987654321), 45) # 9+8+7+6+5+4+3+2+1

    def test_sum_digits_iterative_numbers_with_zeros(self) -> None:
        """Test iterative sum_digits of numbers containing zeros"""
        self.assertEqual(sum_digits_iterative(101), 2)   # 1 + 0 + 1
        self.assertEqual(sum_digits_iterative(1000), 1)  # 1 + 0 + 0 + 0
        self.assertEqual(sum_digits_iterative(2050), 7)  # 2 + 0 + 5 + 0

    def test_sum_digits_iterative_negative_number(self) -> None:
        """Test iterative sum_digits of negative number (should raise ValueError)"""
        with self.assertRaises(ValueError):
            sum_digits_iterative(-1)

        with self.assertRaises(ValueError):
            sum_digits_iterative(-123)

    def test_sum_digits_recursive_zero(self) -> None:
        """Test recursive sum_digits of 0"""
        result: int = sum_digits_recursive(0)
        self.assertEqual(result, 0)

    def test_sum_digits_recursive_single_digit(self) -> None:
        """Test recursive sum_digits of single digit numbers"""
        self.assertEqual(sum_digits_recursive(1), 1)
        self.assertEqual(sum_digits_recursive(5), 5)
        self.assertEqual(sum_digits_recursive(9), 9)

    def test_sum_digits_recursive_two_digits(self) -> None:
        """Test recursive sum_digits of two digit numbers"""
        self.assertEqual(sum_digits_recursive(12), 3)  # 1 + 2
        self.assertEqual(sum_digits_recursive(23), 5)  # 2 + 3
        self.assertEqual(sum_digits_recursive(99), 18) # 9 + 9

    def test_sum_digits_recursive_three_digits(self) -> None:
        """Test recursive sum_digits of three digit numbers"""
        self.assertEqual(sum_digits_recursive(123), 6)   # 1 + 2 + 3
        self.assertEqual(sum_digits_recursive(456), 15)  # 4 + 5 + 6
        self.assertEqual(sum_digits_recursive(999), 27)  # 9 + 9 + 9

    def test_sum_digits_recursive_larger_numbers(self) -> None:
        """Test recursive sum_digits of larger numbers"""
        self.assertEqual(sum_digits_recursive(1234), 10)    # 1 + 2 + 3 + 4
        self.assertEqual(sum_digits_recursive(56789), 35)   # 5 + 6 + 7 + 8 + 9
        self.assertEqual(sum_digits_recursive(987654321), 45) # 9+8+7+6+5+4+3+2+1

    def test_sum_digits_recursive_numbers_with_zeros(self) -> None:
        """Test recursive sum_digits of numbers containing zeros"""
        self.assertEqual(sum_digits_recursive(101), 2)   # 1 + 0 + 1
        self.assertEqual(sum_digits_recursive(1000), 1)  # 1 + 0 + 0 + 0
        self.assertEqual(sum_digits_recursive(2050), 7)  # 2 + 0 + 5 + 0

    def test_sum_digits_recursive_negative_number(self) -> None:
        """Test recursive sum_digits of negative number (should raise ValueError)"""
        with self.assertRaises(ValueError):
            sum_digits_recursive(-1)

        with self.assertRaises(ValueError):
            sum_digits_recursive(-123)

    def test_recursive_vs_iterative_consistency(self) -> None:
        """Test that recursive and iterative implementations produce the same results"""
        test_values: List[int] = [0, 1, 5, 9, 12, 23, 99, 123, 456, 999, 1234, 56789, 987654321, 101, 1000, 2050]

        for n in test_values:
            with self.subTest(n=n):
                recursive_result: int = sum_digits_recursive(n)
                iterative_result: int = sum_digits_iterative(n)
                self.assertEqual(recursive_result, iterative_result,
                               f"Results differ for n={n}: recursive={recursive_result}, iterative={iterative_result}")


if __name__ == '__main__':
    unittest.main()
