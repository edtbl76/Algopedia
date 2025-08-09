import unittest
from search.tree_depth_first_search import dfs_recursive, dfs_iterative, dfs_recursive_return_node, dfs_iterative_return_node
from data_structures.TreeNode import TreeNode


class TestDepthFirstSearch(unittest.TestCase):
    """Test cases for depth-first search implementations."""

    def setUp(self):
        """Set up common test data."""
        # Empty tree
        self.empty_tree = None

        # Single node tree
        self.single_node = TreeNode(1)

        # Simple tree with no cycles
        #       1
        #     /   \
        #    2     3
        #   / \   / \
        #  4   5 6   7
        self.simple_tree = TreeNode(1)
        self.node2 = TreeNode(2)
        self.node3 = TreeNode(3)
        self.node4 = TreeNode(4)
        self.node5 = TreeNode(5)
        self.node6 = TreeNode(6)
        self.node7 = TreeNode(7)
        
        self.simple_tree.add_child(self.node2)
        self.simple_tree.add_child(self.node3)
        self.node2.add_child(self.node4)
        self.node2.add_child(self.node5)
        self.node3.add_child(self.node6)
        self.node3.add_child(self.node7)

    def test_dfs_recursive_empty_tree(self):
        """Test dfs_recursive with an empty tree."""
        self.assertIsNone(dfs_recursive(self.empty_tree, 5))

    def test_dfs_recursive_root_is_target(self):
        """Test dfs_recursive when the root is the target."""
        path = dfs_recursive(self.single_node, 1)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 1)
        self.assertEqual(path[0].value, 1)

    def test_dfs_recursive_target_found(self):
        """Test dfs_recursive when the target is in the tree."""
        # Test finding node at level 1
        path = dfs_recursive(self.simple_tree, 3)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 2)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 3)

        # Test finding node at level 2
        path = dfs_recursive(self.simple_tree, 5)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 2)
        self.assertEqual(path[2].value, 5)

    def test_dfs_recursive_target_not_found(self):
        """Test dfs_recursive when the target is not in the tree."""
        self.assertIsNone(dfs_recursive(self.simple_tree, 10))

    def test_dfs_iterative_empty_tree(self):
        """Test dfs_iterative with an empty tree."""
        self.assertIsNone(dfs_iterative(self.empty_tree, 5))

    def test_dfs_iterative_root_is_target(self):
        """Test dfs_iterative when the root is the target."""
        result = dfs_iterative(self.single_node, 1)
        self.assertIsNotNone(result)
        node, stack = result
        self.assertEqual(node.value, 1)
        self.assertEqual(len(stack), 0)

    def test_dfs_iterative_target_found(self):
        """Test dfs_iterative when the target is in the tree."""
        # Test finding node at level 1
        result = dfs_iterative(self.simple_tree, 3)
        self.assertIsNotNone(result)
        node, stack = result
        self.assertEqual(node.value, 3)
        
        # Test finding node at level 2
        result = dfs_iterative(self.simple_tree, 5)
        self.assertIsNotNone(result)
        node, stack = result
        self.assertEqual(node.value, 5)

    def test_dfs_iterative_target_not_found(self):
        """Test dfs_iterative when the target is not in the tree."""
        self.assertIsNone(dfs_iterative(self.simple_tree, 10))

    def test_dfs_recursive_return_node_empty_tree(self):
        """Test dfs_recursive_return_node with an empty tree."""
        self.assertIsNone(dfs_recursive_return_node(self.empty_tree, 5))

    def test_dfs_recursive_return_node_root_is_target(self):
        """Test dfs_recursive_return_node when the root is the target."""
        node = dfs_recursive_return_node(self.single_node, 1)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 1)

    def test_dfs_recursive_return_node_target_found(self):
        """Test dfs_recursive_return_node when the target is in the tree."""
        # Test finding node at level 1
        node = dfs_recursive_return_node(self.simple_tree, 3)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 3)
        
        # Test finding node at level 2
        node = dfs_recursive_return_node(self.simple_tree, 5)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 5)

    def test_dfs_recursive_return_node_target_not_found(self):
        """Test dfs_recursive_return_node when the target is not in the tree."""
        self.assertIsNone(dfs_recursive_return_node(self.simple_tree, 10))

    def test_dfs_iterative_return_node_empty_tree(self):
        """Test dfs_iterative_return_node with an empty tree."""
        self.assertIsNone(dfs_iterative_return_node(self.empty_tree, 5))

    def test_dfs_iterative_return_node_root_is_target(self):
        """Test dfs_iterative_return_node when the root is the target."""
        node = dfs_iterative_return_node(self.single_node, 1)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 1)

    def test_dfs_iterative_return_node_target_found(self):
        """Test dfs_iterative_return_node when the target is in the tree."""
        # Test finding node at level 1
        node = dfs_iterative_return_node(self.simple_tree, 3)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 3)
        
        # Test finding node at level 2
        node = dfs_iterative_return_node(self.simple_tree, 5)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 5)

    def test_dfs_iterative_return_node_target_not_found(self):
        """Test dfs_iterative_return_node when the target is not in the tree."""
        self.assertIsNone(dfs_iterative_return_node(self.simple_tree, 10))

    def test_dfs_traversal_order(self):
        """Test that DFS traverses in depth-first order."""
        # Create a tree where DFS and BFS would produce different paths
        #       1
        #     /   \
        #    2     3
        #   /     / \
        #  4     5   6
        #       /
        #      7
        tree = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        
        tree.add_child(node2)
        tree.add_child(node3)
        node2.add_child(node4)
        node3.add_child(node5)
        node3.add_child(node6)
        node5.add_child(node7)
        
        # Test recursive DFS - should go deep before wide
        path = dfs_recursive(tree, 7)
        self.assertIsNotNone(path)
        # In DFS, we should find node 7 by going through node 3 and node 5
        self.assertEqual(len(path), 4)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 3)  # DFS will go to node 3 after node 2 is fully explored
        self.assertEqual(path[2].value, 5)
        self.assertEqual(path[3].value, 7)
        
        # Test iterative DFS - should also go deep before wide
        result = dfs_iterative(tree, 7)
        self.assertIsNotNone(result)
        node, _ = result
        self.assertEqual(node.value, 7)


if __name__ == '__main__':
    unittest.main()