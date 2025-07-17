import unittest
from data_structures.HashMap.SimpleAdditionHash import SimpleAdditionHash

class TestSimpleAdditionHash(unittest.TestCase):
    def setUp(self):
        """Set up a SimpleAdditionHash instance for testing"""
        self.hash_function = SimpleAdditionHash()

    def test_hash_key(self):
        """Test hash_key method"""
        # Test with empty string
        self.assertEqual(self.hash_function.hash_key(""), 0)

        # Test with simple strings
        self.assertEqual(self.hash_function.hash_key("a"), ord("a"))
        self.assertEqual(self.hash_function.hash_key("abc"), sum(ord(c) for c in "abc"))

        # Test with longer string
        test_string = "hello world"
        expected_hash = sum(ord(c) for c in test_string)
        self.assertEqual(self.hash_function.hash_key(test_string), expected_hash)

        # Test with special characters
        special_string = "!@#$%^&*()"
        expected_hash = sum(ord(c) for c in special_string)
        self.assertEqual(self.hash_function.hash_key(special_string), expected_hash)

        # Test with Unicode characters
        unicode_string = "こんにちは"  # "Hello" in Japanese
        # The hash_key method uses string.encode() which returns UTF-8 bytes
        expected_hash = sum(unicode_string.encode())
        self.assertEqual(self.hash_function.hash_key(unicode_string), expected_hash)

    def test_handle_collision(self):
        """Test handle_collision method"""
        # Test with no collision (attempt = 0)
        test_key = "test"
        base_hash = self.hash_function.hash_key(test_key)
        self.assertEqual(self.hash_function.handle_collision(test_key, 0), base_hash)

        # Test with linear probing (attempt > 0)
        self.assertEqual(self.hash_function.handle_collision(test_key, 1), base_hash + 1)
        self.assertEqual(self.hash_function.handle_collision(test_key, 5), base_hash + 5)
        self.assertEqual(self.hash_function.handle_collision(test_key, 100), base_hash + 100)

        # Test with different keys
        another_key = "another"
        another_base_hash = self.hash_function.hash_key(another_key)
        self.assertEqual(self.hash_function.handle_collision(another_key, 0), another_base_hash)
        self.assertEqual(self.hash_function.handle_collision(another_key, 10), another_base_hash + 10)

if __name__ == '__main__':
    unittest.main()
