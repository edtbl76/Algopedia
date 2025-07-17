from typing import Optional, Any, List
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
        self._name: str  = name

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
                Raises:
            ValueError: If new_name is empty or contains only whitespace

        """
        if not new_name or new_name.isspace():
            raise ValueError("Stack name cannot be empty or whitespace")
        self._name = new_name


    def _build_display_list(self) -> List[Any]:
        """
           Build a list of stack elements from top to bottom.
           Returns:
               List of stack elements in bottom-to-top order
        """
        display_list = []
        current = self._top
        while current:
            display_list.append(current.data)
            current = current.next
        display_list.reverse()
        return display_list

    def display_contents(self) -> None:
        """ display stack contents from bottom to top """
        contents = self._build_display_list()
        print(f"{self.name} Stack: {contents}")


    def __repr__(self) -> str:
        """Return a detailed string representation of the stack."""
        return f"NamedStack(name='{self.name}', contents={self._build_display_list()})"
