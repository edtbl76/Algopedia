import unittest
from sort.bubble_sort import (
    _swap,
    bubble_sort_basic,
    bubble_sort_optimized,
    bubble_sort_descending
)

class TestBubbleSort(unittest.TestCase):
    """Test cases for all bubble sort implementations."""

    def setUp(self):
        """Set up common test data."""
        self.empty_list = []
        self.single_element = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.reverse_sorted_list = [5, 4, 3, 2, 1]
        self.random_list = [64, 34, 25, 12, 22, 11, 90]
        self.duplicate_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    def test_swap(self):
        """Test the _swap helper function."""
        test_list = [1, 2, 3, 4, 5]
        _swap(test_list, 0, 4)
        self.assertEqual(test_list, [5, 2, 3, 4, 1])
        
        _swap(test_list, 1, 3)
        self.assertEqual(test_list, [5, 4, 3, 2, 1])

    def test_bubble_sort_basic_empty(self):
        """Test bubble_sort_basic with an empty list."""
        test_list = self.empty_list.copy()
        bubble_sort_basic(test_list)
        self.assertEqual(test_list, [])

    def test_bubble_sort_basic_single(self):
        """Test bubble_sort_basic with a single element."""
        test_list = self.single_element.copy()
        bubble_sort_basic(test_list)
        self.assertEqual(test_list, [42])

    def test_bubble_sort_basic_sorted(self):
        """Test bubble_sort_basic with an already sorted list."""
        test_list = self.sorted_list.copy()
        bubble_sort_basic(test_list)
        self.assertEqual(test_list, [1, 2, 3, 4, 5])

    def test_bubble_sort_basic_reverse(self):
        """Test bubble_sort_basic with a reverse sorted list."""
        test_list = self.reverse_sorted_list.copy()
        bubble_sort_basic(test_list)
        self.assertEqual(test_list, [1, 2, 3, 4, 5])

    def test_bubble_sort_basic_random(self):
        """Test bubble_sort_basic with a random list."""
        test_list = self.random_list.copy()
        bubble_sort_basic(test_list)
        self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

    def test_bubble_sort_basic_duplicates(self):
        """Test bubble_sort_basic with a list containing duplicates."""
        test_list = self.duplicate_list.copy()
        bubble_sort_basic(test_list)
        self.assertEqual(test_list, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_bubble_sort_optimized_empty(self):
        """Test bubble_sort_optimized with an empty list."""
        test_list = self.empty_list.copy()
        bubble_sort_optimized(test_list)
        self.assertEqual(test_list, [])

    def test_bubble_sort_optimized_single(self):
        """Test bubble_sort_optimized with a single element."""
        test_list = self.single_element.copy()
        bubble_sort_optimized(test_list)
        self.assertEqual(test_list, [42])

    def test_bubble_sort_optimized_sorted(self):
        """Test bubble_sort_optimized with an already sorted list."""
        test_list = self.sorted_list.copy()
        bubble_sort_optimized(test_list)
        self.assertEqual(test_list, [1, 2, 3, 4, 5])

    def test_bubble_sort_optimized_reverse(self):
        """Test bubble_sort_optimized with a reverse sorted list."""
        test_list = self.reverse_sorted_list.copy()
        bubble_sort_optimized(test_list)
        self.assertEqual(test_list, [1, 2, 3, 4, 5])

    def test_bubble_sort_optimized_random(self):
        """Test bubble_sort_optimized with a random list."""
        test_list = self.random_list.copy()
        bubble_sort_optimized(test_list)
        self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

    def test_bubble_sort_optimized_duplicates(self):
        """Test bubble_sort_optimized with a list containing duplicates."""
        test_list = self.duplicate_list.copy()
        bubble_sort_optimized(test_list)
        self.assertEqual(test_list, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_bubble_sort_descending_empty(self):
        """Test bubble_sort_descending with an empty list."""
        test_list = self.empty_list.copy()
        bubble_sort_descending(test_list)
        self.assertEqual(test_list, [])

    def test_bubble_sort_descending_single(self):
        """Test bubble_sort_descending with a single element."""
        test_list = self.single_element.copy()
        bubble_sort_descending(test_list)
        self.assertEqual(test_list, [42])

    def test_bubble_sort_descending_sorted(self):
        """Test bubble_sort_descending with an already sorted list."""
        test_list = self.sorted_list.copy()
        bubble_sort_descending(test_list)
        self.assertEqual(test_list, [5, 4, 3, 2, 1])

    def test_bubble_sort_descending_reverse(self):
        """Test bubble_sort_descending with a reverse sorted list."""
        test_list = self.reverse_sorted_list.copy()
        bubble_sort_descending(test_list)
        self.assertEqual(test_list, [5, 4, 3, 2, 1])

    def test_bubble_sort_descending_random(self):
        """Test bubble_sort_descending with a random list."""
        test_list = self.random_list.copy()
        bubble_sort_descending(test_list)
        self.assertEqual(test_list, [90, 64, 34, 25, 22, 12, 11])

    def test_bubble_sort_descending_duplicates(self):
        """Test bubble_sort_descending with a list containing duplicates."""
        test_list = self.duplicate_list.copy()
        bubble_sort_descending(test_list)
        self.assertEqual(test_list, [9, 6, 5, 5, 4, 3, 2, 1, 1])

    def test_implementations_match(self):
        """Test that basic and optimized implementations produce the same results."""
        test_cases = [
            self.empty_list.copy(),
            self.single_element.copy(),
            self.sorted_list.copy(),
            self.reverse_sorted_list.copy(),
            self.random_list.copy(),
            self.duplicate_list.copy()
        ]
        
        for test_list in test_cases:
            with self.subTest(test_list=test_list):
                # Create copies for each algorithm
                basic_list = test_list.copy()
                optimized_list = test_list.copy()
                
                # Sort using both algorithms
                bubble_sort_basic(basic_list)
                bubble_sort_optimized(optimized_list)
                
                # Check that results match
                self.assertEqual(basic_list, optimized_list)

if __name__ == '__main__':
    unittest.main()