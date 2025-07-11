import unittest
from data_structures.Node import Node

class TestNode(unittest.TestCase):
    def test_init(self):
        """Test Node initialization"""
        # Test with only data
        node = Node(5)
        self.assertEqual(node.get_data(), 5)
        self.assertIsNone(node.get_next())
        
        # Test with data and next node
        next_node = Node(10)
        node = Node(5, next_node)
        self.assertEqual(node.get_data(), 5)
        self.assertEqual(node.get_next(), next_node)
    
    def test_get_data(self):
        """Test get_data method"""
        node = Node("test_data")
        self.assertEqual(node.get_data(), "test_data")
        
        # Test with None data
        node = Node(None)
        self.assertIsNone(node.get_data())
    
    def test_get_next(self):
        """Test get_next method"""
        # Test with no next node
        node = Node(5)
        self.assertIsNone(node.get_next())
        
        # Test with next node
        next_node = Node(10)
        node = Node(5, next_node)
        self.assertEqual(node.get_next(), next_node)
    
    def test_set_next(self):
        """Test set_next method"""
        node = Node(5)
        next_node = Node(10)
        
        # Set next node
        node.set_next(next_node)
        self.assertEqual(node.get_next(), next_node)
        
        # Change next node
        new_next = Node(15)
        node.set_next(new_next)
        self.assertEqual(node.get_next(), new_next)
        
        # Set next to None
        node.set_next(None)
        self.assertIsNone(node.get_next())

if __name__ == '__main__':
    unittest.main()