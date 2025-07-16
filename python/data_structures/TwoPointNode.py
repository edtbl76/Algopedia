from typing import Any, Optional


class Node:
    """
    A node class for dual-linked data structures like dual linked lists
    """


    def __init__(self, data:Any , next_node: Optional['Node'] = None, prev_node: Optional['Node'] = None) -> None:
        """
        Init a new node
        :param data: data to store in the node
        :param next_node: reference to the next node (None by default)
        :param prev_node: reference to the previous node (None by default)
        """

        self.data = data
        self.next = next_node
        self.prev = prev_node

    @property
    def data(self) -> Any:
        """ data stored in the node """
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    @property
    def next(self) -> Optional['Node']:
        """ reference to the next node in the sequence. """
        return self._next

    @next.setter
    def next(self, next_node: Optional['Node']) -> None:
        self._next = next_node

    @property
    def prev(self) -> Optional['Node']:
        """ reference to the previous node in the sequence. """
        return self._prev

    @prev.setter
    def prev(self, prev_node: Optional['Node']):
        self._prev = prev_node

