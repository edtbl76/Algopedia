import unittest
from data_structures.LinkedList import LinkedList
from data_structures.SinglePointNode import Node

class TestLinkedList(unittest.TestCase):
    def test_init(self):
        """Test LinkedList initialization"""
        # Test with value
        ll = LinkedList(5)
        self.assertIsNotNone(ll.head)
        self.assertEqual(ll.head.data, 5)
        self.assertIsNone(ll.head.next)

        # Test with None value
        ll = LinkedList()
        self.assertIsNotNone(ll.head)
        self.assertIsNone(ll.head.data)
        self.assertIsNone(ll.head.next)

    def test_head(self):
        """Test head property"""
        ll = LinkedList(10)
        head = ll.head
        self.assertIsInstance(head, Node)
        self.assertEqual(head.data, 10)

    def test_insert(self):
        """Test insert method"""
        ll = LinkedList(5)

        # Insert a new node at the start
        ll.insert(10)

        # Verify the new node is now the head
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 5)

        # Insert another node at the start
        ll.insert(15)

        # Verify the newest node is now the head
        self.assertEqual(ll.head.data, 15)
        self.assertEqual(ll.head.next.data, 10)
        self.assertEqual(ll.head.next.next.data, 5)

    def test_stringify(self):
        """Test stringify method"""
        # Test with single node
        ll = LinkedList(5)
        self.assertEqual(ll.stringify(), "5\n")

        # Test with multiple nodes
        ll = LinkedList(5)
        ll.insert(10)  # Now using insert method

        # Expected output should be "10\n5\n" since 10 is now the head
        self.assertEqual(ll.stringify(), "10\n5\n")

        # Test with None values
        ll = LinkedList(None)
        self.assertEqual(ll.stringify(), "")

    def test_remove(self):
        """Test remove method"""
        # Test removing head
        ll = LinkedList(5)
        ll.insert(10)  # Now using insert method

        ll.remove(10)  # Remove the head (10)
        self.assertEqual(ll.head.data, 5)

        # Test removing middle node
        ll = LinkedList(5)
        ll.insert(10)  # Insert 10 at start (becomes head)
        ll.insert(15)  # Insert 15 at start (becomes new head)
        # Now the list is: 15 -> 10 -> 5

        ll.remove(10)  # Remove the middle node (10)
        # Now the list should be: 15 -> 5
        self.assertEqual(ll.head.data, 15)
        self.assertEqual(ll.head.next.data, 5)

        # Test removing non-existent node
        ll = LinkedList(5)
        original_head = ll.head
        ll.remove(20)  # 20 is not in the list
        self.assertEqual(ll.head, original_head)  # Head should remain unchanged

    def test_append(self):
        """Test append method"""
        # Test appending to a list with one node
        ll = LinkedList(5)
        ll.append(10)
        # List should be: 5 -> 10
        self.assertEqual(ll.head.data, 5)
        self.assertEqual(ll.head.next.data, 10)
        self.assertIsNone(ll.head.next.next)
        
        # Test appending multiple nodes
        ll.append(15)
        ll.append(20)
        # List should be: 5 -> 10 -> 15 -> 20
        self.assertEqual(ll.head.data, 5)
        self.assertEqual(ll.head.next.data, 10)
        self.assertEqual(ll.head.next.next.data, 15)
        self.assertEqual(ll.head.next.next.next.data, 20)
        self.assertIsNone(ll.head.next.next.next.next)
        
        # Test appending to an empty list (with None as head data)
        ll = LinkedList()
        ll.append(5)
        # List should be: None -> 5
        self.assertIsNone(ll.head.data)
        self.assertEqual(ll.head.next.data, 5)
        self.assertIsNone(ll.head.next.next)

    def test_swap(self):
        """Test swap method"""
        # Test swapping nodes in the middle of the list
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        # Now the list is: 20 -> 15 -> 10 -> 5

        ll.swap(15, 10)
        # After swap, the list should be: 20 -> 10 -> 15 -> 5
        self.assertEqual(ll.head.data, 20)
        self.assertEqual(ll.head.next.data, 10)
        self.assertEqual(ll.head.next.next.data, 15)
        self.assertEqual(ll.head.next.next.next.data, 5)

        # Test swapping the head node with another node
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        # Now the list is: 15 -> 10 -> 5

        ll.swap(15, 5)
        # After swap, the list should be: 5 -> 10 -> 15
        self.assertEqual(ll.head.data, 5)
        self.assertEqual(ll.head.next.data, 10)
        self.assertEqual(ll.head.next.next.data, 15)

        # Test swapping a node with itself (should do nothing)
        ll = LinkedList(5)
        ll.insert(10)
        # Now the list is: 10 -> 5

        original_head = ll.head
        ll.swap(10, 10)
        # List should remain unchanged: 10 -> 5
        self.assertEqual(ll.head, original_head)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 5)

        # Test swapping with a non-existent node
        ll = LinkedList(5)
        ll.insert(10)
        # Now the list is: 10 -> 5

        original_head = ll.head
        ll.swap(10, 20)  # 20 is not in the list
        # List should remain unchanged: 10 -> 5
        self.assertEqual(ll.head, original_head)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 5)

if __name__ == '__main__':
    unittest.main()
