import unittest
import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(project_root)  # Go up one level to the project root
sys.path.insert(0, project_root)

# Import the test classes directly
from tests.data_structures.test_node import TestNode
from tests.data_structures.test_linked_list import TestLinkedList
from tests.data_structures.test_doubly_linked_list import TestDoublyLinkedList

if __name__ == '__main__':
    # Create a test suite with the test classes
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestNode))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLinkedList))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDoublyLinkedList))

    # Run the tests
    unittest.TextTestRunner(verbosity=2).run(test_suite)
