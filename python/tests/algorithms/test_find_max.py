import unittest
from data_structures.LinkedList import LinkedList
from algorithms.find_max import find_max

class TestFindMax(unittest.TestCase):
    def test_find_max_multiple_elements(self):
        """Test finding maximum in a linked list with multiple elements"""
        # Create a linked list with multiple elements
        ll = LinkedList(5)
        ll.insert(10)  # Now the list is: 10 -> 5
        ll.insert(3)   # Now the list is: 3 -> 10 -> 5
        ll.insert(8)   # Now the list is: 8 -> 3 -> 10 -> 5
        
        # Find the maximum value
        max_value = find_max(ll)
        
        # Verify the maximum value is 10
        self.assertEqual(max_value, 10)
    
    def test_find_max_single_element(self):
        """Test finding maximum in a linked list with a single element"""
        # Create a linked list with a single element
        ll = LinkedList(7)
        
        # Find the maximum value
        max_value = find_max(ll)
        
        # Verify the maximum value is 7
        self.assertEqual(max_value, 7)
    
    def test_find_max_empty_list(self):
        """Test finding maximum in an empty linked list (should raise ValueError)"""
        # Create an empty linked list
        ll = LinkedList()
        
        # Attempt to find the maximum value, should raise ValueError
        with self.assertRaises(ValueError):
            find_max(ll)

if __name__ == '__main__':
    unittest.main()