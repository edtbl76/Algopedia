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
        self._size = 0 # Track size for O(1) operations


    @property
    def head(self) -> Optional[Node]:
        """ Get head of list """
        return self._head

    @head.setter
    def head(self, node: Optional[Node]) -> None:
        """ Sets the head node of the list with validation """
        if node is not None and node.prev is not None:
            node.prev = None
        self._head = node
        if self._head is None:
            self._tail = None

    @property
    def tail(self) -> Optional[Node]:
        """ Get tail of list """
        return self._tail

    @tail.setter
    def tail(self, node: Optional[Node]) -> None:
        """ sets the tail node of the list """
        if node is not None and node.next is not None:
            node.next = None
        self._tail = node
        if self._tail is None:
            self._head = None


    @property
    def size(self) -> int:
        """Get the current size of the list"""
        return self._size

    def __len__(self) -> int:
        """Support for len() function"""
        return self._size

    def _get_length(self) -> int:
        """Helper method to get the length of the list (deprecated - use size property)"""
        return self._size


    def insert_at_index(self, index: int, value: Any) -> None:
        """ insert a new node at the specified index """
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")


        ## Head Case (snicker)
        if index == 0:
            self.insert(value)
            return

        # Tail Case
        if index == self._size:
            self.append(value)
            return

        # General Case
        current = self.head
        for _ in range(index - 1):
            current = current.next


        new_node = Node(value)
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self._size += 1


    def insert(self, value: Any) -> None:
        """ inserts a new node at the head of the list """
        new_head = Node(value)
        current_head = self.head

        if current_head:
            current_head.prev = new_head
            new_head.next = current_head
        else:
            # empty list, so new node is head and tail
            self.tail = new_head


        self.head = new_head
        self._size += 1


    def append(self, value: Any) -> None:
        """ Append a new node at the end of the list """
        new_tail = Node(value)
        current_tail = self.tail

        if current_tail:
            current_tail.next = new_tail
            new_tail.prev = current_tail
        else:
            # empty list, so new node is head and tail
            self.head = new_tail

        self.tail = new_tail
        self._size += 1


    def remove_head(self) -> Optional[Any]:
        """ remove and return the value of the head node """
        if not self.head:
            return None

        removed = self.head
        self.head = removed.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self._size -= 1

        # Clean up removed node
        removed.next = None
        removed.prev = None

        return removed.data

    def remove_tail(self) -> Optional[Any]:
        """ remove and return the value of the tail node """
        if not self.tail:
            return None

        removed = self.tail
        self.tail = removed.prev

        if self.tail:
            self.tail.next = None
        else:
            # empty list, so new node is head and tail
            self.head = None

        self._size -= 1

        # Clean up removed node
        removed.next = None
        removed.prev = None

        return removed.data


    def remove_by_value(self, value:Any) -> Optional[Node]:
        """ Remove and return the first node w/ the specified value """
        current = self.head

        while current and current.data != value:
            current = current.next

        if not current:
            return None

        # If it's the only node in the list
        if current == self.head and current == self.tail:
            self.head = None
            self.tail = None
            self._size -= 1
        # If it's the head node
        elif current == self.head:
            self.remove_head()
            return current
        # If it's the tail node
        elif current == self.tail:
            self.remove_tail()
            return current
        # If it's a middle node
        else:
            current.next.prev = current.prev
            current.prev.next = current.next
            self._size -= 1
        
        # Clean up removed node
        current.next = None
        current.prev = None
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

    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self._size == 0

    def clear(self) -> None:
        """Remove all nodes from the list"""
        # Clean up all node references
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            current.prev = None
            current = next_node

        self._head = None
        self._tail = None
        self._size = 0


    def print(self) -> None:
        """Print the list contents"""
        print(self.to_string())

    def print_reverse(self) -> None:
        """Print the list contents in reverse order"""
        print(self.to_string()[::-1])