"""
MaxHeap

This module provides a complete implementation of a max heap data structure,
where the parent node is always greater than or equal to its children.
The heap is implemented using a list with 1-based indexing for easier
parent-child index calculations.

The heap maintains the max heap property: for any node i,
heap[i] >= heap[2*i] and heap[i] >= heap[2*i + 1]
"""
from typing import Optional, List


class MaxHeap:
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


    def __init__(self) -> None:
        """
        Initialize an empty max heap.

        Creates a heap with a placeholder None at index 0 to enable
        1-based indexing for easier parent-child calculations.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.heap: List[Optional[int]] = [None]
        self.size: int = 0


    def add(self, value: int) -> None:
        """
        Add a new value to the heap while maintaining max heap property.

        The new element is initially added at the end of the heap (bottom level)
        and then bubbled up through heapify_up to restore heap property.

        Args:
            value (int): The integer value to add to the heap

        Time Complexity: O(log n) - worst case bubbles up to root
        Space Complexity: O(1) - only uses constant extra space
        """
        self.size += 1
        self.heap.append(value)
        self.heapify_up()

    def heapify_up(self):
        """
        Restore max heap property by bubbling up the last added element.

        Starting from the newly added element at the end, compare with parent
        and swap if current element is larger. Continue until heap property
        is restored or we reach the root.

        Time Complexity: O(log n) - maximum height of tree traversal
        Space Complexity: O(1) - only uses constant extra space
        """
        index = self.size

        # Continue until we reach root (index 1) or find the correct position
        while index > 1:
            parent_index = self._get_parent_index(index)

            # if current element > parent, swap!
            if self.heap[index] > self.heap[parent_index]:
                self._swap(index, parent_index)

                # Moves the index up to the parent to bubble up
                index = parent_index
            else:

                # The heap property is restored, so we can exit
                break



    ### Helper Methods ###

    @staticmethod
    def _get_parent_index(index: int) -> int:
        """
        Calculate the parent index for a given node index.

        In a 1-based indexed heap, parent of node i is at index i // 2.

        Args:
            index (int): Index of the child node

        Returns:
            int: Index of the parent node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return index // 2

    @staticmethod
    def _get_left_child_index(index: int) -> int:
        """
        Calculate the left child index for a given node index.

        In a 1-based indexed heap, left child of node i is at index 2 * i.

        Args:
            index (int): Index of the parent node

        Returns:
            int: Index of the left child node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return 2 * index

    @staticmethod
    def _get_right_child_index(index: int) -> int:
        """
        Calculate the right child index for a given node index.

        In a 1-based indexed heap, right child of node i is at index 2 * i + 1.

        Args:
            index (int): Index of the parent node

        Returns:
            int: Index of the right child node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return 2 * index + 1

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swap two elements in the heap at given indices.

        Uses Python's tuple unpacking for efficient in-place swapping.

        Args:
            index1 (int): Index of first element to swap
            index2 (int): Index of second element to swap

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
