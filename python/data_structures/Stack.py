from typing import Optional, Any

from .SinglePointNode import Node


class Stack:
    """A stack implementation using linked nodes with optional size limit."""

    def __init__(self, limit: Optional[int] = None) -> None:
        """
        Initialize empty stack.
        Args:
            limit: Maximum number of elements allowed in stack. None for unlimited.
        """

        self._top: Optional[Node] = None
        self._limit: Optional[int] = limit
        self._size: int = 0

    def push(self, value: Any) -> None:
        """
            Push a value onto the stack.
            Args:
                value: Value to push
            Raises:
                OverflowError: If stack is at its size limit
            """
        if not self.has_space():
            raise OverflowError("Stack is full")

        pushed = Node(value)
        pushed.next = self._top
        self._top = pushed
        self._size += 1


    def pop(self) -> Any:
        """
        Remove and return the top element from the stack.
        Returns:
            The value from the top of the stack
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")


        popped = self._top
        self._top = popped.next
        self._size -= 1
        return popped.data

    @property
    def peek(self) -> Optional[Any]:
        """
        Return the top element without removing it.
        Returns:
            The value from the top of the stack, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self._top.data


    def has_space(self) -> bool:
        """
        Check if stack can accept more elements.
        Returns:
            True if stack is unlimited or below size limit, False otherwise
        """
        return self._limit is None or self._limit > self._size

    def is_empty(self) -> bool:
        """
        Check if stack has no elements.
        Returns:
            True if stack contains no elements, False otherwise
        """
        return self._size == 0
