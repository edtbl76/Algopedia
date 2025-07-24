import unittest
from search.naive_pattern_search_v2 import (
    _chars_match,
    naive_pattern_search_character,
    naive_pattern_search_counting,
    naive_pattern_search_safe_bounds,
    naive_pattern_search_slice,
    naive_pattern_search_tunable
)

class TestCharsMatch(unittest.TestCase):
    """Test cases for the _chars_match helper function."""

    def test_case_sensitive_match(self):
        """Test case-sensitive character matching."""
        self.assertTrue(_chars_match('a', 'a', case_sensitive=True))
        self.assertFalse(_chars_match('a', 'A', case_sensitive=True))
        self.assertTrue(_chars_match('X', 'X', case_sensitive=True))

    def test_case_insensitive_match(self):
        """Test case-insensitive character matching."""
        self.assertTrue(_chars_match('a', 'a', case_sensitive=False))
        self.assertTrue(_chars_match('a', 'A', case_sensitive=False))
        self.assertTrue(_chars_match('A', 'a', case_sensitive=False))
        self.assertFalse(_chars_match('a', 'b', case_sensitive=False))


class TestNaivePatternSearchV2(unittest.TestCase):
    """Test cases for all naive pattern search implementations in v2."""

    def setUp(self):
        """Set up common test data."""
        self.text_empty = ""
        self.text_single = "a"
        self.text_simple = "abcdefg"
        self.text_repeated = "abababa"
        self.text_with_overlap = "aaaaa"
        self.text_long = "The quick brown fox jumps over the lazy dog"
        self.text_mixed_case = "AbCdEfG"

    def test_empty_pattern(self):
        """Test with an empty pattern (should return empty list)."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "")
                self.assertEqual(result, [])

    def test_empty_text(self):
        """Test with an empty text (should return empty list)."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func("", "pattern")
                self.assertEqual(result, [])

    def test_pattern_longer_than_text(self):
        """Test with a pattern longer than the text (should return empty list)."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func("abc", "abcdef")
                self.assertEqual(result, [])

    def test_single_match(self):
        """Test with a single match in the text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "cde")
                self.assertEqual(result, [2])

    def test_multiple_matches(self):
        """Test with multiple matches in the text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_repeated, "aba")
                self.assertEqual(result, [0, 2, 4])

    def test_overlapping_matches(self):
        """Test with overlapping matches in the text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_with_overlap, "aa")
                self.assertEqual(result, [0, 1, 2, 3])

    def test_no_match(self):
        """Test with no matches in the text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "xyz")
                self.assertEqual(result, [])

    def test_match_at_beginning(self):
        """Test with a match at the beginning of the text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "abc")
                self.assertEqual(result, [0])

    def test_match_at_end(self):
        """Test with a match at the end of the text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, "efg")
                self.assertEqual(result, [4])

    def test_case_sensitivity_default(self):
        """Test default case sensitivity of the search."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                # Default is case sensitive, so uppercase should not match lowercase
                result = search_func(self.text_simple, "ABC")
                self.assertEqual(result, [])

    def test_case_sensitivity_explicit(self):
        """Test explicit case sensitivity settings."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                # Case sensitive (explicit)
                result = search_func(self.text_mixed_case, "bCd", case_sensitive=True)
                self.assertEqual(result, [1])

                # Case insensitive
                result = search_func(self.text_mixed_case, "BcD", case_sensitive=False)
                self.assertEqual(result, [1])

    def test_long_text(self):
        """Test with a longer text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_long, "the")
                self.assertEqual(result, [31])  # "the" appears at index 31

    def test_entire_text_match(self):
        """Test when the pattern is the entire text."""
        for search_func in [
            naive_pattern_search_character,
            naive_pattern_search_counting,
            naive_pattern_search_safe_bounds,
            naive_pattern_search_slice,
            naive_pattern_search_tunable
        ]:
            with self.subTest(search_func=search_func.__name__):
                result = search_func(self.text_simple, self.text_simple)
                self.assertEqual(result, [0])

    def test_tunable_threshold(self):
        """Test the tunable threshold parameter in naive_pattern_search_tunable."""
        # Test with a pattern shorter than the default threshold (4)
        short_pattern = "abc"
        result1 = naive_pattern_search_tunable(self.text_simple, short_pattern)
        self.assertEqual(result1, [0])

        # Test with a pattern longer than the default threshold
        long_pattern = "abcde"
        result2 = naive_pattern_search_tunable(self.text_simple, long_pattern)
        self.assertEqual(result2, [0])

        # Test with a custom threshold that changes the algorithm selection
        # Setting threshold to 2 should make "abc" use character comparison instead of slicing
        result3 = naive_pattern_search_tunable(self.text_simple, short_pattern, slice_threshold=2)
        self.assertEqual(result3, [0])

        # Setting threshold to 10 should make "abcde" use slicing instead of character comparison
        result4 = naive_pattern_search_tunable(self.text_simple, long_pattern, slice_threshold=10)
        self.assertEqual(result4, [0])


if __name__ == '__main__':
    unittest.main()
