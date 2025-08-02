# TAGS: Recursion, Iteration

def sum_digits_iterative(n: int) -> int:
    """
    Calculate the sum of digits in a non-negative integer using iterative approach.

    This function iteratively extracts each digit using modulo and integer division
    operations, accumulating the sum until all digits have been processed.

    Time Complexity: O(log n) - where n is the input value, since we process
                     each digit once and there are log₁₀(n) digits in n
    Space Complexity: O(1) - constant space, only using a few variables

    Args:
        n: A non-negative integer whose digits will be summed

    Returns:
        The sum of all digits in n

    Raises:
        ValueError: If n is negative

    Examples:
        >>> sum_digits_iterative(123)
        6
        >>> sum_digits_iterative(0)
        0
        >>> sum_digits_iterative(9)
        9
    """

    _validate_non_negative(n)
    total: int = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def sum_digits_recursive(n: int) -> int:
    """
    Calculate the sum of digits in a non-negative integer using recursion.

    This function recursively breaks down the problem by extracting the last digit
    and recursively summing the remaining digits until reaching the base case.

    Time Complexity: O(log n) - where n is the input value, since we make one
                     recursive call per digit and there are log₁₀(n) digits in n
    Space Complexity: O(log n) - linear space due to recursion stack depth of
                      log₁₀(n) frames

    Args:
        n: A non-negative integer whose digits will be summed

    Returns:
        The sum of all digits in n

    Raises:
        ValueError: If n is negative

    Examples:
        >>> sum_digits_recursive(123)
        6
        >>> sum_digits_recursive(0)
        0
        >>> sum_digits_recursive(9)
        9
    """


    _validate_non_negative(n)

    # Base case: single digit numbers return themselves
    if n <= 9:
        return n

    # Recursive case: last digit + sum of remaining digits
    return n % 10 + sum_digits_recursive(n // 10)


def _validate_non_negative(n: int) -> None:
    """Validate that the input is a non-negative integer."""
    if n < 0:
        raise ValueError("Not defined for negative numbers")
