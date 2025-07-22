import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.factorial import factorial, factorial_iterative


class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        """Test factorial of 0 (base case)"""
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_one(self):
        """Test factorial of 1"""
        result = factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_small_positive(self):
        """Test factorial of small positive numbers"""
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_factorial_larger_number(self):
        """Test factorial of a larger number"""
        result = factorial(6)
        self.assertEqual(result, 720)

    def test_factorial_negative_number(self):
        """Test factorial of negative number (should raise ValueError)"""
        with self.assertRaises(ValueError):
            factorial(-1)

        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_iterative_zero(self):
        """Test iterative factorial of 0 (base case)"""
        result = factorial_iterative(0)
        self.assertEqual(result, 1)

    def test_factorial_iterative_one(self):
        """Test iterative factorial of 1"""
        result = factorial_iterative(1)
        self.assertEqual(result, 1)

    def test_factorial_iterative_small_positive(self):
        """Test iterative factorial of small positive numbers"""
        self.assertEqual(factorial_iterative(3), 6)
        self.assertEqual(factorial_iterative(4), 24)
        self.assertEqual(factorial_iterative(5), 120)

    def test_factorial_iterative_larger_number(self):
        """Test iterative factorial of a larger number"""
        result = factorial_iterative(6)
        self.assertEqual(result, 720)

    def test_factorial_iterative_negative_number(self):
        """Test iterative factorial of negative number (should raise ValueError)"""
        with self.assertRaises(ValueError):
            factorial_iterative(-1)

        with self.assertRaises(ValueError):
            factorial_iterative(-5)

    def test_recursive_vs_iterative_consistency(self):
        """Test that recursive and iterative implementations produce the same results"""
        test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for n in test_values:
            with self.subTest(n=n):
                recursive_result = factorial(n)
                iterative_result = factorial_iterative(n)
                self.assertEqual(recursive_result, iterative_result,
                               f"Results differ for n={n}: recursive={recursive_result}, iterative={iterative_result}")


if __name__ == '__main__':
    unittest.main()
