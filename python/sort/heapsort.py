"""
Heapsort

This module implements the heapsort algorithm, a comparison-based sorting technique
that uses a binary heap data structure. Heapsort works by building a max heap from
the input array, then repeatedly extracting the maximum element and placing it in
the sorted portion of the array.

The algorithm consists of two main phases:
1. Build Phase: Insert all elements into a max heap - O(n log n)
2. Sort Phase: Repeatedly extract the maximum element - O(n log n)

Overall time complexity: O(n log n) in all cases (best, average, worst)
Space complexity: O(n) for the heap storage

For heap implementation details, see MaxHeap.py.
"""


from typing import List, Optional

from data_structures.MaxHeap import MaxHeap


def heapsort(arr: List[int], ascending: bool = True) -> List[int]:
    """
    Sort an array using the heapsort algorithm.

    This implementation uses a max heap to sort the input array. Elements are
    first added to the heap (build phase), then repeatedly extracted to form
    the sorted result (sort phase).

    Implementation details:
    - Builds a max heap by inserting all elements: O(n log n)
    - Extracts elements one by one to build sorted list: O(n log n)
    - Uses list.append() for O(1) insertions instead of O(n) list.insert(0)
    - Reverses final result if ascending order is requested

    Args:
        arr (List[int]): The input array to be sorted
        ascending (bool): If True, sort in ascending order; if False, sort in
                         descending order. Defaults to True.

    Returns:
        List[int]: A new sorted list containing the same elements as the input

    Time Complexity:
        - Build phase: O(n log n) - n insertions, each O(log n)
        - Sort phase: O(n log n) - n extractions, each O(log n)
        - Reverse (if needed): O(n)
        - Overall: O(n log n)

    Space Complexity: O(n) - for the heap storage and result list

    Examples:
        >>> heapsort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> heapsort([3, 1, 4, 1, 5, 9, 2, 6], ascending=False)
        [9, 6, 5, 4, 3, 2, 1, 1]
    """
    # return empty list if input is empty
    if not arr:
        return []

    sortedList = []
    max_heap = MaxHeap()

    # Build phase: add all of the elements to the heap
    for value in arr:
        max_heap.add(value)

    # Sort phase: extract maximum elements
    while max_heap.size > 0:
        max_value = max_heap.remove_max()

        # Use append() O(1) instead of insert(0) O(n) to preserve heapsort's O(n log n) complexity.
        # insert(0) requires shifting all existing elements right, making n insertions O(n²) total.
        # append() adds to end without shifting, keeping insertions O(n) and overall algorithm O(n log n).
        # I see a lot of implementations using insert(0) instead of append().
        sortedList.append(max_value)

    # Max heap extraction gives us the sorted list in descending order,
    # so reverse it if ascending order is requested (default)
    if ascending:
        sortedList.reverse()

    return sortedList




