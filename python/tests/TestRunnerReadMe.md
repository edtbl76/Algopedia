# Test Runner How-To Guide

This How-To explains how to run the test suite for Python Algopedia. 


## Prerequisites. 

- Python 3.13.3 w/ pyenv configuredf. 
- Virtual environment activated. (`.venv`)
- All required dependencies installed. 

## Test Directory Structure

The tests are organized in the `tests/` directory: 


    tests/
    ├── __init__.py
    ├── run_tests.py                        # Main test runner
    ├── simple_test_runner.py              # Simple test runner alternative
    ├── data_structures/
    │   ├── test_min_heap.py               # MinHeap tests (example)
    │   └── run_data_structure_tests.py    # Data structure specific runner
    ├── algorithms/
    │   └── run_algorithm_tests.py         # Algorithm specific runner
    ├── search/
    │   └── run_search_tests.py            # Search algorithm specific runner
    ├── sort/
    │   └── run_sort_tests.py              # Sorting algorithm specific runner
    └── apps/
        └── [app-specific tests]


## Running Tests

### Method 1: Run All Tests

Execute all tests across the entire project:

    # From the project root directory
    python -m tests.run_tests

    # Or directly from the tests directory
    cd tests
    python run_tests.py

### Method 2: Run Category-Specific Tests

Run tests for specific algorithm/data structure categories:

    # Data Structure Tests
    python -m tests.data_structures.run_data_structure_tests

    # Algorithm Tests  
    python -m tests.algorithms.run_algorithm_tests

    # Search Algorithm Tests
    python -m tests.search.run_search_tests

    # Sorting Algorithm Tests
    python -m tests.sort.run_sort_tests

    # HashMap Tests (specific)
    python -m tests.data_structures.run_hashmap_tests

### Method 3: Run Individual Test Files

Execute specific test files using Python's unittest module:

    # Run MinHeap tests specifically
    python -m unittest tests.data_structures.test_min_heap

    # Run with verbose output
    python -m unittest -v tests.data_structures.test_min_heap

    # Run a specific test class
    python -m unittest tests.data_structures.test_min_heap.TestMinHeap

    # Run a specific test method
    python -m unittest tests.data_structures.test_min_heap.TestMinHeap.test_initialization

### Method 4: Using pytest (if available)

If pytest is installed, you can also use:

    # Run all tests
    pytest tests/

    # Run with verbose output
    pytest -v tests/

    # Run specific test file
    pytest tests/data_structures/test_min_heap.py

    # Run tests matching a pattern
    pytest -k "test_initialization"

### Method 5: Simple Test Runner

For a simplified approach, use the simple test runner:

    python tests/simple_test_runner.py

## Test Output

When running tests, you'll see output indicating:

- ✅ **Passed tests**: Tests that executed successfully
- ❌ **Failed tests**: Tests that failed with error details
- **Test count**: Total number of tests run
- **Execution time**: How long the tests took to complete

## Example Test Execution

Here's what running the MinHeap tests looks like:

    $ python -m unittest -v tests.data_structures.test_min_heap

    test_add_duplicate_elements (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_add_multiple_elements_no_heapify_needed (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_add_multiple_elements_with_heapify (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_add_negative_elements (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_add_single_element (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_complex_heapify_case (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_get_smallest_child_index_method (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_has_child_method (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_heapify_down_method (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_heapify_up_method (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_helper_methods (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_initialization (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_large_heap (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_remove_all_elements (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_remove_min_and_verify_heap_property (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_remove_min_empty_heap (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_remove_min_multiple_elements (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_remove_min_single_element (tests.data_structures.test_min_heap.TestMinHeap) ... ok
    test_swap_method (tests.data_structures.test_min_heap.TestMinHeap) ... ok

    ----------------------------------------------------------------------
    Ran 19 tests in 0.002s

    OK

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Ensure you're running from the project root and the virtual environment is activated
2. **Import errors**: Check that `__init__.py` files exist in all test directories
3. **Path issues**: Use the `-m` flag with Python to run modules correctly

### Tips

- Always run tests from the project root directory
- Use the `-v` flag for verbose output to see individual test results
- Use specific test runners for faster execution when working on particular components
- Check test coverage by running all tests before committing changes

## Adding New Tests

When adding new test files:

1. Place them in the appropriate category directory under `tests/`
2. Follow the naming convention: `test_<component_name>.py`
3. Inherit from `unittest.TestCase`
4. Add descriptive docstrings for test methods
5. Update the relevant category test runner if needed
