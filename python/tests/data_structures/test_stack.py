import unittest
from data_structures.Stack import Stack

class TestStack(unittest.TestCase):
    def test_init(self):
        """Test Stack initialization"""
        # Test with default limit (None)
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.has_space())

        # Test with specific limit
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.has_space())

    def test_push(self):
        """Test push method"""
        # Test pushing to an empty stack
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.peek, 5)
        self.assertFalse(stack.is_empty())

        # Test pushing to a non-empty stack
        stack.push(10)
        self.assertEqual(stack.peek, 10)
        self.assertFalse(stack.is_empty())

        # Test pushing multiple values
        stack.push(15)
        self.assertEqual(stack.peek, 15)

        # Verify the order by popping elements
        self.assertEqual(stack.pop(), 15)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.pop(), 5)
        self.assertTrue(stack.is_empty())

    def test_push_with_limit(self):
        """Test pushing to a stack with a size limit"""
        # Test pushing with limit
        stack = Stack(2)
        self.assertTrue(stack.has_space())

        stack.push(5)
        self.assertTrue(stack.has_space())

        stack.push(10)
        self.assertFalse(stack.has_space())

        # This should raise an OverflowError
        with self.assertRaises(OverflowError):
            stack.push(15)

        # Verify the stack state hasn't changed after the exception
        self.assertEqual(stack.peek, 10)
        self.assertFalse(stack.has_space())

    def test_pop(self):
        """Test pop method"""
        # Test popping from an empty stack
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

        # Test popping the only element
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertTrue(stack.is_empty())

        # Test popping from a stack with multiple elements
        stack = Stack()
        stack.push(5)
        stack.push(10)
        stack.push(15)
        self.assertEqual(stack.pop(), 15)
        self.assertEqual(stack.peek, 10)
        self.assertFalse(stack.is_empty())

    def test_peek(self):
        """Test peek property"""
        # Test peeking at an empty stack
        stack = Stack()
        self.assertIsNone(stack.peek)

        # Test peeking at a non-empty stack
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.peek, 5)

        # Verify that peek doesn't remove the element
        self.assertEqual(stack.peek, 5)
        self.assertFalse(stack.is_empty())

        # Test peeking after multiple pushes
        stack.push(10)
        self.assertEqual(stack.peek, 10)  # Returns the top element

    def test_has_space(self):
        """Test has_space method"""
        # Test with unlimited stack (limit=None)
        stack = Stack()
        self.assertTrue(stack.has_space())

        # Add some elements to the unlimited stack
        for i in range(10):
            stack.push(i)
            self.assertTrue(stack.has_space())  # Should always have space

        # Test with limited stack
        stack = Stack(3)
        self.assertTrue(stack.has_space())

        stack.push(1)
        self.assertTrue(stack.has_space())

        stack.push(2)
        self.assertTrue(stack.has_space())

        stack.push(3)
        self.assertFalse(stack.has_space())  # Stack is full

        # After popping, should have space again
        stack.pop()
        self.assertTrue(stack.has_space())

    def test_is_empty(self):
        """Test is_empty method"""
        # Test with new stack
        stack = Stack()
        self.assertTrue(stack.is_empty())

        # Test after pushing
        stack.push(5)
        self.assertFalse(stack.is_empty())

        # Test after popping all elements
        stack.pop()
        self.assertTrue(stack.is_empty())

        # Test with multiple push/pop operations
        stack.push(10)
        stack.push(20)
        self.assertFalse(stack.is_empty())

        stack.pop()
        self.assertFalse(stack.is_empty())

        stack.pop()
        self.assertTrue(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
