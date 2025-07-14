import unittest
from data_structures.LinkedList import LinkedList
from data_structures.Node import Node

class TestLinkedList(unittest.TestCase):
    def test_init(self):
        """Test LinkedList initialization"""
        # Test with value
        ll = LinkedList(5)
        self.assertIsNotNone(ll.get_head())
        self.assertEqual(ll.get_head().get_data(), 5)
        self.assertIsNone(ll.get_head().get_next())

        # Test with None value
        ll = LinkedList()
        self.assertIsNotNone(ll.get_head())
        self.assertIsNone(ll.get_head().get_data())
        self.assertIsNone(ll.get_head().get_next())

    def test_get_head(self):
        """Test get_head method"""
        ll = LinkedList(10)
        head = ll.get_head()
        self.assertIsInstance(head, Node)
        self.assertEqual(head.get_data(), 10)

    def test_insert_start(self):
        """Test insert_start method"""
        ll = LinkedList(5)

        # Insert a new node at the start
        ll.insert_start(10)

        # Verify the new node is now the head
        self.assertEqual(ll.get_head().get_data(), 10)
        self.assertEqual(ll.get_head().get_next().get_data(), 5)

        # Insert another node at the start
        ll.insert_start(15)

        # Verify the newest node is now the head
        self.assertEqual(ll.get_head().get_data(), 15)
        self.assertEqual(ll.get_head().get_next().get_data(), 10)
        self.assertEqual(ll.get_head().get_next().get_next().get_data(), 5)

    def test_stringify_list(self):
        """Test stringify_list method"""
        # Test with single node
        ll = LinkedList(5)
        self.assertEqual(ll.stringify_list(), "5\n")

        # Test with multiple nodes
        ll = LinkedList(5)
        ll.insert_start(10)  # Now using insert_start method

        # Expected output should be "10\n5\n" since 10 is now the head
        self.assertEqual(ll.stringify_list(), "10\n5\n")

        # Test with None values
        ll = LinkedList(None)
        self.assertEqual(ll.stringify_list(), "")

    def test_remove_node(self):
        """Test remove_node method"""
        # Test removing head
        ll = LinkedList(5)
        ll.insert_start(10)  # Now using insert_start method

        ll.remove_node(10)  # Remove the head (10)
        self.assertEqual(ll.get_head().get_data(), 5)

        # Test removing middle node
        ll = LinkedList(5)
        ll.insert_start(10)  # Insert 10 at start (becomes head)
        ll.insert_start(15)  # Insert 15 at start (becomes new head)
        # Now the list is: 15 -> 10 -> 5

        ll.remove_node(10)  # Remove the middle node (10)
        # Now the list should be: 15 -> 5
        self.assertEqual(ll.get_head().get_data(), 15)
        self.assertEqual(ll.get_head().get_next().get_data(), 5)

        # Test removing non-existent node
        ll = LinkedList(5)
        original_head = ll.get_head()
        ll.remove_node(20)  # 20 is not in the list
        self.assertEqual(ll.get_head(), original_head)  # Head should remain unchanged

    def test_swap_node(self):
        """Test swap_node method"""
        # Test swapping nodes in the middle of the list
        ll = LinkedList(5)
        ll.insert_start(10)
        ll.insert_start(15)
        ll.insert_start(20)
        # Now the list is: 20 -> 15 -> 10 -> 5

        ll.swap_node(15, 10)
        # After swap, the list should be: 20 -> 10 -> 15 -> 5
        self.assertEqual(ll.get_head().get_data(), 20)
        self.assertEqual(ll.get_head().get_next().get_data(), 10)
        self.assertEqual(ll.get_head().get_next().get_next().get_data(), 15)
        self.assertEqual(ll.get_head().get_next().get_next().get_next().get_data(), 5)

        # Test swapping the head node with another node
        ll = LinkedList(5)
        ll.insert_start(10)
        ll.insert_start(15)
        # Now the list is: 15 -> 10 -> 5

        ll.swap_node(15, 5)
        # After swap, the list should be: 5 -> 10 -> 15
        self.assertEqual(ll.get_head().get_data(), 5)
        self.assertEqual(ll.get_head().get_next().get_data(), 10)
        self.assertEqual(ll.get_head().get_next().get_next().get_data(), 15)

        # Test swapping a node with itself (should do nothing)
        ll = LinkedList(5)
        ll.insert_start(10)
        # Now the list is: 10 -> 5

        original_head = ll.get_head()
        ll.swap_node(10, 10)
        # List should remain unchanged: 10 -> 5
        self.assertEqual(ll.get_head(), original_head)
        self.assertEqual(ll.get_head().get_data(), 10)
        self.assertEqual(ll.get_head().get_next().get_data(), 5)

        # Test swapping with a non-existent node
        ll = LinkedList(5)
        ll.insert_start(10)
        # Now the list is: 10 -> 5

        original_head = ll.get_head()
        ll.swap_node(10, 20)  # 20 is not in the list
        # List should remain unchanged: 10 -> 5
        self.assertEqual(ll.get_head(), original_head)
        self.assertEqual(ll.get_head().get_data(), 10)
        self.assertEqual(ll.get_head().get_next().get_data(), 5)

        # Test swapping adjacent nodes
        ll = LinkedList(5)
        ll.insert_start(10)
        ll.insert_start(15)
        # Now the list is: 15 -> 10 -> 5

        ll.swap_node(15, 10)
        # After swap, the list should be: 10 -> 15 -> 5
        self.assertEqual(ll.get_head().get_data(), 10)
        self.assertEqual(ll.get_head().get_next().get_data(), 15)
        self.assertEqual(ll.get_head().get_next().get_next().get_data(), 5)

    def test_list_nth_last_dual_list(self):
        """Test list_nth_last_dual_list method"""
        # Test with a list of multiple nodes
        ll = LinkedList(5)
        ll.insert_start(10)
        ll.insert_start(15)
        ll.insert_start(20)
        # Now the list is: 20 -> 15 -> 10 -> 5

        # Test getting the 1st element from the end (last element)
        node = ll.list_nth_last_dual_list(1)
        self.assertEqual(node.get_data(), 5)

        # Test getting the 2nd element from the end
        node = ll.list_nth_last_dual_list(2)
        self.assertEqual(node.get_data(), 10)

        # Test getting the 3rd element from the end
        node = ll.list_nth_last_dual_list(3)
        self.assertEqual(node.get_data(), 15)

        # Test getting the 4th element from the end (first element)
        node = ll.list_nth_last_dual_list(4)
        self.assertEqual(node.get_data(), 20)

    def test_list_nth_last_parallel_pointers(self):
        """Test list_nth_last_parallel_pointers method"""
        # Test with a list of multiple nodes
        ll = LinkedList(5)
        ll.insert_start(10)
        ll.insert_start(15)
        ll.insert_start(20)
        # Now the list is: 20 -> 15 -> 10 -> 5

        # Test getting the 1st element from the end (last element)
        node = ll.list_nth_last_parallel_pointers(1)
        self.assertEqual(node.get_data(), 5)

        # Test getting the 2nd element from the end
        node = ll.list_nth_last_parallel_pointers(2)
        self.assertEqual(node.get_data(), 10)

        # Test getting the 3rd element from the end
        node = ll.list_nth_last_parallel_pointers(3)
        self.assertEqual(node.get_data(), 15)

        # Test getting the 4th element from the end (first element)
        node = ll.list_nth_last_parallel_pointers(4)
        self.assertEqual(node.get_data(), 20)

if __name__ == '__main__':
    unittest.main()
