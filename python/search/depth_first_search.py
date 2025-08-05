# TAGS: Tree Traversal
from typing import Optional, Tuple, List

from data_structures.TreeNode import TreeNode


def dfs_recursive(root_node: Optional[TreeNode], target: int, path: Tuple[TreeNode, ...] = ()) -> Optional[Tuple[TreeNode, ...]]:
    """
    Recursively search for a target value in a tree using depth-first search.
    
    Returns the path to the target node if found, None otherwise.
    
    Args:
        root_node: The root node to start searching from (can be None)
        target: The value to search for
        path: Current path of nodes traversed (used internally for recursion)
        
    Returns:
        Tuple containing the path to the target node if found, None otherwise
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    """
    # Base case: null node
    if root_node is None:
        return None
    
    # Add current node to path
    path += (root_node,)
    
    # Check if we found the target
    if root_node.value == target:
        return path
    
    # Recursively search children
    for child in root_node.children:
        # Skip None children to prevent errors
        if child is not None:
            found = dfs_recursive(child, target, path)
            if found:
                return found
    
    return None


def dfs_iterative(root_node: Optional[TreeNode], target: int) -> Optional[Tuple[TreeNode, List[TreeNode]]]:
    """
    Iteratively search for a target value in a tree using depth-first search.
    
    Returns the target node and remaining stack if found, None otherwise.
    
    Args:
        root_node: The root node to start searching from (can be None)
        target: The value to search for
        
    Returns:
        Tuple containing (target_node, remaining_stack) if found, None otherwise
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (stack size)
    """
    if root_node is None:
        return None
    
    stack = [root_node]
    
    while stack:
        current_node = stack.pop()
        
        if current_node.value == target:
            return current_node, stack
        
        # Add children in reverse order for left-to-right traversal
        # (stack is LIFO, so reverse order ensures leftmost child is processed first)
        for child in reversed(current_node.children):
            # Skip None children to prevent errors
            if child is not None:
                stack.append(child)
    
    return None


def dfs_recursive_return_node(root_node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """
    Recursively search for a target value and return only the target node.
    
    Alternative version that returns just the found node instead of the path.
    
    Args:
        root_node: The root node to start searching from (can be None)
        target: The value to search for
        
    Returns:
        The target node if found, None otherwise
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    """
    if root_node is None:
        return None
    
    if root_node.value == target:
        return root_node
    
    for child in root_node.children:
        if child is not None:
            found = dfs_recursive_return_node(child, target)
            if found:
                return found
    
    return None


def dfs_iterative_return_node(root_node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """
    Iteratively search for a target value and return only the target node.
    
    Alternative version that returns just the found node instead of node and stack.
    
    Args:
        root_node: The root node to start searching from (can be None)
        target: The value to search for
        
    Returns:
        The target node if found, None otherwise
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (stack size)
    """
    if root_node is None:
        return None
    
    stack = [root_node]
    
    while stack:
        current_node = stack.pop()
        
        if current_node.value == target:
            return current_node
        
        # Add children in reverse order for left-to-right traversal
        for child in reversed(current_node.children):
            if child is not None:
                stack.append(child)
    
    return None
