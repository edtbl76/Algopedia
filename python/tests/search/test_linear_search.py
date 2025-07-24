import unittest
from search.linear_search import (
    linear_search,
    linear_search_duplicates,
    linear_search_duplicates_pythonic,
    NOT_FOUND
)

class TestLinearSearch(unittest.TestCase):
    """Test cases for all linear search implementations."""

    def setUp(self):
        """Set up common test data."""
        self.empty_list = []
        self.single_element = [42]
        self.simple_list = [1, 3, 5, 7, 9]
        self.duplicates_list = [1, 3, 5, 3, 9, 3]
        self.all_same_list = [7, 7, 7, 7]

    def test_linear_search_found(self):
        """Test linear_search when the target is in the list."""
        self.assertEqual(linear_search(self.simple_list, 5), 2)
        self.assertEqual(linear_search(self.simple_list, 1), 0)
        self.assertEqual(linear_search(self.simple_list, 9), 4)
        self.assertEqual(linear_search(self.single_element, 42), 0)

    def test_linear_search_not_found(self):
        """Test linear_search when the target is not in the list."""
        self.assertEqual(linear_search(self.simple_list, 10), NOT_FOUND)
        self.assertEqual(linear_search(self.simple_list, 0), NOT_FOUND)
        self.assertEqual(linear_search(self.single_element, 43), NOT_FOUND)

    def test_linear_search_empty_list(self):
        """Test linear_search with an empty list."""
        self.assertEqual(linear_search(self.empty_list, 5), NOT_FOUND)

    def test_linear_search_duplicates_first_occurrence(self):
        """Test linear_search returns only the first occurrence of a duplicate value."""
        self.assertEqual(linear_search(self.duplicates_list, 3), 1)
        self.assertEqual(linear_search(self.all_same_list, 7), 0)

    def test_linear_search_duplicates_found(self):
        """Test linear_search_duplicates when the target is in the list."""
        self.assertEqual(linear_search_duplicates(self.simple_list, 5), [2])
        self.assertEqual(linear_search_duplicates(self.duplicates_list, 3), [1, 3, 5])
        self.assertEqual(linear_search_duplicates(self.all_same_list, 7), [0, 1, 2, 3])
        self.assertEqual(linear_search_duplicates(self.single_element, 42), [0])

    def test_linear_search_duplicates_not_found(self):
        """Test linear_search_duplicates when the target is not in the list."""
        self.assertEqual(linear_search_duplicates(self.simple_list, 10), [])
        self.assertEqual(linear_search_duplicates(self.duplicates_list, 0), [])
        self.assertEqual(linear_search_duplicates(self.single_element, 43), [])

    def test_linear_search_duplicates_empty_list(self):
        """Test linear_search_duplicates with an empty list."""
        self.assertEqual(linear_search_duplicates(self.empty_list, 5), [])

    def test_linear_search_duplicates_pythonic_found(self):
        """Test linear_search_duplicates_pythonic when the target is in the list."""
        self.assertEqual(linear_search_duplicates_pythonic(self.simple_list, 5), [2])
        self.assertEqual(linear_search_duplicates_pythonic(self.duplicates_list, 3), [1, 3, 5])
        self.assertEqual(linear_search_duplicates_pythonic(self.all_same_list, 7), [0, 1, 2, 3])
        self.assertEqual(linear_search_duplicates_pythonic(self.single_element, 42), [0])

    def test_linear_search_duplicates_pythonic_not_found(self):
        """Test linear_search_duplicates_pythonic when the target is not in the list."""
        self.assertEqual(linear_search_duplicates_pythonic(self.simple_list, 10), [])
        self.assertEqual(linear_search_duplicates_pythonic(self.duplicates_list, 0), [])
        self.assertEqual(linear_search_duplicates_pythonic(self.single_element, 43), [])

    def test_linear_search_duplicates_pythonic_empty_list(self):
        """Test linear_search_duplicates_pythonic with an empty list."""
        self.assertEqual(linear_search_duplicates_pythonic(self.empty_list, 5), [])

    def test_duplicates_implementations_match(self):
        """Test that both duplicates implementations return the same results."""
        test_cases = [
            (self.simple_list, 5),
            (self.duplicates_list, 3),
            (self.all_same_list, 7),
            (self.single_element, 42),
            (self.simple_list, 10),
            (self.empty_list, 5)
        ]
        
        for values, target in test_cases:
            with self.subTest(values=values, target=target):
                self.assertEqual(
                    linear_search_duplicates(values, target),
                    linear_search_duplicates_pythonic(values, target)
                )

if __name__ == '__main__':
    unittest.main()