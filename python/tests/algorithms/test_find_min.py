import unittest
from data_structures.LinkedList import LinkedList
from algorithms.find_min import find_min_ll, find_minimum_iterative, find_minimum_recursive

class TestFindMin(unittest.TestCase):

    # Tests for find_min_ll (linked list implementation)
    def test_find_min_ll_multiple_elements(self):
        """Test finding minimum in a linked list with multiple elements"""
        # Create a linked list with multiple elements
        ll = LinkedList(5)
        ll.insert(10)  # Now the list is: 10 -> 5
        ll.insert(3)   # Now the list is: 3 -> 10 -> 5
        ll.insert(8)   # Now the list is: 8 -> 3 -> 10 -> 5

        # Find the minimum value
        min_value = find_min_ll(ll)

        # Verify the minimum value is 3
        self.assertEqual(min_value, 3)

    def test_find_min_ll_single_element(self):
        """Test finding minimum in a linked list with a single element"""
        # Create a linked list with a single element
        ll = LinkedList(7)

        # Find the minimum value
        min_value = find_min_ll(ll)

        # Verify the minimum value is 7
        self.assertEqual(min_value, 7)

    def test_find_min_ll_empty_list(self):
        """Test finding minimum in an empty linked list (should raise ValueError)"""
        # Create an empty linked list
        ll = LinkedList()

        # Attempt to find the minimum value, should raise ValueError
        with self.assertRaises(ValueError):
            find_min_ll(ll)

    def test_find_min_ll_negative_numbers(self):
        """Test finding minimum in a linked list with negative numbers"""
        ll = LinkedList(-5)
        ll.insert(-10)  # Now the list is: -10 -> -5
        ll.insert(-3)   # Now the list is: -3 -> -10 -> -5
        ll.insert(-8)   # Now the list is: -8 -> -3 -> -10 -> -5

        min_value = find_min_ll(ll)
        self.assertEqual(min_value, -10)

    def test_find_min_ll_duplicate_min(self):
        """Test finding minimum when there are duplicate minimum values"""
        ll = LinkedList(5)
        ll.insert(3)   # Now the list is: 3 -> 5
        ll.insert(3)   # Now the list is: 3 -> 3 -> 5
        ll.insert(10)  # Now the list is: 10 -> 3 -> 3 -> 5

        min_value = find_min_ll(ll)
        self.assertEqual(min_value, 3)

    # Tests for find_minimum_iterative (list implementation)
    def test_find_minimum_iterative_multiple_elements(self):
        """Test finding minimum in a list with multiple elements using iterative approach"""
        values = [8, 3, 10, 5]
        min_value = find_minimum_iterative(values)
        self.assertEqual(min_value, 3)

    def test_find_minimum_iterative_single_element(self):
        """Test finding minimum in a list with a single element using iterative approach"""
        values = [7]
        min_value = find_minimum_iterative(values)
        self.assertEqual(min_value, 7)

    def test_find_minimum_iterative_empty_list(self):
        """Test finding minimum in an empty list using iterative approach"""
        values = []
        min_value = find_minimum_iterative(values)
        self.assertIsNone(min_value)

    def test_find_minimum_iterative_negative_numbers(self):
        """Test finding minimum in a list with negative numbers using iterative approach"""
        values = [-8, -3, -10, -5]
        min_value = find_minimum_iterative(values)
        self.assertEqual(min_value, -10)

    def test_find_minimum_iterative_duplicate_min(self):
        """Test finding minimum when there are duplicate minimum values using iterative approach"""
        values = [10, 3, 3, 5]
        min_value = find_minimum_iterative(values)
        self.assertEqual(min_value, 3)

    def test_find_minimum_iterative_mixed_numbers(self):
        """Test finding minimum in a list with mixed positive and negative numbers"""
        values = [-5, 3, -10, 8, 0]
        min_value = find_minimum_iterative(values)
        self.assertEqual(min_value, -10)

    # Tests for find_minimum_recursive (list implementation)
    def test_find_minimum_recursive_multiple_elements(self):
        """Test finding minimum in a list with multiple elements using recursive approach"""
        values = [8, 3, 10, 5]
        min_value = find_minimum_recursive(values)
        self.assertEqual(min_value, 3)

    def test_find_minimum_recursive_single_element(self):
        """Test finding minimum in a list with a single element using recursive approach"""
        values = [7]
        min_value = find_minimum_recursive(values)
        self.assertEqual(min_value, 7)

    def test_find_minimum_recursive_empty_list(self):
        """Test finding minimum in an empty list using recursive approach"""
        values = []
        min_value = find_minimum_recursive(values)
        self.assertIsNone(min_value)

    def test_find_minimum_recursive_negative_numbers(self):
        """Test finding minimum in a list with negative numbers using recursive approach"""
        values = [-8, -3, -10, -5]
        min_value = find_minimum_recursive(values)
        self.assertEqual(min_value, -10)

    def test_find_minimum_recursive_duplicate_min(self):
        """Test finding minimum when there are duplicate minimum values using recursive approach"""
        values = [10, 3, 3, 5]
        min_value = find_minimum_recursive(values)
        self.assertEqual(min_value, 3)

    def test_find_minimum_recursive_mixed_numbers(self):
        """Test finding minimum in a list with mixed positive and negative numbers"""
        values = [-5, 3, -10, 8, 0]
        min_value = find_minimum_recursive(values)
        self.assertEqual(min_value, -10)

if __name__ == '__main__':
    unittest.main()
