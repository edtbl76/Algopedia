import unittest
from io import StringIO
import sys
from enum import Enum
from data_structures.TreeNode import TreeNode, TraversalType

class TestTreeNode(unittest.TestCase):
    def test_init(self):
        """Test TreeNode initialization"""
        # Test with default value
        node = TreeNode()
        self.assertEqual(node.value, 0)
        self.assertEqual(node.children, [])

        # Test with custom value
        node = TreeNode(5)
        self.assertEqual(node.value, 5)
        self.assertEqual(node.children, [])

        # Test with string value
        node = TreeNode("test")
        self.assertEqual(node.value, "test")
        self.assertEqual(node.children, [])

    def test_add_child(self):
        """Test add_child method"""
        # Create parent and child nodes
        parent = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)

        # Add first child
        parent.add_child(child1)
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0], child1)

        # Add second child
        parent.add_child(child2)
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0], child1)
        self.assertEqual(parent.children[1], child2)

        # Test adding None child (should be ignored)
        parent.add_child(None)
        self.assertEqual(len(parent.children), 2)  # Count should remain the same

    def test_remove_child(self):
        """Test remove_child method"""
        # Create parent and child nodes
        parent = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        child3 = TreeNode(4)

        # Add children
        parent.add_child(child1)
        parent.add_child(child2)
        parent.add_child(child3)
        self.assertEqual(len(parent.children), 3)

        # Remove middle child
        parent.remove_child(child2)
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0], child1)
        self.assertEqual(parent.children[1], child3)

        # Remove non-existent child (should do nothing)
        non_child = TreeNode(5)
        parent.remove_child(non_child)
        self.assertEqual(len(parent.children), 2)

        # Remove None child (should do nothing)
        parent.remove_child(None)
        self.assertEqual(len(parent.children), 2)

        # Test removing duplicate children
        parent = TreeNode(1)
        child = TreeNode(2)
        parent.add_child(child)
        parent.add_child(child)  # Add same child twice
        self.assertEqual(len(parent.children), 2)

        parent.remove_child(child)
        self.assertEqual(len(parent.children), 0)  # All instances should be removed

    def test_default_visitor(self):
        """Test _default_visitor method"""
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Create node and call default visitor
        node = TreeNode("test_value")
        TreeNode._default_visitor(node)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check that the value was printed
        self.assertEqual(captured_output.getvalue().strip(), "test_value")

    def test_traverse_preorder(self):
        """Test traverse method with PREORDER traversal"""
        # Create a simple tree
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        # Create a list to store visited values
        visited = []

        # Define visitor function
        def visitor(node):
            visited.append(node.value)

        # Traverse with PREORDER
        root.traverse(TraversalType.PREORDER, visitor)

        # Expected order: root, child1, grandchild1, grandchild2, child2
        self.assertEqual(visited, [1, 2, 4, 5, 3])

    def test_traverse_preorder_iterative(self):
        """Test traverse method with PREORDER_ITERATIVE traversal"""
        # Create a simple tree
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        # Create a list to store visited values
        visited = []

        # Define visitor function
        def visitor(node):
            visited.append(node.value)

        # Traverse with PREORDER_ITERATIVE
        root.traverse(TraversalType.PREORDER_ITERATIVE, visitor)

        # Expected order: root, child1, grandchild1, grandchild2, child2
        self.assertEqual(visited, [1, 2, 4, 5, 3])

    def test_traverse_preorder_recursive(self):
        """Test traverse method with PREORDER_RECURSIVE traversal"""
        # Create a simple tree
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        # Create a list to store visited values
        visited = []

        # Define visitor function
        def visitor(node):
            visited.append(node.value)

        # Traverse with PREORDER_RECURSIVE
        root.traverse(TraversalType.PREORDER_RECURSIVE, visitor)

        # The recursive implementation traverses children in reverse order
        # Expected order: root, child2, child1, grandchild2, grandchild1
        self.assertEqual(visited, [1, 3, 2, 5, 4])

    def test_traverse_inorder(self):
        """Test traverse method with INORDER traversal"""
        # Create a simple tree
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        # Create a list to store visited values
        visited = []

        # Define visitor function
        def visitor(node):
            visited.append(node.value)

        # Traverse with INORDER
        root.traverse(TraversalType.INORDER, visitor)

        # For n-ary trees, inorder traversal visits left half of children, 
        # then root, then right half of children
        # Expected order: grandchild1, child1, grandchild2, root, child2
        self.assertEqual(visited, [4, 2, 5, 1, 3])

    def test_traverse_postorder(self):
        """Test traverse method with POSTORDER traversal"""
        # Create a simple tree
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        # Create a list to store visited values
        visited = []

        # Define visitor function
        def visitor(node):
            visited.append(node.value)

        # Traverse with POSTORDER
        root.traverse(TraversalType.POSTORDER, visitor)

        # Expected order: grandchild1, grandchild2, child1, child2, root
        self.assertEqual(visited, [4, 5, 2, 3, 1])

    def test_traverse_default_visitor(self):
        """Test traverse method with default visitor"""
        # Create a simple tree
        root = TreeNode(1)
        child = TreeNode(2)
        root.add_child(child)

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Traverse with default visitor
        root.traverse()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check that the values were printed (preorder: root, child)
        self.assertEqual(captured_output.getvalue().strip(), "1\n2")

    def test_traverse_invalid_type(self):
        """Test traverse method with invalid traversal type"""
        # Create a node
        node = TreeNode(1)

        # Define a custom traversal type that's not implemented
        class CustomTraversalType(Enum):
            CUSTOM = "custom"

            def traverse(self, root, visitor):
                raise ValueError(f"Unknown traversal type: {self}")

        # Try to traverse with invalid type
        with self.assertRaises(ValueError):
            node.traverse(CustomTraversalType.CUSTOM)

    def test_print_tree(self):
        """Test print_tree method"""
        # Create a simple tree
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Print the tree
        root.print_tree()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Expected output
        expected_output = "└── 1\n    ├── 2\n    │   ├── 4\n    │   └── 5\n    └── 3"

        # Check that the tree was printed correctly
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_print_path(self):
        """Test print_path method"""
        # Create nodes
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)

        # Test with a valid path
        path = [node1, node2, node3]

        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Print the path
        TreeNode.print_path(path)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check that the path was printed correctly
        self.assertEqual(captured_output.getvalue().strip(), "Path: 1 -> 2 -> 3")

        # Test with a valid path and custom separator
        captured_output = StringIO()
        sys.stdout = captured_output

        TreeNode.print_path(path, separator=" => ")

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "Path: 1 => 2 => 3")

        # Test with a valid path and show_indices=True
        captured_output = StringIO()
        sys.stdout = captured_output

        TreeNode.print_path(path, show_indices=True)

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "Path: [0] 1 -> [1] 2 -> [2] 3")

        # Test with None path
        captured_output = StringIO()
        sys.stdout = captured_output

        TreeNode.print_path(None)

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "No path found")

        # Test with empty path
        captured_output = StringIO()
        sys.stdout = captured_output

        TreeNode.print_path([])

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "Empty path")

if __name__ == '__main__':
    unittest.main()
