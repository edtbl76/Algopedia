import os
import subprocess
import sys

def run_test_file(test_file_path, project_root):
    """Run a single test file using the python -m unittest command."""
    print(f"\nRunning tests in {test_file_path}")

    # Convert file path to module path for unittest
    rel_path = os.path.relpath(test_file_path, project_root)
    module_path = os.path.splitext(rel_path)[0].replace(os.path.sep, '.')

    # Run the test using python -m unittest
    cmd = [sys.executable, '-m', 'unittest', module_path]
    result = subprocess.run(cmd, capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print(f"Errors: {result.stderr}")
    return result.returncode == 0

if __name__ == '__main__':
    # Get the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(project_root)  # Go up one level to the project root

    # List of test files to run
    test_files = [
        os.path.join(project_root, 'tests', 'data_structures', 'test_node.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_linked_list.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_stack.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_queue.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_doubly_linked_list.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_two_point_node.py'),
        os.path.join(project_root, 'tests', 'apps', 'tower_of_hanoi', 'test_named_stack.py'),
        os.path.join(project_root, 'tests', 'apps', 'tower_of_hanoi', 'test_tower_of_hanoi.py'),
        # HashMap tests
        os.path.join(project_root, 'tests', 'data_structures', 'test_hash_entry.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_hash_function.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_simple_addition_hash.py'),
        os.path.join(project_root, 'tests', 'data_structures', 'test_hash_map.py'),
        # Algorithm tests
        os.path.join(project_root, 'tests', 'algorithms', 'test_find_max.py'),
        os.path.join(project_root, 'tests', 'algorithms', 'test_find_min.py'),
        os.path.join(project_root, 'tests', 'algorithms', 'test_factorial.py'),
        os.path.join(project_root, 'tests', 'algorithms', 'test_iteration_recursion_comparison.py')
    ]

    # Run each test file
    all_passed = True
    for test_file in test_files:
        if not run_test_file(test_file, project_root):
            all_passed = False

    # Run the HashMap tests using the dedicated runner
    print("\nRunning HashMap tests using run_hashmap_tests.py")
    hashmap_tests_path = os.path.join(project_root, 'tests', 'data_structures', 'run_hashmap_tests.py')
    hashmap_result = subprocess.run([sys.executable, hashmap_tests_path], capture_output=True, text=True)
    print(hashmap_result.stdout)
    if hashmap_result.stderr:
        print(f"Errors: {hashmap_result.stderr}")
    if hashmap_result.returncode != 0:
        all_passed = False

    # Run the Algorithm tests using the dedicated runner
    print("\nRunning Algorithm tests using run_algorithm_tests.py")
    algorithm_tests_path = os.path.join(project_root, 'tests', 'algorithms', 'run_algorithm_tests.py')
    algorithm_result = subprocess.run([sys.executable, algorithm_tests_path], capture_output=True, text=True)
    print(algorithm_result.stdout)
    if algorithm_result.stderr:
        print(f"Errors: {algorithm_result.stderr}")
    if algorithm_result.returncode != 0:
        all_passed = False

    # Print summary
    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")
        sys.exit(1)
