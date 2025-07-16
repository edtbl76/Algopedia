import unittest
from data_structures.TwoPointNode import Node

class TestTwoPointNode(unittest.TestCase):
    def test_init(self):
        """Test Node initialization"""
        # Test with only data
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)

        # Test with data and next node
        next_node = Node(10)
        node = Node(5, next_node)
        self.assertEqual(node.data, 5)
        self.assertEqual(node.next, next_node)
        self.assertIsNone(node.prev)

        # Test with data, next node, and prev node
        prev_node = Node(15)
        node = Node(5, next_node, prev_node)
        self.assertEqual(node.data, 5)
        self.assertEqual(node.next, next_node)
        self.assertEqual(node.prev, prev_node)

    def test_data_property(self):
        """Test data property getter and setter"""
        node = Node("test_data")
        self.assertEqual(node.data, "test_data")

        # Test setting data
        node.data = "new_data"
        self.assertEqual(node.data, "new_data")

        # Test with None data
        node.data = None
        self.assertIsNone(node.data)

    def test_next_property(self):
        """Test next property getter and setter"""
        # Test with no next node
        node = Node(5)
        self.assertIsNone(node.next)

        # Test setting next node
        next_node = Node(10)
        node.next = next_node
        self.assertEqual(node.next, next_node)

        # Test changing next node
        new_next = Node(15)
        node.next = new_next
        self.assertEqual(node.next, new_next)

        # Test setting next to None
        node.next = None
        self.assertIsNone(node.next)

    def test_prev_property(self):
        """Test prev property getter and setter"""
        # Test with no prev node
        node = Node(5)
        self.assertIsNone(node.prev)

        # Test setting prev node
        prev_node = Node(10)
        node.prev = prev_node
        self.assertEqual(node.prev, prev_node)

        # Test changing prev node
        new_prev = Node(15)
        node.prev = new_prev
        self.assertEqual(node.prev, new_prev)

        # Test setting prev to None
        node.prev = None
        self.assertIsNone(node.prev)

if __name__ == '__main__':
    unittest.main()
