import unittest
from data_structures.DoublyLinkedLIst import DoublyLinkedList
from data_structures.TwoPointNode import Node

class TestDoublyLinkedList(unittest.TestCase):
    def test_init(self):
        """Test DoublyLinkedList initialization"""
        dll = DoublyLinkedList()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
    
    def test_insert(self):
        """Test insert method"""
        dll = DoublyLinkedList()
        
        # Insert first node
        dll.insert(5)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 5)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.head.next)
        
        # Insert second node (should become new head)
        dll.insert(10)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.tail.data, 5)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.prev, dll.head)
        self.assertIsNone(dll.tail.next)
        
        # Insert third node (should become new head)
        dll.insert(15)
        self.assertEqual(dll.head.data, 15)
        self.assertEqual(dll.head.next.data, 10)
        self.assertEqual(dll.tail.data, 5)
    
    def test_append(self):
        """Test append method"""
        dll = DoublyLinkedList()
        
        # Append first node
        dll.append(5)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 5)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.head.next)
        
        # Append second node (should become new tail)
        dll.append(10)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 10)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.prev, dll.head)
        self.assertIsNone(dll.tail.next)
        
        # Append third node (should become new tail)
        dll.append(15)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.tail.data, 15)
        self.assertEqual(dll.tail.prev.data, 10)
    
    def test_remove_head(self):
        """Test remove_head method"""
        dll = DoublyLinkedList()
        
        # Remove from empty list
        self.assertIsNone(dll.remove_head())
        
        # Remove the only node
        dll.insert(5)
        self.assertEqual(dll.remove_head(), 5)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        
        # Remove from list with multiple nodes
        dll.insert(5)
        dll.insert(10)
        dll.insert(15)
        self.assertEqual(dll.remove_head(), 15)
        self.assertEqual(dll.head.data, 10)
        self.assertIsNone(dll.head.prev)
    
    def test_remove_tail(self):
        """Test remove_tail method"""
        dll = DoublyLinkedList()
        
        # Remove from empty list
        self.assertIsNone(dll.remove_tail())
        
        # Remove the only node
        dll.append(5)
        self.assertEqual(dll.remove_tail(), 5)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        
        # Remove from list with multiple nodes
        dll.append(5)
        dll.append(10)
        dll.append(15)
        self.assertEqual(dll.remove_tail(), 15)
        self.assertEqual(dll.tail.data, 10)
        self.assertIsNone(dll.tail.next)
    
    def test_remove_by_value(self):
        """Test remove_by_value method"""
        dll = DoublyLinkedList()
        
        # Remove from empty list
        self.assertIsNone(dll.remove_by_value(5))
        
        # Remove non-existent value
        dll.append(10)
        self.assertIsNone(dll.remove_by_value(5))
        
        # Remove the only node
        node = dll.remove_by_value(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        
        # Remove head
        dll.append(5)
        dll.append(10)
        dll.append(15)
        node = dll.remove_by_value(5)
        self.assertEqual(node.data, 5)
        self.assertEqual(dll.head.data, 10)
        
        # Remove tail
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(10)
        dll.append(15)
        node = dll.remove_by_value(15)
        self.assertEqual(node.data, 15)
        self.assertEqual(dll.tail.data, 10)
        
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