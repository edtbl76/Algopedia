import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.backpack import recursive_backpack, dynamic_backpack


class TestBackpack(unittest.TestCase):
    def test_recursive_backpack_basic_example(self):
        """Test recursive_backpack with the example from the docstring"""
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        weight_max = 10
        self.assertEqual(recursive_backpack(weight_max, weights, values), 13)

    def test_recursive_backpack_another_example(self):
        """Test recursive_backpack with another example from the docstring"""
        weights = [1, 3, 4]
        values = [15, 20, 30]
        weight_max = 5
        self.assertEqual(recursive_backpack(weight_max, weights, values), 45)

    def test_recursive_backpack_empty_lists(self):
        """Test recursive_backpack with empty lists"""
        weights = []
        values = []
        weight_max = 10
        self.assertEqual(recursive_backpack(weight_max, weights, values), 0)

    def test_recursive_backpack_zero_capacity(self):
        """Test recursive_backpack with zero capacity"""
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        weight_max = 0
        self.assertEqual(recursive_backpack(weight_max, weights, values), 0)

    def test_recursive_backpack_all_items_too_heavy(self):
        """Test recursive_backpack when all items are too heavy"""
        weights = [10, 20, 30]
        values = [60, 100, 120]
        weight_max = 5
        self.assertEqual(recursive_backpack(weight_max, weights, values), 0)

    def test_recursive_backpack_one_item_fits_exactly(self):
        """Test recursive_backpack when one item fits exactly"""
        weights = [5, 10, 15]
        values = [10, 30, 50]
        weight_max = 5
        self.assertEqual(recursive_backpack(weight_max, weights, values), 10)

    def test_recursive_backpack_multiple_optimal_solutions(self):
        """Test recursive_backpack when there are multiple optimal solutions"""
        weights = [1, 2, 3]
        values = [10, 10, 10]
        weight_max = 3
        # Can take either [1, 2] or [3], both give value 20
        self.assertEqual(recursive_backpack(weight_max, weights, values), 20)

    def test_dynamic_backpack_basic_example(self):
        """Test dynamic_backpack with the example from the docstring"""
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        weight_max = 10
        self.assertEqual(dynamic_backpack(weight_max, weights, values), 13)

    def test_dynamic_backpack_another_example(self):
        """Test dynamic_backpack with another example from the docstring"""
        weights = [1, 3, 4]
        values = [15, 20, 30]
        weight_max = 5
        self.assertEqual(dynamic_backpack(weight_max, weights, values), 45)

    def test_dynamic_backpack_empty_lists(self):
        """Test dynamic_backpack with empty lists"""
        weights = []
        values = []
        weight_max = 10
        self.assertEqual(dynamic_backpack(weight_max, weights, values), 0)

    def test_dynamic_backpack_zero_capacity(self):
        """Test dynamic_backpack with zero capacity"""
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        weight_max = 0
        self.assertEqual(dynamic_backpack(weight_max, weights, values), 0)

    def test_dynamic_backpack_all_items_too_heavy(self):
        """Test dynamic_backpack when all items are too heavy"""
        weights = [10, 20, 30]
        values = [60, 100, 120]
        weight_max = 5
        self.assertEqual(dynamic_backpack(weight_max, weights, values), 0)

    def test_dynamic_backpack_one_item_fits_exactly(self):
        """Test dynamic_backpack when one item fits exactly"""
        weights = [5, 10, 15]
        values = [10, 30, 50]
        weight_max = 5
        self.assertEqual(dynamic_backpack(weight_max, weights, values), 10)

    def test_dynamic_backpack_multiple_optimal_solutions(self):
        """Test dynamic_backpack when there are multiple optimal solutions"""
        weights = [1, 2, 3]
        values = [10, 10, 10]
        weight_max = 3
        # Can take either [1, 2] or [3], both give value 20
        self.assertEqual(dynamic_backpack(weight_max, weights, values), 20)

    def test_implementations_consistency(self):
        """Test that both implementations produce the same results"""
        test_cases = [
            # weight_max, weights, values
            (10, [2, 3, 4, 5], [3, 4, 5, 6]),
            (5, [1, 3, 4], [15, 20, 30]),
            (8, [2, 3, 4, 5], [3, 4, 5, 6]),
            (0, [1, 2, 3], [10, 20, 30]),
            (15, [5, 7, 8, 9], [10, 13, 15, 17]),
            (6, [1, 2, 3, 4], [1, 4, 5, 7])
        ]
        
        for weight_max, weights, values in test_cases:
            with self.subTest(weight_max=weight_max, weights=weights, values=values):
                recursive_result = recursive_backpack(weight_max, weights, values)
                dynamic_result = dynamic_backpack(weight_max, weights, values)
                self.assertEqual(recursive_result, dynamic_result, 
                               f"Results differ for weight_max={weight_max}, weights={weights}, values={values}: "
                               f"recursive={recursive_result}, dynamic={dynamic_result}")

    def test_large_capacity(self):
        """Test with a large capacity where all items can be included"""
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        weight_max = 100
        expected = sum(values)  # All items can be included
        self.assertEqual(dynamic_backpack(weight_max, weights, values), expected)
        self.assertEqual(recursive_backpack(weight_max, weights, values), expected)


if __name__ == '__main__':
    unittest.main()