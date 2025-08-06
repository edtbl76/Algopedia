import unittest
from data_structures.DoublyLinkedLIst import DoublyLinkedList
from data_structures.TwoPointNode import Node

class TestDoublyLinkedList(unittest.TestCase):
    def test_init(self):
        """Test DoublyLinkedList initialization"""
        dll = DoublyLinkedList()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(dll._size, 0)
    
    def test_insert(self):
        """Test insert method"""
        dll = DoublyLinkedList()
        
        # Insert first node
        dll.insert(5)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 5)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.head.next)
        self.assertEqual(dll._size, 1)
        
        # Insert second node (should become new head)
        dll.insert(10)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.tail.data, 5)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.prev, dll.head)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(dll._size, 2)
        
        # Insert third node (should become new head)
        dll.insert(15)
        self.assertEqual(dll.head.data, 15)
        self.assertEqual(dll.head.next.data, 10)
        self.assertEqual(dll.tail.data, 5)
        self.assertEqual(dll._size, 3)
    
    def test_append(self):
        """Test append method"""
        dll = DoublyLinkedList()
        
        # Append first node
        dll.append(5)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 5)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.head.next)
        self.assertEqual(dll._size, 1)
        
        # Append second node (should become new tail)
        dll.append(10)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 10)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.prev, dll.head)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(dll._size, 2)
        
        # Append third node (should become new tail)
        dll.append(15)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 15)
        self.assertEqual(dll.tail.prev.data, 10)
        self.assertEqual(dll._size, 3)
    
    def test_insert_at_index(self):
        """Test insert_at_index method"""
        dll = DoublyLinkedList()
        
        # Insert at index 0 (empty list)
        dll.insert_at_index(0, 5)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 5)
        self.assertEqual(dll._size, 1)
        
        # Insert at index 0 (non-empty list)
        dll.insert_at_index(0, 10)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.tail.data, 5)
        self.assertEqual(dll._size, 2)
        
        # Insert at end
        dll.insert_at_index(2, 15)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.tail.data, 15)
        self.assertEqual(dll._size, 3)
        
        # Insert in middle
        dll.insert_at_index(1, 20)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.head.next.data, 20)
        self.assertEqual(dll.head.next.next.data, 5)
        self.assertEqual(dll.tail.data, 15)
        self.assertEqual(dll._size, 4)
        
        # Test index out of range
        with self.assertRaises(IndexError):
            dll.insert_at_index(-1, 25)
        with self.assertRaises(IndexError):
            dll.insert_at_index(5, 25)
    
    def test_size_and_len(self):
        """Test _size property and __len__ method"""
        dll = DoublyLinkedList()
        self.assertEqual(dll._size, 0)
        self.assertEqual(len(dll), 0)
        
        dll.append(5)
        self.assertEqual(dll._size, 1)
        self.assertEqual(len(dll), 1)
        
        dll.append(10)
        self.assertEqual(dll._size, 2)
        self.assertEqual(len(dll), 2)
        
        dll.remove_head()
        self.assertEqual(dll._size, 1)
        self.assertEqual(len(dll), 1)
        
        dll.remove_tail()
        self.assertEqual(dll._size, 0)
        self.assertEqual(len(dll), 0)
    
    def test_remove_head(self):
        """Test remove_head method"""
        dll = DoublyLinkedList()
        
        # Remove from empty list
        self.assertIsNone(dll.remove_head())
        self.assertEqual(dll._size, 0)
        
        # Remove the only node
        dll.insert(5)
        self.assertEqual(dll.remove_head(), 5)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(dll._size, 0)
        
        # Remove from list with multiple nodes
        dll.insert(5)
        dll.insert(10)
        dll.insert(15)
        self.assertEqual(dll.remove_head(), 15)
        self.assertEqual(dll.head.data, 10)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll._size, 2)
    
    def test_remove_tail(self):
        """Test remove_tail method"""
        dll = DoublyLinkedList()
        
        # Remove from empty list
        self.assertIsNone(dll.remove_tail())
        self.assertEqual(dll._size, 0)
        
        # Remove the only node
        dll.append(5)
        self.assertEqual(dll.remove_tail(), 5)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(dll._size, 0)
        
        # Remove from list with multiple nodes
        dll.append(5)
        dll.append(10)
        dll.append(15)
        self.assertEqual(dll.remove_tail(), 15)
        self.assertEqual(dll.tail.data, 10)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(dll._size, 2)
    
    def test_remove_by_value(self):
        """Test remove_by_value method"""
        dll = DoublyLinkedList()
        
        # Remove from empty list
        self.assertIsNone(dll.remove_by_value(5))
        
        # Remove non-existent value
        dll.append(10)
        self.assertIsNone(dll.remove_by_value(5))
        self.assertEqual(dll._size, 1)
        
        # Remove the only node
        node = dll.remove_by_value(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(dll._size, 0)
        
        # Remove head
        dll.append(5)
        dll.append(10)
        dll.append(15)
        node = dll.remove_by_value(5)
        self.assertEqual(node.data, 5)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll._size, 2)
        
        # Remove tail
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        node = dll.remove_by_value(15)
        self.assertEqual(node.data, 15)
        self.assertEqual(dll.tail.data, 10)
        self.assertEqual(dll._size, 2)
        
        # Remove middle node
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        node = dll.remove_by_value(10)
        self.assertEqual(node.data, 10)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 15)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.prev, dll.head)
        self.assertEqual(dll._size, 2)
    
    def test_to_string(self):
        """Test to_string method"""
        dll = DoublyLinkedList()
        
        # Empty list
        self.assertEqual(dll.to_string(), "")
        
        # Single node
        dll.append(5)
        self.assertEqual(dll.to_string(), "5\n")
        
        # Multiple nodes
        dll.append(10)
        dll.append(15)
        self.assertEqual(dll.to_string(), "5\n10\n15\n")
        
        # With None values
        dll = DoublyLinkedList()
        dll.append(None)
        dll.append(5)
        self.assertEqual(dll.to_string(), "5\n")

if __name__ == '__main__':
    unittest.main()