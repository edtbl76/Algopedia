import unittest
from data_structures.Queue import Queue

class TestQueue(unittest.TestCase):
    def test_init(self):
        """Test Queue initialization"""
        # Test with max_size
        queue = Queue(5)
        self.assertTrue(queue.is_empty())
        self.assertTrue(queue.has_space())
        self.assertEqual(queue.size, 0)

        # Test without max_size
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertTrue(queue.has_space())
        self.assertEqual(queue.size, 0)

    def test_enqueue(self):
        """Test enqueue method"""
        queue = Queue(3)

        # Enqueue one item
        queue.enqueue(5)
        self.assertEqual(queue.peek(), 5)
        self.assertFalse(queue.is_empty())
        self.assertTrue(queue.has_space())
        self.assertEqual(queue.size, 1)

        # Enqueue to max_size
        queue.enqueue(10)
        queue.enqueue(15)
        self.assertEqual(queue.peek(), 5)  # First in, first out
        self.assertFalse(queue.has_space())
        self.assertEqual(queue.size, 3)

        # Enqueue beyond max_size should not add item
        queue.enqueue(20)
        self.assertEqual(queue.size, 3)  # Size remains the same

        # Test enqueue with unlimited queue
        unlimited_queue = Queue()
        for i in range(100):  # Enqueue a large number of items
            unlimited_queue.enqueue(i)
        self.assertEqual(unlimited_queue.peek(), 0)  # First item is still at the front
        self.assertTrue(unlimited_queue.has_space())
        self.assertEqual(unlimited_queue.size, 100)

    def test_dequeue(self):
        """Test dequeue method"""
        queue = Queue(5)

        # Dequeue from empty queue should return None
        self.assertIsNone(queue.dequeue())

        # Enqueue and dequeue one item
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)
        self.assertTrue(queue.is_empty())

        # Enqueue and dequeue multiple items (FIFO order)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)
        self.assertTrue(queue.is_empty())

        # Test dequeue when only one item in queue
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)
        self.assertTrue(queue.is_empty())
        # We don't test private attributes directly

    def test_peek(self):
        """Test peek method"""
        queue = Queue(5)

        # Peek on empty queue should raise AttributeError
        with self.assertRaises(AttributeError):
            queue.peek()

        # Enqueue and peek
        queue.enqueue(5)
        self.assertEqual(queue.peek(), 5)

        # Enqueue another and peek (should still show the first item)
        queue.enqueue(10)
        self.assertEqual(queue.peek(), 5)

        # Peek should not remove items
        self.assertEqual(queue.peek(), 5)
        queue.dequeue()
        self.assertEqual(queue.peek(), 10)

    def test_size(self):
        """Test size property"""
        queue = Queue(5)
        self.assertEqual(queue.size, 0)

        queue.enqueue(5)
        self.assertEqual(queue.size, 1)

        queue.enqueue(10)
        self.assertEqual(queue.size, 2)

        queue.dequeue()
        self.assertEqual(queue.size, 1)

        queue.dequeue()
        self.assertEqual(queue.size, 0)

    def test_has_space(self):
        """Test has_space method"""
        # Test with max_size
        queue = Queue(2)
        self.assertTrue(queue.has_space())

        queue.enqueue(5)
        self.assertTrue(queue.has_space())

        queue.enqueue(10)
        self.assertFalse(queue.has_space())

        queue.dequeue()
        self.assertTrue(queue.has_space())

        # Test without max_size
        unlimited_queue = Queue()
        for i in range(100):  # Enqueue a large number of items
            unlimited_queue.enqueue(i)
            self.assertTrue(unlimited_queue.has_space())

    def test_is_empty(self):
        """Test is_empty method"""
        queue = Queue(5)
        self.assertTrue(queue.is_empty())

        queue.enqueue(5)
        self.assertFalse(queue.is_empty())

        queue.dequeue()
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()
