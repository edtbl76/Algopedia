import unittest
from typing import Tuple

from data_structures.HashMap.ArrayBasedStorage import ArrayBasedStorage
from data_structures.HashMap.HashEntry import HashEntry
from data_structures.HashMap.HashFunction import HashFunction
from data_structures.HashMap.SimpleAdditionHash import SimpleAdditionHash


class TestArrayBasedStorage(unittest.TestCase):
    def setUp(self):
        """Set up an ArrayBasedStorage instance for testing"""
        self.capacity = 10
        self.storage = ArrayBasedStorage(capacity=self.capacity)
        self.hash_function = SimpleAdditionHash()
        
        # Helper function to compress hash codes to array indices
        self.compress_hash = lambda hash_code: hash_code % self.capacity

    def test_init(self):
        """Test ArrayBasedStorage initialization"""
        self.assertEqual(self.storage.get_capacity(), self.capacity)
        
        # All slots should be empty initially
        for i in range(self.capacity):
            self.assertTrue(self.storage.is_slot_available(i))
    
    def test_find_slot_empty(self):
        """Test finding a slot in an empty storage"""
        key = "test_key"
        index, entry = self.storage.find_slot(key, self.hash_function, self.compress_hash)
        
        # The slot should be empty
        self.assertIsNone(entry)
        
        # The index should be the compressed hash of the key
        expected_index = self.compress_hash(self.hash_function.hash_key(key))
        self.assertEqual(index, expected_index)
    
    def test_put_and_get(self):
        """Test putting and getting entries"""
        key = "test_key"
        value = "test_value"
        entry = HashEntry(key=key, value=value)
        
        # Find a slot for the entry
        index, _ = self.storage.find_slot(key, self.hash_function, self.compress_hash)
        
        # Put the entry in the slot
        is_new = self.storage.put(index, entry)
        self.assertTrue(is_new)  # Should be a new entry
        
        # Get the entry back
        retrieved_entry = self.storage.get(index, key)
        self.assertIsNotNone(retrieved_entry)
        self.assertEqual(retrieved_entry.key, key)
        self.assertEqual(retrieved_entry.value, value)
        
        # The slot should no longer be available
        self.assertFalse(self.storage.is_slot_available(index))
    
    def test_put_existing_key(self):
        """Test putting an entry with an existing key"""
        key = "test_key"
        value1 = "test_value1"
        value2 = "test_value2"
        entry1 = HashEntry(key=key, value=value1)
        entry2 = HashEntry(key=key, value=value2)
        
        # Find a slot for the first entry
        index, _ = self.storage.find_slot(key, self.hash_function, self.compress_hash)
        
        # Put the first entry in the slot
        is_new1 = self.storage.put(index, entry1)
        self.assertTrue(is_new1)  # Should be a new entry
        
        # Put the second entry in the same slot
        is_new2 = self.storage.put(index, entry2)
        self.assertFalse(is_new2)  # Should not be a new entry
        
        # Get the entry back
        retrieved_entry = self.storage.get(index, key)
        self.assertIsNotNone(retrieved_entry)
        self.assertEqual(retrieved_entry.key, key)
        self.assertEqual(retrieved_entry.value, value2)  # Should be the updated value
    
    def test_remove(self):
        """Test removing entries"""
        key = "test_key"
        value = "test_value"
        entry = HashEntry(key=key, value=value)
        
        # Find a slot for the entry
        index, _ = self.storage.find_slot(key, self.hash_function, self.compress_hash)
        
        # Put the entry in the slot
        self.storage.put(index, entry)
        
        # Remove the entry
        removed = self.storage.remove(index, key)
        self.assertTrue(removed)  # Should be removed
        
        # The slot should be available again
        self.assertTrue(self.storage.is_slot_available(index))
        
        # The entry should no longer be retrievable
        retrieved_entry = self.storage.get(index, key)
        self.assertIsNone(retrieved_entry)
    
    def test_remove_nonexistent(self):
        """Test removing a nonexistent entry"""
        key = "nonexistent_key"
        index = self.compress_hash(self.hash_function.hash_key(key))
        
        # Try to remove the nonexistent entry
        removed = self.storage.remove(index, key)
        self.assertFalse(removed)  # Should not be removed
    
    def test_get_all_values(self):
        """Test getting all values"""
        # Add some entries
        entries = [
            ("key1", "value1"),
            ("key2", "value2"),
            ("key3", "value3")
        ]
        
        for key, value in entries:
            entry = HashEntry(key=key, value=value)
            index, _ = self.storage.find_slot(key, self.hash_function, self.compress_hash)
            self.storage.put(index, entry)
        
        # Get all values
        values = self.storage.get_all_values()
        
        # Check that all values are present
        for _, value in entries:
            self.assertIn(value, values)
        
        # Check that the length is correct (capacity)
        self.assertEqual(len(values), self.capacity)
        
        # Check that empty slots have None values
        self.assertEqual(values.count(None), self.capacity - len(entries))
    
    def test_collision_handling(self):
        """Test collision handling"""
        # Create a hash function that always returns the same hash
        class CollisionHashFunction(HashFunction):
            def hash_key(self, key: str) -> int:
                return 1  # Always return the same hash
            
            def handle_collision(self, key: str, attempt: int) -> int:
                return (self.hash_key(key) + attempt) % 10  # Linear probing with wrap-around
        
        collision_hash = CollisionHashFunction()
        
        # Add multiple entries that will collide
        entries = [
            ("key1", "value1"),
            ("key2", "value2"),
            ("key3", "value3")
        ]
        
        for key, value in entries:
            entry = HashEntry(key=key, value=value)
            index, _ = self.storage.find_slot(key, collision_hash, self.compress_hash)
            self.storage.put(index, entry)
        
        # Verify all entries can be retrieved
        for key, value in entries:
            index, _ = self.storage.find_slot(key, collision_hash, self.compress_hash)
            retrieved_entry = self.storage.get(index, key)
            self.assertIsNotNone(retrieved_entry)
            self.assertEqual(retrieved_entry.key, key)
            self.assertEqual(retrieved_entry.value, value)
    
    def test_max_collision_attempts(self):
        """Test maximum collision attempts"""
        # Create a hash function that always returns the same hash and doesn't handle collisions
        class BadCollisionHashFunction(HashFunction):
            def hash_key(self, key: str) -> int:
                return 1  # Always return the same hash
            
            def handle_collision(self, key: str, attempt: int) -> int:
                return self.hash_key(key)  # Always return the same hash (no probing)
        
        bad_collision_hash = BadCollisionHashFunction()
        
        # Add one entry
        self.storage.put(1, HashEntry(key="key1", value="value1"))
        
        # Try to find a slot for another entry (should raise OverflowError)
        with self.assertRaises(OverflowError):
            self.storage.find_slot("key2", bad_collision_hash, self.compress_hash)


if __name__ == '__main__':
    unittest.main()