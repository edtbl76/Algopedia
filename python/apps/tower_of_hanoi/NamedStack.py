from typing import Optional, Any
from data_structures.Stack import Stack


class NamedStack(Stack):
    """A wrapper for Stack that adds a name attribute."""

    def __init__(self, name: str, limit: Optional[int] = None) -> None:
        """
        Initialize named stack.
        Args:
            name: Name of the stack
            limit: Maximum number of elements allowed in stack. None for unlimited.
        """
        super().__init__(limit)
        self._name = name

    @property
    def name(self) -> str:
        """
        Get the name of the stack.
        Returns:
            The name of the stack
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set a new name for the stack.
        Args:
            new_name: New name for the stack
        """
        self._name = new_name

    def display(self) -> None:
        current = self._top
        print_list = []
        while current:
            print_list.append(current.data)
            current = current.next
        print_list.reverse()
        print(f"{self.name} Stack: {print_list}")