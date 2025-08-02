# TAGS: Recursion, Iteration


from typing import List, Dict, Tuple

# Extract constant for dictionary key
EXECUTION_CONTEXT_VALUE_KEY = 'n_value'


def iterative_sum_to_one(n: int) -> Tuple[int, List[Dict[str, int]]]:
    """
    Calculate the sum from n down to 1 using an iterative approach that simulates recursion.

    This function demonstrates how recursion can be implemented iteratively using a stack
    to store execution contexts. It mimics the call stack behavior of the recursive version.

    Time Complexity: O(n) - linear time as we iterate from n down to 1
    Space Complexity: O(n) - linear space for storing execution contexts in the call stack

    Args:
        n: A positive integer to sum down to 1

    Returns:
        A tuple containing:
            - The sum result (n + (n-1) + ... + 1)
            - The final call stack (empty after processing)

    Raises:
        ValueError: If n is not a positive integer

    Examples:
        >>> result, stack = iterative_sum_to_one(5)
        >>> result
        15
        >>> len(stack)
        0
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    result: int = 0
    call_stack: List[Dict[str, int]] = []

    # Make consistent with recursive version - stop at 1, not 0
    while n >= 1:
        execution_context = {EXECUTION_CONTEXT_VALUE_KEY: n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)

    print("Recursive Base Case Reached")

    while len(call_stack) != 0:
        popped_context = call_stack.pop()
        print(call_stack)
        print(f"Adding {popped_context[EXECUTION_CONTEXT_VALUE_KEY]} to {result}")
        result += popped_context[EXECUTION_CONTEXT_VALUE_KEY]

    return result, call_stack


def recursive_sum_to_one(n: int) -> int:
    """
    Calculate the sum from n down to 1 using recursion.

    This function recursively computes the sum n + (n-1) + ... + 1 by breaking
    the problem down into smaller subproblems until reaching the base case.

    Time Complexity: O(n) - linear time due to n recursive calls
    Space Complexity: O(n) - linear space due to call stack depth of n frames

    Args:
        n: A positive integer to sum down to 1

    Returns:
        The sum result (n + (n-1) + ... + 1)

    Raises:
        ValueError: If n is not a positive integer
        RecursionError: If n is too large and exceeds Python's recursion limit

    Examples:
        >>> recursive_sum_to_one(5)
        15
        >>> recursive_sum_to_one(1)
        1
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Base case: when n equals 1, return 1
    if n == 1:
        return n

    print(f"Recursing with input: {n}")

    # Recursive step: return n plus the sum of numbers from (n-1) down to 1
    return n + recursive_sum_to_one(n - 1)
