import unittest
from data_structures.Heap.MinHeap import MinHeap


class TestMinHeap(unittest.TestCase):
    """
    Test cases for the MinHeap class implementation.
    
    These tests verify the functionality of the MinHeap class including:
    - Initialization
    - Adding elements
    - Removing elements
    - Maintaining the min heap property
    - Helper methods
    - Edge cases
    """

    def test_initialization(self):
        """Test initialization of an empty MinHeap"""
        min_heap = MinHeap()
        self.assertEqual(min_heap.size, 0)
        self.assertEqual(min_heap.heap, [None])

    def test_add_single_element(self):
        """Test adding a single element to an empty heap"""
        min_heap = MinHeap()
        min_heap.add(10)
        
        self.assertEqual(min_heap.size, 1)
        self.assertEqual(min_heap.heap, [None, 10])

    def test_add_multiple_elements_no_heapify_needed(self):
        """Test adding multiple elements in increasing order (no heapify needed)"""
        min_heap = MinHeap()
        min_heap.add(10)
        min_heap.add(20)
        min_heap.add(30)
        
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap, [None, 10, 20, 30])

    def test_add_multiple_elements_with_heapify(self):
        """Test adding multiple elements that require heapify to maintain min heap property"""
        min_heap = MinHeap()
        min_heap.add(30)
        min_heap.add(20)
        min_heap.add(10)
        
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap, [None, 10, 30, 20])

    def test_complex_heapify_case(self):
        """Test a more complex case requiring multiple heapify operations"""
        min_heap = MinHeap()
        elements = [30, 25, 20, 15, 10, 5]
        for element in elements:
            min_heap.add(element)
        
        # The min element should be at the root (index 1)
        self.assertEqual(min_heap.heap[1], 5)
        
        # Verify the heap property: parent <= children
        for i in range(1, min_heap.size // 2 + 1):
            parent_index = i
            left_child_index = min_heap._get_left_child_index(parent_index)
            right_child_index = min_heap._get_right_child_index(parent_index)
            
            # Check left child if it exists
            if left_child_index <= min_heap.size:
                self.assertLessEqual(min_heap.heap[parent_index], min_heap.heap[left_child_index])
            
            # Check right child if it exists
            if right_child_index <= min_heap.size:
                self.assertLessEqual(min_heap.heap[parent_index], min_heap.heap[right_child_index])

    def test_add_duplicate_elements(self):
        """Test adding duplicate elements to the heap"""
        min_heap = MinHeap()
        min_heap.add(10)
        min_heap.add(10)
        min_heap.add(10)
        
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap, [None, 10, 10, 10])

    def test_add_negative_elements(self):
        """Test adding negative elements to the heap"""
        min_heap = MinHeap()
        min_heap.add(-5)
        min_heap.add(-10)
        min_heap.add(-3)
        
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap[1], -10)  # -10 is the min of the negative numbers

    def test_helper_methods(self):
        """Test the helper methods for index calculations"""
        # Test parent index calculation
        self.assertEqual(MinHeap._get_parent_index(2), 1)
        self.assertEqual(MinHeap._get_parent_index(3), 1)
        self.assertEqual(MinHeap._get_parent_index(4), 2)
        self.assertEqual(MinHeap._get_parent_index(5), 2)
        
        # Test left child index calculation
        self.assertEqual(MinHeap._get_left_child_index(1), 2)
        self.assertEqual(MinHeap._get_left_child_index(2), 4)
        self.assertEqual(MinHeap._get_left_child_index(3), 6)
        
        # Test right child index calculation
        self.assertEqual(MinHeap._get_right_child_index(1), 3)
        self.assertEqual(MinHeap._get_right_child_index(2), 5)
        self.assertEqual(MinHeap._get_right_child_index(3), 7)

    def test_swap_method(self):
        """Test the swap method"""
        min_heap = MinHeap()
        min_heap.heap = [None, 10, 20, 30]
        min_heap.size = 3
        
        min_heap._swap(1, 3)
        self.assertEqual(min_heap.heap, [None, 30, 20, 10])
        
        min_heap._swap(2, 3)
        self.assertEqual(min_heap.heap, [None, 30, 10, 20])
        
    def test_has_child_method(self):
        """Test the _has_child method"""
        min_heap = MinHeap()
        min_heap.heap = [None, 10, 20, 30, 40]
        min_heap.size = 4
        
        # Node at index 1 has children
        self.assertTrue(min_heap._has_child(1))
        
        # Node at index 2 has a child
        self.assertTrue(min_heap._has_child(2))
        
        # Node at index 4 has no children (it's a leaf)
        self.assertFalse(min_heap._has_child(4))
        
    def test_get_smallest_child_index_method(self):
        """Test the _get_smallest_child_index method"""
        min_heap = MinHeap()
        
        # Case 1: Both children exist, right child is smaller
        min_heap.heap = [None, 10, 30, 20, 50, 40]
        min_heap.size = 5
        self.assertEqual(min_heap._get_smallest_child_index(1), 3)  # Right child (20) < left child (30)
        
        # Case 2: Both children exist, left child is smaller
        min_heap.heap = [None, 10, 20, 30, 50, 40]
        min_heap.size = 5
        self.assertEqual(min_heap._get_smallest_child_index(1), 2)  # Left child (20) < right child (30)
        
        # Case 3: Only left child exists
        min_heap.heap = [None, 10, 20, 30]
        min_heap.size = 3
        self.assertEqual(min_heap._get_smallest_child_index(1), 2)  # Only left child exists

    def test_heapify_up_method(self):
        """Test the heapify_up method directly"""
        min_heap = MinHeap()
        min_heap.heap = [None, 20, 30]
        min_heap.size = 2
        
        # Add a new element that should bubble up
        min_heap.heap.append(10)
        min_heap.size += 1
        min_heap.heapify_up()
        
        self.assertEqual(min_heap.heap, [None, 10, 30, 20])

    def test_large_heap(self):
        """Test creating a larger heap with many elements"""
        min_heap = MinHeap()
        elements = list(range(1, 101))  # 1 to 100
        
        # Add elements in random order
        for element in elements:
            min_heap.add(element)
        
        self.assertEqual(min_heap.size, 100)
        self.assertEqual(min_heap.heap[1], 1)  # Min should be at the root
        
        # Verify heap property for a sample of nodes
        sample_indices = [1, 2, 3, 10, 20, 50]
        for i in sample_indices:
            left_idx = min_heap._get_left_child_index(i)
            right_idx = min_heap._get_right_child_index(i)
            
            if left_idx <= min_heap.size:
                self.assertLessEqual(min_heap.heap[i], min_heap.heap[left_idx])
            
            if right_idx <= min_heap.size:
                self.assertLessEqual(min_heap.heap[i], min_heap.heap[right_idx])

    def test_remove_min_empty_heap(self):
        """Test removing min element from an empty heap"""
        min_heap = MinHeap()
        result = min_heap.remove_min()
        
        self.assertIsNone(result)
        self.assertEqual(min_heap.size, 0)
        self.assertEqual(min_heap.heap, [None])

    def test_remove_min_single_element(self):
        """Test removing min element from a heap with a single element"""
        min_heap = MinHeap()
        min_heap.add(42)
        
        result = min_heap.remove_min()
        
        self.assertEqual(result, 42)
        self.assertEqual(min_heap.size, 0)
        self.assertEqual(min_heap.heap, [None])

    def test_remove_min_multiple_elements(self):
        """Test removing min element from a heap with multiple elements"""
        min_heap = MinHeap()
        elements = [30, 10, 20, 25, 15]
        for element in elements:
            min_heap.add(element)
        
        # First removal should give us 10
        result = min_heap.remove_min()
        self.assertEqual(result, 10)
        self.assertEqual(min_heap.size, 4)
        self.assertEqual(min_heap.heap[1], 15)  # New min should be 15
        
        # Second removal should give us 15
        result = min_heap.remove_min()
        self.assertEqual(result, 15)
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap[1], 20)  # New min should be 20

    def test_heapify_down_method(self):
        """Test the heapify_down method directly"""
        min_heap = MinHeap()
        # Create a heap that needs heapify_down
        min_heap.heap = [None, 30, 10, 20]
        min_heap.size = 3
        
        # Heapify down from the root
        min_heap.heapify_down()
        
        # After heapify_down, 10 should be at the root
        self.assertEqual(min_heap.heap, [None, 10, 30, 20])

    def test_remove_min_and_verify_heap_property(self):
        """Test removing min elements and verify heap property is maintained"""
        min_heap = MinHeap()
        elements = [30, 25, 20, 15, 10, 5]
        for element in elements:
            min_heap.add(element)
        
        # Remove min element (5)
        min_heap.remove_min()
        
        # Verify heap property after removal
        for i in range(1, min_heap.size // 2 + 1):
            parent_index = i
            left_child_index = min_heap._get_left_child_index(parent_index)
            right_child_index = min_heap._get_right_child_index(parent_index)
            
            # Check left child if it exists
            if left_child_index <= min_heap.size:
                self.assertLessEqual(min_heap.heap[parent_index], min_heap.heap[left_child_index])
            
            # Check right child if it exists
            if right_child_index <= min_heap.size:
                self.assertLessEqual(min_heap.heap[parent_index], min_heap.heap[right_child_index])

    def test_remove_all_elements(self):
        """Test removing all elements from the heap one by one"""
        min_heap = MinHeap()
        elements = [25, 10, 5, 20, 15]
        for element in elements:
            min_heap.add(element)
        
        # Remove all elements and verify they come out in ascending order
        expected_order = sorted(elements)
        actual_order = []
        
        while min_heap.size > 0:
            actual_order.append(min_heap.remove_min())
        
        self.assertEqual(actual_order, expected_order)
        self.assertEqual(min_heap.size, 0)
        self.assertEqual(min_heap.heap, [None])


if __name__ == '__main__':
    unittest.main()