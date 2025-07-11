import unittest
import sys
import os

if __name__ == '__main__':
    # Add the project root directory to the Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(project_root)  # Go up one level to the project root
    sys.path.insert(0, project_root)

    # Discover and run all tests in the tests directory
    test_suite = unittest.defaultTestLoader.discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test_suite)
