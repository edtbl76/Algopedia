from typing import Any, Optional
from data_structures.SinglePointNode import Node


class LinkedList:
    """ A singly linked list implementation """

    def __init__(self, value: Any = None) -> None:
        """ Initialize the LL w/ an optional value """
        self._head = Node(value)

    @property
    def head(self) -> Node:
        """ Get the head node of the list """
        return self._head

    @head.setter
    def head(self, node: Node) -> None:
        """ Set head node of the list """
        self._head = node

    def insert(self, value: Any) -> None:
        """ Insert a new node w/ given value at the start of the list """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def stringify(self) -> str:
        """Convert the list contents to a string representation."""
        nodes = []
        current = self.head
        while current:
            if current.data is not None:
                nodes.append(str(current.data))
            current = current.next
        return '\n'.join(nodes) + '\n' if nodes else ''


    def remove(self, value_to_remove: Any) -> None:
        """Remove the first node with the specified value."""
        if self.head.data == value_to_remove:
            self.head = self.head.next
            return

        current = self.head
        while current and current.next:
            if current.next.data == value_to_remove:
                current.next = current.next.next
                break
            current = current.next



    def swap(self, value1: Any, value2: Any) -> None:
        """Swap positions of two nodes with given values."""
        if value1 == value2:
            return

        # Find nodes and their predecessors
        prev1, node1 = self._find_node(value1)
        prev2, node2 = self._find_node(value2)

        if not node1 or not node2:
            return

        # Update head if necessary
        if prev1 is None:
            self.head = node2
        else:
            prev1.next = node2

        if prev2 is None:
            self.head = node1
        else:
            prev2.next = node1

        # Swap the next pointers
        node1.next, node2.next = node2.next, node1.next


    """ HELPERS """

    def _find_node(self, value: Any) -> tuple[Optional[Node], Optional[Node]]:
        """Find a node with given value and its predecessor."""
        current = self.head
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        return prev, current
