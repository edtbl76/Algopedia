from typing import List, Any

NODE_DATA_KEY = 'data'
LEFT_CHILD_KEY = 'left_child'
RIGHT_CHILD_KEY = 'right_child'


def build_balanced_bst_from_sorted_array(sorted_values: List[Any]) -> dict[str, Any] | None:
    """
    Build a balanced binary search tree from a sorted array using divide-and-conquer recursion.

    This algorithm creates a height-balanced BST by recursively selecting the middle element
    as the root and building left and right subtrees from the remaining elements. The resulting
    tree maintains optimal search performance with O(log n) height.

    Time Complexity: O(n) - each element is processed exactly once
    Space Complexity: O(log n) - recursion depth for a balanced tree, plus O(n) for the tree structure

    Args:
        sorted_values: A list of values in sorted order to build the BST from

    Returns:
        A dictionary representing the root node of the BST with keys 'data', 'left_child',
        and 'right_child', or None if the input array is empty

    Examples:
        >>> build_balanced_bst_from_sorted_array([1, 2, 3, 4, 5])
        {'data': 3, 'left_child': {'data': 1, 'left_child': None, 'right_child': {'data': 2, 'left_child': None, 'right_child': None}}, 'right_child': {'data': 4, 'left_child': None, 'right_child': {'data': 5, 'left_child': None, 'right_child': None}}}
        >>> build_balanced_bst_from_sorted_array([])
        None
    """

    # Bse cse: empty array returns 'None' (no subtree)
    if not sorted_values:
        return None

    mid_index = len(sorted_values) // 2
    root_value = sorted_values[mid_index]

    # Recursive step: build left and right subtrees from remaining elements.
    """
        Implementation Note: 
        
        Uses dictionary literals for node creation instead of procedural
        construction (e.g., creating empty dict and setting keys separately), which is more
        concise and expresses the tree structure declaratively.
        
        This might be a trade-off between "readability" and Pythonic purism. 

    """
    bst_node = {
        NODE_DATA_KEY: root_value,
        LEFT_CHILD_KEY: build_balanced_bst_from_sorted_array(sorted_values[:mid_index]),
        RIGHT_CHILD_KEY: build_balanced_bst_from_sorted_array(sorted_values[mid_index + 1:])
    }

    return bst_node



