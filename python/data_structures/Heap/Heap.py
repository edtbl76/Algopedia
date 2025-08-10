from abc import ABC, abstractmethod
from typing import Optional, List


class BaseHeap(ABC):
    """
    Abstract base class for heap implementations using a list-based binary heap.

    THis implementation uses 1-based indexing where the first element (index 0)
    is None and serves as a placeholder.

    This simplifies parent-child index calculations:
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
        Initialize an empty heap.

        Creates a heap with a placeholder None at index 0 to enable
        1-based indexing for easier parent-child calculations.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.heap: List[Optional[int]] = [None]
        self.size = 0


    def add(self, value: int) -> None:
        """
        Add a new value to the heap while maintaining heap property.

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
        Restore heap property by bubbling up the last added element.

        Starting from the newly added element at the end, compare with parent
        and swap if needed. Continue until heap property is restored or we reach the root.

        Time Complexity: O(log n) - maximum height of tree traversal
        Space Complexity: O(1) - only uses constant extra space
        """
        current_index = self.size

        # Continue until we reach root (index 1) or find the correct position
        while current_index > self._ROOT_INDEX:
            parent_index = self._get_parent_index(current_index)

            # Use abstract method to determine if swap is needed
            if self._should_swap_up(current_index, parent_index):
                self._swap(current_index, parent_index)
                current_index = parent_index
            else:
                # The heap property is restored, so we can exit
                break

    def heapify_down(self) -> None:
        """
        Restore heap property by bubbling down from the root.

        Starting from the root, compare with children and swap with the appropriate child
        if needed. Continue until heap property is restored or we reach a leaf node.

        Time Complexity: O(log n) - maximum height of tree traversal
        Space Complexity: O(1) - only uses constant extra space
        """
        current_index = self._ROOT_INDEX

        # Continue until we reach a leaf node or find the correct position
        while self._has_child(current_index):
            # Find the appropriate child index (largest for max heap, smallest for min heap)
            target_child_index = self._get_target_child_index(current_index)

            # Use abstract method to determine if swap is needed
            if self._should_swap_down(current_index, target_child_index):
                self._swap(current_index, target_child_index)
                current_index = target_child_index
            else:
                # The heap property is restored, so we can exit
                break

    def peek(self) -> Optional[int]:
        """
        Return the root element without removing it.

        Returns:
            Optional[int]: The root element, or None if heap is empty

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.size == 0:
            return None
        return self.heap[self._ROOT_INDEX]

    def is_empty(self) -> bool:
        """
        Check if the heap is empty.

        Returns:
            bool: True if heap is empty, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.size == 0

    def _remove_root(self) -> Optional[int]:
        """
        Remove and return the root element from the heap.

        The root element is replaced with the last element,
        then heapify_down is called to restore the heap property.

        Returns:
            Optional[int]: The root element, or None if heap is empty

        Time Complexity: O(log n) - heapify_down operation
        Space Complexity: O(1) - only uses constant extra space
        """
        if self.size == 0:
            return None

        root_value = self.heap[self._ROOT_INDEX]

        # Short circuit if we're removing the only element
        if self.size == 1:
            self.heap.pop()
            self.size = 0
            return root_value

        # Replace root with last element and remove last element
        self.heap[self._ROOT_INDEX] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.heapify_down()
        return root_value

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

    ### Abstract Methods ###

    @abstractmethod
    def _should_swap_up(self, child_index: int, parent_index: int) -> bool:
        """
        Determine if child should be swapped with parent during heapify_up.

        Args:
            child_index (int): Index of the child node
            parent_index (int): Index of the parent node

        Returns:
            bool: True if swap should occur, False otherwise
        """
        pass

    @abstractmethod
    def _should_swap_down(self, parent_index: int, child_index: int) -> bool:
        """
        Determine if parent should be swapped with child during heapify_down.

        Args:
            parent_index (int): Index of the parent node
            child_index (int): Index of the child node

        Returns:
            bool: True if swap should occur, False otherwise
        """
        pass

    @abstractmethod
    def _get_target_child_index(self, index: int) -> int:
        """
        Get the index of the target child for comparison during heapify_down.

        For max heap: returns index of largest child
        For min heap: returns index of smallest child

        Args:
            index (int): Index of the parent node

        Returns:
            int: Index of the target child

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        pass

