from typing import List

from data_structures.LinkedList import LinkedList


def find_max_ll(linked_list: LinkedList) -> int:
    """
    Find the maximum value in a linked list.

    This algorithm traverses the linked list once, comparing each node's data
    with the current maximum value and updating it if a larger value is found.

    Time Complexity: O(n) - where n is the number of nodes in the linked list.
                    The algorithm needs to visit each node exactly once.

    Space Complexity: O(1) - only a constant amount of extra space is used
                     regardless of the input size.

    Args:
        linked_list: A LinkedList object to search through

    Returns:
        The maximum value found in the linked list

    Raises:
        ValueError: If the linked list is empty
    """
    if not linked_list.head or linked_list.head.data is None:
        raise ValueError("Cannot find maximum in empty list")

    current = linked_list.head
    maximum_value: int = current.data

    """ 
        We can start from the 2nd node, because we've
        initialized 'maximum value' to the head. 


    """
    while current.next:
        current = current.next
        if current.data > maximum_value:
            maximum_value = current.data

    return maximum_value


def find_maximum_iterative(values: list) -> int | None:
    """
    Find the maximum value in a list using iterative approach.

    This algorithm iterates through the list once, maintaining a running
    maximum value and updating it when a larger value is encountered..

    Time Complexity: O(n) - where n is the number of elements in the list.
                    Each element is visited exactly once.

    Space Complexity: O(1) - only uses constant additional space regardless
                     of input size.

    Args:
        values: List of integers to search through

    Returns:
        The maximum value found in the list, or None if the list is empty
    """

    if len(values) == 0:
        return None

    maximum_value: int = values[0]
    for value in values[1:]:
        if value > maximum_value:
            maximum_value = value

    return maximum_value

def find_maximum_recursive(values: List[int], maximum_value: int = None) -> int | None:
    """
     Find the maximum value in a list using recursive approach.

     This algorithm recursively processes the list by comparing the first element
     with the current maximum and recursively processing the remaining elements.

     Time Complexity: O(n) - where n is the number of elements in the list.
                     Each element is processed exactly once through recursive calls.

     Space Complexity: O(n) - due to the call stack depth, which grows linearly
                      with the input size (each recursive call adds a frame).

     Args:
         values: List of integers to search through
         maximum_value: Current maximum value found so far (used internally for recursion)

     Returns:
         The maximum value found in the list, or None if the list is empty
     """

    # Base case: if the list is empty, return the current maximum
    if len(values) == 0:
        return maximum_value

    head_value: int = values[0]
    remaining_values: List[int] = values[1:]

    if maximum_value is None or head_value > maximum_value:
        maximum_value = head_value

    # recursive step: process the remaining elements with the updated minimum
    return find_maximum_recursive(remaining_values, maximum_value)