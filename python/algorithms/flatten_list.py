# TAGS: Recursion

from typing import List, Any

def flatten_list(values: List[Any]) -> List[Any]:
    """
    Recursively flattens a nested list structure into a single-level list.

    This algorithm uses a depth-first recursive approach to traverse nested lists.

    Time Complexity: O(n) where n is the total number of elements across all nesting levels
    Space Complexity: O(d) where d is the maximum depth of nesting (recursion stack)

    Args:
        values: A list that may contain nested lists and other elements

    Returns:
        A flattened list containing all elements from the input in order

    Example:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    flattened: List[Any] = []
    for item in values:

        # Recursive step: List items are recursively flattened and their contents added
        if isinstance(item, list):
            """ 
                Implementation Detail: 
                
                extend() is used instead of += because it adds individual elements from the 
                flattened sublist without creating intermediate list objects, making it more memory efficient. 
            """
            flattened.extend(_process_nested_list(item))

        # Base case: Non-list items are added directly to the result.
        else:
            flattened.append(item)

    return flattened

def _process_nested_list(nested_list: List[Any]) -> List[Any]:
    return flatten_list(nested_list)
