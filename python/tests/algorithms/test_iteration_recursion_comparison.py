import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.iteration_recursion_comparison import iterative_sum_to_one, recursive_sum_to_one


class TestIterationRecursionComparison(unittest.TestCase):
    def test_iterative_sum_to_one_small_numbers(self):
        """Test iterative sum for small positive numbers"""
        result, stack = iterative_sum_to_one(1)
        self.assertEqual(result, 1)
        self.assertEqual(len(stack), 0)  # Stack should be empty after processing

        result, stack = iterative_sum_to_one(3)
        self.assertEqual(result, 6)  # 3 + 2 + 1 = 6
        self.assertEqual(len(stack), 0)

        result, stack = iterative_sum_to_one(5)
        self.assertEqual(result, 15)  # 5 + 4 + 3 + 2 + 1 = 15
        self.assertEqual(len(stack), 0)

    def test_recursive_sum_to_one_small_numbers(self):
        """Test recursive sum for small positive numbers"""
        self.assertEqual(recursive_sum_to_one(1), 1)
        self.assertEqual(recursive_sum_to_one(3), 6)  # 3 + 2 + 1 = 6
        self.assertEqual(recursive_sum_to_one(5), 15)  # 5 + 4 + 3 + 2 + 1 = 15

    def test_iterative_sum_to_one_larger_number(self):
        """Test iterative sum for a larger number"""
        result, stack = iterative_sum_to_one(10)
        expected = sum(range(1, 11))  # 1 + 2 + ... + 10 = 55
        self.assertEqual(result, expected)
        self.assertEqual(len(stack), 0)

    def test_recursive_sum_to_one_larger_number(self):
        """Test recursive sum for a larger number"""
        result = recursive_sum_to_one(10)
        expected = sum(range(1, 11))  # 1 + 2 + ... + 10 = 55
        self.assertEqual(result, expected)

    def test_both_functions_produce_same_result(self):
        """Test that both iterative and recursive functions produce the same results"""
        test_values = [1, 2, 3, 4, 5, 7, 10]

        for n in test_values:
            iterative_result, _ = iterative_sum_to_one(n)
            recursive_result = recursive_sum_to_one(n)
            self.assertEqual(iterative_result, recursive_result, 
                           f"Results differ for n={n}: iterative={iterative_result}, recursive={recursive_result}")

    def test_iterative_sum_invalid_input(self):
        """Test iterative sum with invalid input"""
        with self.assertRaises(ValueError):
            iterative_sum_to_one(0)

        with self.assertRaises(ValueError):
            iterative_sum_to_one(-1)

        with self.assertRaises(ValueError):
            iterative_sum_to_one("not_an_int")

    def test_recursive_sum_invalid_input(self):
        """Test recursive sum with invalid input"""
        with self.assertRaises(ValueError):
            recursive_sum_to_one(0)

        with self.assertRaises(ValueError):
            recursive_sum_to_one(-1)

        with self.assertRaises(ValueError):
            recursive_sum_to_one("not_an_int")


if __name__ == '__main__':
    unittest.main()
