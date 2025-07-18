from data_structures.LinkedList import LinkedList


def find_min(linked_list: LinkedList) -> int:
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
