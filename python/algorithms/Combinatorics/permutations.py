"""
Permutations Module

This module provides efficient implementations for calculating and generating permutations,
which represent ordered arrangements of items. A permutation P(n,k) counts the number
of ways to arrange k items from n items where order matters, fundamental to combinatorics,
probability theory, and algorithm design.

Mathematical Foundation:
    The permutation is defined as:
    P(n,k) = n! / (n-k)!

    Where:
    • n is the total number of items
    • k is the number of items to arrange
    • ! denotes factorial (n! = n × (n-1) × ... × 2 × 1)

Key Difference from Combinations:
    • Permutations: Order matters - (A,B,C) ≠ (B,A,C)
    • Combinations: Order doesn't matter - {A,B,C} = {B,A,C}
    • Relationship: P(n,k) = C(n,k) × k!

Mathematical Properties:
    • P(n,0) = 1 (one way to arrange nothing)
    • P(n,1) = n (n ways to choose first item)
    • P(n,n) = n! (all possible arrangements)
    • P(n,k) = n × P(n-1,k-1) (recursive relation)

Applications:
    • Arranging people in a line or around a table
    • Creating passwords with distinct characters
    • Scheduling and sequencing problems
    • Ranking and ordering systems
    • Algorithm analysis (worst-case scenarios)
    • Cryptographic key generation

Implementation Philosophy:
    This module provides both counting functions (how many permutations exist) and
    generation functions (enumerate all permutations). Multiple algorithmic approaches
    accommodate different use cases from simple counts to memory-efficient iteration.
"""
from enum import Enum
from typing import List, Any, Iterator

from algorithms.Combinatorics.utils.validation import validate_inputs


class PermutationMethod(Enum):
    """
    Available permutation generation methods.

    RECURSIVE: Basic recursive backtracking, O(P(n,k) × k) time/space
    BACKTRACKING: Optimized backtracking with better memory usage
    LEXICOGRAPHIC: Sorted order generation, O(n × n!) time for full permutations
    HEAPS: Heap's algorithm for full permutations only, O(n!) time/space

    Additional methods (different return types):
    COUNT: Calculate count only, O(k) time, O(1) space
    ITERATOR: Memory-efficient streaming, O(k) space per permutation

    Performance Recommendations:
        • For counts only: Use COUNT_ONLY
        • For small complete sets: Use RECURSIVE or BACKTRACKING
        • For sorted output: Use LEXICOGRAPHIC
        • For full permutations: Use HEAPS
        • For large datasets: Use ITERATOR
        • For memory efficiency: Use ITERATOR or BACKTRACKING
    """
    RECURSIVE = "recursive"
    BACKTRACKING = "backtracking"
    LEXICOGRAPHIC = "lexicographic"
    HEAPS = "heaps"



def permutation_count(n: int, k: int) -> int:
    """
    Calculate P(n,k) = n! / (n-k)! using multiplicative formula.

    Uses P(n,k) = n × (n-1) × ... × (n-k+1) to avoid factorial overflow.

    Time Complexity: O(k)
    Space Complexity: O(1)

    Args:
        n: Total number of items (n ≥ 0)
        k: Number of items to arrange (0 ≤ k ≤ n)

    Returns:
        int: Number of k-permutations of n items

    Raises:
        ValueError: If n < 0, k < 0, or k > n

    Examples:
        >>> permutation_count(5, 3)
        60
        >>> permutation_count(4, 0)
        1
    """
    validate_inputs(n, k)


    # Base case: P(n,0) = 1 (one way to arrange nothing)
    if k == 0:
        return 1

    # Multiplicative formula: P(n,k) = n * (n-1) * ... * (n-k+1)
    # This avoids computing large factorials directly. (Therefore, avoids overflow issues).
    result = 1

    # Iterate from n down to (n-k+1)
    for i in range(n, n - k, -1):
        result *= i

    return result


def permutation_iterator(items: List[Any], k: int) -> Iterator[List[Any]]:
    """
    Memory-efficient iterator yielding k-permutations one at a time.

    Time Complexity: O(P(n,k) × k) total, O(k) per iteration
    Space Complexity: O(k)

    Args:
        items: List of items to permute
        k: Number of items in each permutation

    Yields:
        List[Any]: Each k-permutation

    Examples:
        >>> list(permutation_iterator([1, 2, 3], 2))
        [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
    """
    n = len(items)
    validate_inputs(n, k)

    if k == 0:
        yield []
        return

    yield from _generate_iterator(items, k)





def generate_permutations(items: List[Any], k: int,
                          method: PermutationMethod = PermutationMethod.RECURSIVE) -> List[List[Any]]:
    """
    Generate all k-permutations using specified method.

    Args:
        items: List of items to permute
        k: Number of items per permutation (0 ≤ k ≤ len(items))
        method: Generation algorithm

    Returns:
        List[List[Any]]: All k-permutations

    Raises:
        ValueError: If k < 0, k > len(items), or unsupported method
    """
    n = len(items)
    validate_inputs(n, k)

    # Handle base cases
    if k == 0:
        # Single empty permutation
        return [[]]

    # Method dispatcher
    method_map = {
        PermutationMethod.RECURSIVE: lambda: _generate_recursive(items,k),
        PermutationMethod.BACKTRACKING: lambda: _generate_backtracking(items,k),
        PermutationMethod.LEXICOGRAPHIC:
            lambda: _generate_lexicographic(items) if k == n else _generate_recursive(items,k),
        PermutationMethod.HEAPS: lambda: _generate_heaps(items) if k == n else _generate_recursive(items,k),
    }

    if method not in method_map:
        raise ValueError(f"Unsupported method: {method}")

    return method_map[method]()


def _generate_recursive(items: List[Any], k: int) -> List[List[Any]]:
    """
    Generate k-permutations using recursive approach.

    This implementation uses a straightforward recursive strategy where each
    recursive call chooses one item and generates (k-1)-permutations from
    the remaining items. Clear and educational but can use significant memory.

    Time Complexity: O(P(n,k) × k)
    Space Complexity: O(P(n,k) × k + k) - results + recursion stack

    Algorithm:
        1. Base case: if k=0, return single empty permutation
        2. For each item in the list:
           a. Choose the item as first element
           b. Recursively generate (k-1)-permutations from remaining items
           c. Prepend chosen item to each sub-permutation
    """
    if k == 0:
        return [[]]

    result = []
    for i in range(len(items)):
      # Get current, remaining items
      current_item = items[i]
      remaining_items = items[:i] + items[i+1:]

      # Generate (k-1)-permutations from remaining items
      for permutation in _generate_recursive(remaining_items, k-1):
        result.append([current_item] + permutation)
    return result


def _generate_backtracking(items: List[Any], k: int) -> List[List[Any]]:
    """
    Generate k-permutations using backtracking approach.

    This implementation uses backtracking to generate permutations, which
    provides better space efficiency by reusing the same partial permutation
    array and marking items as used/unused with a boolean array.

    Time Complexity: O(P(n,k) × k)
    Space Complexity: O(k + n + P(n,k) × k) - better recursion depth
    """

    # I decided to use a wrapper for the logic because I wanted to avoid
    # using a global variable for the partial permutation array.
    def backtrack(current_permutation: List[Any], used: List[bool], remaining_k: int) -> None:
        # Base case: we've selected k items:
        if remaining_k == 0:
            # copy current permutation
            result.append(current_permutation[:])
            return


        # Loop through unused items.
        for i in range(len(items)):
            if not used[i]:
                # choose unused item mark it used
                current_permutation.append(items[i])
                used[i] = True

                # Recurse w/ one less item to choose
                backtrack(current_permutation, used, remaining_k - 1)

                # Backtrack by unmarking and removing the item
                used[i] = False
                current_permutation.pop()

    result = []
    backtrack([], [False] * len(items), k)
    return result


def _generate_lexicographic(items: List[Any]) -> List[List[Any]]:
    """
    Generate all permutations in lexicographic (dictionary) order.

    This implementation generates permutations in sorted order using the
    next_permutation algorithm. Only works for full permutations (k=n).

    Time Complexity: O(n × n!)
    Space Complexity: O(n!)
    """



    # Sort items to start with smallest lexicographic permutation
    sorted_items = sorted(items)
    result = [sorted_items[:]]

    while _next_permutation(sorted_items):
        result.append(sorted_items[:])

    return result


def _generate_heaps(items: List[Any]) -> List[List[Any]]:
    """
    Generate all permutations using Heap's algorithm.

    Heap's algorithm is very efficient for generating ALL permutations
    of a complete set. Only works for full permutations (k=n).

    Time Complexity: O(n!)
    Space Complexity: O(n!)
    """

    def generate(k: int, arr: List[Any]):
        if k == 1:
            result.append(arr[:])
            return

        generate(k - 1, arr)

        for i in range(k - 1):
            if k % 2 == 0:  # k is even
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
            else:  # k is odd
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            generate(k - 1, arr)

    result = []
    generate(len(items), items[:])
    return result


### Helper Methods ###




def _generate_iterator(items: List[Any], k: int) -> Iterator[List[Any]]:
    """
    Iterator implementation using backtracking for memory efficiency.

    This generator yields permutations one at a time without storing
    all of them in memory, making it suitable for large datasets.
    """

    def backtrack_generator(current_perm: List[Any], used: List[bool], remaining_k: int):
        if remaining_k == 0:
            yield current_perm[:]
            return

        for i in range(len(items)):
            if not used[i]:
                current_perm.append(items[i])
                used[i] = True

                yield from backtrack_generator(current_perm, used, remaining_k - 1)

                current_perm.pop()
                used[i] = False

    yield from backtrack_generator([], [False] * len(items), k)


def _next_permutation(arr: List[Any]) -> bool:
    """
    Generate the next lexicographic permutation in-place.

    This function implements the standard next_permutation algorithm
    used in lexicographic permutation generation.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: Array to modify in-place

    Returns:
        bool: True if next permutation exists, False if this was the last one
    """
    # Step 1: Find the largest index i such that arr[i] < arr[i + 1]
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # If no such index exists, this is the last permutation
    if i == -1:
        return False

    # Step 2: Find the largest index j such that arr[i] < arr[j]
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1

    # Step 3: Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]

    # Step 4: Reverse the suffix starting at arr[i + 1]
    arr[i + 1:] = reversed(arr[i + 1:])

    return True



