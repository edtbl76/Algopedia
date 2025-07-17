import unittest
from data_structures.HashMap.HashEntry import HashEntry

class TestHashEntry(unittest.TestCase):
    def test_init(self):
        """Test HashEntry initialization"""
        entry = HashEntry(key="test_key", value="test_value")
        self.assertEqual(entry.key, "test_key")
        self.assertEqual(entry.value, "test_value")
        
        # Test with different value types
        int_entry = HashEntry(key="int_key", value=42)
        self.assertEqual(int_entry.key, "int_key")
        self.assertEqual(int_entry.value, 42)
        
        list_entry = HashEntry(key="list_key", value=[1, 2, 3])
        self.assertEqual(list_entry.key, "list_key")
        self.assertEqual(list_entry.value, [1, 2, 3])
        
        dict_entry = HashEntry(key="dict_key", value={"a": 1, "b": 2})
        self.assertEqual(dict_entry.key, "dict_key")
        self.assertEqual(dict_entry.value, {"a": 1, "b": 2})
    
    def test_matches_key(self):
        """Test matches_key method"""
        entry = HashEntry(key="test_key", value="test_value")
        
        # Test matching key
        self.assertTrue(entry.matches_key("test_key"))
        
        # Test non-matching key
        self.assertFalse(entry.matches_key("other_key"))
        
        # Test case sensitivity
        self.assertFalse(entry.matches_key("TEST_KEY"))
        
        # Test empty key
        empty_entry = HashEntry(key="", value="empty_key_value")
        self.assertTrue(empty_entry.matches_key(""))
        self.assertFalse(empty_entry.matches_key("non_empty"))

if __name__ == '__main__':
    unittest.main()