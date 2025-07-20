import unittest
from data_structures.BST import build_balanced_bst_from_sorted_array, NODE_DATA_KEY, LEFT_CHILD_KEY, RIGHT_CHILD_KEY


class TestBST(unittest.TestCase):

    def test_empty_array(self):
        """Test BST creation from empty array"""
        result = build_balanced_bst_from_sorted_array([])
        self.assertIsNone(result)

    def test_single_element(self):
        """Test BST creation from single element array"""
        result = build_balanced_bst_from_sorted_array([5])
        expected = {
            NODE_DATA_KEY: 5,
            LEFT_CHILD_KEY: None,
            RIGHT_CHILD_KEY: None
        }
        self.assertEqual(result, expected)

    def test_two_elements(self):
        """Test BST creation from two element array"""
        result = build_balanced_bst_from_sorted_array([1, 2])
        expected = {
            NODE_DATA_KEY: 2,
            LEFT_CHILD_KEY: {
                NODE_DATA_KEY: 1,
                LEFT_CHILD_KEY: None,
                RIGHT_CHILD_KEY: None
            },
            RIGHT_CHILD_KEY: None
        }
        self.assertEqual(result, expected)

    def test_three_elements(self):
        """Test BST creation from three element array"""
        result = build_balanced_bst_from_sorted_array([1, 2, 3])
        expected = {
            NODE_DATA_KEY: 2,
            LEFT_CHILD_KEY: {
                NODE_DATA_KEY: 1,
                LEFT_CHILD_KEY: None,
                RIGHT_CHILD_KEY: None
            },
            RIGHT_CHILD_KEY: {
                NODE_DATA_KEY: 3,
                LEFT_CHILD_KEY: None,
                RIGHT_CHILD_KEY: None
            }
        }
        self.assertEqual(result, expected)

    def test_five_elements(self):
        """Test BST creation from five element array"""
        result = build_balanced_bst_from_sorted_array([1, 2, 3, 4, 5])
        expected = {
            NODE_DATA_KEY: 3,
            LEFT_CHILD_KEY: {
                NODE_DATA_KEY: 2,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: 1,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: None
            },
            RIGHT_CHILD_KEY: {
                NODE_DATA_KEY: 5,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: 4,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: None
            }
        }
        self.assertEqual(result, expected)

    def test_seven_elements(self):
        """Test BST creation from seven element array"""
        result = build_balanced_bst_from_sorted_array([1, 2, 3, 4, 5, 6, 7])
        expected = {
            NODE_DATA_KEY: 4,
            LEFT_CHILD_KEY: {
                NODE_DATA_KEY: 2,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: 1,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: {
                    NODE_DATA_KEY: 3,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                }
            },
            RIGHT_CHILD_KEY: {
                NODE_DATA_KEY: 6,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: 5,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: {
                    NODE_DATA_KEY: 7,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                }
            }
        }
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Test BST creation with negative numbers"""
        result = build_balanced_bst_from_sorted_array([-3, -1, 0, 2, 4])
        expected = {
            NODE_DATA_KEY: 0,
            LEFT_CHILD_KEY: {
                NODE_DATA_KEY: -1,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: -3,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: None
            },
            RIGHT_CHILD_KEY: {
                NODE_DATA_KEY: 4,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: 2,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: None
            }
        }
        self.assertEqual(result, expected)

    def test_duplicate_values(self):
        """Test BST creation with duplicate values"""
        result = build_balanced_bst_from_sorted_array([1, 1, 2, 2, 3])
        expected = {
            NODE_DATA_KEY: 2,
            LEFT_CHILD_KEY: {
                NODE_DATA_KEY: 1,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: 1,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: None
            },
            RIGHT_CHILD_KEY: {
                NODE_DATA_KEY: 3,
                LEFT_CHILD_KEY: {
                    NODE_DATA_KEY: 2,
                    LEFT_CHILD_KEY: None,
                    RIGHT_CHILD_KEY: None
                },
                RIGHT_CHILD_KEY: None
            }
        }
        self.assertEqual(result, expected)

    def test_string_values(self):
        """Test BST creation with string values"""
        result = build_balanced_bst_from_sorted_array(['a', 'b', 'c'])
        expected = {
            NODE_DATA_KEY: 'b',
            LEFT_CHILD_KEY: {
                NODE_DATA_KEY: 'a',
                LEFT_CHILD_KEY: None,
                RIGHT_CHILD_KEY: None
            },
            RIGHT_CHILD_KEY: {
                NODE_DATA_KEY: 'c',
                LEFT_CHILD_KEY: None,
                RIGHT_CHILD_KEY: None
            }
        }
        self.assertEqual(result, expected)

    def test_large_array(self):
        """Test BST creation with larger array"""
        # Test with 15 elements to ensure proper balancing
        input_array = list(range(1, 16))  # [1, 2, 3, ..., 15]
        result = build_balanced_bst_from_sorted_array(input_array)

        # Verify root is the middle element
        self.assertEqual(result[NODE_DATA_KEY], 8)

        # Verify structure exists (not testing exact structure due to complexity)
        self.assertIsNotNone(result[LEFT_CHILD_KEY])
        self.assertIsNotNone(result[RIGHT_CHILD_KEY])

        # Verify left subtree root
        self.assertEqual(result[LEFT_CHILD_KEY][NODE_DATA_KEY], 4)

        # Verify right subtree root
        self.assertEqual(result[RIGHT_CHILD_KEY][NODE_DATA_KEY], 12)

    def test_bst_property_validation(self):
        """Test that the created BST maintains BST property"""
        def validate_bst(node, min_val=float('-inf'), max_val=float('inf')):
            """Helper function to validate BST property"""
            if node is None:
                return True

            if node[NODE_DATA_KEY] <= min_val or node[NODE_DATA_KEY] >= max_val:
                return False

            return (validate_bst(node[LEFT_CHILD_KEY], min_val, node[NODE_DATA_KEY]) and
                    validate_bst(node[RIGHT_CHILD_KEY], node[NODE_DATA_KEY], max_val))

        # Test with various arrays
        test_arrays = [
            [1, 2, 3, 4, 5],
            [1, 3, 5, 7, 9, 11],
            [-5, -2, 0, 3, 8, 12, 15],
            [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        ]

        for array in test_arrays:
            with self.subTest(array=array):
                result = build_balanced_bst_from_sorted_array(array)
                self.assertTrue(validate_bst(result), f"BST property violated for array {array}")

    def test_height_balance(self):
        """Test that the created BST is height-balanced"""
        def get_height(node):
            """Helper function to get height of tree"""
            if node is None:
                return 0
            return 1 + max(get_height(node[LEFT_CHILD_KEY]), get_height(node[RIGHT_CHILD_KEY]))

        def is_balanced(node):
            """Helper function to check if tree is balanced"""
            if node is None:
                return True

            left_height = get_height(node[LEFT_CHILD_KEY])
            right_height = get_height(node[RIGHT_CHILD_KEY])

            return (abs(left_height - right_height) <= 1 and
                    is_balanced(node[LEFT_CHILD_KEY]) and
                    is_balanced(node[RIGHT_CHILD_KEY]))

        # Test with various arrays
        test_arrays = [
            [1, 2, 3],
            [1, 2, 3, 4, 5, 6, 7],
            list(range(1, 16)),  # 15 elements
            list(range(1, 32))   # 31 elements
        ]

        for array in test_arrays:
            with self.subTest(array=array):
                result = build_balanced_bst_from_sorted_array(array)
                self.assertTrue(is_balanced(result), f"Tree not balanced for array {array}")


if __name__ == '__main__':
    unittest.main()
