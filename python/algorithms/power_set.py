from typing import List, Set


def iterative_power_set(values: Set[int]) -> List[List[int]]:
    """
    Generate the power set of a given set using an iterative bit manipulation approach.

    Algorithm: Uses binary representation to enumerate all possible subsets. Each number
    from 0 to 2^n-1 represents a unique subset, where each bit position indicates whether
    to include the corresponding element from the input set.

    Time Complexity: O(n * 2^n) - we generate 2^n subsets, each taking O(n) time to construct
    Space Complexity: O(2^n) - storing all 2^n subsets in the result list

    Args:
        values: A set of integers to generate power set from

    Returns:
        A list containing all possible subsets (including empty set and original set)

    Examples:
        >>> iterative_power_set({1, 2})
        [[], [1], [2], [1, 2]]
        >>> iterative_power_set({1, 2, 3})
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """

    # Convert set to list for indexing
    values_list = list(values)
    size: int = 2 ** len(values_list)
    result: List[List[int]] = []

    # Iterate through all possible binary representations (0 to 2^n - 1)
    for mask in range(size):
        subset: List[int] = []

        # Check each bit position in the current mask
        for position in range(len(values_list)):

            # if bit at position is set, include the corresponding element
            if (mask & (1 << position)) > 0:
                subset.append(values_list[position])
        result.append(subset)
    return result


def recursive_power_set(values: List[int]) -> List[List[int]]:
    """
    Generate the power set of a given list using divide-and-conquer recursion.

    Algorithm: Recursively builds power set by considering two cases for each element:
    subsets that include the first element and subsets that don't include it.

    Time Complexity: O(2^n) - we generate exactly 2^n subsets
    Space Complexity: O(n * 2^n) - recursion depth O(n) plus O(2^n) space for result

    Args:
        values: A list of integers to generate power set from

    Returns:
        A list containing all possible subsets (including empty set and original set)

    Examples:
        >>> recursive_power_set([1, 2])
        [[1, 2], [1], [2], []]
        >>> recursive_power_set([1, 2, 3])
        [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    """

    # base case: empty list has only one subset (the empty subset)
    if len(values) == 0:
        return [[]]

    # recursive step: gets all subsets without the first element
    subsets_without_first_element = recursive_power_set(values[1:])

    # construct subsets that include the first element by prepending it to each existing subnet
    subsets_with_first_element = [[values[0]] + remaining for remaining in subsets_without_first_element]

    # combine both cases: subsets w/ and w/o the first element.
    return subsets_with_first_element + subsets_without_first_element

