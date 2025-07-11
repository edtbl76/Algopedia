# Algopedia Data Structures

This repository contains implementations of common data structures in Python.

## Data Structures

### Node
A simple node implementation with data and a reference to the next node.

### LinkedList
A linked list implementation with methods for:
- Initializing a linked list with a value
- Getting the head node
- Inserting a node at the start of the list
- Converting the list to a string
- Removing a node with a specific value

## Tests

Tests have been implemented for all classes and methods using Python's unittest framework.

### Running the Tests

You can run the tests using the simple test runner:

```bash
python tests/simple_test_runner.py
```

This will run all the tests for the Node and LinkedList classes.

## Bug Fixes

During the implementation of the tests, the following bugs were identified and fixed:

1. **LinkedList.insert_start method**: The method was creating a new node but not updating the head reference. This has been fixed by adding `self.head = new_node` to update the head reference.

2. **LinkedList.stringify_list method**: The method was using `get__data()` (with two underscores) instead of `get_data()` (with one underscore). This has been fixed to use the correct method name.

3. **LinkedList.remove_node method**: The method was not handling the case where the end of the list is reached without finding the value to remove. This has been fixed by modifying the while loop condition to check if `current_node` and `current_node.get_next()` are not None.

## Project Structure

```
.
├── data_structures/
│   ├── __init__.py
│   ├── LinkedList.py
│   └── Node.py
└── tests/
    ├── __init__.py
    ├── data_structures/
    │   ├── __init__.py
    │   ├── test_linked_list.py
    │   └── test_node.py
    ├── run_tests.py
    └── simple_test_runner.py
```