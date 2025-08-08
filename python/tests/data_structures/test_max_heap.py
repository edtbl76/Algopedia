import unittest
from data_structures.MaxHeap import MaxHeap


class TestMaxHeap(unittest.TestCase):
    """
    Test cases for the MaxHeap class implementation.
    
    These tests verify the functionality of the MaxHeap class including:
    - Initialization
    - Adding elements
    - Removing elements
    - Maintaining the max heap property
    - Helper methods
    - Edge cases
    """

    def test_initialization(self):
        """Test initialization of an empty MaxHeap"""
        max_heap = MaxHeap()
        self.assertEqual(max_heap.size, 0)
        self.assertEqual(max_heap.heap, [None])

    def test_add_single_element(self):
        """Test adding a single element to an empty heap"""
        max_heap = MaxHeap()
        max_heap.add(10)
        
        self.assertEqual(max_heap.size, 1)
        self.assertEqual(max_heap.heap, [None, 10])

    def test_add_multiple_elements_no_heapify_needed(self):
        """Test adding multiple elements in decreasing order (no heapify needed)"""
        max_heap = MaxHeap()
        max_heap.add(30)
        max_heap.add(20)
        max_heap.add(10)
        
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap, [None, 30, 20, 10])

    def test_add_multiple_elements_with_heapify(self):
        """Test adding multiple elements that require heapify to maintain max heap property"""
        max_heap = MaxHeap()
        max_heap.add(10)
        max_heap.add(20)
        max_heap.add(30)
        
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap, [None, 30, 10, 20])

    def test_complex_heapify_case(self):
        """Test a more complex case requiring multiple heapify operations"""
        max_heap = MaxHeap()
        elements = [5, 10, 15, 20, 25, 30]
        for element in elements:
            max_heap.add(element)
        
        # The max element should be at the root (index 1)
        self.assertEqual(max_heap.heap[1], 30)
        
        # Verify the heap property: parent >= children
        for i in range(1, max_heap.size // 2 + 1):
            parent_index = i
            left_child_index = max_heap._get_left_child_index(parent_index)
            right_child_index = max_heap._get_right_child_index(parent_index)
            
            # Check left child if it exists
            if left_child_index <= max_heap.size:
                self.assertGreaterEqual(max_heap.heap[parent_index], max_heap.heap[left_child_index])
            
            # Check right child if it exists
            if right_child_index <= max_heap.size:
                self.assertGreaterEqual(max_heap.heap[parent_index], max_heap.heap[right_child_index])

    def test_add_duplicate_elements(self):
        """Test adding duplicate elements to the heap"""
        max_heap = MaxHeap()
        max_heap.add(10)
        max_heap.add(10)
        max_heap.add(10)
        
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap, [None, 10, 10, 10])

    def test_add_negative_elements(self):
        """Test adding negative elements to the heap"""
        max_heap = MaxHeap()
        max_heap.add(-5)
        max_heap.add(-10)
        max_heap.add(-3)
        
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap[1], -3)  # -3 is the max of the negative numbers

    def test_helper_methods(self):
        """Test the helper methods for index calculations"""
        # Test parent index calculation
        self.assertEqual(MaxHeap._get_parent_index(2), 1)
        self.assertEqual(MaxHeap._get_parent_index(3), 1)
        self.assertEqual(MaxHeap._get_parent_index(4), 2)
        self.assertEqual(MaxHeap._get_parent_index(5), 2)
        
        # Test left child index calculation
        self.assertEqual(MaxHeap._get_left_child_index(1), 2)
        self.assertEqual(MaxHeap._get_left_child_index(2), 4)
        self.assertEqual(MaxHeap._get_left_child_index(3), 6)
        
        # Test right child index calculation
        self.assertEqual(MaxHeap._get_right_child_index(1), 3)
        self.assertEqual(MaxHeap._get_right_child_index(2), 5)
        self.assertEqual(MaxHeap._get_right_child_index(3), 7)

    def test_swap_method(self):
        """Test the swap method"""
        max_heap = MaxHeap()
        max_heap.heap = [None, 10, 20, 30]
        max_heap.size = 3
        
        max_heap._swap(1, 3)
        self.assertEqual(max_heap.heap, [None, 30, 20, 10])
        
        max_heap._swap(2, 3)
        self.assertEqual(max_heap.heap, [None, 30, 10, 20])
        
    def test_has_child_method(self):
        """Test the _has_child method"""
        max_heap = MaxHeap()
        max_heap.heap = [None, 10, 20, 30, 40]
        max_heap.size = 4
        
        # Node at index 1 has children
        self.assertTrue(max_heap._has_child(1))
        
        # Node at index 2 has a child
        self.assertTrue(max_heap._has_child(2))
        
        # Node at index 4 has no children (it's a leaf)
        self.assertFalse(max_heap._has_child(4))
        
    def test_get_largest_child_index_method(self):
        """Test the _get_largest_child_index method"""
        max_heap = MaxHeap()
        
        # Case 1: Both children exist, right child is larger
        max_heap.heap = [None, 50, 30, 40, 10, 20]
        max_heap.size = 5
        self.assertEqual(max_heap._get_largest_child_index(1), 3)  # Right child (40) > left child (30)
        
        # Case 2: Both children exist, left child is larger
        max_heap.heap = [None, 50, 40, 30, 10, 20]
        max_heap.size = 5
        self.assertEqual(max_heap._get_largest_child_index(1), 2)  # Left child (40) > right child (30)
        
        # Case 3: Only left child exists
        max_heap.heap = [None, 50, 40, 30]
        max_heap.size = 3
        self.assertEqual(max_heap._get_largest_child_index(1), 2)  # Only left child exists

    def test_heapify_up_method(self):
        """Test the heapify_up method directly"""
        max_heap = MaxHeap()
        max_heap.heap = [None, 10, 20]
        max_heap.size = 2
        
        # Add a new element that should bubble up
        max_heap.heap.append(30)
        max_heap.size += 1
        max_heap.heapify_up()
        
        self.assertEqual(max_heap.heap, [None, 30, 20, 10])

    def test_large_heap(self):
        """Test creating a larger heap with many elements"""
        max_heap = MaxHeap()
        elements = list(range(1, 101))  # 1 to 100
        
        # Add elements in reverse order to avoid heapify
        for element in reversed(elements):
            max_heap.add(element)
        
        self.assertEqual(max_heap.size, 100)
        self.assertEqual(max_heap.heap[1], 100)  # Max should be at the root
        
        # Verify heap property for a sample of nodes
        sample_indices = [1, 2, 3, 10, 20, 50]
        for i in sample_indices:
            left_idx = max_heap._get_left_child_index(i)
            right_idx = max_heap._get_right_child_index(i)
            
            if left_idx <= max_heap.size:
                self.assertGreaterEqual(max_heap.heap[i], max_heap.heap[left_idx])
            
            if right_idx <= max_heap.size:
                self.assertGreaterEqual(max_heap.heap[i], max_heap.heap[right_idx])

    def test_remove_max_empty_heap(self):
        """Test removing max element from an empty heap"""
        max_heap = MaxHeap()
        result = max_heap.remove_max()
        
        self.assertIsNone(result)
        self.assertEqual(max_heap.size, 0)
        self.assertEqual(max_heap.heap, [None])

    def test_remove_max_single_element(self):
        """Test removing max element from a heap with a single element"""
        max_heap = MaxHeap()
        max_heap.add(42)
        
        result = max_heap.remove_max()
        
        self.assertEqual(result, 42)
        self.assertEqual(max_heap.size, 0)
        self.assertEqual(max_heap.heap, [None])

    def test_remove_max_multiple_elements(self):
        """Test removing max element from a heap with multiple elements"""
        max_heap = MaxHeap()
        elements = [10, 30, 20, 15, 25]
        for element in elements:
            max_heap.add(element)
        
        # First removal should give us 30
        result = max_heap.remove_max()
        self.assertEqual(result, 30)
        self.assertEqual(max_heap.size, 4)
        self.assertEqual(max_heap.heap[1], 25)  # New max should be 25
        
        # Second removal should give us 25
        result = max_heap.remove_max()
        self.assertEqual(result, 25)
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap[1], 20)  # New max should be 20

    def test_heapify_down_method(self):
        """Test the heapify_down method directly"""
        max_heap = MaxHeap()
        # Create a heap that needs heapify_down
        max_heap.heap = [None, 10, 30, 20]
        max_heap.size = 3
        
        # Heapify down from the root
        max_heap.heapify_down()
        
        # After heapify_down, 30 should be at the root
        self.assertEqual(max_heap.heap, [None, 30, 10, 20])

    def test_remove_max_and_verify_heap_property(self):
        """Test removing max elements and verify heap property is maintained"""
        max_heap = MaxHeap()
        elements = [5, 10, 15, 20, 25, 30]
        for element in elements:
            max_heap.add(element)
        
        # Remove max element (30)
        max_heap.remove_max()
        
        # Verify heap property after removal
        for i in range(1, max_heap.size // 2 + 1):
            parent_index = i
            left_child_index = max_heap._get_left_child_index(parent_index)
            right_child_index = max_heap._get_right_child_index(parent_index)
            
            # Check left child if it exists
            if left_child_index <= max_heap.size:
                self.assertGreaterEqual(max_heap.heap[parent_index], max_heap.heap[left_child_index])
            
            # Check right child if it exists
            if right_child_index <= max_heap.size:
                self.assertGreaterEqual(max_heap.heap[parent_index], max_heap.heap[right_child_index])

    def test_remove_all_elements(self):
        """Test removing all elements from the heap one by one"""
        max_heap = MaxHeap()
        elements = [5, 10, 15, 20, 25]
        for element in elements:
            max_heap.add(element)
        
        # Remove all elements and verify they come out in descending order
        expected_order = sorted(elements, reverse=True)
        actual_order = []
        
        while max_heap.size > 0:
            actual_order.append(max_heap.remove_max())
        
        self.assertEqual(actual_order, expected_order)
        self.assertEqual(max_heap.size, 0)
        self.assertEqual(max_heap.heap, [None])


if __name__ == '__main__':
    unittest.main()