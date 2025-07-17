import unittest
from data_structures.HashMap.HashMap import HashMap
from data_structures.HashMap.HashFunction import HashFunction
from data_structures.HashMap.SimpleAdditionHash import SimpleAdditionHash
from data_structures.HashMap.ArrayBasedStorage import ArrayBasedStorage
from data_structures.HashMap.SeparateChaining import SeparateChaining

class TestHashMap(unittest.TestCase):
    def setUp(self):
        """Set up a HashMap instance for testing"""
        self.hash_map = HashMap(capacity=10)

        # Also create a small HashMap to test edge cases
        self.small_hash_map = HashMap(capacity=3)

    def test_init(self):
        """Test HashMap initialization"""
        # Test with default hash function
        hash_map = HashMap(capacity=5)
        self.assertEqual(hash_map.size, 0)
        self.assertIsInstance(hash_map._hash_function, SimpleAdditionHash)

        # Test with custom hash function
        class CustomHashFunction(HashFunction):
            def hash_key(self, key: str) -> int:
                return len(key)

            def handle_collision(self, key: str, attempt: int) -> int:
                return self.hash_key(key) + attempt

        custom_hash_map = HashMap(capacity=5, hash_function=CustomHashFunction())
        self.assertEqual(custom_hash_map.size, 0)
        self.assertIsInstance(custom_hash_map._hash_function, CustomHashFunction)

    def test_setitem(self):
        """Test __setitem__ method (dictionary-style assignment)"""
        # Test basic assignment
        self.hash_map["key1"] = "value1"
        self.assertEqual(self.hash_map["key1"], "value1")
        self.assertEqual(self.hash_map.size, 1)

        # Test overwriting existing key
        self.hash_map["key1"] = "new_value"
        self.assertEqual(self.hash_map["key1"], "new_value")
        self.assertEqual(self.hash_map.size, 1)

        # Test multiple assignments
        self.hash_map["key2"] = "value2"
        self.hash_map["key3"] = "value3"
        self.assertEqual(self.hash_map["key1"], "new_value")
        self.assertEqual(self.hash_map["key2"], "value2")
        self.assertEqual(self.hash_map["key3"], "value3")
        self.assertEqual(self.hash_map.size, 3)

        # Test with different value types
        self.hash_map["int_key"] = 42
        self.hash_map["list_key"] = [1, 2, 3]
        self.hash_map["dict_key"] = {"a": 1, "b": 2}
        self.assertEqual(self.hash_map["int_key"], 42)
        self.assertEqual(self.hash_map["list_key"], [1, 2, 3])
        self.assertEqual(self.hash_map["dict_key"], {"a": 1, "b": 2})
        self.assertEqual(self.hash_map.size, 6)

    def test_getitem(self):
        """Test __getitem__ method (dictionary-style access)"""
        # Test getting non-existent key
        self.assertIsNone(self.hash_map["non_existent"])

        # Test getting after assignment
        self.hash_map["key1"] = "value1"
        self.assertEqual(self.hash_map["key1"], "value1")

        # Test getting after overwriting
        self.hash_map["key1"] = "new_value"
        self.assertEqual(self.hash_map["key1"], "new_value")

    def test_collision_handling(self):
        """Test collision handling"""
        # Create a HashMap with a hash function that always returns the same hash
        class CollisionHashFunction(HashFunction):
            def hash_key(self, key: str) -> int:
                return 1  # Always return the same hash

            def handle_collision(self, key: str, attempt: int) -> int:
                return (self.hash_key(key) + attempt) % 10  # Linear probing with wrap-around

        collision_map = HashMap(capacity=10, hash_function=CollisionHashFunction())

        # Add multiple items (should cause collisions)
        collision_map["key1"] = "value1"
        collision_map["key2"] = "value2"
        collision_map["key3"] = "value3"

        # Verify all items can be retrieved
        self.assertEqual(collision_map["key1"], "value1")
        self.assertEqual(collision_map["key2"], "value2")
        self.assertEqual(collision_map["key3"], "value3")
        self.assertEqual(collision_map.size, 3)

    def test_max_collision_attempts(self):
        """Test maximum collision attempts"""
        # Create a HashMap with a hash function that always returns the same hash
        class CollisionHashFunction(HashFunction):
            def hash_key(self, key: str) -> int:
                return 1  # Always return the same hash

            def handle_collision(self, key: str, attempt: int) -> int:
                return self.hash_key(key)  # Always return the same hash (no probing)

        collision_map = HashMap(capacity=10, hash_function=CollisionHashFunction())

        # Add one item
        collision_map["key1"] = "value1"

        # Try to add another item (should raise OverflowError after MAX_COLLISION_ATTEMPTS)
        with self.assertRaises(OverflowError):
            collision_map["key2"] = "value2"

    def test_values_property(self):
        """Test values property"""
        # Test empty HashMap
        self.assertEqual(len(self.hash_map.values), 10)
        self.assertEqual(self.hash_map.values.count(None), 10)

        # Test with items
        self.hash_map["key1"] = "value1"
        self.hash_map["key2"] = "value2"

        values = self.hash_map.values
        self.assertEqual(len(values), 10)
        self.assertIn("value1", values)
        self.assertIn("value2", values)
        self.assertEqual(values.count(None), 8)

    def test_size_property(self):
        """Test size property"""
        # Test empty HashMap
        self.assertEqual(self.hash_map.size, 0)

        # Test after adding items
        self.hash_map["key1"] = "value1"
        self.assertEqual(self.hash_map.size, 1)

        self.hash_map["key2"] = "value2"
        self.assertEqual(self.hash_map.size, 2)

        # Test after overwriting
        self.hash_map["key1"] = "new_value"
        self.assertEqual(self.hash_map.size, 2)

    def test_full_hash_map(self):
        """Test behavior when HashMap is full"""
        # Fill the small HashMap
        self.small_hash_map["key1"] = "value1"
        self.small_hash_map["key2"] = "value2"
        self.small_hash_map["key3"] = "value3"

        # Try to add another item (should raise OverflowError)
        with self.assertRaises(OverflowError):
            self.small_hash_map["key4"] = "value4"

        # Verify existing items are still accessible
        self.assertEqual(self.small_hash_map["key1"], "value1")
        self.assertEqual(self.small_hash_map["key2"], "value2")
        self.assertEqual(self.small_hash_map["key3"], "value3")
        self.assertEqual(self.small_hash_map.size, 3)

    def test_storage_strategies(self):
        """Test HashMap with different storage strategies"""
        # Test with ArrayBasedStorage (default)
        array_map = HashMap(capacity=10)
        self.assertIsInstance(array_map._storage, ArrayBasedStorage)

        # Add some items
        array_map["key1"] = "value1"
        array_map["key2"] = "value2"

        # Verify items can be retrieved
        self.assertEqual(array_map["key1"], "value1")
        self.assertEqual(array_map["key2"], "value2")
        self.assertEqual(array_map.size, 2)

        # Test with SeparateChaining
        # Since SeparateChaining is marked as abstract, we need to create a concrete subclass
        class ConcreteSeparateChaining(SeparateChaining):
            pass

        chained_storage = ConcreteSeparateChaining(capacity=10)
        chained_map = HashMap(capacity=10, storage_strategy=chained_storage)
        self.assertIsInstance(chained_map._storage, SeparateChaining)

        # Add some items
        chained_map["key1"] = "value1"
        chained_map["key2"] = "value2"

        # Verify items can be retrieved
        self.assertEqual(chained_map["key1"], "value1")
        self.assertEqual(chained_map["key2"], "value2")
        self.assertEqual(chained_map.size, 2)

        # Test collision handling with SeparateChaining
        class CollisionHashFunction(HashFunction):
            def hash_key(self, key: str) -> int:
                return 1  # Always return the same hash

            def handle_collision(self, key: str, attempt: int) -> int:
                return self.hash_key(key)  # Always return the same hash

        collision_chained_map = HashMap(
            capacity=10,
            hash_function=CollisionHashFunction(),
            storage_strategy=ConcreteSeparateChaining(capacity=10)
        )

        # Add multiple items that will collide
        collision_chained_map["key1"] = "value1"
        collision_chained_map["key2"] = "value2"
        collision_chained_map["key3"] = "value3"

        # Verify all items can be retrieved
        self.assertEqual(collision_chained_map["key1"], "value1")
        self.assertEqual(collision_chained_map["key2"], "value2")
        self.assertEqual(collision_chained_map["key3"], "value3")
        self.assertEqual(collision_chained_map.size, 3)

if __name__ == '__main__':
    unittest.main()
