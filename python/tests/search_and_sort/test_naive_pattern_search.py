import unittest
from search_and_sort.naive_pattern_search import (
    naive_pattern_search_slice,
    naive_pattern_search_character,
    naive_pattern_search_safe_bounds,
    naive_pattern_search_counting,
    naive_pattern_search_optimized
)

class TestNaivePatternSearch(unittest.TestCase):
    """Test cases for all naive pattern search implementations."""

    def setUp(self):
        """Set up common test data."""
        self.text_empty = ""
        self.text_single = "a"
        self.text_simple = "abcdefg"
        self.text_repeated = "abababa"
        self.text_with_overlap = "aaaaa"
        self.text_long = "The quick brown fox jumps over the lazy dog"

    def test_empty_pattern(self):
        """Test with an empty pattern (should return empty list)."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "")
                self.assertEqual(result, [])

    def test_empty_text(self):
        """Test with an empty text (should return empty list)."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func("", "pattern")
                self.assertEqual(result, [])

    def test_pattern_longer_than_text(self):
        """Test with a pattern longer than the text (should return empty list)."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func("abc", "abcdef")
                self.assertEqual(result, [])

    def test_single_match(self):
        """Test with a single match in the text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "cde")
                self.assertEqual(result, [2])

    def test_multiple_matches(self):
        """Test with multiple matches in the text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_repeated, "aba")
                self.assertEqual(result, [0, 2, 4])

    def test_overlapping_matches(self):
        """Test with overlapping matches in the text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_with_overlap, "aa")
                self.assertEqual(result, [0, 1, 2, 3])

    def test_no_match(self):
        """Test with no matches in the text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "xyz")
                self.assertEqual(result, [])

    def test_match_at_beginning(self):
        """Test with a match at the beginning of the text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "abc")
                self.assertEqual(result, [0])

    def test_match_at_end(self):
        """Test with a match at the end of the text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "efg")
                self.assertEqual(result, [4])

    def test_case_sensitivity(self):
        """Test case sensitivity of the search."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "ABC")
                self.assertEqual(result, [])

    def test_long_text(self):
        """Test with a longer text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_long, "the")
                self.assertEqual(result, [31])  # "the" appears at index 31

    def test_entire_text_match(self):
        """Test when the pattern is the entire text."""
        for search_func in [
            naive_pattern_search_slice,
            naive_pattern_search_character,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_counting,
            naive_pattern_search_optimized
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, self.text_simple)
                self.assertEqual(result, [0])

if __name__ == '__main__':
    unittest.main()