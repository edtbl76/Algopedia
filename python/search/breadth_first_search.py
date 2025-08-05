# TAGS: Tree Traversal
from collections import deque
from typing import List, Optional, Dict

from data_structures.TreeNode import TreeNode


def bfs_simple(root_node: Optional[TreeNode], target: int) -> Optional[List[TreeNode]]:
    """
    Simplified BFS implementation without cycle protection.

    Use this version when you're certain the tree structure is valid
    and contains no cycles. This is more memory efficient for guaranteed trees.

    Args:
        root_node: The root node to start searching from
        target: The target value to search for

    Returns:
        List of TreeNode objects representing the path from root to target,
        or None if target is not found

    Time Complexity: O(n) where n is the total number of nodes in the tree
                    (each node is visited at most once)

    Space Complexity: O(w + d) where w is the maximum width of the tree at any level
                     and d is the depth of the target node:
                     - O(w) for the frontier queue (stores nodes at current level)
                     - O(n) for the parent_map (stores mapping for all visited nodes)
                     - Overall: O(n) in worst case
    """
    # Base case: empty tree - O(1)
    if root_node is None:
        return None

    # Initialize BFS data structures - O(1)
    #
    # - frontier is the queue for level-order traversal
    # - parent-map is to track parent relationships
    frontier = deque([root_node])
    parent_map: Dict[int, Optional[TreeNode]] = {id(root_node): None}

    # Process nodes level by level - O(n) overall
    while frontier:
        # O(1) deque operation
        current_node = frontier.popleft()

        # O(1) check if target is found.
        if current_node.value == target:
            # O(d) where d = tree depth
            return _reconstruct_path(current_node, parent_map)

        # Add all children to frontier for next level - O(c) where c is number of children
        if hasattr(current_node, 'children') and current_node.children:
            for child in current_node.children:
                if child is not None:
                    frontier.append(child)
                    parent_map[id(child)] = current_node

    # Target not found after exploring all nodes
    return None


def bfs_cycle_protection(root_node: Optional[TreeNode], target: int) -> Optional[List[TreeNode]]:
    """
    Perform breadth-first search to find a path from root to target value.

    This function implements an optimized BFS algorithm using a queue to maintain
    nodes and a parent mapping for efficient path reconstruction. It explores the
    tree level by level, ensuring the shortest path is found in terms of number of edges.

    Algorithm:
    1. Initialize a queue with the root node and a parent mapping
    2. While the queue is not empty:
       a. Dequeue the next node to explore
       b. Check if the node contains the target value
       c. If found, reconstruct and return the complete path to target
       d. Otherwise, enqueue all unvisited children with parent tracking
    3. If queue becomes empty without finding target, return None

    The algorithm uses parent mapping instead of storing complete paths to optimize
    memory usage and improve performance.

    Args:
        root_node: The root node to start searching from (can be None)
        target: The target value to search for

    Returns:
        List of TreeNode objects representing the path from root to target,
        or None if target is not found in the tree

    Time Complexity: O(V + E) where V is number of nodes and E is number of edges
                    In trees: O(n) where n is total number of nodes
                    (each node and edge is processed at most once)

    Space Complexity: O(n) where n is the number of nodes:
                     - O(w) for frontier queue where w is maximum tree width
                     - O(n) for visited set (tracks all processed nodes)
                     - O(n) for parent mapping (stores relationships for all nodes)
                     - Overall: O(n) dominated by visited set and parent map

    Examples:
        >>> root = TreeNode(1)
        >>> root.add_child(TreeNode(2))
        >>> root.add_child(TreeNode(3))
        >>> path = bfs(root, 3)
        >>> [node.value for node in path] if path else None
        [1, 3]
    """

    # Base case: empty tree - O(1)
    if root_node is None:
        return None

    # Early termination: root is target - O(1)
    if root_node.value == target:
        return [root_node]


    # Initialize BFS data structures - O(1)
    #
    # - frontier queue for level-order traversal
    # - visited is to track visited nodes by id to prevent cycle - O(1) per lookup/insert
    # - parent mapping is used for path reconstruction.
    frontier = deque([root_node])
    visited = set() # Track visited nodes by id to prevent cycles
    parent_map: Dict[int, Optional[TreeNode]] = {id(root_node): None}


    # Main BFS loop - processes each node exactly once - O(n) overall
    while frontier:
        current_node = frontier.popleft()
        current_id = id(current_node)

        # Cycle protection: skip already processed nodes - O(1) set lookup
        if current_id in visited:
            continue
        # O(1) set insertion
        visited.add(current_id)


        # O(1) check if target is found.
        if current_node.value == target:
            # O(d) where d = tree depth
            return _reconstruct_path(current_node, parent_map)


        # Explore children: add unvisited children to frontier - O(c) where c is number of children
        if hasattr(current_node, 'children') and current_node.children:
            for child in current_node.children:
                # Skip leaves (No kids!)
                if child is not None:
                    child_id = id(child)

                    # Only process unvisited children to avoid cycles - O(1) set lookup
                    if child_id not in visited:
                        frontier.append(child)
                        parent_map[child_id] = current_node


    # Target not found after exploring all reachable nodes
    return None


def _reconstruct_path(target_node: TreeNode, parent_map: Dict[int, Optional[TreeNode]]) -> List[TreeNode]:
    """
    Reconstruct the path from root to target using the parent mapping.

    This helper function builds the path by following parent pointers from
    the target node back to the root, then reverses the result to get the
    correct root-to-target ordering.

    Args:
        target_node: The node where the target was found
        parent_map: Mapping from node id to parent node

    Returns:
        List of TreeNode objects representing the path from root to target

    Time Complexity: O(d) where d is the depth of the target node
                    (follows parent chain from target to root, then reverses)
                    - Path construction: O(d)
                    - List reversal: O(d)
                    - Overall: O(d)

    Space Complexity: O(d) for storing the path list
                     (path length equals depth of target node)
    """
    path = []
    current = target_node

    # Build path from target back to root - O(d) where d is depth
    while current is not None:
        path.append(current)  # O(1) list append
        current = parent_map.get(id(current))  # O(1) dict lookup

    # Reverse to get path from root to target - O(d)
    path.reverse()
    return path

