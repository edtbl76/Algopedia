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
from tests.data_structures.test_queue import TestQueue
from tests.data_structures.test_stack import TestStack
from tests.data_structures.test_two_point_node import TestTwoPointNode
from tests.apps.tower_of_hanoi.test_named_stack import TestNamedStack
from tests.apps.tower_of_hanoi.test_tower_of_hanoi import TestTowerOfHanoi

if __name__ == '__main__':
    # Create a test suite with the test classes
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestNode))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLinkedList))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDoublyLinkedList))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestQueue))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestStack))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestTwoPointNode))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestNamedStack))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestTowerOfHanoi))

    # Run the tests
    unittest.TextTestRunner(verbosity=2).run(test_suite)
