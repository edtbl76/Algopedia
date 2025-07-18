from data_structures.LinkedList import LinkedList


def find_max(linked_list: LinkedList) -> int:
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
