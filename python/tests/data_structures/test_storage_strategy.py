import unittest
from abc import ABC, abstractmethod
from typing import Optional, List, Any, Tuple

from data_structures.HashMap.HashEntry import HashEntry
from data_structures.HashMap.StorageStrategy import StorageStrategy
from data_structures.HashMap.ArrayBasedStorage import ArrayBasedStorage
from data_structures.HashMap.SeparateChaining import SeparateChaining
from data_structures.HashMap.SimpleAdditionHash import SimpleAdditionHash


class TestStorageStrategy(unittest.TestCase):
    def setUp(self):
        """Set up test instances for each storage strategy"""
        self.capacity = 10
        self.hash_function = SimpleAdditionHash()
        
        # Helper function to compress hash codes to array indices
        self.compress_hash = lambda hash_code: hash_code % self.capacity
        
        # Create instances of concrete implementations
        self.array_storage = ArrayBasedStorage(capacity=self.capacity)
        
        # Since SeparateChaining is marked as abstract, we need to create a concrete subclass
        class ConcreteSeparateChaining(SeparateChaining):
            pass
        
        self.chained_storage = ConcreteSeparateChaining(capacity=self.capacity)
        
        # List of all storage strategies to test
        self.storage_strategies = [
            self.array_storage,
            self.chained_storage
        ]

    def test_interface_implementation(self):
        """Test that all storage strategies implement the required interface"""
        for storage in self.storage_strategies:
            self.assertIsInstance(storage, StorageStrategy)
            
            # Check that all required methods are implemented
            self.assertTrue(hasattr(storage, 'find_slot'))
            self.assertTrue(hasattr(storage, 'get'))
            self.assertTrue(hasattr(storage, 'put'))
            self.assertTrue(hasattr(storage, 'remove'))
            self.assertTrue(hasattr(storage, 'get_all_values'))
            self.assertTrue(hasattr(storage, 'is_slot_available'))
            self.assertTrue(hasattr(storage, 'get_capacity'))
    
    def test_capacity(self):
        """Test that all storage strategies return the correct capacity"""
        for storage in self.storage_strategies:
            self.assertEqual(storage.get_capacity(), self.capacity)
    
    def test_basic_operations(self):
        """Test basic operations on all storage strategies"""
        for storage in self.storage_strategies:
            # Test putting and getting an entry
            key = "test_key"
            value = "test_value"
            entry = HashEntry(key=key, value=value)
            
            # Find a slot for the entry
            index, _ = storage.find_slot(key, self.hash_function, self.compress_hash)
            
            # Put the entry in the slot
            is_new = storage.put(index, entry)
            self.assertTrue(is_new)  # Should be a new entry
            
            # Get the entry back
            retrieved_entry = storage.get(index, key)
            self.assertIsNotNone(retrieved_entry)
            self.assertEqual(retrieved_entry.key, key)
            self.assertEqual(retrieved_entry.value, value)
            
            # Remove the entry
            removed = storage.remove(index, key)
            self.assertTrue(removed)  # Should be removed
            
            # The entry should no longer be retrievable
            retrieved_entry = storage.get(index, key)
            self.assertIsNone(retrieved_entry)
    
    def test_get_all_values(self):
        """Test get_all_values on all storage strategies"""
        for storage in self.storage_strategies:
            # Add some entries
            entries = [
                ("key1", "value1"),
                ("key2", "value2"),
                ("key3", "value3")
            ]
            
            for key, value in entries:
                entry = HashEntry(key=key, value=value)
                index, _ = storage.find_slot(key, self.hash_function, self.compress_hash)
                storage.put(index, entry)
            
            # Get all values
            values = storage.get_all_values()
            
            # Check that all values are present
            for _, value in entries:
                self.assertIn(value, values)
    
    def test_collision_handling(self):
        """Test collision handling on all storage strategies"""
        # Create a hash function that always returns the same hash
        class CollisionHashFunction(SimpleAdditionHash):
            def hash_key(self, key: str) -> int:
                return 1  # Always return the same hash
        
        collision_hash = CollisionHashFunction()
        
        for storage in self.storage_strategies:
            # Add multiple entries that will collide
            entries = [
                ("key1", "value1"),
                ("key2", "value2"),
                ("key3", "value3")
            ]
            
            for key, value in entries:
                entry = HashEntry(key=key, value=value)
                index, _ = storage.find_slot(key, collision_hash, self.compress_hash)
                storage.put(index, entry)
            
            # Verify all entries can be retrieved
            for key, value in entries:
                index, _ = storage.find_slot(key, collision_hash, self.compress_hash)
                retrieved_entry = storage.get(index, key)
                self.assertIsNotNone(retrieved_entry)
                self.assertEqual(retrieved_entry.key, key)
                self.assertEqual(retrieved_entry.value, value)


if __name__ == '__main__':
    unittest.main()