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
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    """ Base case: factorial(0) = 1 """
    if n == 0:
        return 1
    
    """ Recursive step: factorial(n) = n * factorial(n-1) for n > 0 """
    return n * factorial(n - 1)


