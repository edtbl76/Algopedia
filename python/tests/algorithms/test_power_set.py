import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.power_set import iterative_power_set, recursive_power_set


class TestPowerSet(unittest.TestCase):

    def test_iterative_power_set_empty_set(self):
        """Test iterative power set with empty set"""
        result = iterative_power_set(set())
        self.assertEqual(result, [[]])

    def test_iterative_power_set_single_element(self):
        """Test iterative power set with single element"""
        result = iterative_power_set({1})
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (1,)}
        self.assertEqual(result_set, expected_set)

    def test_iterative_power_set_two_elements(self):
        """Test iterative power set with two elements"""
        result = iterative_power_set({1, 2})
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (1,), (2,), (1, 2)}
        self.assertEqual(result_set, expected_set)

    def test_iterative_power_set_three_elements(self):
        """Test iterative power set with three elements"""
        result = iterative_power_set({1, 2, 3})
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
        self.assertEqual(result_set, expected_set)

    def test_iterative_power_set_negative_numbers(self):
        """Test iterative power set with negative numbers"""
        result = iterative_power_set({-1, -2})
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (-2,), (-1,), (-2, -1)}
        self.assertEqual(result_set, expected_set)

    def test_recursive_power_set_empty_list(self):
        """Test recursive power set with empty list"""
        result = recursive_power_set([])
        self.assertEqual(result, [[]])

    def test_recursive_power_set_single_element(self):
        """Test recursive power set with single element"""
        result = recursive_power_set([1])
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (1,)}
        self.assertEqual(result_set, expected_set)

    def test_recursive_power_set_two_elements(self):
        """Test recursive power set with two elements"""
        result = recursive_power_set([1, 2])
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (1,), (2,), (1, 2)}
        self.assertEqual(result_set, expected_set)

    def test_recursive_power_set_three_elements(self):
        """Test recursive power set with three elements"""
        result = recursive_power_set([1, 2, 3])
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
        self.assertEqual(result_set, expected_set)

    def test_recursive_power_set_negative_numbers(self):
        """Test recursive power set with negative numbers"""
        result = recursive_power_set([-1, -2])
        # Convert to set of tuples for order-independent comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {(), (-2,), (-1,), (-2, -1)}
        self.assertEqual(result_set, expected_set)

    def test_recursive_power_set_duplicates_in_list(self):
        """Test recursive power set with duplicate elements in list"""
        result = recursive_power_set([1, 1])
        # Should still generate all combinations even with duplicates
        result_sorted = [sorted(subset) for subset in result]
        result_sorted.sort()
        expected = [[], [1], [1], [1, 1]]
        self.assertEqual(result_sorted, expected)

    def test_power_set_size_consistency(self):
        """Test that both functions return the correct number of subsets"""
        # For a set/list of size n, power set should have 2^n subsets
        test_cases = [
            (set(), []),  # empty
            ({1}, [1]),   # size 1
            ({1, 2}, [1, 2]),  # size 2
            ({1, 2, 3}, [1, 2, 3])  # size 3
        ]

        for test_set, test_list in test_cases:
            iterative_result = iterative_power_set(test_set)
            recursive_result = recursive_power_set(test_list)
            expected_size = 2 ** len(test_set)

            self.assertEqual(len(iterative_result), expected_size)
            self.assertEqual(len(recursive_result), expected_size)

    def test_both_functions_equivalent_results(self):
        """Test that both functions produce equivalent results (ignoring order)"""
        test_cases = [
            (set(), []),
            ({1}, [1]),
            ({1, 2}, [1, 2]),
            ({1, 2, 3}, [1, 2, 3])
        ]

        for test_set, test_list in test_cases:
            iterative_result = iterative_power_set(test_set)
            recursive_result = recursive_power_set(test_list)

            # Sort both results for comparison
            iterative_sorted = [sorted(subset) for subset in iterative_result]
            iterative_sorted.sort()

            recursive_sorted = [sorted(subset) for subset in recursive_result]
            recursive_sorted.sort()

            self.assertEqual(iterative_sorted, recursive_sorted)


if __name__ == '__main__':
    unittest.main()
