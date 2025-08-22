"""
Tests for permutation functions in the Combinatorics module.
"""
import unittest
from itertools import permutations as itertools_permutations

from algorithms.Combinatorics.permutations import (
    permutation_count,
    permutation_iterator,
    generate_permutations,
    PermutationMethod,
)


class TestPermutations(unittest.TestCase):
    """Test cases for permutation functions."""

    def test_permutation_count(self):
        """Test permutation_count function with various inputs."""
        test_cases = [
            # n, k, expected
            (5, 3, 60),      # P(5,3) = 5!/(5-3)! = 5!/2! = 60
            (5, 5, 120),     # P(5,5) = 5! = 120
            (5, 0, 1),       # P(5,0) = 1
            (0, 0, 1),       # P(0,0) = 1
            (10, 4, 5040),   # P(10,4) = 10!/(10-4)! = 10!/6! = 5040
        ]
        
        for n, k, expected in test_cases:
            with self.subTest(n=n, k=k):
                result = permutation_count(n, k)
                self.assertEqual(result, expected)
    
    def test_permutation_iterator(self):
        """Test permutation_iterator function."""
        # Test with a small list
        items = [1, 2, 3]
        k = 2
        
        # Get all permutations using our iterator
        result = list(permutation_iterator(items, k))
        
        # Get expected permutations using itertools
        expected = list(itertools_permutations(items, k))
        
        # Convert lists to sets of tuples for comparison (order might be different)
        result_set = {tuple(r) for r in result}
        expected_set = set(expected)
        
        self.assertEqual(result_set, expected_set)
        
        # Test with k=len(items)
        k = len(items)
        result = list(permutation_iterator(items, k))
        expected = list(itertools_permutations(items, k))
        result_set = {tuple(r) for r in result}
        expected_set = set(expected)
        self.assertEqual(result_set, expected_set)
        
        # Test with k=0 (should return empty tuple)
        k = 0
        result = list(permutation_iterator(items, k))
        expected = list(itertools_permutations(items, k))
        # Convert to sets for comparison
        result_set = {tuple(r) if r else tuple() for r in result}
        expected_set = set(expected)
        self.assertEqual(result_set, expected_set)
    
    def test_generate_permutations_methods(self):
        """Test all methods of generate_permutations function."""
        items = [1, 2, 3]
        k = 2
        
        # Expected permutations using itertools
        expected = set(itertools_permutations(items, k))
        
        # Test each method
        for method in [
            PermutationMethod.RECURSIVE,
            PermutationMethod.BACKTRACKING,
            PermutationMethod.LEXICOGRAPHIC,
            PermutationMethod.HEAPS,
        ]:
            with self.subTest(method=method.value):
                # Skip LEXICOGRAPHIC and HEAPS if k != len(items)
                if method in [PermutationMethod.LEXICOGRAPHIC, PermutationMethod.HEAPS] and k != len(items):
                    continue
                
                result = generate_permutations(items, k, method)
                # Convert lists to tuples for comparison
                result_set = {tuple(r) for r in result}
                self.assertEqual(result_set, expected)
    
    def test_generate_full_permutations(self):
        """Test generate_permutations with k=len(items) for all methods."""
        items = [1, 2, 3]
        k = len(items)
        
        # Expected permutations using itertools
        expected = set(itertools_permutations(items, k))
        
        # Test each method
        for method in [
            PermutationMethod.RECURSIVE,
            PermutationMethod.BACKTRACKING,
            PermutationMethod.LEXICOGRAPHIC,
            PermutationMethod.HEAPS,
        ]:
            with self.subTest(method=method.value):
                result = generate_permutations(items, k, method)
                # Convert lists to tuples for comparison
                result_set = {tuple(r) for r in result}
                self.assertEqual(result_set, expected)
    
    def test_empty_and_single_item(self):
        """Test edge cases with empty list and single item."""
        # Empty list
        items = []
        result = generate_permutations(items, 0)
        result_set = {tuple(r) if r else tuple() for r in result}
        self.assertEqual(result_set, {()})
        
        # Single item
        items = [1]
        result = generate_permutations(items, 0)
        result_set = {tuple(r) if r else tuple() for r in result}
        self.assertEqual(result_set, {()})
        
        result = generate_permutations(items, 1)
        result_set = {tuple(r) for r in result}
        self.assertEqual(result_set, {(1,)})
    
    def test_permutation_count_large_numbers(self):
        """Test permutation_count with larger numbers."""
        # P(20,5) = 20!/(20-5)! = 20!/15! = 20*19*18*17*16 = 1860480
        self.assertEqual(permutation_count(20, 5), 1860480)
        
        # P(15,10) = 15!/(15-10)! = 15!/5! = 15*14*13*12*11*10*9*8*7*6 = 10897286400
        self.assertEqual(permutation_count(15, 10), 10897286400)


if __name__ == "__main__":
    unittest.main()