import unittest
from typing import List, Optional

from data_structures.Heap.Heap import BaseHeap
from data_structures.Heap.MinHeap import MinHeap
from tests.data_structures.test_heap_base import TestHeapBase


class TestMinHeap(TestHeapBase):
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
    
    def create_heap(self) -> BaseHeap:
        """Create and return a new MinHeap instance."""
        return MinHeap()
    
    def get_expected_order(self, elements: List[int]) -> List[int]:
        """
        Return the expected order of elements when removed from the min heap.
        
        For MinHeap: ascending order
        """
        return sorted(elements)
    
    def compare_parent_child(self, parent: int, child: int) -> bool:
        """
        Compare parent and child values according to min heap property.
        
        For MinHeap: parent <= child
        
        Returns True if the heap property is satisfied.
        """
        return parent <= child
    
    def get_root_value_after_heapify(self, elements: List[int]) -> int:
        """
        Return the expected root value after heapifying the given elements.
        
        For MinHeap: minimum value
        """
        return min(elements)
    
    def get_extreme_element_name(self) -> str:
        """
        Return the name of the extreme element for this heap type.
        
        For MinHeap: "min"
        """
        return "min"
    
    def remove_extreme_element(self, heap: BaseHeap) -> Optional[int]:
        """
        Remove and return the minimum element from the heap.
        
        For MinHeap: calls remove_min()
        """
        return heap.remove_min()
    
    def test_add_multiple_elements_no_heapify_needed(self):
        """Test adding multiple elements in increasing order (no heapify needed)"""
        min_heap = self.create_heap()
        min_heap.add(10)
        min_heap.add(20)
        min_heap.add(30)
        
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap, [None, 10, 20, 30])
    
    def test_add_multiple_elements_with_heapify(self):
        """Test adding multiple elements that require heapify to maintain min heap property"""
        min_heap = self.create_heap()
        min_heap.add(30)
        min_heap.add(20)
        min_heap.add(10)
        
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap, [None, 10, 30, 20])
    
    def test_add_negative_elements(self):
        """Test adding negative elements to the heap"""
        min_heap = self.create_heap()
        min_heap.add(-5)
        min_heap.add(-10)
        min_heap.add(-3)
        
        self.assertEqual(min_heap.size, 3)
        self.assertEqual(min_heap.heap[1], -10)  # -10 is the min of the negative numbers
    
    def test_get_smallest_child_index_method(self):
        """Test the _get_target_child_index method for MinHeap"""
        min_heap = MinHeap()
        
        # Case 1: Both children exist, right child is smaller
        min_heap.heap = [None, 10, 30, 20, 50, 40]
        min_heap.size = 5
        self.assertEqual(min_heap._get_target_child_index(1), 3)  # Right child (20) < left child (30)
        
        # Case 2: Both children exist, left child is smaller
        min_heap.heap = [None, 10, 20, 30, 50, 40]
        min_heap.size = 5
        self.assertEqual(min_heap._get_target_child_index(1), 2)  # Left child (20) < right child (30)
        
        # Case 3: Only left child exists
        min_heap.heap = [None, 10, 20, 30]
        min_heap.size = 3
        self.assertEqual(min_heap._get_target_child_index(1), 2)  # Only left child exists
    
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
    
    def test_remove_extreme_multiple_elements(self):
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


if __name__ == '__main__':
    unittest.main()