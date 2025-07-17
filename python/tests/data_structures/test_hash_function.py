import unittest
from data_structures.HashMap.HashFunction import HashFunction
from abc import ABC

class TestHashFunction(unittest.TestCase):
    def test_abstract_methods(self):
        """Test that HashFunction is an abstract class with required methods"""
        # Verify HashFunction is an ABC
        self.assertTrue(issubclass(HashFunction, ABC))
        
        # Verify abstract methods exist
        self.assertTrue(hasattr(HashFunction, 'hash_key'))
        self.assertTrue(hasattr(HashFunction, 'handle_collision'))
        
        # Verify we can't instantiate HashFunction directly
        with self.assertRaises(TypeError):
            HashFunction()
    
    def test_concrete_implementation(self):
        """Test a concrete implementation of HashFunction"""
        # Create a concrete implementation for testing
        class TestImplementation(HashFunction):
            def hash_key(self, key: str) -> int:
                return len(key)
            
            def handle_collision(self, key: str, attempt: int) -> int:
                return self.hash_key(key) + attempt
        
        # Test the implementation
        hash_func = TestImplementation()
        
        # Test hash_key
        self.assertEqual(hash_func.hash_key("test"), 4)
        self.assertEqual(hash_func.hash_key(""), 0)
        self.assertEqual(hash_func.hash_key("hello world"), 11)
        
        # Test handle_collision
        self.assertEqual(hash_func.handle_collision("test", 0), 4)
        self.assertEqual(hash_func.handle_collision("test", 1), 5)
        self.assertEqual(hash_func.handle_collision("test", 10), 14)

if __name__ == '__main__':
    unittest.main()