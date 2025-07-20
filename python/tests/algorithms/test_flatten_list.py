import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.flatten_list import flatten_list


class TestFlattenList(unittest.TestCase):
    def test_flatten_list_example_from_docstring(self):
        """Test the example from the function's docstring"""
        result = flatten_list([1, [2, 3], [4, [5, 6]]])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected)

    def test_flatten_list_empty_list(self):
        """Test flattening an empty list"""
        result = flatten_list([])
        self.assertEqual(result, [])

    def test_flatten_list_single_element(self):
        """Test flattening a list with a single non-list element"""
        result = flatten_list([42])
        self.assertEqual(result, [42])

    def test_flatten_list_single_nested_list(self):
        """Test flattening a list with a single nested list"""
        result = flatten_list([[1, 2, 3]])
        self.assertEqual(result, [1, 2, 3])

    def test_flatten_list_already_flat(self):
        """Test flattening a list that's already flat"""
        result = flatten_list([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_flatten_list_deeply_nested(self):
        """Test flattening a deeply nested list"""
        result = flatten_list([1, [2, [3, [4, [5]]]]])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_flatten_list_mixed_types(self):
        """Test flattening a list with mixed data types"""
        result = flatten_list([1, ['hello', [2.5, [True, None]]]])
        expected = [1, 'hello', 2.5, True, None]
        self.assertEqual(result, expected)

    def test_flatten_list_empty_nested_lists(self):
        """Test flattening a list containing empty nested lists"""
        result = flatten_list([1, [], [2, []], 3])
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_flatten_list_multiple_levels(self):
        """Test flattening a list with multiple nesting levels"""
        result = flatten_list([[1, 2], [3, [4, 5]], [[6], 7]])
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(result, expected)

    def test_flatten_list_strings_and_numbers(self):
        """Test flattening a list with strings and numbers"""
        result = flatten_list(['a', [1, ['b', 2]], 'c'])
        expected = ['a', 1, 'b', 2, 'c']
        self.assertEqual(result, expected)

    def test_flatten_list_nested_empty_lists(self):
        """Test flattening nested empty lists"""
        result = flatten_list([[], [[]], [[[]]]])
        expected = []
        self.assertEqual(result, expected)

    def test_flatten_list_complex_structure(self):
        """Test flattening a complex nested structure"""
        result = flatten_list([1, [2, 3, [4, 5, [6]]], 7, [8, [9, [10]]]])
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()