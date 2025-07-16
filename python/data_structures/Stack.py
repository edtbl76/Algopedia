from typing import Optional, Any

from .SinglePointNode import Node


class Stack:
    def __init__(self, limit: Optional[int] = None) -> None:
        self._top: Optional[Node] = None
        self._limit: Optional[int] = limit
        self._size: int = 0

    def push(self, value: Any) -> None:
        if self._limit and self._size >= self._limit:
            raise OverflowError("Stack Overflow")

        pushed = Node(value)
        pushed.next = self._top
        self._top = pushed
        self._size += 1


    def pop(self) -> Any:
        if not self._top:
            raise IndexError("Stack Underflow")

        popped = self._top
        self._top = popped.next
        self._size -= 1
        return popped.data

    @property
    def peek(self) -> Optional[Any]:
        return self._top.data if self._size > 0 else None