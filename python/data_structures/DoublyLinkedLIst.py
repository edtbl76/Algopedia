from typing import Optional, Any
from .TwoPointNode import Node


class DoublyLinkedList:
    """
    Implementation of a Doubly Linked List data structure.
    Provides bidirectional traversal capabilities with nodes containing references
    to both next and previous nodes.
    """
    def __init__(self) -> None:
        self._head = None
        self._tail = None


    @property
    def head(self) -> Optional[Node]:
        """ Get head of list """
        return self._head

    @head.setter
    def head(self, node: Optional[Node]) -> None:
        """ sets the head node of the list """
        self._head = node

    @property
    def tail(self) -> Optional[Node]:
        """ Get tail of list """
        return self._tail

    @tail.setter
    def tail(self, node: Optional[Node]) -> None:
        """ sets the tail node of the list """
        self._tail = node

    def insert(self, value: Any) -> None:
        """ inserts a new node at the head of the list """
        new_head = Node(value)
        current_head = self.head

        if current_head:
            current_head.prev = new_head
            new_head.next = current_head

        self.head = new_head

        if not self.tail:
            self.tail = new_head


    def append(self, value: Any) -> None:
        """ Append a new node at the end of the list """
        new_tail = Node(value)
        current_tail = self.tail

        if current_tail:
            current_tail.next = new_tail
            new_tail.prev = current_tail

        self.tail = new_tail
        if not self.head:
            self.head = new_tail


    def remove_head(self) -> Optional[Any]:
        """ remove and return the value of the head node """
        if not self.head:
            return None

        removed = self.head
        self.head = removed.next

        if self.head:
            self.head.prev = None

        if removed == self.tail:
            self.remove_tail()

        return removed.data

    def remove_tail(self) -> Optional[Any]:
        """ remove and return the value of the tail node """
        if not self.tail:
            return None

        removed = self.tail
        self.tail = removed.prev

        if self.tail:
            self.tail.next = None

        if removed == self.head:
            self.remove_head()

        return removed.data


    def remove_by_value(self, value:Any) -> Optional[Node]:
        """ Remove and return the first node w/ the specified value """
        current = self.head

        while current and current.data != value:
            current = current.next

        if not current:
            return None

        if current == self.head:
            self.remove_head()
        elif current == self.tail:
            self.remove_tail()
        else:
            current.next.prev = current.prev
            current.prev.next = current.next

        return current


    def to_string(self) -> str:
        """Convert the list contents to a string representation."""
        result = []
        current = self.head
        while current:
            if current.data is not None:
                result.append(str(current.data))
            current = current.next
        return '\n'.join(result) + '\n' if result else ''


