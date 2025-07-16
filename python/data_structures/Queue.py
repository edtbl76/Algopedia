from typing import Optional, Any
from .SinglePointNode import Node

class Queue:
    """A queue implementation using a linked list structure."""

    """
        Initialize an empty queue
        Args: 
        max_size: Maximum number of elements allowed in the queue. None for unlimited. 
    """
    def __init__(self, max_size: Optional[int] = None) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._max_size: Optional[int] = max_size
        self._size: int = 0


    @property
    def size(self) -> int:
        """ Current number of elements in the queue """
        return self._size

    @property
    def max_size(self) -> Optional[int]:
        """ Maximum allowed size of the queue """
        return self._max_size

    def enqueue(self, value: Any) -> None:
        """
        Adds element to the end of the queue
        :param value: value to add to the queue
        """
        if self.has_space():
            added = Node(value)

            if self.is_empty():
                self._head = added
                self._tail = added
            else:
                self._tail.next = added
                self._tail = added

            self._size += 1


    def dequeue(self) -> Optional[Any]:
        """
        Removes and returns first element from the queue
        :return: first element in the queue (None for empty queue)
        """

        if not self.is_empty():
            removed = self._head

            if self.size == 1:
                self._head = None
                self._tail = None
            else:
                self._head = removed.next

            self._size -= 1

            return removed.data

        return None

    def peek(self) -> Optional[Any]:
        """
          Return the first element in the queue without removing it.
          Returns:
              The first element in the queue, or None if queue is empty.
          """
        return self._head.data

    def has_space(self):
        """ checks if queue has space for more elements """
        return self._max_size is None or self._max_size > self._size

    def is_empty(self):
        """ check if queue is empty """
        return self._size == 0
