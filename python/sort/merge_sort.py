from typing import Any, List
"""
Merge Sort Implementation

Merge sort is a divide-and-conquer algorithm invented by John von Neumann in 1945.
It was one of the first algorithms to achieve O(n log n) time complexity in the worst case,
making it significantly more efficient than earlier O(n²) algorithms like bubble sort
and insertion sort for large datasets.

The algorithm works by recursively dividing the array into smaller subarrays until each
subarray contains only one element, then merging these subarrays back together in sorted order.
This approach guarantees consistent O(n log n) performance regardless of input distribution,
unlike quicksort which can degrade to O(n²) in worst-case scenarios. T

Merge sort is widely used in practice due to its stability (maintains relative order of
equal elements) and predictable performance characteristics.
"""



def merge_sort(values: List[Any]) -> List[Any]:
    """
    Sorts a list using the merge sort algorithm.

    Time Complexity: O(n log n) - The algorithm divides the array log n times,
                    and each merge operation takes O(n) time.
    Space Complexity: O(n) - Additional space is needed for the temporary arrays
                     during the merge process.

    Args:
        values: List of comparable elements to be sorted

    Returns:
        A new sorted list containing all elements from the input

    Example:
        >>> merge_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    # Base case: arrays with 0 or 1 element are already sorted

    if len(values) <= 1:
        return values

    # Divide
    middle_index = len(values) // 2

    # Conquer: recursive step sorts both halves
    left_side = merge_sort(values[:middle_index])
    right_side = merge_sort(values[middle_index:])

    # merge 'em back!
    return _merge(left_side, right_side)

def _merge(left_side: List[Any], right_side: List[Any]) -> List[Any]:
    """
    Merges two sorted lists into a single sorted list with optimized performance.

    Time Complexity: O(n + m) where n and m are the lengths of the input lists
    Space Complexity: O(n + m) for the result list and index variables

    OPTIMIZATIONS IMPLEMENTED:

    1. Index-based iteration instead of pop(0):
       - pop(0) is O(n) for Python lists as it requires shifting all remaining elements
       - Using indices maintains O(1) access time per element
       - This reduces merge complexity from O(n²) to O(n), preserving the overall
         O(n log n) guarantee of merge sort

    2. Using <= instead of < for stability:
       - Ensures merge sort is "stable" - maintains relative order of equal elements
       - When elements are equal, we take from the left array first, preserving
         the original order from the input array
       - Critical for sorting objects where equal keys should maintain their
         original relative positions
       - Example: sorting [(1,'a'), (2,'b'), (1,'c')] by first element should
         preserve 'a' before 'c' in the final result

    3. Slice-based extension for remaining elements:
       - Uses list slicing (left_side[left_idx:]) instead of individual appends
       - More efficient as it leverages optimized C-level operations
       - Handles the common case where one array is exhausted before the other

    Args:
        left_side: First sorted list
        right_side: Second sorted list

    Returns:
        A new sorted list containing all elements from both input lists

    Example:
        >>> _merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> _merge([1, 1], [1, 1])  # Demonstrates stability
        [1, 1, 1, 1]
    """

    result = []
    left_idx = 0
    right_idx = 0


    # Merges elements in sorted order while both lists have elements.
    while left_idx < len(left_side) and right_idx < len(right_side):
        # Use <= for stability: when equal, prioritize left array element
        if left_side[left_idx] <= right_side[right_idx]:
            result.append(left_side[left_idx])
            left_idx += 1
        else:
            result.append(right_side[right_idx])
            right_idx += 1

    # Adds any remaining stragglers due to odd length collection. 
    # (only one of these will actually add elements)
    result.extend(left_side[left_idx:])
    result.extend(right_side[right_idx:])

    return result
