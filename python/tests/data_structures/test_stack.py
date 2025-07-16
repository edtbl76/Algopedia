import unittest
from data_structures.Stack import Stack

class TestStack(unittest.TestCase):
    def test_init(self):
        """Test Stack initialization"""
        # Test with limit
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.has_space())
        
        # Test without limit
        stack = Stack(None)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.has_space())
    
    def test_push(self):
        """Test push method"""
        stack = Stack(3)
        
        # Push one item
        stack.push(5)
        self.assertEqual(stack.peek, 5)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.has_space())
        
        # Push to limit
        stack.push(10)
        stack.push(15)
        self.assertEqual(stack.peek, 15)
        self.assertFalse(stack.has_space())
        
        # Push beyond limit should raise OverflowError
        with self.assertRaises(OverflowError):
            stack.push(20)
        
        # Test push with unlimited stack
        unlimited_stack = Stack(None)
        for i in range(100):  # Push a large number of items
            unlimited_stack.push(i)
        self.assertEqual(unlimited_stack.peek, 99)
        self.assertTrue(unlimited_stack.has_space())
    
    def test_pop(self):
        """Test pop method"""
        stack = Stack(5)
        
        # Pop from empty stack should raise IndexError
        with self.assertRaises(IndexError):
            stack.pop()
        
        # Push and pop one item
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertTrue(stack.is_empty())
        
        # Push and pop multiple items (LIFO order)
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())
    
    def test_peek(self):
        """Test peek property"""
        stack = Stack(5)
        
        # Peek on empty stack should return None
        self.assertIsNone(stack.peek)
        
        # Push and peek
        stack.push(5)
        self.assertEqual(stack.peek, 5)
        
        # Push another and peek (should show the top item)
        stack.push(10)
        self.assertEqual(stack.peek, 10)
        
        # Peek should not remove items
        self.assertEqual(stack.peek, 10)
        stack.pop()
        self.assertEqual(stack.peek, 5)
    
    def test_has_space(self):
        """Test has_space method"""
        # Test with limit
        stack = Stack(2)
        self.assertTrue(stack.has_space())
        
        stack.push(5)
        self.assertTrue(stack.has_space())
        
        stack.push(10)
        self.assertFalse(stack.has_space())
        
        stack.pop()
        self.assertTrue(stack.has_space())
        
        # Test without limit
        unlimited_stack = Stack(None)
        for i in range(100):  # Push a large number of items
            unlimited_stack.push(i)
            self.assertTrue(unlimited_stack.has_space())
    
    def test_is_empty(self):
        """Test is_empty method"""
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        
        stack.push(5)
        self.assertFalse(stack.is_empty())
        
        stack.pop()
        self.assertTrue(stack.is_empty())

if __name__ == '__main__':
    unittest.main()