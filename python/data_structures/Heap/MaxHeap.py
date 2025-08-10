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

    # Constant for heap indexing strategy
    # 1-based indexing for easier parent-child calculations.
    # Includes a placeholder None at index 0.
    _ROOT_INDEX = 1

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

    def heapify_up(self) -> None:
        """
        Restore max heap property by bubbling up the last added element.

        Starting from the newly added element at the end, compare with parent
        and swap if current element is larger. Continue until heap property
        is restored or we reach the root.

        Time Complexity: O(log n) - maximum height of tree traversal
        Space Complexity: O(1) - only uses constant extra space
        """
        current_index = self.size

        # Continue until we reach root (index 1) or find the correct position
        while current_index > self._ROOT_INDEX:
            parent_index = self._get_parent_index(current_index)

            # if current element > parent, swap!
            if self.heap[current_index] > self.heap[parent_index]:
                self._swap(current_index, parent_index)

                # Moves the index up to the parent to bubble up
                current_index = parent_index
            else:
                # The heap property is restored, so we can exit
                break

    def heapify_down(self) -> None:
        """
        Restore max heap property by bubbling down from the root.

        Starting from the root, compare with children and swap with the larger child
        if the current node is smaller. Continue until heap property is restored
        or we reach a leaf node.

        Time Complexity: O(log n) - maximum height of tree traversal
        Space Complexity: O(1) - only uses constant extra space
        """
        current_index = self._ROOT_INDEX

        # Continue until we reach a leaf node or find the correct position
        while self._has_child(current_index):

            # Find the largest child index
            largest_child_index = self._get_largest_child_index(current_index)

            # get the current and largest child values
            child = self.heap[largest_child_index]
            parent = self.heap[current_index]

            # swap if current element is smaller than largest child
            if child > parent:
                self._swap(current_index, largest_child_index)
                current_index = largest_child_index
            else:
                # The heap property is restored, so we can exit
                break

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
        if self.size == 0:
            return None

        max_value = self.heap[self._ROOT_INDEX]

        # short circuit if we're removing the only element
        if self.size == 1:
            self.heap.pop()
            self.size = 0
            return max_value

        # Replace root with last element and remove last element
        self.heap[self._ROOT_INDEX] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.heapify_down()
        return max_value

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


    def _has_child(self, index: int) -> bool:
        """
        Check if a node at given index has at least one child.

        Args:
            index (int): Index of the node to check

        Returns:
            bool: True if node has at least one child, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self._get_left_child_index(index) <= self.size

    def _get_largest_child_index(self, index: int) -> int:
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
