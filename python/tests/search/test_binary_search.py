import unittest
from search.binary_search import binary_search, binary_search_two_pointer


class TestBinarySearch(unittest.TestCase):
    """Test cases for binary search implementations."""

    def setUp(self):
        """Set up common test data."""
        self.empty_list = []
        self.single_element = [42]
        self.simple_list = [1, 3, 5, 7, 9, 11]
        self.large_list = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        self.string_list = ["apple", "banana", "cherry", "date", "elderberry"]
        self.duplicate_list = [1, 3, 3, 5, 7, 7, 9]

    def test_binary_search_found(self):
        """Test binary_search when the target is in the list."""
        self.assertEqual(binary_search(self.simple_list, 5), 2)
        self.assertEqual(binary_search(self.simple_list, 1), 0)
        self.assertEqual(binary_search(self.simple_list, 11), 5)
        self.assertEqual(binary_search(self.single_element, 42), 0)
        self.assertEqual(binary_search(self.large_list, 48), 24)
        self.assertEqual(binary_search(self.string_list, "cherry"), 2)

    def test_binary_search_not_found(self):
        """Test binary_search when the target is not in the list."""
        self.assertIsNone(binary_search(self.simple_list, 4))
        self.assertIsNone(binary_search(self.simple_list, 0))
        self.assertIsNone(binary_search(self.simple_list, 12))
        self.assertIsNone(binary_search(self.single_element, 43))
        self.assertIsNone(binary_search(self.large_list, 49))
        self.assertIsNone(binary_search(self.string_list, "blueberry"))

    def test_binary_search_empty_list(self):
        """Test binary_search with an empty list."""
        self.assertIsNone(binary_search(self.empty_list, 5))

    def test_binary_search_duplicate_elements(self):
        """Test binary_search with duplicate elements (should find one of them)."""
        # For duplicates, binary search will find one of the occurrences, but which one is not guaranteed
        result = binary_search(self.duplicate_list, 3)
        self.assertIn(result, [1, 2])  # 3 appears at indices 1 and 2
        
        result = binary_search(self.duplicate_list, 7)
        self.assertIn(result, [4, 5])  # 7 appears at indices 4 and 5

    def test_binary_search_two_pointer_found(self):
        """Test binary_search_two_pointer when the target is in the list."""
        self.assertEqual(binary_search_two_pointer(self.simple_list, 0, len(self.simple_list) - 1, 5), 2)
        self.assertEqual(binary_search_two_pointer(self.simple_list, 0, len(self.simple_list) - 1, 1), 0)
        self.assertEqual(binary_search_two_pointer(self.simple_list, 0, len(self.simple_list) - 1, 11), 5)
        self.assertEqual(binary_search_two_pointer(self.single_element, 0, 0, 42), 0)
        self.assertEqual(binary_search_two_pointer(self.large_list, 0, len(self.large_list) - 1, 48), 24)
        self.assertEqual(binary_search_two_pointer(self.string_list, 0, len(self.string_list) - 1, "cherry"), 2)

    def test_binary_search_two_pointer_not_found(self):
        """Test binary_search_two_pointer when the target is not in the list."""
        self.assertIsNone(binary_search_two_pointer(self.simple_list, 0, len(self.simple_list) - 1, 4))
        self.assertIsNone(binary_search_two_pointer(self.simple_list, 0, len(self.simple_list) - 1, 0))
        self.assertIsNone(binary_search_two_pointer(self.simple_list, 0, len(self.simple_list) - 1, 12))
        self.assertIsNone(binary_search_two_pointer(self.single_element, 0, 0, 43))
        self.assertIsNone(binary_search_two_pointer(self.large_list, 0, len(self.large_list) - 1, 49))
        self.assertIsNone(binary_search_two_pointer(self.string_list, 0, len(self.string_list) - 1, "blueberry"))

    def test_binary_search_two_pointer_empty_list(self):
        """Test binary_search_two_pointer with an empty list."""
        self.assertIsNone(binary_search_two_pointer(self.empty_list, 0, -1, 5))

    def test_binary_search_two_pointer_duplicate_elements(self):
        """Test binary_search_two_pointer with duplicate elements (should find one of them)."""
        # For duplicates, binary search will find one of the occurrences, but which one is not guaranteed
        result = binary_search_two_pointer(self.duplicate_list, 0, len(self.duplicate_list) - 1, 3)
        self.assertIn(result, [1, 2])  # 3 appears at indices 1 and 2
        
        result = binary_search_two_pointer(self.duplicate_list, 0, len(self.duplicate_list) - 1, 7)
        self.assertIn(result, [4, 5])  # 7 appears at indices 4 and 5

    def test_binary_search_partial_search(self):
        """Test binary_search_two_pointer with partial search range."""
        # Search only in the first half of the list
        self.assertEqual(binary_search_two_pointer(self.simple_list, 0, 2, 3), 1)
        self.assertIsNone(binary_search_two_pointer(self.simple_list, 0, 2, 7))
        
        # Search only in the second half of the list
        self.assertEqual(binary_search_two_pointer(self.simple_list, 3, 5, 9), 4)
        self.assertIsNone(binary_search_two_pointer(self.simple_list, 3, 5, 3))

    def test_implementations_match(self):
        """Test that both binary search implementations return the same results."""
        test_cases = [
            (self.simple_list, 5),
            (self.simple_list, 1),
            (self.simple_list, 11),
            (self.simple_list, 4),  # Not found
            (self.single_element, 42),
            (self.single_element, 43),  # Not found
            (self.empty_list, 5),  # Empty list
            (self.large_list, 48),
            (self.large_list, 49),  # Not found
            (self.string_list, "cherry"),
            (self.string_list, "blueberry")  # Not found
        ]
        
        for values, target in test_cases:
            with self.subTest(values=values, target=target):
                # For the two-pointer version, we need to provide the full range
                two_pointer_result = binary_search_two_pointer(
                    values, 0, len(values) - 1 if values else -1, target
                )
                self.assertEqual(
                    binary_search(values, target),
                    two_pointer_result
                )


if __name__ == '__main__':
    unittest.main()