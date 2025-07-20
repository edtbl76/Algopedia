import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.fibonacci import fibonacci_basic, fibonacci_memoization


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_basic_base_cases(self):
        """Test fibonacci_basic with base cases"""
        self.assertEqual(fibonacci_basic(0), 0)
        self.assertEqual(fibonacci_basic(1), 1)

    def test_fibonacci_basic_small_numbers(self):
        """Test fibonacci_basic with small positive numbers"""
        self.assertEqual(fibonacci_basic(2), 1)
        self.assertEqual(fibonacci_basic(3), 2)
        self.assertEqual(fibonacci_basic(4), 3)
        self.assertEqual(fibonacci_basic(5), 5)
        self.assertEqual(fibonacci_basic(6), 8)
        self.assertEqual(fibonacci_basic(7), 13)

    def test_fibonacci_basic_larger_numbers(self):
        """Test fibonacci_basic with larger numbers (but not too large due to exponential complexity)"""
        self.assertEqual(fibonacci_basic(8), 21)
        self.assertEqual(fibonacci_basic(9), 34)
        self.assertEqual(fibonacci_basic(10), 55)

    def test_fibonacci_memoization_base_cases(self):
        """Test fibonacci_memoization with base cases"""
        self.assertEqual(fibonacci_memoization(0), 0)
        self.assertEqual(fibonacci_memoization(1), 1)

    def test_fibonacci_memoization_small_numbers(self):
        """Test fibonacci_memoization with small positive numbers"""
        self.assertEqual(fibonacci_memoization(2), 1)
        self.assertEqual(fibonacci_memoization(3), 2)
        self.assertEqual(fibonacci_memoization(4), 3)
        self.assertEqual(fibonacci_memoization(5), 5)
        self.assertEqual(fibonacci_memoization(6), 8)
        self.assertEqual(fibonacci_memoization(7), 13)

    def test_fibonacci_memoization_larger_numbers(self):
        """Test fibonacci_memoization with larger numbers"""
        self.assertEqual(fibonacci_memoization(15), 610)
        self.assertEqual(fibonacci_memoization(20), 6765)
        self.assertEqual(fibonacci_memoization(25), 75025)

    def test_fibonacci_consistency(self):
        """Test that both implementations produce the same results for small numbers"""
        for n in range(11):  # Test up to 10 to avoid exponential slowdown
            basic_result = fibonacci_basic(n)
            memo_result = fibonacci_memoization(n)
            self.assertEqual(basic_result, memo_result, 
                           f"Results differ for n={n}: basic={basic_result}, memo={memo_result}")

    def test_fibonacci_memoization_with_explicit_cache(self):
        """Test fibonacci_memoization with explicit memory dictionary"""
        cache = {}
        result = fibonacci_memoization(5, cache)
        self.assertEqual(result, 5)
        # Cache should contain intermediate results
        self.assertGreater(len(cache), 0)
        # Verify some expected values are cached
        self.assertEqual(cache[0], 0)
        self.assertEqual(cache[1], 1)
        self.assertEqual(cache[5], 5)

    def test_fibonacci_memoization_cache_reuse(self):
        """Test that memoization cache is properly reused"""
        cache = {}
        # First call should populate cache
        fibonacci_memoization(10, cache)
        initial_cache_size = len(cache)
        
        # Second call with smaller number should reuse cache
        result = fibonacci_memoization(8, cache)
        self.assertEqual(result, 21)
        # Cache size should not increase significantly
        self.assertEqual(len(cache), initial_cache_size)

    def test_fibonacci_sequence_properties(self):
        """Test mathematical properties of Fibonacci sequence"""
        # Test that F(n) = F(n-1) + F(n-2) for n > 1
        for n in range(2, 15):
            fn = fibonacci_memoization(n)
            fn_1 = fibonacci_memoization(n - 1)
            fn_2 = fibonacci_memoization(n - 2)
            self.assertEqual(fn, fn_1 + fn_2, 
                           f"Fibonacci property violated at n={n}: F({n})={fn} != F({n-1})+F({n-2})={fn_1}+{fn_2}")

    def test_fibonacci_known_values(self):
        """Test against known Fibonacci values"""
        known_values = {
            0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55,
            11: 89, 12: 144, 13: 233, 14: 377, 15: 610, 16: 987, 17: 1597, 18: 2584,
            19: 4181, 20: 6765
        }
        
        for n, expected in known_values.items():
            with self.subTest(n=n):
                self.assertEqual(fibonacci_memoization(n), expected)


if __name__ == '__main__':
    unittest.main()