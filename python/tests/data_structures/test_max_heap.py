import unittest
from typing import List, Optional

from data_structures.Heap.Heap import BaseHeap
from data_structures.Heap.MaxHeap import MaxHeap
from tests.data_structures.test_heap_base import TestHeapBase


class TestMaxHeap(TestHeapBase):
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
    
    def create_heap(self) -> BaseHeap:
        """Create and return a new MaxHeap instance."""
        return MaxHeap()
    
    def get_expected_order(self, elements: List[int]) -> List[int]:
        """
        Return the expected order of elements when removed from the max heap.
        
        For MaxHeap: descending order
        """
        return sorted(elements, reverse=True)
    
    def compare_parent_child(self, parent: int, child: int) -> bool:
        """
        Compare parent and child values according to max heap property.
        
        For MaxHeap: parent >= child
        
        Returns True if the heap property is satisfied.
        """
        return parent >= child
    
    def get_root_value_after_heapify(self, elements: List[int]) -> int:
        """
        Return the expected root value after heapifying the given elements.
        
        For MaxHeap: maximum value
        """
        return max(elements)
    
    def get_extreme_element_name(self) -> str:
        """
        Return the name of the extreme element for this heap type.
        
        For MaxHeap: "max"
        """
        return "max"
    
    def remove_extreme_element(self, heap: BaseHeap) -> Optional[int]:
        """
        Remove and return the maximum element from the heap.
        
        For MaxHeap: calls remove_max()
        """
        return heap.remove_max()
    
    def test_add_multiple_elements_no_heapify_needed(self):
        """Test adding multiple elements in decreasing order (no heapify needed)"""
        max_heap = self.create_heap()
        max_heap.add(30)
        max_heap.add(20)
        max_heap.add(10)
        
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap, [None, 30, 20, 10])
    
    def test_add_multiple_elements_with_heapify(self):
        """Test adding multiple elements that require heapify to maintain max heap property"""
        max_heap = self.create_heap()
        max_heap.add(10)
        max_heap.add(20)
        max_heap.add(30)
        
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap, [None, 30, 10, 20])
    
    def test_add_negative_elements(self):
        """Test adding negative elements to the heap"""
        max_heap = self.create_heap()
        max_heap.add(-5)
        max_heap.add(-10)
        max_heap.add(-3)
        
        self.assertEqual(max_heap.size, 3)
        self.assertEqual(max_heap.heap[1], -3)  # -3 is the max of the negative numbers
    
    def test_get_largest_child_index_method(self):
        """Test the _get_target_child_index method for MaxHeap"""
        max_heap = MaxHeap()
        
        # Case 1: Both children exist, right child is larger
        max_heap.heap = [None, 50, 30, 40, 10, 20]
        max_heap.size = 5
        self.assertEqual(max_heap._get_target_child_index(1), 3)  # Right child (40) > left child (30)
        
        # Case 2: Both children exist, left child is larger
        max_heap.heap = [None, 50, 40, 30, 10, 20]
        max_heap.size = 5
        self.assertEqual(max_heap._get_target_child_index(1), 2)  # Left child (40) > right child (30)
        
        # Case 3: Only left child exists
        max_heap.heap = [None, 50, 40, 30]
        max_heap.size = 3
        self.assertEqual(max_heap._get_target_child_index(1), 2)  # Only left child exists
    
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
    
    def test_remove_extreme_multiple_elements(self):
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


if __name__ == '__main__':
    unittest.main()