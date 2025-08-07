from typing import List, Any, Optional


def binary_search(arr: List[Any], target: Any) -> Optional[int]:
    """
    Perform binary search on a sorted array using recursive slicing approach.

    WARNING: This implementation creates new array slices in each recursive call,
    resulting in O(n) space complexity and O(n log n) time complexity due to
    array copying overhead. For better performance, use binary_search_two_pointer.

    Binary search is a divide-and-conquer algorithm that efficiently searches
    for a target value in a sorted array by repeatedly dividing the search
    interval in half. If the target is less than the middle element, the search
    continues in the lower half; otherwise, it continues in the upper half.

    REQUIREMENTS:
    - Array must be sorted in ascending order
    - Elements must be comparable (support <, >, == operators)

    Time Complexity: O(n log n) - due to array slicing overhead
    Space Complexity: O(n) - due to recursive array slicing
    Standard binary search is O(log n) time, O(log n) space for recursion

    Args:
        arr: Sorted list of comparable elements to search in
        target: Element to search for

    Returns:
        Index of target element if found, None otherwise

    Example:
        >>> binary_search([1, 3, 5, 7, 9, 11], 7)
        3
        >>> binary_search([1, 3, 5, 7, 9, 11], 4)
        None
        >>> binary_search([], 5)
        None
    """

    if not arr:
        return None

    # Avoid integer overflow for very large arrays
    mid = len(arr) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # Search right half - need to adjust the returned index
        #
        # INDEX ADJUSTMENT EXPLANATION:
        # When we slice the array with arr[mid+1:], we create a new array that starts
        # at the original index (mid+1). However, the recursive call returns an index
        # relative to this NEW sliced array (starting from 0).
        #
        # Example: Original array [10, 20, 30, 40, 50], target = 40
        # - mid = 2 (element 30)
        # - We slice arr[3:] = [40, 50] and search recursively
        # - Recursive call finds 40 at index 0 in the sliced array [40, 50]
        # - But in the original array, 40 is at index 3
        # - So we must adjust: mid + 1 + right_result = 2 + 1 + 0 = 3
        #
        # The adjustment formula is: original_mid + 1 + sliced_result
        # - original_mid: the mid index in current array
        # - +1: accounts for the slice starting at mid+1
        # - sliced_result: the index returned from recursive call on sliced array

        right_result = binary_search(arr[mid + 1:], target)
        return None if right_result is None else mid + 1 + right_result
    else:
        # Search left half - index remains relative to original array start
        #
        # NO INDEX ADJUSTMENT NEEDED:
        # When we slice with arr[:mid], the sliced array starts at index 0,
        # same as the original array. Therefore, any index returned by the
        # recursive call is already correct relative to the original array.
        return binary_search(arr[:mid], target)


def binary_search_two_pointer(arr: List[Any], left: int, right: int, target: Any) -> Optional[int]:
    """
    Perform binary search using two pointers (more efficient approach).

    This implementation uses index boundaries instead of array slicing,
    providing optimal O(log n) time and O(log n) space complexity.
    This is the preferred binary search implementation.

    Binary search divides the search space in half at each step by comparing
    the target with the middle element and eliminating half of the remaining
    elements based on the comparison result.

    REQUIREMENTS:
    - Array must be sorted in ascending order
    - Elements must be comparable (support <, >, == operators)
    - Initial call should use left=0, right=len(arr)-1

    Time Complexity: O(log n) - halves search space each iteration
    Space Complexity: O(log n) - recursive call stack depth

    Args:
        arr: Sorted list of comparable elements to search in
        left: Left boundary index (inclusive)
        right: Right boundary index (inclusive)
        target: Element to search for

    Returns:
        Index of target element if found, None otherwise

    Example:
        >>> arr = [1, 3, 5, 7, 9, 11]
        >>> binary_search_two_pointer(arr, 0, len(arr)-1, 7)
        3
        >>> binary_search_two_pointer(arr, 0, len(arr)-1, 4)
        None
        >>> binary_search_two_pointer([], 0, -1, 5)
        None
    """
    if left > right:
        return None

    # Avoid integer overflow for very large arrays
    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # NO INDEX ADJUSTMENT NEEDED:
        # Unlike the slicing approach, we're working with the same original array
        # throughout all recursive calls. We only change the boundary parameters
        # (left and right), but the array itself never changes.
        #
        # This is another reason to use the 2 pointer method instead of slicing.
        #
        # The 'mid' index calculated here is always relative to the original array,
        # so when we find a match at arr[mid], that 'mid' is the correct index
        # in the original array. No conversion or adjustment is necessary.
        #
        # Example: Original array [10, 20, 30, 40, 50], target = 40
        # - Initial call: left=0, right=4, mid=2 (element 30)
        # - Recursive call: left=3, right=4, mid=3 (element 40)
        # - Found at mid=3, which is correct index in original array
        return binary_search_two_pointer(arr, mid+1, right, target)
    else:
        return binary_search_two_pointer(arr, left, mid-1, target)