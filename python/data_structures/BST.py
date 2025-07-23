from collections import deque
from typing import Any, Dict, List

NODE_DATA_KEY = 'data'
LEFT_CHILD_KEY = 'left_child'
RIGHT_CHILD_KEY = 'right_child'


def build_balanced_bst(sorted_values: List[Any]) -> Dict[str, Any] | None:
    """
    Build a balanced binary search tree from a sorted array using divide-and-conquer recursion.
    This algorithm creates a height-balanced BST by recursively selecting the middle element
    as the root and building left and right subtrees from the remaining elements. The resulting
    tree maintains optimal search performance with O(log n) height.

    Uses dictionary literals for node creation instead of procedural construction
    (e.g., creating empty dict and setting keys separately), which is more concise
    and expresses the tree structure declaratively.

    Time Complexity: O(n) - each element is processed exactly once
    Space Complexity: O(log n) - recursion depth for a balanced tree, plus O(n) for the tree structure
    Args:
        sorted_values: A list of values in sorted order to build the BST from
    Returns:
        A dictionary representing the root node of the BST with keys 'data', 'left_child',
        and 'right_child', or None if the input array is empty

    Examples:
        >>> build_balanced_bst([1, 2, 3, 4, 5])
        {'data': 3, 'left_child': {'data': 1, 'left_child': None, 'right_child': {'data': 2, 'left_child': None, 'right_child': None}}, 'right_child': {'data': 4, 'left_child': None, 'right_child': {'data': 5, 'left_child': None, 'right_child': None}}}
        >>> build_balanced_bst([])
        None
    """

    # Base cse: empty array returns 'None' (no subtree)
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
        LEFT_CHILD_KEY: build_balanced_bst(sorted_values[:mid_index]),
        RIGHT_CHILD_KEY: build_balanced_bst(sorted_values[mid_index + 1:])
    }

    return bst_node


"""
I felt like this was an interesting case, because iteration and recursion represent different approaches
to finding the depth of a binary search trees, moreso than other iteration and recursion problems.

Comparison of Iterative (BFS) vs. Recursive (DFS) Tree Traversal Approaches

Both functions find the depth of a binary search tree but use fundamentally different traversal strategies:

Iterative Approach (find_depth_iterative):
    - Implements Breadth-First Search (BFS) traversal using a queue
    - Processes the tree level-by-level (horizontally)
    - Uses a queue data structure (FIFO) to track nodes to visit
    - Time Complexity: O(n) - each node is processed once
    - Space Complexity: O(w) - where w is the maximum width of the tree
    - Avoids call stack limitations for very deep trees
    - Most efficient for wide, shallow trees

Recursive Approach (find_depth_recursive):
    - Implements Depth-First Search (DFS) traversal using recursion
    - Explores branches completely before backtracking (vertically)
    - Uses the call stack to implicitly track the traversal path
    - Time Complexity: O(n) - each node is processed once
    - Space Complexity: O(h) - where h is the height of the tree (recursion stack)
    - Can hit stack overflow for very deep trees
    - Most efficient for deep, narrow trees

Memory Usage Patterns:
    - In balanced trees (height ≈ log n): Both use O(log n) space
    - In skewed trees: Recursive DFS may use O(n) space
    - In wide, shallow trees: Iterative BFS may use more space than DFS

The choice between these approaches depends on the tree structure and specific application requirements.
"""



def find_depth_iterative(bst_tree: Dict[str, Any]) -> int:
    """
    Find the depth of a binary search tree using breadth-first traversal (iterative approach).

    Time Complexity: O(n) - each node is processed exactly once
    Space Complexity: O(w) - where w is the maximum width of the tree (worst case O(n/2) for a complete tree)

    This function implements a level-order traversal using a queue data structure. Each level
    of the tree is processed completely before moving to the next level, incrementing the depth
    counter with each level processed.

    Args:
        bst_tree: Dictionary representing the root node of a BST

    Returns:
        The depth (height) of the tree as an integer

    Examples:
        >>> find_depth_iterative(build_balanced_bst([1, 2, 3, 4, 5]))
        3
    """

    tree_depth: int  = 0

    queue = deque([bst_tree])

    """
        Note on queue implementation:
        - Uses deque.popleft() which is O(1) time complexity
        - Standard list.pop(0) would be O(n) as it requires shifting all elements
        - For breadth-first traversal, the deque implementation provides significant
          performance benefits for large trees

    """
    while queue:
        for _ in range(len(queue)):
            current_node = queue.popleft()
            if current_node[LEFT_CHILD_KEY]:
                queue.append(current_node[LEFT_CHILD_KEY])
            if current_node[RIGHT_CHILD_KEY]:
                queue.append(current_node[RIGHT_CHILD_KEY])

        tree_depth += 1

    return tree_depth

def find_depth_recursive(bst_tree: Dict[str, Any]) -> int:
    """
      Find the depth of a binary search tree using depth-first traversal (recursive approach).

      Time Complexity: O(n) - each node is processed exactly once
      Space Complexity: O(h) - where h is the height of the tree (recursion stack)
                               Best case O(log n) for balanced tree, worst case O(n) for skewed tree

      This function uses a classic recursive approach to find tree depth. It recursively computes
      the depth of left and right subtrees, then returns the maximum of these two values plus 1.

      Args:
          bst_tree: Dictionary representing the root node of a BST, or None

      Returns:
          The depth (height) of the tree as an integer

      Examples:
          >>> find_depth_recursive(build_balanced_bst([1, 2, 3, 4, 5]))
          3
          >>> find_depth_recursive(None)
          0
      """

    # Base case: an empty subtree (None) has depth 0
    if not bst_tree:
        return 0

    # Recursive step: compute the depth of the left and right subtrees recursively
    left_subtree_depth = find_depth_recursive(bst_tree[LEFT_CHILD_KEY])
    right_subtree_depth = find_depth_recursive(bst_tree[RIGHT_CHILD_KEY])

    # Using conditional expression instead of max() to avoid
    # obfuscating the internals of the algorithm
    #
    # returns 1 (for current node) + the larger of the depths
    return (left_subtree_depth if left_subtree_depth > right_subtree_depth
            else right_subtree_depth) + 1


