from typing import List, Any
"""
Bubble Sort Algorithm Implementation

This module provides various implementations of the bubble sort algorithm, one of the
simplest and most well-known sorting algorithms in computer science.

ALGORITHM OVERVIEW:
Bubble sort works by repeatedly stepping through the list, comparing adjacent elements
and swapping them if they are in the wrong order. The algorithm gets its name because
smaller elements "bubble" to the beginning of the list, just like air bubbles rising
to the surface of water.

HISTORICAL BACKGROUND:
Bubble sort is one of the oldest sorting algorithms, with its origins tracing back to
the early days of computing in the 1950s. While the exact inventor is debated, it was
popularized in the 1962 book "A Primer of ALGOL 60 Programming" by E.W. Dijkstra.

The algorithm gained widespread recognition in Donald Knuth's seminal work "The Art of
Computer Programming" (1973), where he dubbed it "bubble sort" due to the way smaller
elements bubble to the top of the list. Knuth also noted that despite its simplicity
and educational value, bubble sort is inefficient for practical use on large datasets.

CHARACTERISTICS:
- Time Complexity: O(n²) in worst and average cases, O(n) in best case (already sorted)
- Space Complexity: O(1) - sorts in-place
- Stability: Stable (maintains relative order of equal elements)
- Adaptive: Can be optimized to detect if the list becomes sorted early

EDUCATIONAL VALUE:
While bubble sort is rarely used in production code due to its poor performance on
large datasets, it remains valuable for educational purposes because:
1. It's easy to understand and implement
2. It demonstrates fundamental sorting concepts
3. It shows the importance of algorithm analysis and optimization
4. It serves as a baseline for comparing other sorting algorithms

This module includes multiple variants:
- Basic implementation for learning purposes
- Optimized version with reduced comparisons
- Descending order implementation
"""


def _swap(values: List[Any], i: int, j: int) -> None:
    """
    Swap two elements in an array using Pythonic tuple unpacking.

    This implementation uses Python's tuple unpacking feature for swapping,
    which is more readable and idiomatic than the classic approach.

    Pythonic approach (current):
        values[i], values[j] = values[j], values[i]

    Classic approach (alternative):
        temp = values[i]
        values[i] = values[j]
        values[j] = temp

    Args:
        values: The list containing elements to swap
        i: Index of the first element
        j: Index of the second element
    """
    values[i], values[j] = values[j], values[i]


def bubble_sort_basic(values: List[Any]) -> None:
    """
    Sort a list using the basic bubble sort algorithm.

    Bubble sort works by repeatedly stepping through the list, comparing adjacent
    elements and swapping them if they are in the wrong order. The pass through
    the list is repeated until the list is sorted. The algorithm gets its name
    because smaller elements "bubble" to the top of the list.

    Time Complexity: O(n²) in all cases (best, average, worst)
    Space Complexity: O(1) - sorts in-place
    Stability: Stable (maintains relative order of equal elements)

    Args:
        values: The list to be sorted in-place. Can contain any comparable elements.
                The list is modified directly and not returned.

    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> bubble_sort_basic(arr)
        >>> print(arr)  # [11, 12, 22, 25, 34, 64, 90]
    """

    # Outer loop (Performs n passes through the array)
    # Each pass ensures that at least one element reaches its correct position
    for _ in values:

        # Inner loop: (Compares adjacent elements and swaps if necessary)
        #
        # We use len(values) - 1 as BOUNDS CHECKING, because as we compare
        # values[i] w/ values[i + 1] we risk INDEX OUT OF BOUNDS when i
        # reaches the last position
        for i in range(len(values) - 1):

            # compares current and next elements.
            if values[i] > values[i + 1]:

                # swaps elements so that the "right" element is the largest
                # (ascending bubble sort)
                _swap(values, i, i + 1)


def bubble_sort_optimized(values: List[Any]) -> None:
    """
    Sort a list using an optimized bubble sort algorithm.

    This optimized version improves upon the basic bubble sort by reducing
    the number of comparisons in each subsequent pass. After each pass,
    the largest element is guaranteed to be in its correct position at the end,
    so we don't need to check it again in future passes.

    Another way of thinking about this is that after each pass, we are only
    performing comparisons for the remaining unsorted portion of the list, as if it were
    a subset of the original list that is shorter by one element.

    Optimization: Reduces the range of comparisons after each pass
    - Pass 1: Compare all n-1 adjacent pairs
    - Pass 2: Compare first n-2 pairs (last element is already sorted)
    - Pass 3: Compare first n-3 pairs (last 2 elements are already sorted)
    - And so on...

    Time Complexity: O(n²) worst/average case, but with fewer comparisons than basic version
    Space Complexity: O(1) - sorts in-place
    Stability: Stable (maintains relative order of equal elements)

    Args:
        values: The list to be sorted in-place. Can contain any comparable elements.
                The list is modified directly and not returned.

    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> bubble_sort_optimized(arr)
        >>> print(arr)  # [11, 12, 22, 25, 34, 64, 90]
    """

    # Outer loop; Controls the number of passes (represented by 'i')
    # The worst case is n passes for n elements (n = len(values))
    for i in range(len(values)):

        # Inner loop: Compare adjacent elements in the unsorted portion
        # Key optimization: Use (len(values) - i - 1) as the upper bound
        #
        # Breakdown of the range calculation:
        # - len(values): Total number of elements
        # - i: Current pass number (0, 1, 2, ...)
        # - 1: Subtracted because we compare index with index+1
        #
        # Why this works:
        # - After pass 0 (i=0): Last 1 element is in correct position
        # - After pass 1 (i=1): Last 2 elements are in correct position
        # - After pass k (i=k): Last k+1 elements are in correct position
        # - So we only need to check the first (n-i-1) pairs
        #
        # This is more or less an optimization of the BOUNDS CHECK, by considering
        # the sorted portion of the structure as "out of bounds", which supports the
        # in-place sort.
        for index in range(len(values) - i - 1):

            # Comparison step (current element w/ next element)
            if values[index] > values[index + 1]:

                # Ascending swap
                _swap(values, index, index + 1)

def bubble_sort_descending (values: List[Any]) -> None:
    """
    Sort a list in descending order using optimized bubble sort.

    Identical to bubble_sort_optimized() but with reversed comparison logic
    to achieve descending order instead of ascending order.

    Args:
        values: The list to be sorted in-place in descending order.

    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> bubble_sort_descending(arr)
        >>> print(arr)  # [90, 64, 34, 25, 22, 12, 11]
    """

    for i in range(len(values)):
        for index in range(len(values) - i - 1):
            # KEY DIFFERENCE: Reversed comparison (< instead of >) for descending order
            # If current element is SMALLER than next element, swap them
            # This bubbles larger elements toward the beginning of the list
            if values[index] < values[index + 1]:
                _swap(values, index, index + 1)