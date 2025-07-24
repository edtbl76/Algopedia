

NOT_FOUND: int = -1

def linear_search(values: list, target: int) -> int:
    """
    Find the first occurrence of a target value in a list using linear search.

    This algorithm sequentially examines each element in the list until the target
    is found or all elements have been checked. It's a simple but effective search
    method for unsorted data.

    Time Complexity: O(n) - where n is the number of elements in the list.
                    In the worst case, we need to examine every element.
    Space Complexity: O(1) - only uses constant additional space regardless
                     of input size.

    Args:
        values: List of integers to search through
        target: The integer value to search for

    Returns:
        The index of the first occurrence of the target value,
        or NOT_FOUND (-1) if the target is not present in the list

    Examples:
        >>> linear_search([1, 3, 5, 7, 9], 5)
        2
        >>> linear_search([1, 3, 5, 7, 9], 10)
        -1
        >>> linear_search([], 5)
        -1
    """
    for i, value in enumerate(values):
        if value == target:
            return i
    return NOT_FOUND

def linear_search_duplicates(values: list, target: int) -> list:
    """
    Find all occurrences of a target value in a list using linear search.

    This algorithm sequentially examines each element in the list and collects
    the indices of all positions where the target value is found. Unlike the
    basic linear search that stops at the first match, this continues through
    the entire list to find duplicates.

    Time Complexity: O(n) - where n is the number of elements in the list.
                    Always examines every element regardless of matches found.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        values: List of integers to search through
        target: The integer value to search for

    Returns:
        A list containing all indices where the target value was found.
        Returns an empty list if the target is not present in the list.

    Examples:
        >>> linear_search_duplicates([1, 3, 5, 3, 9, 3], 3)
        [1, 3, 5]
        >>> linear_search_duplicates([1, 2, 3, 4, 5], 6)
        []
        >>> linear_search_duplicates([7, 7, 7], 7)
        [0, 1, 2]
        >>> linear_search_duplicates([], 5)
        []
    """
    indices = []
    for i, value in enumerate(values):
        if value == target:
            indices.append(i)
    return indices

def linear_search_duplicates_pythonic(values: list, target: int) -> list:
    """
    Pythonic version of linear_search_duplicates using list comprehension.

    Implements the same functionality as linear_search_duplicates but uses
    a more concise Python list comprehension syntax.

    Args:
        values: List of integers to search through
        target: The integer value to search for

    Returns:
        A list containing all indices where the target value was found
    """
    return [i for i, value in enumerate(values) if value == target]

