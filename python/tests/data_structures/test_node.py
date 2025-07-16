import unittest
from data_structures.SinglePointNode import Node

class TestNode(unittest.TestCase):
    def test_init(self):
        """Test Node initialization"""
        # Test with only data
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.next)

        # Test with data and next node
        next_node = Node(10)
        node = Node(5, next_node)
        self.assertEqual(node.data, 5)
        self.assertEqual(node.next, next_node)

    def test_data_property(self):
        """Test data property"""
        node = Node("test_data")
        self.assertEqual(node.data, "test_data")

        # Test with None data
        node = Node(None)
        self.assertIsNone(node.data)

    def test_next_property(self):
        """Test next property"""
        # Test with no next node
        node = Node(5)
        self.assertIsNone(node.next)

        # Test with next node
        next_node = Node(10)
        node = Node(5, next_node)
        self.assertEqual(node.next, next_node)

    def test_next_setter(self):
        """Test next setter"""
        node = Node(5)
        next_node = Node(10)

        # Set next node
        node.next = next_node
        self.assertEqual(node.next, next_node)

        # Change next node
        new_next = Node(15)
        node.next = new_next
        self.assertEqual(node.next, new_next)

        # Set next to None
        node.next = None
        self.assertIsNone(node.next)

if __name__ == '__main__':
    unittest.main()
