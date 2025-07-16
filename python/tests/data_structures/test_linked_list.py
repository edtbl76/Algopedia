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

    def test_head_property(self):
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

    def test_to_string(self):
        """Test to_string method"""
        # Test with single node
        ll = LinkedList(5)
        self.assertEqual(ll.to_string(), "5\n")

        # Test with multiple nodes
        ll = LinkedList(5)
        ll.insert(10)  # Now using insert method

        # Expected output should be "10\n5\n" since 10 is now the head
        self.assertEqual(ll.to_string(), "10\n5\n")

        # Test with None values
        ll = LinkedList(None)
        self.assertEqual(ll.to_string(), "")

    def test_remove_by_value(self):
        """Test remove_by_value method"""
        # Test removing head
        ll = LinkedList(5)
        ll.insert(10)  # Now using insert method

        ll.remove_by_value(10)  # Remove the head (10)
        self.assertEqual(ll.head.data, 5)

        # Test removing middle node
        ll = LinkedList(5)
        ll.insert(10)  # Insert 10 at start (becomes head)
        ll.insert(15)  # Insert 15 at start (becomes new head)
        # Now the list is: 15 -> 10 -> 5

        ll.remove_by_value(10)  # Remove the middle node (10)
        # Now the list should be: 15 -> 5
        self.assertEqual(ll.head.data, 15)
        self.assertEqual(ll.head.next.data, 5)

        # Test removing non-existent node
        ll = LinkedList(5)
        original_head = ll.head
        ll.remove_by_value(20)  # 20 is not in the list
        self.assertEqual(ll.head, original_head)  # Head should remain unchanged

    def test_swap_node(self):
        """Test swap_node method"""
        # Test swapping nodes in the middle of the list
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        # Now the list is: 20 -> 15 -> 10 -> 5

        ll.swap_node(15, 10)
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

        ll.swap_node(15, 5)
        # After swap, the list should be: 5 -> 10 -> 15
        self.assertEqual(ll.head.data, 5)
        self.assertEqual(ll.head.next.data, 10)
        self.assertEqual(ll.head.next.next.data, 15)

        # Test swapping a node with itself (should do nothing)
        ll = LinkedList(5)
        ll.insert(10)
        # Now the list is: 10 -> 5

        original_head = ll.head
        ll.swap_node(10, 10)
        # List should remain unchanged: 10 -> 5
        self.assertEqual(ll.head, original_head)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 5)

        # Test swapping with a non-existent node
        ll = LinkedList(5)
        ll.insert(10)
        # Now the list is: 10 -> 5

        original_head = ll.head
        ll.swap_node(10, 20)  # 20 is not in the list
        # List should remain unchanged: 10 -> 5
        self.assertEqual(ll.head, original_head)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 5)

        # Test swapping adjacent nodes
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        # Now the list is: 15 -> 10 -> 5

        ll.swap_node(15, 10)
        # After swap, the list should be: 10 -> 15 -> 5
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 15)
        self.assertEqual(ll.head.next.next.data, 5)

    def test_find_nth_last(self):
        """Test find_nth_last method"""
        # Test with a list of multiple nodes
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        # Now the list is: 20 -> 15 -> 10 -> 5

        # Test getting the 1st element from the end (last element)
        node = ll.find_nth_last(1)
        self.assertEqual(node.data, 5)

        # Test getting the 2nd element from the end
        node = ll.find_nth_last(2)
        self.assertEqual(node.data, 10)

        # Test getting the 3rd element from the end
        node = ll.find_nth_last(3)
        self.assertEqual(node.data, 15)

        # Test getting the 4th element from the end (first element)
        node = ll.find_nth_last(4)
        self.assertEqual(node.data, 20)

    def test_find_middle(self):
        """Test find_middle method"""
        # Test with odd number of nodes
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        ll.insert(25)
        # Now the list is: 25 -> 20 -> 15 -> 10 -> 5
        # Middle node should be 15

        node = ll.find_middle()
        self.assertEqual(node.data, 15)

        # Test with even number of nodes
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        # Now the list is: 20 -> 15 -> 10 -> 5
        # Middle node should be 10 (the second of the two middle nodes)

        node = ll.find_middle()
        self.assertEqual(node.data, 10)

        # Test with single node
        ll = LinkedList(5)
        # List is just: 5
        # Middle node should be 5

        node = ll.find_middle()
        self.assertEqual(node.data, 5)

        # Test with two nodes
        ll = LinkedList(5)
        ll.insert(10)
        # Now the list is: 10 -> 5
        # Middle node should be 5

        node = ll.find_middle()
        self.assertEqual(node.data, 5)

    def test_find_middle_alt(self):
        """Test find_middle_alt method"""
        # Test with odd number of nodes
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        ll.insert(25)
        # Now the list is: 25 -> 20 -> 15 -> 10 -> 5
        # Middle node should be 15

        node = ll.find_middle_alt()
        self.assertEqual(node.data, 15)

        # Test with even number of nodes
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        # Now the list is: 20 -> 15 -> 10 -> 5
        # Middle node should be 10 (the second of the two middle nodes)

        node = ll.find_middle_alt()
        self.assertEqual(node.data, 10)

        # Test with single node
        ll = LinkedList(5)
        # List is just: 5
        # Middle node should be 5

        node = ll.find_middle_alt()
        self.assertEqual(node.data, 5)

        # Test with two nodes
        ll = LinkedList(5)
        ll.insert(10)
        # Now the list is: 10 -> 5
        # Middle node should be 5

        node = ll.find_middle_alt()
        self.assertEqual(node.data, 5)

    def test_find_nth_last_naive(self):
        """Test find_nth_last_naive method"""
        # Test with a list of multiple nodes
        ll = LinkedList(5)
        ll.insert(10)
        ll.insert(15)
        ll.insert(20)
        # Now the list is: 20 -> 15 -> 10 -> 5

        # Test getting the 1st element from the end (last element)
        node = ll.find_nth_last_naive(1)
        self.assertEqual(node.data, 5)

        # Test getting the 2nd element from the end
        node = ll.find_nth_last_naive(2)
        self.assertEqual(node.data, 10)

        # Test getting the 3rd element from the end
        node = ll.find_nth_last_naive(3)
        self.assertEqual(node.data, 15)

        # Test getting the 4th element from the end (first element)
        node = ll.find_nth_last_naive(4)
        self.assertEqual(node.data, 20)

if __name__ == '__main__':
    unittest.main()
