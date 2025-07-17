import unittest
from apps.tower_of_hanoi.NamedStack import NamedStack

class TestNamedStack(unittest.TestCase):
    def test_init(self):
        """Test NamedStack initialization"""
        # Test with name and default limit
        stack = NamedStack("Test")
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.has_space())
        self.assertEqual(stack.name, "Test")
        
        # Test with name and specific limit
        stack = NamedStack("Limited", 3)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.has_space())
        self.assertEqual(stack.name, "Limited")
    
    def test_name_property(self):
        """Test name property getter and setter"""
        stack = NamedStack("Original")
        self.assertEqual(stack.name, "Original")
        
        # Test setting a valid name
        stack.name = "New Name"
        self.assertEqual(stack.name, "New Name")
        
        # Test setting invalid names
        with self.assertRaises(ValueError):
            stack.name = ""
        
        with self.assertRaises(ValueError):
            stack.name = "   "
            
        # Ensure name wasn't changed after failed attempts
        self.assertEqual(stack.name, "New Name")
    
    def test_build_display_list(self):
        """Test _build_display_list method"""
        stack = NamedStack("Display")
        
        # Empty stack should return empty list
        self.assertEqual(stack._build_display_list(), [])
        
        # Add items and check display list (bottom to top order)
        stack.push(1)
        self.assertEqual(stack._build_display_list(), [1])
        
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack._build_display_list(), [1, 2, 3])
        
        # Removing items should update the display list
        stack.pop()
        self.assertEqual(stack._build_display_list(), [1, 2])
    
    def test_repr(self):
        """Test __repr__ method"""
        stack = NamedStack("Repr")
        self.assertEqual(repr(stack), "NamedStack(name='Repr', contents=[])")
        
        stack.push(10)
        stack.push(20)
        self.assertEqual(repr(stack), "NamedStack(name='Repr', contents=[10, 20])")
    
    def test_inherited_functionality(self):
        """Test that inherited Stack functionality works correctly"""
        stack = NamedStack("Inherited", 3)
        
        # Test push and peek
        stack.push(5)
        self.assertEqual(stack.peek, 5)
        
        # Test push to limit
        stack.push(10)
        stack.push(15)
        self.assertFalse(stack.has_space())
        
        # Test overflow
        with self.assertRaises(OverflowError):
            stack.push(20)
        
        # Test pop (LIFO order)
        self.assertEqual(stack.pop(), 15)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.pop(), 5)
        self.assertTrue(stack.is_empty())
        
        # Test pop from empty
        with self.assertRaises(IndexError):
            stack.pop()

if __name__ == '__main__':
    unittest.main()