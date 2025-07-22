import unittest
from data_structures.LinkedList import LinkedList
from algorithms.find_max import find_max_ll, find_maximum_iterative, find_maximum_recursive

class TestFindMax(unittest.TestCase):

    # Tests for find_max_ll (linked list implementation)
    def test_find_max_ll_multiple_elements(self):
        """Test finding maximum in a linked list with multiple elements"""
        # Create a linked list with multiple elements
        ll = LinkedList(5)
        ll.insert(10)  # Now the list is: 10 -> 5
        ll.insert(3)   # Now the list is: 3 -> 10 -> 5
        ll.insert(8)   # Now the list is: 8 -> 3 -> 10 -> 5

        # Find the maximum value
        max_value = find_max_ll(ll)

        # Verify the maximum value is 10
        self.assertEqual(max_value, 10)

    def test_find_max_ll_single_element(self):
        """Test finding maximum in a linked list with a single element"""
        # Create a linked list with a single element
        ll = LinkedList(7)

        # Find the maximum value
        max_value = find_max_ll(ll)

        # Verify the maximum value is 7
        self.assertEqual(max_value, 7)

    def test_find_max_ll_empty_list(self):
        """Test finding maximum in an empty linked list (should raise ValueError)"""
        # Create an empty linked list
        ll = LinkedList()

        # Attempt to find the maximum value, should raise ValueError
        with self.assertRaises(ValueError):
            find_max_ll(ll)

    def test_find_max_ll_negative_numbers(self):
        """Test finding maximum in a linked list with negative numbers"""
        ll = LinkedList(-5)
        ll.insert(-10)  # Now the list is: -10 -> -5
        ll.insert(-3)   # Now the list is: -3 -> -10 -> -5
        ll.insert(-8)   # Now the list is: -8 -> -3 -> -10 -> -5

        max_value = find_max_ll(ll)
        self.assertEqual(max_value, -3)

    def test_find_max_ll_duplicate_max(self):
        """Test finding maximum when there are duplicate maximum values"""
        ll = LinkedList(5)
        ll.insert(10)  # Now the list is: 10 -> 5
        ll.insert(10)  # Now the list is: 10 -> 10 -> 5
        ll.insert(3)   # Now the list is: 3 -> 10 -> 10 -> 5

        max_value = find_max_ll(ll)
        self.assertEqual(max_value, 10)

    # Tests for find_maximum_iterative (list implementation)
    def test_find_maximum_iterative_multiple_elements(self):
        """Test finding maximum in a list with multiple elements using iterative approach"""
        values = [3, 8, 10, 5]
        max_value = find_maximum_iterative(values)
        self.assertEqual(max_value, 10)

    def test_find_maximum_iterative_single_element(self):
        """Test finding maximum in a list with a single element using iterative approach"""
        values = [7]
        max_value = find_maximum_iterative(values)
        self.assertEqual(max_value, 7)

    def test_find_maximum_iterative_empty_list(self):
        """Test finding maximum in an empty list using iterative approach"""
        values = []
        max_value = find_maximum_iterative(values)
        self.assertIsNone(max_value)

    def test_find_maximum_iterative_negative_numbers(self):
        """Test finding maximum in a list with negative numbers using iterative approach"""
        values = [-8, -3, -10, -5]
        max_value = find_maximum_iterative(values)
        self.assertEqual(max_value, -3)

    def test_find_maximum_iterative_duplicate_max(self):
        """Test finding maximum when there are duplicate maximum values using iterative approach"""
        values = [3, 10, 10, 5]
        max_value = find_maximum_iterative(values)
        self.assertEqual(max_value, 10)

    def test_find_maximum_iterative_mixed_numbers(self):
        """Test finding maximum in a list with mixed positive and negative numbers"""
        values = [-5, 3, -10, 8, 0]
        max_value = find_maximum_iterative(values)
        self.assertEqual(max_value, 8)

    # Tests for find_maximum_recursive (list implementation)
    def test_find_maximum_recursive_multiple_elements(self):
        """Test finding maximum in a list with multiple elements using recursive approach"""
        values = [3, 8, 10, 5]
        max_value = find_maximum_recursive(values)
        self.assertEqual(max_value, 10)

    def test_find_maximum_recursive_single_element(self):
        """Test finding maximum in a list with a single element using recursive approach"""
        values = [7]
        max_value = find_maximum_recursive(values)
        self.assertEqual(max_value, 7)

    def test_find_maximum_recursive_empty_list(self):
        """Test finding maximum in an empty list using recursive approach"""
        values = []
        max_value = find_maximum_recursive(values)
        self.assertIsNone(max_value)

    def test_find_maximum_recursive_negative_numbers(self):
        """Test finding maximum in a list with negative numbers using recursive approach"""
        values = [-8, -3, -10, -5]
        max_value = find_maximum_recursive(values)
        self.assertEqual(max_value, -3)

    def test_find_maximum_recursive_duplicate_max(self):
        """Test finding maximum when there are duplicate maximum values using recursive approach"""
        values = [3, 10, 10, 5]
        max_value = find_maximum_recursive(values)
        self.assertEqual(max_value, 10)

    def test_find_maximum_recursive_mixed_numbers(self):
        """Test finding maximum in a list with mixed positive and negative numbers"""
        values = [-5, 3, -10, 8, 0]
        max_value = find_maximum_recursive(values)
        self.assertEqual(max_value, 8)

if __name__ == '__main__':
    unittest.main()
