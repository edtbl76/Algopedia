import unittest
from data_structures.DoublyLinkedLIst import DoublyLinkedList
from data_structures.TwoPointNode import Node

class TestDoublyLinkedList(unittest.TestCase):
    def test_init(self):
        """Test DoublyLinkedList initialization"""
        # Test initialization
        dll = DoublyLinkedList()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_insert(self):
        """Test insert method"""
        # Test inserting into an empty list
        dll = DoublyLinkedList()
        dll.insert(5)
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.tail.get_data(), 5)
        self.assertIsNone(dll.head.get_prev())
        self.assertIsNone(dll.head.get_next())
        self.assertEqual(dll.head, dll.tail)

        # Test inserting into a non-empty list
        dll.insert(10)
        self.assertEqual(dll.head.get_data(), 10)
        self.assertEqual(dll.tail.get_data(), 5)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next(), dll.tail)
        self.assertEqual(dll.tail.get_prev(), dll.head)
        self.assertIsNone(dll.tail.get_next())

        # Test inserting multiple values
        dll.insert(15)
        self.assertEqual(dll.head.get_data(), 15)
        self.assertEqual(dll.head.get_next().get_data(), 10)
        self.assertEqual(dll.tail.get_data(), 5)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next().get_prev(), dll.head)
        self.assertEqual(dll.tail.get_prev().get_data(), 10)
        self.assertIsNone(dll.tail.get_next())

    def test_append(self):
        """Test append method"""
        # Test appending to an empty list
        dll = DoublyLinkedList()
        dll.append(5)
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.tail.get_data(), 5)
        self.assertIsNone(dll.head.get_prev())
        self.assertIsNone(dll.head.get_next())
        self.assertEqual(dll.head, dll.tail)

        # Test appending to a non-empty list
        dll.append(10)
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.tail.get_data(), 10)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next(), dll.tail)
        self.assertEqual(dll.tail.get_prev(), dll.head)
        self.assertIsNone(dll.tail.get_next())

        # Test appending multiple values
        dll.append(15)
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.head.get_next().get_data(), 10)
        self.assertEqual(dll.tail.get_data(), 15)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next().get_prev(), dll.head)
        self.assertEqual(dll.tail.get_prev().get_data(), 10)
        self.assertIsNone(dll.tail.get_next())

    def test_remove_head(self):
        """Test remove_head method"""
        # Test removing from an empty list
        dll = DoublyLinkedList()
        self.assertIsNone(dll.remove_head())
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        # Test removing the only node
        dll = DoublyLinkedList()
        dll.insert(5)
        self.assertEqual(dll.remove_head(), 5)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        # Test removing from a list with multiple nodes
        dll = DoublyLinkedList()
        dll.insert(5)
        dll.insert(10)
        dll.insert(15)
        # Now the list is: 15 <-> 10 <-> 5
        self.assertEqual(dll.remove_head(), 15)
        # Now the list should be: 10 <-> 5
        self.assertEqual(dll.head.get_data(), 10)
        self.assertEqual(dll.tail.get_data(), 5)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next(), dll.tail)
        self.assertEqual(dll.tail.get_prev(), dll.head)
        self.assertIsNone(dll.tail.get_next())

    def test_remove_tail(self):
        """Test remove_tail method"""
        # Test removing from an empty list
        dll = DoublyLinkedList()
        self.assertIsNone(dll.remove_tail())
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        # Test removing the only node
        dll = DoublyLinkedList()
        dll.append(5)
        self.assertEqual(dll.remove_tail(), 5)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        # Test removing from a list with multiple nodes
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        # Now the list is: 5 <-> 10 <-> 15
        self.assertEqual(dll.remove_tail(), 15)
        # Now the list should be: 5 <-> 10
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.tail.get_data(), 10)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next(), dll.tail)
        self.assertEqual(dll.tail.get_prev(), dll.head)
        self.assertIsNone(dll.tail.get_next())

    def test_remove_node_by_value(self):
        """Test remove_node_by_value method"""
        # Test removing from an empty list
        dll = DoublyLinkedList()
        self.assertIsNone(dll.remove_node_by_value(5))
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        # Test removing a non-existent value
        dll = DoublyLinkedList()
        dll.append(5)
        self.assertIsNone(dll.remove_node_by_value(10))
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.tail.get_data(), 5)

        # Test removing the head
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        # Now the list is: 5 <-> 10 <-> 15
        removed = dll.remove_node_by_value(5)
        self.assertIsNotNone(removed)
        # Now the list should be: 10 <-> 15
        self.assertEqual(dll.head.get_data(), 10)
        self.assertEqual(dll.tail.get_data(), 15)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next(), dll.tail)
        self.assertEqual(dll.tail.get_prev(), dll.head)
        self.assertIsNone(dll.tail.get_next())

        # Test removing the tail
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        # Now the list is: 5 <-> 10 <-> 15
        removed = dll.remove_node_by_value(15)
        self.assertIsNotNone(removed)
        # Now the list should be: 5 <-> 10
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.tail.get_data(), 10)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next(), dll.tail)
        self.assertEqual(dll.tail.get_prev(), dll.head)
        self.assertIsNone(dll.tail.get_next())

        # Test removing a middle node
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        # Now the list is: 5 <-> 10 <-> 15
        removed = dll.remove_node_by_value(10)
        self.assertIsNotNone(removed)
        # Now the list should be: 5 <-> 15
        self.assertEqual(dll.head.get_data(), 5)
        self.assertEqual(dll.tail.get_data(), 15)
        self.assertIsNone(dll.head.get_prev())
        self.assertEqual(dll.head.get_next(), dll.tail)
        self.assertEqual(dll.tail.get_prev(), dll.head)
        self.assertIsNone(dll.tail.get_next())

    def test_stringify(self):
        """Test stringify method"""
        # Test with an empty list
        dll = DoublyLinkedList()
        self.assertEqual(dll.stringify(), "")

        # Test with a single node
        dll = DoublyLinkedList()
        dll.append(5)
        self.assertEqual(dll.stringify(), "5\n")

        # Test with multiple nodes
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        # Now the list is: 5 <-> 10 <-> 15
        self.assertEqual(dll.stringify(), "5\n10\n15\n")

        # Test with None values
        dll = DoublyLinkedList()
        dll.append(None)
        dll.append(10)
        dll.append(None)
        # Now the list is: None <-> 10 <-> None
        self.assertEqual(dll.stringify(), "10\n")

if __name__ == '__main__':
    unittest.main()
