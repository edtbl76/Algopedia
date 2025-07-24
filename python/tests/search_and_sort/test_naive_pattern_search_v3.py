import unittest
from search_and_sort.naive_pattern_search_v3_find_replace import (
    _chars_match,
    naive_find_replace_character,
    naive_find_replace_counting,
    naive_find_replace_safe_bounds,
    naive_find_replace_slice,
    naive_find_replace_tunable,
    _handle_edge_cases,
    _handle_single_char_replacement,
    _setup_replacement_variables,
    _add_remaining_characters,
    _replace_using_slice_strategy,
    _replace_using_character_strategy
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

    def test_invalid_inputs(self):
        """Test with invalid inputs."""
        with self.assertRaises(TypeError):
            _chars_match(1, 'a')
        with self.assertRaises(TypeError):
            _chars_match('a', 1)
        with self.assertRaises(ValueError):
            _chars_match('ab', 'a')
        with self.assertRaises(ValueError):
            _chars_match('a', 'ab')


class TestHelperFunctions(unittest.TestCase):
    """Test cases for helper functions."""

    def test_handle_edge_cases(self):
        """Test the _handle_edge_cases function."""
        # Empty pattern
        should_return, result = _handle_edge_cases("text", "", )
        self.assertTrue(should_return)
        self.assertEqual(result, "text")

        # Pattern longer than text
        should_return, result = _handle_edge_cases("abc", "abcdef")
        self.assertTrue(should_return)
        self.assertEqual(result, "abc")

        # Empty text
        should_return, result = _handle_edge_cases("", "pattern")
        self.assertTrue(should_return)
        self.assertEqual(result, "")

        # Normal case
        should_return, result = _handle_edge_cases("longer text", "pat")
        self.assertFalse(should_return)

    def test_handle_single_char_replacement(self):
        """Test the _handle_single_char_replacement function."""
        # Case sensitive, single char pattern
        should_return, result = _handle_single_char_replacement("abcabc", "a", "X", True)
        self.assertTrue(should_return)
        self.assertEqual(result, "XbcXbc")

        # Case insensitive, single char pattern
        should_return, result = _handle_single_char_replacement("aBcAbC", "a", "X", False)
        self.assertTrue(should_return)
        self.assertEqual(result, "XBcXbC")

        # Multi-char pattern
        should_return, result = _handle_single_char_replacement("abcabc", "ab", "X", True)
        self.assertFalse(should_return)

    def test_setup_replacement_variables(self):
        """Test the _setup_replacement_variables function."""
        # Case sensitive
        search_text, search_pattern, text_length, pattern_length, max_search_position = _setup_replacement_variables(
            "abcABC", "abc", True
        )
        self.assertEqual(search_text, "abcABC")
        self.assertEqual(search_pattern, "abc")
        self.assertEqual(text_length, 6)
        self.assertEqual(pattern_length, 3)
        self.assertEqual(max_search_position, 4)

        # Case insensitive
        search_text, search_pattern, text_length, pattern_length, max_search_position = _setup_replacement_variables(
            "abcABC", "abc", False
        )
        self.assertEqual(search_text, "abcabc")
        self.assertEqual(search_pattern, "abc")
        self.assertEqual(text_length, 6)
        self.assertEqual(pattern_length, 3)
        self.assertEqual(max_search_position, 4)

    def test_add_remaining_characters(self):
        """Test the _add_remaining_characters function."""
        # With remaining characters
        result_parts = ["a", "b", "c"]
        _add_remaining_characters(result_parts, "abcdef", 3, 6)
        self.assertEqual(result_parts, ["a", "b", "c", "def"])

        # Without remaining characters
        result_parts = ["a", "b", "c", "d", "e", "f"]
        _add_remaining_characters(result_parts, "abcdef", 6, 6)
        self.assertEqual(result_parts, ["a", "b", "c", "d", "e", "f"])


class TestNaivePatternSearchV3(unittest.TestCase):
    """Test cases for all naive pattern search v3 implementations."""

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
        """Test with an empty pattern (should return original text)."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_simple, "", "REPLACEMENT")
                self.assertEqual(result, self.text_simple)

    def test_empty_text(self):
        """Test with an empty text (should return empty string)."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func("", "pattern", "REPLACEMENT")
                self.assertEqual(result, "")

    def test_pattern_longer_than_text(self):
        """Test with a pattern longer than the text (should return original text)."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func("abc", "abcdef", "REPLACEMENT")
                self.assertEqual(result, "abc")

    def test_single_match(self):
        """Test with a single match in the text."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_simple, "cde", "X")
                self.assertEqual(result, "abXfg")

    def test_multiple_matches(self):
        """Test with multiple matches in the text."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_repeated, "aba", "X")
                self.assertEqual(result, "XbX")

    def test_overlapping_matches(self):
        """Test with overlapping matches in the text."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_with_overlap, "aa", "X")
                self.assertEqual(result, "XXa")

    def test_no_match(self):
        """Test with no matches in the text."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_simple, "xyz", "REPLACEMENT")
                self.assertEqual(result, self.text_simple)

    def test_match_at_beginning(self):
        """Test with a match at the beginning of the text."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_simple, "abc", "X")
                self.assertEqual(result, "Xdefg")

    def test_match_at_end(self):
        """Test with a match at the end of the text."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_simple, "efg", "X")
                self.assertEqual(result, "abcdX")

    def test_case_sensitivity_default(self):
        """Test default case sensitivity of the search."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                # Default is case sensitive, so uppercase should not match lowercase
                result = replace_func(self.text_simple, "ABC", "X")
                self.assertEqual(result, self.text_simple)

    def test_case_sensitivity_explicit(self):
        """Test explicit case sensitivity settings."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                # Case sensitive (explicit)
                result = replace_func(self.text_mixed_case, "bCd", "X", case_sensitive=True)
                self.assertEqual(result, "AXEfG")

                # Case insensitive
                result = replace_func(self.text_mixed_case, "BcD", "X", case_sensitive=False)
                self.assertEqual(result, "AXEfG")

    def test_empty_replacement(self):
        """Test with an empty replacement string (should delete the pattern)."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_simple, "cde", "")
                self.assertEqual(result, "abfg")

    def test_entire_text_match(self):
        """Test when the pattern is the entire text."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func(self.text_simple, self.text_simple, "X")
                self.assertEqual(result, "X")

    def test_single_character_pattern(self):
        """Test with a single character pattern."""
        for replace_func in [
            naive_find_replace_character,
            naive_find_replace_counting,
            naive_find_replace_safe_bounds,
            naive_find_replace_slice,
            naive_find_replace_tunable
        ]:
            with self.subTest(replace_func=replace_func.__name__):
                result = replace_func("ababa", "a", "X")
                self.assertEqual(result, "XbXbX")

    def test_tunable_threshold(self):
        """Test the tunable threshold parameter in naive_find_replace_tunable."""
        # Test with a pattern shorter than the default threshold (4)
        short_pattern = "abc"
        result1 = naive_find_replace_tunable(self.text_simple, short_pattern, "X")
        self.assertEqual(result1, "Xdefg")

        # Test with a pattern longer than the default threshold
        long_pattern = "abcde"
        result2 = naive_find_replace_tunable(self.text_simple, long_pattern, "X")
        self.assertEqual(result2, "Xfg")

        # Test with a custom threshold that changes the algorithm selection
        # Setting threshold to 2 should make "abc" use character comparison instead of slicing
        result3 = naive_find_replace_tunable(self.text_simple, short_pattern, "X", slice_threshold=2)
        self.assertEqual(result3, "Xdefg")

        # Setting threshold to 10 should make "abcde" use slicing instead of character comparison
        result4 = naive_find_replace_tunable(self.text_simple, long_pattern, "X", slice_threshold=10)
        self.assertEqual(result4, "Xfg")


if __name__ == '__main__':
    unittest.main()
