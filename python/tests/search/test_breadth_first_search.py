import unittest
from search.tree.tree_breadth_first_search import bfs_simple, bfs_cycle_protection
from data_structures.TreeNode import TreeNode


class TestBreadthFirstSearch(unittest.TestCase):
    """Test cases for breadth-first search implementations."""

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

        # Tree with a cycle (for testing cycle protection)
        #       1
        #     /   \
        #    2     3
        #   / \   / \
        #  4   5 6   7
        #       |
        #       2 (cycle back to node2)
        self.cycle_tree = TreeNode(1)
        self.cycle_node2 = TreeNode(2)
        self.cycle_node3 = TreeNode(3)
        self.cycle_node4 = TreeNode(4)
        self.cycle_node5 = TreeNode(5)
        self.cycle_node6 = TreeNode(6)
        self.cycle_node7 = TreeNode(7)
        
        self.cycle_tree.add_child(self.cycle_node2)
        self.cycle_tree.add_child(self.cycle_node3)
        self.cycle_node2.add_child(self.cycle_node4)
        self.cycle_node2.add_child(self.cycle_node5)
        self.cycle_node3.add_child(self.cycle_node6)
        self.cycle_node3.add_child(self.cycle_node7)
        # Create cycle
        self.cycle_node5.add_child(self.cycle_node2)

    def test_bfs_simple_empty_tree(self):
        """Test bfs_simple with an empty tree."""
        self.assertIsNone(bfs_simple(self.empty_tree, 5))

    def test_bfs_simple_root_is_target(self):
        """Test bfs_simple when the root is the target."""
        path = bfs_simple(self.single_node, 1)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 1)
        self.assertEqual(path[0].value, 1)

    def test_bfs_simple_target_found(self):
        """Test bfs_simple when the target is in the tree."""
        # Test finding node at level 1
        path = bfs_simple(self.simple_tree, 3)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 2)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 3)

        # Test finding node at level 2
        path = bfs_simple(self.simple_tree, 5)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 2)
        self.assertEqual(path[2].value, 5)

    def test_bfs_simple_target_not_found(self):
        """Test bfs_simple when the target is not in the tree."""
        self.assertIsNone(bfs_simple(self.simple_tree, 10))

    def test_bfs_cycle_protection_empty_tree(self):
        """Test bfs_cycle_protection with an empty tree."""
        self.assertIsNone(bfs_cycle_protection(self.empty_tree, 5))

    def test_bfs_cycle_protection_root_is_target(self):
        """Test bfs_cycle_protection when the root is the target."""
        path = bfs_cycle_protection(self.single_node, 1)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 1)
        self.assertEqual(path[0].value, 1)

    def test_bfs_cycle_protection_target_found(self):
        """Test bfs_cycle_protection when the target is in the tree."""
        # Test finding node at level 1
        path = bfs_cycle_protection(self.simple_tree, 3)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 2)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 3)

        # Test finding node at level 2
        path = bfs_cycle_protection(self.simple_tree, 5)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 2)
        self.assertEqual(path[2].value, 5)

    def test_bfs_cycle_protection_target_not_found(self):
        """Test bfs_cycle_protection when the target is not in the tree."""
        self.assertIsNone(bfs_cycle_protection(self.simple_tree, 10))

    def test_bfs_cycle_protection_with_cycle(self):
        """Test bfs_cycle_protection with a tree containing a cycle."""
        # Test that cycle protection prevents infinite loop
        path = bfs_cycle_protection(self.cycle_tree, 5)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0].value, 1)
        self.assertEqual(path[1].value, 2)
        self.assertEqual(path[2].value, 5)

    def test_bfs_simple_vs_cycle_protection(self):
        """Test that both implementations return the same results for trees without cycles."""
        test_cases = [
            (self.empty_tree, 5),
            (self.single_node, 1),
            (self.simple_tree, 3),
            (self.simple_tree, 5),
            (self.simple_tree, 10)
        ]
        
        for tree, target in test_cases:
            with self.subTest(tree=tree, target=target):
                simple_result = bfs_simple(tree, target)
                cycle_result = bfs_cycle_protection(tree, target)
                
                # Check if both are None or both are not None
                self.assertEqual(simple_result is None, cycle_result is None)
                
                # If not None, check path values
                if simple_result is not None and cycle_result is not None:
                    self.assertEqual(len(simple_result), len(cycle_result))
                    for i in range(len(simple_result)):
                        self.assertEqual(simple_result[i].value, cycle_result[i].value)


if __name__ == '__main__':
    unittest.main()