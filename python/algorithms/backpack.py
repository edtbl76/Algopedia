from typing import List
"""
Backpack/Knapsack Problem Implementation

This module provides two solutions to the classic 0/1 Knapsack problem:
1. Recursive solution with exponential time complexity
2. Dynamic programming solution with polynomial time complexity

The 0/1 Knapsack problem is a classic optimization problem where given a set of items,
each with a weight and value, the goal is to determine the number of each item to include
in a collection so that the total weight is less than or equal to a given limit and the
total value is as large as possible. In the 0/1 variant, each item can only be selected
once (hence "0/1" - either take it or leave it).

Example Problem:
- Knapsack capacity: 10 kg
- Items: [(weight=2, value=3), (weight=3, value=4), (weight=4, value=5), (weight=5, value=6)]
- Optimal solution: Take items with weights [2, 3, 5] for total value = 13

"""


def recursive_backpack(weight_max: int, weights: List[int], values: List[int], item_index: int = 0) -> int:
    """
    Solve the Backpage problem using a recursive approach.

    This function uses a top-down recursive approach to explore all possible combinations
    of items. For each item, it decides whether to include it or exclude it, and returns
    the maximum value achievable.

    Args:
        weight_max (int): Maximum weight capacity of the knapsack
        weights (List[int]): List of item weights
        values (List[int]): List of item values (same order as weights)
        item_index (int, optional): Current item index being considered. Defaults to 0.

    Returns:
        int: Maximum value that can be achieved within the weight constraint

    Time Complexity: O(2^n) where n is the number of items
    Space Complexity: O(n) due to recursion stack depth

    Examples:
        >>> weights = [2, 3, 4, 5]
        >>> values = [3, 4, 5, 6]
        >>> recursive_backpack(10, weights, values)
        13

        >>> weights = [1, 3, 4]
        >>> values = [15, 20, 30]
        >>> recursive_backpack(5, weights, values)
        45
    """
    # Base case: no capacity left or no more items to consider
    if weight_max == 0 or item_index >= len(weights):
        return 0

    # Recursive case 1: Current item is too heavy to include
    # Skip this item and move to the next one
    if weights[item_index] > weight_max:
        return recursive_backpack(weight_max, weights, values, item_index + 1)

    # Recursive case 2: We have a choice - include or exclude current item
    # Calculate value if we include the current item
    include = values[item_index] + recursive_backpack(
        weight_max - weights[item_index], weights, values, item_index + 1
    )
    # Calculate value if we exclude the current item
    exclude = recursive_backpack(weight_max, weights, values, item_index + 1)

    # Return the maximum of including or excluding the current item
    return max(include, exclude)


def dynamic_backpack(weight_max: int, weights: List[int], values: List[int]) -> int:
    """
    Solve the Backpack problem using dynamic programming approach.

    This function uses a bottom-up dynamic programming approach with a 2D matrix
    where dp[i][w] represents the maximum value achievable using the first i items
    with a weight limit of w.

    Args:
        weight_max (int): Maximum weight capacity of the knapsack
        weights (List[int]): List of item weights
        values (List[int]): List of item values (same order as weights)

    Returns:
        int: Maximum value that can be achieved within the weight constraint

    Time Complexity: O(n * W) where n is number of items and W is weight capacity
    Space Complexity: O(n * W) for the DP matrix

    Examples:
        >>> weights = [2, 3, 4, 5]
        >>> values = [3, 4, 5, 6]
        >>> dynamic_backpack(10, weights, values)
        13

        >>> weights = [1, 3, 4]
        >>> values = [15, 20, 30]
        >>> dynamic_backpack(5, weights, values)
        45
    """
    # Initialize dimensions: rows = items + 1, cols = weight capacity + 1

    # Matrix of rows (number of items) v.s columns (weight maximum + 1)
    num_items = len(weights)
    rows = num_items + 1    # +1 includes the base case of 0 items
    cols = weight_max + 1   # +1 includes weight capacity of 0

    # Initialize DP matrix with zeros
    # matrix[i][w] = max value using first i items with weight limit w
    matrix = [[0 for x in range(cols)] for y in range(rows)]

    # Fill the DP matrix using bottom-up approach
    # Outer loop: iterate through each item (1-indexed to match matrix)
    for item_idx in range(1, rows):
        # Inner loop: iterate through each possible weight capacity
        for current_weight in range(cols):
            # Get current item's properties (0-indexed for weights/values arrays)
            item_weight = weights[item_idx - 1]
            item_value = values[item_idx - 1]

            # Check if current item can fit in the current weight capacity
            if item_weight <= current_weight:
                # We have a choice: include or exclude the current item
                # Option 1: Include current item
                include = item_value + matrix[item_idx - 1][current_weight - item_weight]
                # Option 2: Exclude current item (take value from previous row)
                exclude = matrix[item_idx - 1][current_weight]
                # Choose the maximum of both options
                matrix[item_idx][current_weight] = max(include, exclude)
            else:
                # Current item is too heavy, exclude it
                # Copy value from previous row (same weight, one less item)
                matrix[item_idx][current_weight] = matrix[item_idx - 1][current_weight]

    # Return the maximum value using all items with full weight capacity
    return matrix[num_items][weight_max]

