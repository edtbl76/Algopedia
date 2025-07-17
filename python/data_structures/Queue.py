from typing import Optional, Any

from data_structures.SinglePointNode import Node

class Queue:
    """A FIFO (First-In-First-Out) queue implementation using a linked list."""

    def __init__(self, max_size: Optional[int] = None) -> None:
        """
        Initialize an empty queue.

        Args:
            max_size: Maximum number of elements allowed in the queue. None for unlimited.
        """
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._max_size: Optional[int] = max_size
        self._size: int = 0


    @property
    def size(self) -> int:
        """ Return the current number of elements in the queue """
        return self._size

    def enqueue(self, value: Any) -> None:
        """
        Add an element to the end of the queue if space is available.

        Args:
            value: The value to add to the queue.
        """
        if self.has_space():
            added = Node(value)

            if self.is_empty():
                self._head = self._tail = added
            else:
                self._tail.next = added
                self._tail = added

            self._size += 1

    def dequeue(self) -> Optional[Any]:
        """
         Remove and return the first element from the queue.

         Returns:
             The first element in the queue, or None if queue is empty.
         """
        if self.is_empty():
            return None

        removed = self._head

        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = removed.next

        self._size -= 1
        return removed.data

    def peek(self) -> Any:
        """
        Return the first element in the queue without removing it.

        Raises:
            AttributeError: If the queue is empty.
        """
        if self.is_empty():
            raise AttributeError("Cannot peek an empty queue")
        return self._head.data

    def has_space(self) -> bool:
        """Check if the queue has space for more elements."""
        return self._max_size is None or self._max_size > self.size

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._size == 0

