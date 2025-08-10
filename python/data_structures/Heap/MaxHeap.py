"""
MaxHeap

This module provides a complete implementation of a max heap data structure,
where the parent node is always greater than or equal to its children.
The heap is implemented using a list with 1-based indexing for easier
parent-child index calculations.

The heap maintains the max heap property: for any node i,
heap[i] >= heap[2*i] and heap[i] >= heap[2*i + 1]
"""
from typing import Optional

from data_structures.Heap.Heap import BaseHeap


class MaxHeap(BaseHeap):
    """
    A max heap implementation using a list-based binary heap.

    This implementation uses 1-based indexing where the first element (index 0)
    is None and serves as a placeholder. This simplifies parent-child index
    calculations:
    - Parent of node at index i: i // 2
    - Left child of node at index i: 2 * i
    - Right child of node at index i: 2 * i + 1

    Attributes:
        heap (List[Optional[int]]): The underlying list storing heap elements
        size (int): Current number of elements in the heap
    """

    def remove_max(self) -> Optional[int]:
        """
        Remove and return the maximum element from the heap.

        The root element (maximum) is replaced with the last element,
        then heapify_down is called to restore the heap property.

        Returns:
            Optional[int]: The maximum element, or None if heap is empty

        Time Complexity: O(log n) - heapify_down operation
        Space Complexity: O(1) - only uses constant extra space
        """
        return self._remove_root()


    def _should_swap_up(self, child_index: int, parent_index: int) -> bool:
        """
        Determine if child should be swapped with parent during heapify_up..

        FOr max heap: swap if child > parent.

        Args:
            child_index (int): Index of the child node
            parent_index (int): Index of the parent node

        Returns:
            bool: True if swap should occur, False otherwise
        """
        return self.heap[child_index] > self.heap[parent_index]


    def _should_swap_down(self, parent_index: int, child_index: int) -> bool:
        """
        Determine if parent should be swapped with child during heapify_down.

        FOr max heap: swap if child > parent.

        Args:
            child_index (int): Index of the child node
            parent_index (int): Index of the parent node

        Returns:
            bool: True if swap should occur, False otherwise
        """
        return self.heap[child_index] > self.heap[parent_index]


    def _get_target_child_index(self, index: int) -> int:
        """
        Get the index of the largest child of the given node.

        Compares left and right children (if they exist) and returns
        the index of the larger one.

        Args:
            index (int): Index of the parent node

        Returns:
            int: Index of the largest child

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)

        # If only left child exists, return it
        if right_child_index > self.size:
            return left_child_index

        # Both children exist, compare and return the largest
        left_child = self.heap[left_child_index]
        right_child = self.heap[right_child_index]
        return left_child_index if left_child > right_child else right_child_index
