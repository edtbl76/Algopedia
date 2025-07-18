import unittest
from data_structures.LinkedList import LinkedList
from algorithms.find_min import find_min

class TestFindMin(unittest.TestCase):
    def test_find_min_multiple_elements(self):
        """Test finding minimum in a linked list with multiple elements"""
        # Create a linked list with multiple elements
        ll = LinkedList(5)
        ll.insert(10)  # Now the list is: 10 -> 5
        ll.insert(3)   # Now the list is: 3 -> 10 -> 5
        ll.insert(8)   # Now the list is: 8 -> 3 -> 10 -> 5
        
        # Find the minimum value
        min_value = find_min(ll)
        
        # Verify the minimum value is 3
        self.assertEqual(min_value, 3)
    
    def test_find_min_single_element(self):
        """Test finding minimum in a linked list with a single element"""
        # Create a linked list with a single element
        ll = LinkedList(7)
        
        # Find the minimum value
        min_value = find_min(ll)
        
        # Verify the minimum value is 7
        self.assertEqual(min_value, 7)
    
    def test_find_min_empty_list(self):
        """Test finding minimum in an empty linked list (should raise ValueError)"""
        # Create an empty linked list
        ll = LinkedList()
        
        # Attempt to find the minimum value, should raise ValueError
        with self.assertRaises(ValueError):
            find_min(ll)

if __name__ == '__main__':
    unittest.main()