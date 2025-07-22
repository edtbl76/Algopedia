from typing import List

from data_structures.LinkedList import LinkedList


def find_min_ll(linked_list: LinkedList) -> int:
    """
    Find the minimum value in a linked list.

    This algorithm traverses the linked list once, comparing each node's data
    with the current minimum value and updating it if a smaller value is found.

    Time Complexity: O(n) - where n is the number of nodes in the linked list.
                    The algorithm needs to visit each node exactly once.

    Space Complexity: O(1) - only a constant amount of extra space is used
                     regardless of the input size.

    Args:
        linked_list: A LinkedList object to search through

    Returns:
        The minimum value found in the linked list

    Raises:
        ValueError: If the linked list is empty
    """
    if not linked_list.head or linked_list.head.data is None:
        raise ValueError("Cannot find minimum in empty list")

    current = linked_list.head
    minimum_value: int = current.data

    """ 
        We can start from the 2nd node, because we've
        initialized 'minimum value' to the head. 
    """
    while current.next:
        current = current.next
        if current.data < minimum_value:
            minimum_value = current.data

    return minimum_value


def find_minimum_iterative(values: List[int]) -> int | None:
    """
    Find the minimum value in a list using iterative approach.

    This algorithm iterates through the list once, maintaining a running
    minimum value and updating it when a smaller value is encountered.

    Time Complexity: O(n) - where n is the number of elements in the list.
                    Each element is visited exactly once.

    Space Complexity: O(1) - only uses constant additional space regardless
                     of input size.

    Args:
        values: List of integers to search through

    Returns:
        The minimum value found in the list, or None if the list is empty
    """

    if len(values) == 0:
        return None

    minimum_value: int = values[0]
    for value in values[1:]:
        if value < minimum_value:
            minimum_value = value

    return minimum_value

def find_minimum_recursive(values: List[int], minimum_value: int = None) -> int | None:
    """
     Find the minimum value in a list using recursive approach.

     This algorithm recursively processes the list by comparing the first element
     with the current minimum and recursively processing the remaining elements.

     Time Complexity: O(n) - where n is the number of elements in the list.
                     Each element is processed exactly once through recursive calls.

     Space Complexity: O(n) - due to the call stack depth, which grows linearly
                      with the input size (each recursive call adds a frame).

     Args:
         values: List of integers to search through
         minimum_value: Current minimum value found so far (used internally for recursion)

     Returns:
         The minimum value found in the list, or None if the list is empty
     """

    # Base cse: if the list is empty, return the current minimum
    if len(values) == 0:
        return minimum_value

    head_value: int = values[0]
    remaining_values: List[int] = values[1:]

    if minimum_value is None or head_value < minimum_value:
        minimum_value = head_value

    # recursive step: process the remaining elements with the updated minimum
    return find_minimum_recursive(remaining_values, minimum_value)
