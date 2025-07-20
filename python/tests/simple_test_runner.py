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
from tests.data_structures.test_bst import TestBST
from tests.apps.tower_of_hanoi.test_named_stack import TestNamedStack
from tests.apps.tower_of_hanoi.test_tower_of_hanoi import TestTowerOfHanoi
# HashMap test classes
from tests.data_structures.test_hash_entry import TestHashEntry
from tests.data_structures.test_hash_function import TestHashFunction
from tests.data_structures.test_simple_addition_hash import TestSimpleAdditionHash
from tests.data_structures.test_hash_map import TestHashMap
from tests.data_structures.test_array_based_storage import TestArrayBasedStorage
from tests.data_structures.test_separate_chaining import TestSeparateChaining
from tests.data_structures.test_storage_strategy import TestStorageStrategy
# Algorithm test classes
from tests.algorithms.test_find_max import TestFindMax
from tests.algorithms.test_find_min import TestFindMin
from tests.algorithms.test_factorial import TestFactorial
from tests.algorithms.test_fibonacci import TestFibonacci
from tests.algorithms.test_flatten_list import TestFlattenList
from tests.algorithms.test_power_set import TestPowerSet
from tests.algorithms.test_iteration_recursion_comparison import TestIterationRecursionComparison

if __name__ == '__main__':
    # Create a test suite with the test classes
    test_suite = unittest.TestSuite()

    # Data structure test classes
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestNode))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLinkedList))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDoublyLinkedList))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestQueue))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestStack))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestTwoPointNode))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestBST))

    # App test classes
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestNamedStack))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestTowerOfHanoi))

    # HashMap test classes
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestHashEntry))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestHashFunction))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSimpleAdditionHash))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestHashMap))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestArrayBasedStorage))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSeparateChaining))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestStorageStrategy))

    # Algorithm test classes
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestFindMax))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestFindMin))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestFactorial))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestFibonacci))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestFlattenList))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestPowerSet))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestIterationRecursionComparison))

    # Run the tests
    unittest.TextTestRunner(verbosity=2).run(test_suite)
