import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.factorial import factorial


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


if __name__ == '__main__':
    unittest.main()
