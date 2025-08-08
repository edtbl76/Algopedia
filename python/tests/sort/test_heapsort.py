import unittest
from sort.heapsort import heapsort


class TestHeapSort(unittest.TestCase):
    """Test cases for the heapsort algorithm implementation."""

    def setUp(self):
        """Set up common test data."""
        self.empty_list = []
        self.single_element = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.reverse_sorted_list = [5, 4, 3, 2, 1]
        self.random_list = [64, 34, 25, 12, 22, 11, 90]
        self.duplicate_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    def test_empty_list(self):
        """Test heapsort with an empty list."""
        result = heapsort(self.empty_list)
        self.assertEqual(result, [])
        # Verify original list is unchanged
        self.assertEqual(self.empty_list, [])

    def test_single_element(self):
        """Test heapsort with a single element."""
        result = heapsort(self.single_element)
        self.assertEqual(result, [42])
        # Verify original list is unchanged
        self.assertEqual(self.single_element, [42])

    def test_sorted_list(self):
        """Test heapsort with an already sorted list."""
        result = heapsort(self.sorted_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        # Verify original list is unchanged
        self.assertEqual(self.sorted_list, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test heapsort with a reverse sorted list."""
        result = heapsort(self.reverse_sorted_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        # Verify original list is unchanged
        self.assertEqual(self.reverse_sorted_list, [5, 4, 3, 2, 1])

    def test_random_list(self):
        """Test heapsort with a random list."""
        result = heapsort(self.random_list)
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
        # Verify original list is unchanged
        self.assertEqual(self.random_list, [64, 34, 25, 12, 22, 11, 90])

    def test_duplicate_list(self):
        """Test heapsort with a list containing duplicates."""
        result = heapsort(self.duplicate_list)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])
        # Verify original list is unchanged
        self.assertEqual(self.duplicate_list, [3, 1, 4, 1, 5, 9, 2, 6, 5])

    def test_descending_order(self):
        """Test heapsort with ascending=False parameter."""
        result = heapsort(self.random_list, ascending=False)
        self.assertEqual(result, [90, 64, 34, 25, 22, 12, 11])
        # Verify original list is unchanged
        self.assertEqual(self.random_list, [64, 34, 25, 12, 22, 11, 90])

    def test_descending_order_with_duplicates(self):
        """Test heapsort with ascending=False parameter and duplicates."""
        result = heapsort(self.duplicate_list, ascending=False)
        self.assertEqual(result, [9, 6, 5, 5, 4, 3, 2, 1, 1])
        # Verify original list is unchanged
        self.assertEqual(self.duplicate_list, [3, 1, 4, 1, 5, 9, 2, 6, 5])

    def test_negative_numbers(self):
        """Test heapsort with negative numbers."""
        test_list = [-5, -10, -3, -7, -1]
        result = heapsort(test_list)
        self.assertEqual(result, [-10, -7, -5, -3, -1])
        # Verify original list is unchanged
        self.assertEqual(test_list, [-5, -10, -3, -7, -1])

    def test_mixed_numbers(self):
        """Test heapsort with a mix of positive and negative numbers."""
        test_list = [5, -10, 0, 7, -1]
        result = heapsort(test_list)
        self.assertEqual(result, [-10, -1, 0, 5, 7])
        # Verify original list is unchanged
        self.assertEqual(test_list, [5, -10, 0, 7, -1])

    def test_large_list(self):
        """Test heapsort with a larger list."""
        test_list = list(range(100, 0, -1))  # 100 down to 1
        result = heapsort(test_list)
        self.assertEqual(result, list(range(1, 101)))  # 1 up to 100
        # Verify original list is unchanged
        self.assertEqual(test_list, list(range(100, 0, -1)))


if __name__ == '__main__':
    unittest.main()