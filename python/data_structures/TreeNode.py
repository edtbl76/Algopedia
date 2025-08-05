from enum import Enum
from typing import Any, Optional, List, Callable

"""
=== Tree Data Structure Implementation ===

This module provides a generic tree data structure implementation with various
traversal algorithms. It includes:

- TreeNode: A generic n-ary tree node implementation
- TraversalType: An enumeration of different tree traversal algorithms

The implementation supports trees with arbitrary branching factors and provides
both iterative and recursive traversal methods with different time and space
complexities.

Classes:
    TreeNode: Generic tree node with value and children
    TraversalType: Enumeration of traversal algorithms with implementations

Time Complexities:
    - Tree operations: O(1) to O(n) depending on operation
    - Traversals: O(n) where n is the number of nodes

Space Complexities:
    - Node storage: O(n) for tree structure
    - Traversal: O(h) to O(n) depending on method (h = height)



=== Visitor Pattern Implementation ===

This module provides a generic visitor pattern implementation for traversing
trees with different traversal algorithms. 

It is a fundamental design pattern that separates the traversal logic from the action performed on each node (visitor). 
This allows for different algorithms to be used interchangeably without modifying the traversal code.

Instead of hardcoding the traversal logic in the visitor function, the visitor pattern allows for different algorithms
 to be used interchangeably by passing in a function pointer / first-order function that defines the action to be 
 performed on each node. 
 
 Why? 
 - Separation of concerns (traversal logic separate from action) 
 - flexibility (different traversal algorithms can be used interchangeably) 
 - extensibility (new traversal algorithms can be added easily)
 - reduces code duplication (same traversal logic can be used across different tree structures)
 - embraces functional programming (visitor pattern is a functional programming paradigm) 
"""


class TraversalType(Enum):
    """
    Enumeration of tree traversal algorithms.

    This enum provides different methods for traversing tree structures,
    each with specific ordering and implementation characteristics.

    Traversal Types:
        PREORDER: Visit node, then children (iterative implementation)
        PREORDER_ITERATIVE: Explicit iterative preorder traversal
        PREORDER_RECURSIVE: Recursive preorder traversal
        INORDER: Left subtree, node, right subtree
        POSTORDER: Children first, then node
        BREADTH_FIRST: Level-by-level traversal
        DEPTH_FIRST: Deep exploration before backtracking

    Time Complexity: O(n) for all traversal methods
    Space Complexity:
        - Iterative: O(h) where h is tree height
        - Recursive: O(h) due to call stack
    """

    PREORDER = "preorder"
    PREORDER_ITERATIVE = "preorder_iterative"
    PREORDER_RECURSIVE = "preorder_recursive"
    INORDER = "inorder"
    POSTORDER = "postorder"
    BREADTH_FIRST = "breadth_first"
    DEPTH_FIRST = "depth_first"

    def traverse(self, root: 'TreeNode', visitor: Callable[['TreeNode'], None]) -> None:
        """
          Execute the traversal algorithm on the given tree.

          Dispatches to the appropriate traversal implementation based on the
          enum value. Currently only preorder traversals are implemented.

          Args:
              root: The root node of the tree to traverse
              visitor: Function to call on each visited node

          Time Complexity: O(n) where n is number of nodes
          Space Complexity: O(h) where h is tree height
        """

        if self == TraversalType.PREORDER:
            self._preorder_iterative(root, visitor)
        elif self == TraversalType.PREORDER_ITERATIVE:
            self._preorder_iterative(root, visitor)
        elif self == TraversalType.PREORDER_RECURSIVE:
            self._preorder_recursive(root, visitor)
        elif self == TraversalType.INORDER:
            self._inorder_nary(root, visitor)
        elif self == TraversalType.POSTORDER:
            self._postorder_nary(root, visitor)
        else:
            raise ValueError(f"Unknown traversal type: {self}")

    @staticmethod
    def _preorder_iterative(root: 'TreeNode', visitor: Callable[['TreeNode'], None]) -> None:
        """
        Iterative preorder traversal using an explicit stack.

        Visits nodes in order: root -> left subtree -> right subtree
        Uses a stack to simulate the call stack of recursive traversal.

        Algorithm:
        1. Push root onto stack
        2. While stack is not empty:
           a. Pop node from stack
           b. Visit the node
           c. Push children in reverse order (rightmost first)

        Args:
            root: Starting node for traversal
            visitor: Function to apply to each visited node

        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) - stack size proportional to tree height
                         Worst case O(n) for completely unbalanced tree
        """
        # Base case: empty tree
        if root is None:
            return

        # Initialize stack w/ root node
        nodestack = [root]

        # Process nodes until stack is empty
        while nodestack:

            # Pop next node to process
            current_node = nodestack.pop()

            # visit current node (means to process its value)
            visitor(current_node)

            # Add children in reverse order to maintain left-to-right traversal
            # Stack is LIFO, so reverse order ensures that the left children are processed first.
            # (i.e. the elements in the children list are appended from the end of the list onto the stack
            # ensuring that the left / lower-index elements end up on top of the right / higher-index elements)
            nodestack.extend(reversed(current_node.children))

    def _preorder_recursive(self, root: 'TreeNode', visitor: Callable[['TreeNode'], None]) -> None:
        """
        Recursive preorder traversal implementation.

        Visits nodes in order: root -> children (left to right)
        Uses the system call stack for traversal state management.

        Algorithm:
        1. Visit current node
        2. Recursively traverse each child in reverse order
           (reverse order maintains left-to-right processing)

        Args:
            root: Current node in the traversal
            visitor: Function to apply to each visited node

        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) - call stack depth equals tree height
                         Worst case O(n) for completely unbalanced tree
        """
        # Base case: null node, stop recursion
        if root is None:
            return

        # visit the current node (means to process its value)
        visitor(root)

        # Recursively traverse children in reverse order
        # Reverse order ensures left-to-right traversal when children are processed
        for child in reversed(root.children):
            self._preorder_recursive(child, visitor)


    def _inorder_nary(self, root: 'TreeNode', visitor: Callable[['TreeNode'], None]) -> None:
        """
        Recursive inorder traversal implementation for n-ary trees.

        Performs inorder traversal on n-ary trees by dividing children into left and right
        groups around a midpoint, visiting left children first, then the root, then right
        children. This generalizes the binary tree inorder concept to n-ary trees.

        Algorithm:
        1. Return immediately if root is None (base case)
        2. Calculate midpoint to divide children into left/right groups
        3. Recursively traverse left half of children (indices 0 to midpoint-1)
        4. Visit the current root node
        5. Recursively traverse right half of children (indices midpoint to end)

        For n-ary trees with odd number of children, the middle child goes to the right group.
        For even number of children, children are split evenly between left and right groups.

        As you can see, this works very similar to the binary tree inorder traversal,
        except that the midpoint is calculated differently. This allows the algorithm
        to work with any number of children, not just 2.

        Args:
            root: Current node in the traversal (None for empty subtree)
            visitor: Function to apply to each visited node

        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) - call stack depth equals tree height
                         Worst case O(n) for completely unbalanced tree
        """
        # Base case: empty subtree, terminate recursion
        if root is None:
            return

        # Calculate midpoint to divide children into left and right groups
        # For odd number of children, middle child goes to right group
        midpoint = len(root.children) // 2

        # Traverse left half of children (0, midpoint - 1)
        # This is the "left subtree" equivalent in n-ary inorder traversal
        for i in range(midpoint):
            self._inorder_nary(root.children[i], visitor)

        # Visit current root node
        visitor(root)

        # Traverse right half of children (midpoint, -1)
        # This is the "right-subtree"
        for i in range(midpoint, len(root.children)):
            self._inorder_nary(root.children[i], visitor)

    def _postorder_nary(self, root: 'TreeNode', visitor: Callable[['TreeNode'], None]) -> None:
        """
        Recursive postorder traversal implementation for n-ary trees.

        Performs postorder traversal by visiting all children first (left to right),
        then visiting the root node last. This ensures that a node is processed only
        after all of its descendants have been processed.

        Algorithm:
        1. Return immediately if root is None (base case)
        2. Recursively traverse all children in left-to-right order
        3. Visit the current root node (after all children are processed)

        This traversal is useful for operations that need to process child nodes
        before their parent (e.g., calculating directory sizes, deleting nodes).

        Args:
            root: Current node in the traversal (None for empty subtree)
            visitor: Function to apply to each visited node

        Time Complexity: O(n) - visits each node exactly once
        Space Complexity: O(h) - call stack depth equals tree height
                         Worst case O(n) for completely unbalanced tree
        """
        # Base case: empty subtree, terminate recursion
        if root is None:
            return

        # Recursively traverse all children first (left to right)
        # Process all descendants before processing the current node
        for child in root.children:
            self._postorder_nary(child, visitor)

        # Visit the current root node last (after all children are processed)
        # This is the key characteristic of postorder traversal
        visitor(root)

class TreeNode:
    """
    Generic n-ary tree node implementation.

    A tree node that can hold any value and maintain a list of child nodes.
    Supports dynamic addition/removal of children and various traversal methods.

    Structure:
        - Each node contains a value of any type
        - Children are stored in a list (ordered)
        - No parent references (single-direction tree)
        - No limit on number of children (n-ary tree)

    Attributes:
        value: The data stored in this node
        children: List of child TreeNode objects

    Time Complexities:
        - Node creation: O(1)
        - Add child: O(1)
        - Remove child: O(k) where k is number of children
        - Traversal: O(n) where n is total nodes in subtree

    Space Complexity: O(n) for storing n nodes in the tree
    """

    def __init__(self, value: Any = 0) -> None:
        self.value = value
        self.children: List['TreeNode'] = []

    def add_child(self, child_node: Optional['TreeNode']) -> None:
        """
        Add a child node to this node's children list.

        Appends the child to the end of the children list, maintaining
        insertion order. Ignores None values to prevent invalid tree states.

        Args:
            child_node: The TreeNode to add as a child (None values ignored)

        Time Complexity: O(1) - list append operation
        Space Complexity: O(1) - no additional space beyond the reference
        """
        # Only add non-None children to maintain tree integrity
        if child_node is not None:
            self.children.append(child_node)
        
    def remove_child(self, child_node: Optional['TreeNode']) -> None:
        """
        Remove a child node from this node's children list.

        Removes ALL instances of the specified child node using identity
        comparison (is operator). Creates a new list without the target child.

        Args:
            child_node: The TreeNode to remove (None values ignored)

        Time Complexity: O(k) where k is number of children
                        (list comprehension iterates through all children)
        Space Complexity: O(k) - creates new list of remaining children
        """
        # Check for valid child and ensure it exists in children list
        if child_node is not None and child_node in self.children:
            # Create new list excluding all instances of child_node
            # Uses identity comparison (is) to ensure exact object match
            self.children = [child for child in self.children
                     if child is not child_node]


    def traverse(self, traversal_type: TraversalType = TraversalType.PREORDER,
                 visitor: Callable[['TreeNode'], None] = None) -> None:
        """
        Traverse this node's subtree using the specified algorithm.

        Convenience method that delegates to the TraversalType enum for
        the actual traversal implementation. Uses default visitor if none provided.

        Args:
            traversal_type: The traversal algorithm to use (default: PREORDER)
            visitor: Function to call on each node (default: print node value)

        Time Complexity: O(n) where n is nodes in subtree
        Space Complexity: O(h) where h is subtree height
        """
        if visitor is None:
            visitor = self._default_visitor

        # Delegate to the traversal type's implementation
        traversal_type.traverse(self, visitor)


    @staticmethod
    def _default_visitor(node: 'TreeNode') -> None:
        """
        Default visitor function that prints the node's value.

        Used when no custom visitor is provided to traverse method.
        Simple implementation for debugging and demonstration purposes.

        Args:
            node: The TreeNode being visited

        Time Complexity: O(1) - single print operation
        Space Complexity: O(1) - no additional memory used
        """
        print(node.value)

    def print_tree(self, prefix: str = "", is_last: bool = True) -> None:
        """
        Print a visual representation of the tree structure.

        Uses ASCII characters to create a tree-like visualization with proper
        indentation and connecting lines. This method recursively prints the
        entire subtree rooted at this node.

        Args:
            prefix: String prefix for current line (used internally for recursion)
            is_last: Whether this node is the last child of its parent

        Time Complexity: O(n) where n is the number of nodes in the subtree
        Space Complexity: O(h) where h is the height of the tree (recursion stack)

        Example output:
            1
            ├── 2
            │   ├── 4
            │   └── 5
            └── 3
                └── 6
        """
        # Print current node with appropriate connector
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{self.value}")

        # Calculate prefix for children
        child_prefix = prefix + ("    " if is_last else "│   ")

        # Print all children except the last one
        for i, child in enumerate(self.children[:-1]):
            if child is not None:
                child.print_tree(child_prefix, False)

        # Print the last child (if any exist)
        if self.children:
            last_child = self.children[-1]
            if last_child is not None:
                last_child.print_tree(child_prefix, True)

    @staticmethod
    def print_path(path: Optional[List['TreeNode']],
                   separator: str = " -> ",
                   show_indices: bool = False) -> None:
        """
        Print a formatted representation of a path through the tree.

        Takes a list of TreeNode objects (typically from a search result)
        and prints them in a readable format showing the traversal path.

        Args:
            path: List of TreeNode objects representing a path (None for no path)
            separator: String to separate node values in output (default: " -> ")
            show_indices: Whether to show the index of each node in the path

        Time Complexity: O(p) where p is the length of the path
        Space Complexity: O(1) - only uses temporary variables

        Examples:
            >>> TreeNode.print_path([node1, node2, node3])
            Path: 1 -> 2 -> 3

            >>> TreeNode.print_path([node1, node2, node3], show_indices=True)
            Path: [0] 1 -> [1] 2 -> [2] 3

            >>> TreeNode.print_path(None)
            No path found
        """
        if path is None:
            print("No path found")
            return

        if not path:
            print("Empty path")
            return

        # Build the path string
        if show_indices:
            path_elements = [f"[{i}] {node.value}" for i, node in enumerate(path)]
        else:
            path_elements = [str(node.value) for node in path]

        path_string = separator.join(path_elements)
        print(f"Path: {path_string}")

