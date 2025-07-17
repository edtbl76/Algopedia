import unittest
from typing import Tuple

from data_structures.HashMap.SeparateChaining import SeparateChaining
from data_structures.HashMap.HashEntry import HashEntry
from data_structures.HashMap.HashFunction import HashFunction
from data_structures.HashMap.SimpleAdditionHash import SimpleAdditionHash


class TestSeparateChaining(unittest.TestCase):
    def setUp(self):
        """Set up a SeparateChaining instance for testing"""
        self.capacity = 10
        # Since SeparateChaining is marked as abstract, we need to create a concrete subclass
        class ConcreteSeparateChaining(SeparateChaining):
            pass
        
        self.storage = ConcreteSeparateChaining(capacity=self.capacity)
        self.hash_function = SimpleAdditionHash()
        
        # Helper function to compress hash codes to array indices
        self.compress_hash = lambda hash_code: hash_code % self.capacity

    def test_init(self):
        """Test SeparateChaining initialization"""
        self.assertEqual(self.storage.get_capacity(), self.capacity)
        
        # All buckets should be empty initially
        for i in range(self.capacity):
            self.assertTrue(self.storage.is_slot_available(i))
    
    def test_find_slot(self):
        """Test finding a slot"""
        key = "test_key"
        index, entry = self.storage.find_slot(key, self.hash_function, self.compress_hash)
        
        # The entry should be None initially
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
        
        # Check that the length is correct (number of entries)
        self.assertEqual(len(values), len(entries))
    
    def test_collision_handling(self):
        """Test collision handling"""
        # Create a hash function that always returns the same hash
        class CollisionHashFunction(HashFunction):
            def hash_key(self, key: str) -> int:
                return 1  # Always return the same hash
            
            def handle_collision(self, key: str, attempt: int) -> int:
                return self.hash_key(key)  # Always return the same hash
        
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
    
    def test_is_slot_available(self):
        """Test is_slot_available method"""
        # In separate chaining, slots are always available
        for i in range(self.capacity):
            self.assertTrue(self.storage.is_slot_available(i))
        
        # Add an entry
        key = "test_key"
        value = "test_value"
        entry = HashEntry(key=key, value=value)
        index, _ = self.storage.find_slot(key, self.hash_function, self.compress_hash)
        self.storage.put(index, entry)
        
        # The slot should still be available
        self.assertTrue(self.storage.is_slot_available(index))


if __name__ == '__main__':
    unittest.main()