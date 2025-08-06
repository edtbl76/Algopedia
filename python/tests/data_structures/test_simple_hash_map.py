import unittest
from data_structures.HashMap.SImpleHashMap import HashMap

class TestSimpleHashMap(unittest.TestCase):
    def setUp(self):
        """Set up a SimpleHashMap instance for testing"""
        self.hash_map = HashMap(size=10)
        
        # Also create a small HashMap to test edge cases
        self.small_hash_map = HashMap(size=3)
    
    def test_init(self):
        """Test SimpleHashMap initialization"""
        hash_map = HashMap(size=5)
        self.assertEqual(len(hash_map.array), 5)
        self.assertEqual(hash_map.size, 5)
        
        # Check that all array elements are initialized to None
        for element in hash_map.array:
            self.assertIsNone(element)
    
    def test_hash_function(self):
        """Test the hash_function method"""
        # Test basic hash function
        hash_code = self.hash_map.hash_function("test")
        self.assertEqual(hash_code, sum("test".encode()))
        
        # Test with collision count
        hash_code_with_collision = self.hash_map.hash_function("test", 3)
        self.assertEqual(hash_code_with_collision, sum("test".encode()) + 3)
    
    def test_compressor(self):
        """Test the compressor method"""
        # Test basic compression
        compressed = self.hash_map.compressor(100)
        self.assertEqual(compressed, 100 % 10)
        
        # Test with large hash code
        compressed_large = self.hash_map.compressor(1000)
        self.assertEqual(compressed_large, 1000 % 10)
    
    def test_assign_and_retrieve(self):
        """Test assign and retrieve methods"""
        # Test basic assignment and retrieval
        self.hash_map.assign("key1", "value1")
        self.assertEqual(self.hash_map.retrieve("key1"), "value1")
        
        # Test overwriting existing key
        self.hash_map.assign("key1", "new_value")
        self.assertEqual(self.hash_map.retrieve("key1"), "new_value")
        
        # Test multiple assignments
        self.hash_map.assign("key2", "value2")
        self.hash_map.assign("key3", "value3")
        self.assertEqual(self.hash_map.retrieve("key1"), "new_value")
        self.assertEqual(self.hash_map.retrieve("key2"), "value2")
        self.assertEqual(self.hash_map.retrieve("key3"), "value3")
        
        # Test with different value types
        self.hash_map.assign("int_key", 42)
        self.hash_map.assign("list_key", [1, 2, 3])
        self.hash_map.assign("dict_key", {"a": 1, "b": 2})
        self.assertEqual(self.hash_map.retrieve("int_key"), 42)
        self.assertEqual(self.hash_map.retrieve("list_key"), [1, 2, 3])
        self.assertEqual(self.hash_map.retrieve("dict_key"), {"a": 1, "b": 2})
    
    def test_retrieve_nonexistent(self):
        """Test retrieving non-existent keys"""
        # Test retrieving non-existent key
        self.assertIsNone(self.hash_map.retrieve("non_existent"))
    
    def test_collision_handling(self):
        """Test collision handling"""
        # Create keys that will collide
        # We'll use a simple approach: create keys that have the same sum of bytes
        # For example, "ab" and "ba" have the same byte sum
        key1 = "ab"
        key2 = "ba"
        
        # Verify they have the same hash
        self.assertEqual(self.hash_map.hash_function(key1), self.hash_map.hash_function(key2))
        
        # Assign values to both keys
        self.hash_map.assign(key1, "value1")
        self.hash_map.assign(key2, "value2")
        
        # Verify both values can be retrieved correctly
        self.assertEqual(self.hash_map.retrieve(key1), "value1")
        self.assertEqual(self.hash_map.retrieve(key2), "value2")
    
    def test_multiple_collisions(self):
        """Test handling of multiple collisions"""
        # Create keys that will collide in a small hash map
        # We'll manually create keys that will hash to the same index
        # For a size=3 hash map, keys with byte sums that differ by 3 will collide
        
        # First, let's find a base key
        base_key = "a"  # ASCII 97
        base_hash = self.small_hash_map.compressor(self.small_hash_map.hash_function(base_key))
        
        # Create keys that will hash to the same index
        keys = [base_key]
        values = ["value1"]
        
        # Add a key that will collide with base_key
        # We'll use 'd' (ASCII 100) which is 3 more than 'a'
        collision_key = "d"
        collision_hash = self.small_hash_map.compressor(self.small_hash_map.hash_function(collision_key))
        self.assertEqual(collision_hash, base_hash)
        keys.append(collision_key)
        values.append("value2")
        
        # Add another key that will collide
        # We'll use 'g' (ASCII 103) which is 6 more than 'a'
        collision_key2 = "g"
        collision_hash2 = self.small_hash_map.compressor(self.small_hash_map.hash_function(collision_key2))
        self.assertEqual(collision_hash2, base_hash)
        keys.append(collision_key2)
        values.append("value3")
        
        # Assign all key-value pairs
        for key, value in zip(keys, values):
            self.small_hash_map.assign(key, value)
        
        # Verify all values can be retrieved correctly
        for key, value in zip(keys, values):
            self.assertEqual(self.small_hash_map.retrieve(key), value)

if __name__ == '__main__':
    unittest.main()