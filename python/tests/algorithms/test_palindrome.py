import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.palindrome import (
    is_palindrome,
    is_palindrome_quadratic,
    is_palindrome_recursive_optimized,
    is_palindrome_recursive_quadratic
)


class TestPalindrome(unittest.TestCase):

    def test_is_palindrome_regular_cases(self):
        """Test is_palindrome with regular palindromes and non-palindromes"""
        # Palindromes
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("deified"))
        self.assertTrue(is_palindrome("radar"))
        
        # Non-palindromes
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("algorithm"))
        self.assertFalse(is_palindrome("python"))

    def test_is_palindrome_edge_cases(self):
        """Test is_palindrome with edge cases"""
        # Empty string
        self.assertTrue(is_palindrome(""))
        # Single character
        self.assertTrue(is_palindrome("a"))
        # Two same characters
        self.assertTrue(is_palindrome("aa"))
        # Two different characters
        self.assertFalse(is_palindrome("ab"))

    def test_is_palindrome_special_cases(self):
        """Test is_palindrome with special cases (case sensitivity)"""
        # Case sensitivity
        self.assertFalse(is_palindrome("Racecar"))  # 'R' != 'r'
        self.assertFalse(is_palindrome("Level"))    # 'L' != 'l'
        
        # With spaces (not handled by default implementation)
        self.assertFalse(is_palindrome("race car"))
        self.assertFalse(is_palindrome("a man a plan a canal panama"))

    def test_is_palindrome_quadratic_regular_cases(self):
        """Test is_palindrome_quadratic with regular palindromes and non-palindromes"""
        # Palindromes
        self.assertTrue(is_palindrome_quadratic("racecar"))
        self.assertTrue(is_palindrome_quadratic("level"))
        self.assertTrue(is_palindrome_quadratic("deified"))
        self.assertTrue(is_palindrome_quadratic("radar"))
        
        # Non-palindromes
        self.assertFalse(is_palindrome_quadratic("hello"))
        self.assertFalse(is_palindrome_quadratic("world"))
        self.assertFalse(is_palindrome_quadratic("algorithm"))
        self.assertFalse(is_palindrome_quadratic("python"))

    def test_is_palindrome_quadratic_edge_cases(self):
        """Test is_palindrome_quadratic with edge cases"""
        # Empty string
        self.assertTrue(is_palindrome_quadratic(""))
        # Single character
        self.assertTrue(is_palindrome_quadratic("a"))
        # Two same characters
        self.assertTrue(is_palindrome_quadratic("aa"))
        # Two different characters
        self.assertFalse(is_palindrome_quadratic("ab"))

    def test_is_palindrome_recursive_optimized_regular_cases(self):
        """Test is_palindrome_recursive_optimized with regular palindromes and non-palindromes"""
        # Palindromes
        self.assertTrue(is_palindrome_recursive_optimized("racecar"))
        self.assertTrue(is_palindrome_recursive_optimized("level"))
        self.assertTrue(is_palindrome_recursive_optimized("deified"))
        self.assertTrue(is_palindrome_recursive_optimized("radar"))
        
        # Non-palindromes
        self.assertFalse(is_palindrome_recursive_optimized("hello"))
        self.assertFalse(is_palindrome_recursive_optimized("world"))
        self.assertFalse(is_palindrome_recursive_optimized("algorithm"))
        self.assertFalse(is_palindrome_recursive_optimized("python"))

    def test_is_palindrome_recursive_optimized_edge_cases(self):
        """Test is_palindrome_recursive_optimized with edge cases"""
        # Empty string
        self.assertTrue(is_palindrome_recursive_optimized(""))
        # Single character
        self.assertTrue(is_palindrome_recursive_optimized("a"))
        # Two same characters
        self.assertTrue(is_palindrome_recursive_optimized("aa"))
        # Two different characters
        self.assertFalse(is_palindrome_recursive_optimized("ab"))

    def test_is_palindrome_recursive_quadratic_regular_cases(self):
        """Test is_palindrome_recursive_quadratic with regular palindromes and non-palindromes"""
        # Palindromes
        self.assertTrue(is_palindrome_recursive_quadratic("racecar"))
        self.assertTrue(is_palindrome_recursive_quadratic("level"))
        self.assertTrue(is_palindrome_recursive_quadratic("deified"))
        self.assertTrue(is_palindrome_recursive_quadratic("radar"))
        
        # Non-palindromes
        self.assertFalse(is_palindrome_recursive_quadratic("hello"))
        self.assertFalse(is_palindrome_recursive_quadratic("world"))
        self.assertFalse(is_palindrome_recursive_quadratic("algorithm"))
        self.assertFalse(is_palindrome_recursive_quadratic("python"))

    def test_is_palindrome_recursive_quadratic_edge_cases(self):
        """Test is_palindrome_recursive_quadratic with edge cases"""
        # Empty string
        self.assertTrue(is_palindrome_recursive_quadratic(""))
        # Single character
        self.assertTrue(is_palindrome_recursive_quadratic("a"))
        # Two same characters
        self.assertTrue(is_palindrome_recursive_quadratic("aa"))
        # Two different characters
        self.assertFalse(is_palindrome_recursive_quadratic("ab"))

    def test_all_implementations_consistent(self):
        """Test that all implementations produce consistent results"""
        test_cases = [
            "",           # Empty string
            "a",          # Single character
            "aa",         # Two same characters
            "ab",         # Two different characters
            "racecar",    # Odd-length palindrome
            "level",      # Even-length palindrome
            "hello",      # Non-palindrome
            "python"      # Non-palindrome
        ]
        
        for test_case in test_cases:
            result1 = is_palindrome(test_case)
            result2 = is_palindrome_quadratic(test_case)
            result3 = is_palindrome_recursive_optimized(test_case)
            result4 = is_palindrome_recursive_quadratic(test_case)
            
            self.assertEqual(result1, result2, 
                             f"is_palindrome and is_palindrome_quadratic differ for '{test_case}'")
            self.assertEqual(result1, result3, 
                             f"is_palindrome and is_palindrome_recursive_optimized differ for '{test_case}'")
            self.assertEqual(result1, result4, 
                             f"is_palindrome and is_palindrome_recursive_quadratic differ for '{test_case}'")


if __name__ == '__main__':
    unittest.main()