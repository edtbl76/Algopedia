"""
Binary Search Tree Implementation

This module provides a generic Binary Search Tree (BST) data structure that supports
any type implementing comparison operations. The BST maintains the fundamental property
that for any node:
- All values in the left subtree are less than the node's value
- All values in the right subtree are greater than or equal to the node's value

Key Features:
- Generic type support through Protocol-based typing
- Recursive insertion with duplicate handling (right-subtree placement)
- Node search functionality
- Complete traversal methods (preorder, inorder, postorder, level-order)
- Depth tracking for each node

Duplicate Strategy:
This implementation places duplicate values in the RIGHT subtree. When inserting
a value equal to the current node's value, it follows the right branch. This ensures:
- Consistent behavior for duplicate handling
- Maintains BST property (left < root ≤ right)
- Allows multiple instances of the same value
- Preserves insertion order for duplicates (first duplicate becomes parent)

Time Complexities:
- Insert: O(h) where h is height - O(log n) balanced, O(n) worst case
- Search: O(h) where h is height - O(log n) balanced, O(n) worst case
- Traversals: O(n) where n is number of nodes
Space Complexities:
- Storage: O(n) for n nodes
- Recursive operations: O(h) for call stack
"""
from collections import deque
from typing import Any, Optional, Protocol, TypeVar, Generic



# Define a protocol for comparable types
class SupportsComparison(Protocol):
    """
    Protocol defining the comparison operations required for BST elements.

    Any type used with BinarySearchTree must implement these comparison methods
    to enable proper ordering and searching within the tree structure.
    """
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...


# Type variable that's bound to the protocol
T = TypeVar("T", bound=SupportsComparison)


class BinarySearchTree(Generic[T]):
    """
    A generic Binary Search Tree implementation supporting any comparable type.

    This BST maintains the fundamental ordering property and provides standard
    tree operations including insertion, search, and various traversal methods.
    Each node tracks its depth for debugging and visualization purposes.

    Attributes:
        value: The data stored in this node
        depth: The depth level of this node (root is depth 0)
        left: Reference to left child node (contains values < self.value)
        right: Reference to right child node (contains values >= self.value)
    """

    def __init__(self, value: T, depth: int = 0):
        """
        Initialize a new BST node with the given value and depth.

        Args:
            value: The comparable value to store in this node
            depth: The depth level of this node in the tree (default: 0 for root)

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.value = value
        self.depth = depth
        self.left: Optional['BinarySearchTree[T]'] = None
        self.right: Optional['BinarySearchTree[T]'] = None



    def insert(self, value: T) -> None:
        """
        Insert a new value into the binary search tree.

        Maintains BST property by placing values < current value in left subtree
        and values >= current value in right subtree. This implementation handles
        duplicates by placing them in the RIGHT subtree, ensuring consistent behavior.

        Duplicate Strategy Details:
        - Equal values go to the right subtree
        - This maintains BST invariant (left < root <= right)
        - Preserves insertion order for duplicates
        - First duplicate becomes the parent of subsequent duplicates

        Args:
            value: The comparable value to insert into the tree

        Time Complexity: O(h) where h is the height of the tree
                        - Best/Average case: O(log n) for balanced trees
                        - Worst case: O(n) for completely unbalanced trees
        Space Complexity: O(h) due to recursive call stack

        Example:
            >>> bst = BinarySearchTree(5)
            >>> bst.insert(3)
            >>> bst.insert(7)
            >>> bst.insert(5)  # Duplicate goes to right subtree
        """
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
            else:
                self.left.insert(value)
        else:
            # Duplicate handling: place in right subtree if equal
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
            else:
                self.right.insert(value)


    def get_node_by_value(self, value: T) -> Optional['BinarySearchTree[T]']:
        """
        Search for a node with the specified value in the BST.

        Uses the BST property to efficiently navigate the tree, going left for
        smaller values and right for larger values. Returns the first node found
        with the target value (important for trees with duplicates).

        Args:
            value: The value to search for in the tree

        Returns:
            The node containing the target value, or None if not found

        Time Complexity: O(h) where h is the height of the tree
                        - Best/Average case: O(log n) for balanced trees
                        - Worst case: O(n) for completely unbalanced trees
        Space Complexity: O(h) due to recursive call stack

        Example:
            >>> bst = BinarySearchTree(5)
            >>> bst.insert(3)
            >>> node = bst.get_node_by_value(3)
            >>> print(node.value if node else "Not found")  # Outputs: 3
        """

        if value == self.value:
            # Hit! You sunk my battleship!
            return self
        elif value < self.value and self.left is not None:
            # smaller values go left
            return self.left.get_node_by_value(value)
        elif value > self.value and self.right is not None:
            # larger values go right
            return self.right.get_node_by_value(value)
        else:
            # value not found
            return None


    def traverse_preorder(self) -> None:
        """
        Perform preorder traversal: Root → Left → Right.

        Visits the current node first, then recursively visits left and right
        subtrees. Useful for creating a copy of the tree or evaluating prefix
        expressions. Prints each node's depth and value.

        Traversal Order:
        1. Process current node
        2. Traverse left subtree
        3. Traverse right subtree

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) due to recursive call stack

        Use Cases:
        - Tree serialization
        - Creating tree copies
        - Prefix expression evaluation
        """
        print(f"Depth: {self.depth}, Value: {self.value}")

        # recursive traversal of left subtree
        if self.left:
            self.left.traverse_preorder()

        # recursive traversal of right subtree
        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self) -> None:
        """
        Perform inorder traversal: Left → Root → Right.

        For BSTs, inorder traversal visits nodes in sorted ascending order,
        making it ideal for retrieving data in sorted sequence. This is the
        most commonly used traversal for BSTs when sorted output is needed.

        Traversal Order:
        1. Traverse left subtree
        2. Process current node
        3. Traverse right subtree

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) due to recursive call stack

        Use Cases:
        - Getting sorted output from BST
        - Validating BST property
        - Range queries in sorted order

        Note: For BSTs, this traversal produces values in sorted order
        """

        # Left subtree traversal
        if self.left:
            self.left.traverse_inorder()

        # Current node traversal
        print(f"Depth: {self.depth}, Value: {self.value}")

        # Right subtree traversal
        if self.right:
            self.right.traverse_inorder()


    def traverse_postorder(self) -> None:
        """
        Perform postorder traversal: Left → Right → Root.

        Visits children before processing the current node. Useful for operations
        that need to process children before parents, such as calculating tree
        heights, deleting trees, or evaluating postfix expressions.

        Traversal Order:
        1. Traverse left subtree
        2. Traverse right subtree
        3. Process current node

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) due to recursive call stack

        Use Cases:
        - Tree deletion (delete children before parent)
        - Calculating tree properties (height, size)
        - Postfix expression evaluation
        - Memory cleanup operations
        """

        # Recursively traverse left subtree first
        if self.left:
            self.left.traverse_postorder()

        # Recursively traverse right subtree
        if self.right:
            self.right.traverse_postorder()

        # Current node last!
        print(f"Depth: {self.depth}, Value: {self.value}")


    def traverse_levelorder(self) -> None:
        """
        Perform level-order (breadth-first) traversal using a queue.

        Visits nodes level by level from left to right, starting from the root.
        This traversal provides a "breadth-first" view of the tree and is useful
        for finding shortest paths or processing nodes by their distance from root.

        Algorithm:
        1. Initialize queue with root node
        2. While queue is not empty:
           - Dequeue a node and process it
           - Enqueue its left child (if exists)
           - Enqueue its right child (if exists)

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree
                         - Best case: O(1) for completely unbalanced tree
                         - Worst case: O(n/2) ≈ O(n) for complete binary tree

        Use Cases:
        - Finding nodes at specific levels
        - Serializing tree level by level
        - Finding shortest path between nodes
        - Tree visualization by levels

        Note: Uses deque for efficient O(1) append/popleft operations
        """

        # Initialize queue with root node
        queue = deque([self])

        # Continue until all nodes are processed
        while queue:

            # remove and process current node (FIFO)
            current = queue.popleft()
            print(current.value)

            # add left child for future processing
            if current.left:
                queue.append(current.left)

            # add right child for future processing
            if current.right:
                queue.append(current.right)



