import unittest
import sys
import os

# Add the parent directory to the path so we can import the test modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the test modules
from tests.data_structures.test_node import TestNode
from tests.data_structures.test_linked_list import TestLinkedList
from tests.data_structures.test_stack import TestStack
from tests.data_structures.test_queue import TestQueue
from tests.data_structures.test_doubly_linked_list import TestDoublyLinkedList
from tests.data_structures.test_two_point_node import TestTwoPointNode
from tests.data_structures.test_bst import TestBST
from tests.data_structures.test_tree_node import TestTreeNode
from tests.data_structures.test_binary_search_tree import TestBinarySearchTree
from tests.data_structures.test_max_heap import TestMaxHeap

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add the test cases
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestNode))
    test_suite.addTest(loader.loadTestsFromTestCase(TestLinkedList))
    test_suite.addTest(loader.loadTestsFromTestCase(TestStack))
    test_suite.addTest(loader.loadTestsFromTestCase(TestQueue))
    test_suite.addTest(loader.loadTestsFromTestCase(TestDoublyLinkedList))
    test_suite.addTest(loader.loadTestsFromTestCase(TestTwoPointNode))
    test_suite.addTest(loader.loadTestsFromTestCase(TestBST))
    test_suite.addTest(loader.loadTestsFromTestCase(TestTreeNode))
    test_suite.addTest(loader.loadTestsFromTestCase(TestBinarySearchTree))
    test_suite.addTest(loader.loadTestsFromTestCase(TestMaxHeap))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print a summary
    print(f"\nRan {result.testsRun} tests")
    if result.wasSuccessful():
        print("All data structure tests passed!")
    else:
        print(f"Failed tests: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        sys.exit(1)
