def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.

    Time complexity: O(n) - linear recursion depth
    Space complexity: O(n) - due to call stack frames

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        ValueError: If n is negative

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """

    _validate_factorial_input(n)

    """ Base case: factorial(0) = 1 """
    if n == 0:
        return 1
    
    """ Recursive step: factorial(n) = n * factorial(n-1) for n > 0 """
    return n * factorial(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using iteration.
    Time complexity: O(n) - single loop
    Space complexity: O(1) - constant space

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n (n!)

    Raises:
        ValueError: If n is negative

    Examples:
        >>> factorial_iterative(0)
        1
        >>> factorial_iterative(5)
        120
    """
    _validate_factorial_input(n)

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def _validate_factorial_input(n: int) -> None:
    """
    Validate input for factorial calculation.

    Args:
        n: Integer to validate

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
