import unittest
from sort.merge_sort import merge_sort, _merge

class TestMergeSort(unittest.TestCase):
    """Test cases for merge sort implementation."""

    def setUp(self):
        """Set up common test data."""
        self.empty_list = []
        self.single_element = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.reverse_sorted_list = [5, 4, 3, 2, 1]
        self.random_list = [64, 34, 25, 12, 22, 11, 90]
        self.duplicate_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        self.negative_list = [-5, -10, 0, 10, 5]
        self.mixed_types_list = ["apple", "banana", "cherry"]

    def test_merge_empty_lists(self):
        """Test _merge with empty lists."""
        result = _merge([], [])
        self.assertEqual(result, [])

    def test_merge_one_empty_list(self):
        """Test _merge with one empty list."""
        result1 = _merge([1, 2, 3], [])
        self.assertEqual(result1, [1, 2, 3])
        
        result2 = _merge([], [4, 5, 6])
        self.assertEqual(result2, [4, 5, 6])

    def test_merge_sorted_lists(self):
        """Test _merge with two sorted lists."""
        result = _merge([1, 3, 5], [2, 4, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_merge_with_duplicates(self):
        """Test _merge with lists containing duplicate values."""
        result = _merge([1, 2, 2], [2, 3, 3])
        self.assertEqual(result, [1, 2, 2, 2, 3, 3])

    def test_merge_stability(self):
        """Test that _merge maintains stability (order of equal elements)."""
        # Create tuples with same first element but different second elements
        left = [(1, 'a'), (2, 'b'), (3, 'c')]
        right = [(1, 'd'), (2, 'e'), (3, 'f')]
        
        result = _merge(left, right)
        # Check that elements from left come before elements from right when keys are equal
        self.assertEqual(result, [(1, 'a'), (1, 'd'), (2, 'b'), (2, 'e'), (3, 'c'), (3, 'f')])

    def test_merge_sort_empty(self):
        """Test merge_sort with an empty list."""
        result = merge_sort(self.empty_list)
        self.assertEqual(result, [])
        # Ensure original list is unchanged (merge_sort should not modify input)
        self.assertEqual(self.empty_list, [])

    def test_merge_sort_single(self):
        """Test merge_sort with a single element."""
        result = merge_sort(self.single_element)
        self.assertEqual(result, [42])
        # Ensure original list is unchanged
        self.assertEqual(self.single_element, [42])

    def test_merge_sort_sorted(self):
        """Test merge_sort with an already sorted list."""
        result = merge_sort(self.sorted_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        # Ensure original list is unchanged
        self.assertEqual(self.sorted_list, [1, 2, 3, 4, 5])

    def test_merge_sort_reverse(self):
        """Test merge_sort with a reverse sorted list."""
        result = merge_sort(self.reverse_sorted_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        # Ensure original list is unchanged
        self.assertEqual(self.reverse_sorted_list, [5, 4, 3, 2, 1])

    def test_merge_sort_random(self):
        """Test merge_sort with a random list."""
        result = merge_sort(self.random_list)
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
        # Ensure original list is unchanged
        self.assertEqual(self.random_list, [64, 34, 25, 12, 22, 11, 90])

    def test_merge_sort_duplicates(self):
        """Test merge_sort with a list containing duplicates."""
        result = merge_sort(self.duplicate_list)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])
        # Ensure original list is unchanged
        self.assertEqual(self.duplicate_list, [3, 1, 4, 1, 5, 9, 2, 6, 5])

    def test_merge_sort_negative(self):
        """Test merge_sort with a list containing negative numbers."""
        result = merge_sort(self.negative_list)
        self.assertEqual(result, [-10, -5, 0, 5, 10])
        # Ensure original list is unchanged
        self.assertEqual(self.negative_list, [-5, -10, 0, 10, 5])

    def test_merge_sort_strings(self):
        """Test merge_sort with a list of strings."""
        result = merge_sort(self.mixed_types_list)
        self.assertEqual(result, ["apple", "banana", "cherry"])
        # Ensure original list is unchanged
        self.assertEqual(self.mixed_types_list, ["apple", "banana", "cherry"])

    def test_merge_sort_immutability(self):
        """Test that merge_sort does not modify the original list."""
        original = [3, 1, 4, 1, 5, 9]
        original_copy = original.copy()
        
        # Call merge_sort
        merge_sort(original)
        
        # Verify original is unchanged
        self.assertEqual(original, original_copy)

if __name__ == '__main__':
    unittest.main()