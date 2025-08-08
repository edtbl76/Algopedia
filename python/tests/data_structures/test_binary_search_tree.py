import unittest
from unittest.mock import patch
import io
from data_structures.BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    """
    Test cases for the BinarySearchTree class implementation.
    
    These tests verify the functionality of the BinarySearchTree class including:
    - Initialization
    - Insertion
    - Search
    - Traversal methods
    - Edge cases
    """

    def test_initialization(self):
        """Test initialization of a BST with a value"""
        bst = BinarySearchTree(10)
        self.assertEqual(bst.value, 10)
        self.assertEqual(bst.depth, 0)
        self.assertIsNone(bst.left)
        self.assertIsNone(bst.right)

    def test_initialization_with_depth(self):
        """Test initialization of a BST with a value and specific depth"""
        bst = BinarySearchTree(10, 2)
        self.assertEqual(bst.value, 10)
        self.assertEqual(bst.depth, 2)
        self.assertIsNone(bst.left)
        self.assertIsNone(bst.right)

    def test_insert_less_than(self):
        """Test inserting a value less than the root"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        self.assertIsNotNone(bst.left)
        self.assertEqual(bst.left.value, 5)
        self.assertEqual(bst.left.depth, 1)
        self.assertIsNone(bst.right)

    def test_insert_greater_than(self):
        """Test inserting a value greater than the root"""
        bst = BinarySearchTree(10)
        bst.insert(15)
        self.assertIsNotNone(bst.right)
        self.assertEqual(bst.right.value, 15)
        self.assertEqual(bst.right.depth, 1)
        self.assertIsNone(bst.left)

    def test_insert_equal(self):
        """Test inserting a value equal to the root (should go right)"""
        bst = BinarySearchTree(10)
        bst.insert(10)
        self.assertIsNotNone(bst.right)
        self.assertEqual(bst.right.value, 10)
        self.assertEqual(bst.right.depth, 1)
        self.assertIsNone(bst.left)

    def test_insert_multiple_levels(self):
        """Test inserting multiple values creating a multi-level tree"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(17)
        
        # Check left subtree
        self.assertEqual(bst.left.value, 5)
        self.assertEqual(bst.left.left.value, 3)
        self.assertEqual(bst.left.right.value, 7)
        
        # Check right subtree
        self.assertEqual(bst.right.value, 15)
        self.assertEqual(bst.right.left.value, 12)
        self.assertEqual(bst.right.right.value, 17)
        
        # Check depths
        self.assertEqual(bst.depth, 0)
        self.assertEqual(bst.left.depth, 1)
        self.assertEqual(bst.right.depth, 1)
        self.assertEqual(bst.left.left.depth, 2)
        self.assertEqual(bst.left.right.depth, 2)
        self.assertEqual(bst.right.left.depth, 2)
        self.assertEqual(bst.right.right.depth, 2)

    def test_get_node_by_value_root(self):
        """Test finding the root node by its value"""
        bst = BinarySearchTree(10)
        node = bst.get_node_by_value(10)
        self.assertIs(node, bst)

    def test_get_node_by_value_left(self):
        """Test finding a node in the left subtree"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        node = bst.get_node_by_value(5)
        self.assertIs(node, bst.left)

    def test_get_node_by_value_right(self):
        """Test finding a node in the right subtree"""
        bst = BinarySearchTree(10)
        bst.insert(15)
        node = bst.get_node_by_value(15)
        self.assertIs(node, bst.right)

    def test_get_node_by_value_deep(self):
        """Test finding a node deep in the tree"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(17)
        
        node = bst.get_node_by_value(3)
        self.assertIs(node, bst.left.left)
        
        node = bst.get_node_by_value(17)
        self.assertIs(node, bst.right.right)

    def test_get_node_by_value_not_found(self):
        """Test searching for a value not in the tree"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        bst.insert(15)
        
        node = bst.get_node_by_value(20)
        self.assertIsNone(node)
        
        node = bst.get_node_by_value(7)
        self.assertIsNone(node)

    def test_get_node_by_value_duplicate(self):
        """Test finding the first occurrence of a duplicate value"""
        bst = BinarySearchTree(10)
        bst.insert(10)  # Duplicate goes right
        bst.insert(10)  # Another duplicate goes right->right
        
        node = bst.get_node_by_value(10)
        self.assertIs(node, bst)  # Should find the root first

    def test_string_values(self):
        """Test BST with string values"""
        bst = BinarySearchTree("m")
        bst.insert("a")
        bst.insert("z")
        
        self.assertEqual(bst.value, "m")
        self.assertEqual(bst.left.value, "a")
        self.assertEqual(bst.right.value, "z")
        
        node = bst.get_node_by_value("a")
        self.assertIs(node, bst.left)

    def test_custom_comparable_objects(self):
        """Test BST with custom objects that implement comparison methods"""
        class ComparableObject:
            def __init__(self, value):
                self.value = value
                
            def __lt__(self, other):
                return self.value < other.value
                
            def __gt__(self, other):
                return self.value > other.value
                
            def __eq__(self, other):
                return self.value == other.value
                
            def __ne__(self, other):
                return self.value != other.value
                
            def __le__(self, other):
                return self.value <= other.value
                
            def __ge__(self, other):
                return self.value >= other.value
        
        obj10 = ComparableObject(10)
        obj5 = ComparableObject(5)
        obj15 = ComparableObject(15)
        
        bst = BinarySearchTree(obj10)
        bst.insert(obj5)
        bst.insert(obj15)
        
        self.assertEqual(bst.value.value, 10)
        self.assertEqual(bst.left.value.value, 5)
        self.assertEqual(bst.right.value.value, 15)
        
        node = bst.get_node_by_value(obj5)
        self.assertIs(node, bst.left)

    def test_traverse_preorder(self):
        """Test preorder traversal (Root -> Left -> Right)"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        
        # Capture stdout to test the printed output
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            bst.traverse_preorder()
            output = fake_stdout.getvalue().strip().split('\n')
        
        # Expected output order: 10, 5, 3, 7, 15
        self.assertEqual(len(output), 5)
        self.assertIn("Depth: 0, Value: 10", output[0])  # Root first
        self.assertIn("Depth: 1, Value: 5", output[1])   # Left subtree
        self.assertIn("Depth: 2, Value: 3", output[2])   # Left's left
        self.assertIn("Depth: 2, Value: 7", output[3])   # Left's right
        self.assertIn("Depth: 1, Value: 15", output[4])  # Right subtree

    def test_traverse_inorder(self):
        """Test inorder traversal (Left -> Root -> Right)"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        
        # Capture stdout to test the printed output
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            bst.traverse_inorder()
            output = fake_stdout.getvalue().strip().split('\n')
        
        # Expected output order: 3, 5, 7, 10, 15 (sorted order)
        self.assertEqual(len(output), 5)
        self.assertIn("Depth: 2, Value: 3", output[0])   # Leftmost first
        self.assertIn("Depth: 1, Value: 5", output[1])   # Left subtree root
        self.assertIn("Depth: 2, Value: 7", output[2])   # Left's right
        self.assertIn("Depth: 0, Value: 10", output[3])  # Root
        self.assertIn("Depth: 1, Value: 15", output[4])  # Right subtree

    def test_traverse_postorder(self):
        """Test postorder traversal (Left -> Right -> Root)"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        
        # Capture stdout to test the printed output
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            bst.traverse_postorder()
            output = fake_stdout.getvalue().strip().split('\n')
        
        # Expected output order: 3, 7, 5, 15, 10
        self.assertEqual(len(output), 5)
        self.assertIn("Depth: 2, Value: 3", output[0])   # Leftmost first
        self.assertIn("Depth: 2, Value: 7", output[1])   # Left's right
        self.assertIn("Depth: 1, Value: 5", output[2])   # Left subtree root
        self.assertIn("Depth: 1, Value: 15", output[3])  # Right subtree
        self.assertIn("Depth: 0, Value: 10", output[4])  # Root last

    def test_traverse_levelorder(self):
        """Test level-order traversal (breadth-first)"""
        bst = BinarySearchTree(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(17)
        
        # Capture stdout to test the printed output
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            bst.traverse_levelorder()
            output = fake_stdout.getvalue().strip().split('\n')
        
        # Expected output order: 10, 5, 15, 3, 7, 12, 17
        self.assertEqual(len(output), 7)
        self.assertEqual("10", output[0])  # Level 0: Root
        # Level 1: Left to right
        self.assertEqual("5", output[1])
        self.assertEqual("15", output[2])
        # Level 2: Left to right
        self.assertEqual("3", output[3])
        self.assertEqual("7", output[4])
        self.assertEqual("12", output[5])
        self.assertEqual("17", output[6])

    def test_traverse_empty_subtrees(self):
        """Test traversals with empty subtrees"""
        # Create a tree with only right children
        right_only = BinarySearchTree(10)
        right_only.insert(15)
        right_only.insert(20)
        
        # Test preorder traversal
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            right_only.traverse_preorder()
            output = fake_stdout.getvalue().strip().split('\n')
        
        self.assertEqual(len(output), 3)
        self.assertIn("Depth: 0, Value: 10", output[0])
        self.assertIn("Depth: 1, Value: 15", output[1])
        self.assertIn("Depth: 2, Value: 20", output[2])
        
        # Create a tree with only left children
        left_only = BinarySearchTree(30)
        left_only.insert(20)
        left_only.insert(10)
        
        # Test inorder traversal
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            left_only.traverse_inorder()
            output = fake_stdout.getvalue().strip().split('\n')
        
        self.assertEqual(len(output), 3)
        self.assertIn("Depth: 2, Value: 10", output[0])
        self.assertIn("Depth: 1, Value: 20", output[1])
        self.assertIn("Depth: 0, Value: 30", output[2])


if __name__ == '__main__':
    unittest.main()