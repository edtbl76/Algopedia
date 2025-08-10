import unittest
from abc import ABC, abstractmethod
from typing import List, Type, Optional

from data_structures.Heap.Heap import BaseHeap


class TestHeapBase(ABC, unittest.TestCase):
    # Prevent this class from being collected by test runners
    __test__ = False
    """
    Base test class for heap implementations.
    
    This abstract base class provides common test methods for both MinHeap and MaxHeap
    implementations. Specific heap tests should inherit from this class and implement
    the abstract methods to provide heap-specific functionality.
    """
    
    @abstractmethod
    def create_heap(self) -> BaseHeap:
        """Create and return a new heap instance of the appropriate type."""
        pass
    
    @abstractmethod
    def get_expected_order(self, elements: List[int]) -> List[int]:
        """
        Return the expected order of elements when removed from the heap.
        
        For MinHeap: ascending order
        For MaxHeap: descending order
        """
        pass
    
    @abstractmethod
    def compare_parent_child(self, parent: int, child: int) -> bool:
        """
        Compare parent and child values according to heap property.
        
        For MinHeap: parent <= child
        For MaxHeap: parent >= child
        
        Returns True if the heap property is satisfied.
        """
        pass
    
    @abstractmethod
    def get_root_value_after_heapify(self, elements: List[int]) -> int:
        """
        Return the expected root value after heapifying the given elements.
        
        For MinHeap: minimum value
        For MaxHeap: maximum value
        """
        pass
    
    @abstractmethod
    def get_extreme_element_name(self) -> str:
        """
        Return the name of the extreme element for this heap type.
        
        For MinHeap: "min"
        For MaxHeap: "max"
        """
        pass
    
    @abstractmethod
    def remove_extreme_element(self, heap: BaseHeap) -> Optional[int]:
        """
        Remove and return the extreme element from the heap.
        
        For MinHeap: calls remove_min()
        For MaxHeap: calls remove_max()
        """
        pass
    
    def test_initialization(self):
        """Test initialization of an empty heap"""
        heap = self.create_heap()
        self.assertEqual(heap.size, 0)
        self.assertEqual(heap.heap, [None])
    
    def test_add_single_element(self):
        """Test adding a single element to an empty heap"""
        heap = self.create_heap()
        heap.add(10)
        
        self.assertEqual(heap.size, 1)
        self.assertEqual(heap.heap, [None, 10])
    
    def test_add_multiple_elements_no_heapify_needed(self):
        """Test adding multiple elements in order (no heapify needed)"""
        heap = self.create_heap()
        # The specific elements and order will be tested in subclasses
        # This test just verifies the size is correct
        elements = [10, 20, 30]
        for element in elements:
            heap.add(element)
        
        self.assertEqual(heap.size, 3)
    
    def test_add_duplicate_elements(self):
        """Test adding duplicate elements to the heap"""
        heap = self.create_heap()
        heap.add(10)
        heap.add(10)
        heap.add(10)
        
        self.assertEqual(heap.size, 3)
        self.assertEqual(heap.heap, [None, 10, 10, 10])
    
    def test_add_negative_elements(self):
        """Test adding negative elements to the heap"""
        heap = self.create_heap()
        heap.add(-5)
        heap.add(-10)
        heap.add(-3)
        
        self.assertEqual(heap.size, 3)
        # The specific root value will be tested in subclasses
    
    def test_helper_methods(self):
        """Test the helper methods for index calculations"""
        heap_class = type(self.create_heap())
        
        # Test parent index calculation
        self.assertEqual(heap_class._get_parent_index(2), 1)
        self.assertEqual(heap_class._get_parent_index(3), 1)
        self.assertEqual(heap_class._get_parent_index(4), 2)
        self.assertEqual(heap_class._get_parent_index(5), 2)
        
        # Test left child index calculation
        self.assertEqual(heap_class._get_left_child_index(1), 2)
        self.assertEqual(heap_class._get_left_child_index(2), 4)
        self.assertEqual(heap_class._get_left_child_index(3), 6)
        
        # Test right child index calculation
        self.assertEqual(heap_class._get_right_child_index(1), 3)
        self.assertEqual(heap_class._get_right_child_index(2), 5)
        self.assertEqual(heap_class._get_right_child_index(3), 7)
    
    def test_swap_method(self):
        """Test the swap method"""
        heap = self.create_heap()
        heap.heap = [None, 10, 20, 30]
        heap.size = 3
        
        heap._swap(1, 3)
        self.assertEqual(heap.heap, [None, 30, 20, 10])
        
        heap._swap(2, 3)
        self.assertEqual(heap.heap, [None, 30, 10, 20])
    
    def test_has_child_method(self):
        """Test the _has_child method"""
        heap = self.create_heap()
        heap.heap = [None, 10, 20, 30, 40]
        heap.size = 4
        
        # Node at index 1 has children
        self.assertTrue(heap._has_child(1))
        
        # Node at index 2 has a child
        self.assertTrue(heap._has_child(2))
        
        # Node at index 4 has no children (it's a leaf)
        self.assertFalse(heap._has_child(4))
    
    def test_complex_heapify_case(self):
        """Test a more complex case requiring multiple heapify operations"""
        heap = self.create_heap()
        elements = [30, 25, 20, 15, 10, 5]
        for element in elements:
            heap.add(element)
        
        # The extreme element should be at the root (index 1)
        expected_root = self.get_root_value_after_heapify(elements)
        self.assertEqual(heap.heap[1], expected_root)
        
        # Verify the heap property: parent comparison with children
        for i in range(1, heap.size // 2 + 1):
            parent_index = i
            left_child_index = heap._get_left_child_index(parent_index)
            right_child_index = heap._get_right_child_index(parent_index)
            
            # Check left child if it exists
            if left_child_index <= heap.size:
                self.assertTrue(
                    self.compare_parent_child(
                        heap.heap[parent_index], 
                        heap.heap[left_child_index]
                    )
                )
            
            # Check right child if it exists
            if right_child_index <= heap.size:
                self.assertTrue(
                    self.compare_parent_child(
                        heap.heap[parent_index], 
                        heap.heap[right_child_index]
                    )
                )
    
    def test_heapify_up_method(self):
        """Test the heapify_up method directly"""
        # This will be implemented in subclasses as the behavior is specific
        pass
    
    def test_heapify_down_method(self):
        """Test the heapify_down method directly"""
        # This will be implemented in subclasses as the behavior is specific
        pass
    
    def test_large_heap(self):
        """Test creating a larger heap with many elements"""
        heap = self.create_heap()
        elements = list(range(1, 101))  # 1 to 100
        
        # Add elements
        for element in elements:
            heap.add(element)
        
        self.assertEqual(heap.size, 100)
        expected_root = self.get_root_value_after_heapify(elements)
        self.assertEqual(heap.heap[1], expected_root)
        
        # Verify heap property for a sample of nodes
        sample_indices = [1, 2, 3, 10, 20, 50]
        for i in sample_indices:
            left_idx = heap._get_left_child_index(i)
            right_idx = heap._get_right_child_index(i)
            
            if left_idx <= heap.size:
                self.assertTrue(
                    self.compare_parent_child(
                        heap.heap[i], 
                        heap.heap[left_idx]
                    )
                )
            
            if right_idx <= heap.size:
                self.assertTrue(
                    self.compare_parent_child(
                        heap.heap[i], 
                        heap.heap[right_idx]
                    )
                )
    
    def test_remove_extreme_empty_heap(self):
        """Test removing extreme element from an empty heap"""
        heap = self.create_heap()
        result = self.remove_extreme_element(heap)
        
        self.assertIsNone(result)
        self.assertEqual(heap.size, 0)
        self.assertEqual(heap.heap, [None])
    
    def test_remove_extreme_single_element(self):
        """Test removing extreme element from a heap with a single element"""
        heap = self.create_heap()
        heap.add(42)
        
        result = self.remove_extreme_element(heap)
        
        self.assertEqual(result, 42)
        self.assertEqual(heap.size, 0)
        self.assertEqual(heap.heap, [None])
    
    def test_remove_extreme_multiple_elements(self):
        """Test removing extreme element from a heap with multiple elements"""
        # This will be implemented in subclasses as the behavior is specific
        pass
    
    def test_remove_extreme_and_verify_heap_property(self):
        """Test removing extreme elements and verify heap property is maintained"""
        heap = self.create_heap()
        elements = [30, 25, 20, 15, 10, 5]
        for element in elements:
            heap.add(element)
        
        # Remove extreme element
        self.remove_extreme_element(heap)
        
        # Verify heap property after removal
        for i in range(1, heap.size // 2 + 1):
            parent_index = i
            left_child_index = heap._get_left_child_index(parent_index)
            right_child_index = heap._get_right_child_index(parent_index)
            
            # Check left child if it exists
            if left_child_index <= heap.size:
                self.assertTrue(
                    self.compare_parent_child(
                        heap.heap[parent_index], 
                        heap.heap[left_child_index]
                    )
                )
            
            # Check right child if it exists
            if right_child_index <= heap.size:
                self.assertTrue(
                    self.compare_parent_child(
                        heap.heap[parent_index], 
                        heap.heap[right_child_index]
                    )
                )
    
    def test_remove_all_elements(self):
        """Test removing all elements from the heap one by one"""
        heap = self.create_heap()
        elements = [25, 10, 5, 20, 15]
        for element in elements:
            heap.add(element)
        
        # Remove all elements and verify they come out in the expected order
        expected_order = self.get_expected_order(elements)
        actual_order = []
        
        while heap.size > 0:
            actual_order.append(self.remove_extreme_element(heap))
        
        self.assertEqual(actual_order, expected_order)
        self.assertEqual(heap.size, 0)
        self.assertEqual(heap.heap, [None])