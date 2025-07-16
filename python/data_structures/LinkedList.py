from typing import Optional, Any
from .SinglePointNode import Node


class LinkedList:
    def __init__(self, value: Any = None) -> None:
        self._head = Node(value)

    @property
    def head(self) -> Node:
        """ head node of the Linked List """
        return self._head

    def insert(self, value: Any) -> None:
        """ inserts a Node at the head of the list """
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    def to_string(self) -> str:
        """ Convert LL to a str representation """
        result = []
        current = self._head
        while current:
            if current.data is not None:
                result.append(str(current.data))
            current = current.next

        return "\n".join(result) + "\n" if result else ""


    def remove_by_value(self, value: Any) -> None:
        """ Removes the first occurrence of a node w/ given value """
        if not self._head:
            return

        if self._head.data == value:
            self._head = self._head.next
            return

        current = self._head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                break
            current = current.next



    def swap_node(self, value1: Any, value2: Any) -> None:
        """ Swaps two nodes w/ given values """

        # short circuit
        if value1 == value2:
            return

        prev1 = prev2 = None
        node1 = node2 = self._head

        # Find nodes w/ previous nodes
        while node1 and node1.data != value1:
            prev1 = node1
            node1 = node1.next

        while node2 and node2.data != value2:
            prev2 = node2
            node2 = node2.next

        if not node1 or not node2:
            return

        # update head if necessary
        if not prev1:
            self._head = node2
        else:
            prev1.next = node2

        if not prev2:
            self._head = node1
        else:
            prev2.next = node1

        # Update pointers
        temp = node1.next
        node1.next = node2.next
        node2.next = temp


    def find_nth_last(self, n: int) -> Optional[Node]:
        """ Finds nth last element using two (parallel) pointers approach """

        if n < 1:
            return None

        # Initialize two pointers
        fast = slow = self._head

        # Move fast pointer n nodes ahead
        for _ in range(n):
            if not fast:
                return None  # List is shorter than n
            fast = fast.next

        # If n is exactly the length of the list, return the head
        if not fast:
            return self._head

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        return slow

    def find_nth_last_naive(self, n: int) -> Optional[Node]:
        """
        Naive / Brute force implementation that gets the nth element from the tail of the list by storing
        an entire representation of the list

        (Obvi, doesn't scale!)
        """

        ll_copy = []
        current = self._head
        while current:
            ll_copy.append(current)
            current = current.next
        return ll_copy[len(ll_copy) - n]

    def find_middle(self) -> Optional[Node]:
        """ Find middle node using fast/slow pointer technique """

        if not self._head:
            return None

        slow = fast = self._head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def find_middle_alt(self) -> Optional[Node]:
        """ This alternative implementation uses a counter and moves the slow pointer at 1/2 speed. """

        if not self._head:
            return None

        count = 0
        fast = slow = self._head

        while fast:
            fast = fast.next
            if count % 2 != 0:
                slow = slow.next
            count += 1

        return slow