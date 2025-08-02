# TAGS: Recursion, Iteration

def multiplication(multiplicand: int, multiplier: int) -> int:
    """
    Multiply two integers using iterative addition approach.

    This algorithm performs multiplication by repeatedly adding the multiplicand
    to itself for the number of times specified by the multiplier.

    Time Complexity: O(n) - where n is the absolute value of the multiplier.
                    The loop executes exactly |multiplier| times.
    Space Complexity: O(1) - uses only a constant amount of extra space
                     regardless of input size.

    Args:
        multiplicand: The number to be multiplied
        multiplier: The number of times to add the multiplicand (can be negative)

    Returns:
        The product of multiplicand and multiplier

    Examples:
        >>> multiplication(6, 4)
        24
        >>> multiplication(5, -3)
        -15
        >>> multiplication(7, 0)
        0

    Note:
        Handles negative multipliers by using absolute value in calculation
        and applying sign correction to the final result.
    """
    # Multiplication by 0 is always 0
    if multiplier == 0:
        return 0

    # Normalize inputs and determine the result sign
    normalized_multiplicand, normalized_multiplier, is_negative = _validate_multiplication_inputs(multiplicand,
                                                                                                  multiplier)
    # Iteratively add multiplicand to accumulate the product.
    product = 0
    for i in range(normalized_multiplier):
        product += normalized_multiplicand

    # Apply sign correction based on original multiplier sign
    return -product if is_negative else product


def multiplication_recursive(multiplicand: int, multiplier: int) -> int:
    """
    Multiply two integers using recursive addition approach.

    This algorithm implements multiplication through recursive decomposition,
    breaking down the multiplication into smaller subproblems until reaching
    the base case.

    Time Complexity: O(n) - where n is the absolute value of the multiplier.
                    Makes exactly |multiplier| recursive calls.
    Space Complexity: O(n) - due to call stack depth of |multiplier| recursive calls.

    Args:
        multiplicand: The number to be multiplied
        multiplier: The number of times to add the multiplicand (can be negative)

    Returns:
        The product of multiplicand and multiplier

    Examples:
        >>> multiplication_recursive(6, 4)
        24
        >>> multiplication_recursive(5, -3)
        -15
        >>> multiplication_recursive(7, 0)
        0

    Note:
        Uses a nested helper function to maintain clean interface while
        handling the recursive logic with normalized positive values.
    """
    # Base case: multiplication by zero always yields zero

    if multiplier == 0:
        return 0

    # Normalize inputs and determine result sign
    normalized_multiplicand, normalized_multiplier, is_negative = _validate_multiplication_inputs(multiplicand,
                                                                                                  multiplier)

    def _recursive_multiply(m: int, n: int) -> int:
        """
        Inner recursive helper function for multiplication.

        Implements the core recursive multiplication algorithm using
        the mathematical principle: m × n = m + (m × (n-1))

        I like doing this to hide the recursive logic from the outer function call.

        Time Complexity: O(n) - makes exactly n recursive calls
        Space Complexity: O(n) - call stack depth equals n

        Args:
            m: multiplicand value (always positive after normalization)
            n: multiplier value (always positive after normalization)

        Returns:
            Product of m and n using recursive addition
        """
        # Base case: multiplying by zero results in zero (when no more additions are needed)
        if n == 0:
            return 0

        # Recursive step: m × n = m + (m × (n-1))
        # Add multiplicand once and recursively calculate remaining product
        return m + _recursive_multiply(m, n - 1)

    # Calculate product using normalized positive values, then apply sign correction based on
    # the original multiplier sign.
    product = _recursive_multiply(normalized_multiplicand, normalized_multiplier)
    return -product if is_negative else product


def _validate_multiplication_inputs(multiplicand: int, multiplier: int) -> tuple[int, int, bool]:
    """
    Validate and normalize inputs for multiplication functions.

    Handles negative multipliers by converting them to positive values
    and tracking whether the final result should be negated.

    Time Complexity: O(1) - constant time operations only
    Space Complexity: O(1) - uses only a fixed amount of extra space

    Args:
        multiplicand: The number to be multiplied (multiplicand × multiplier)
        multiplier: The number of times to add the multiplicand

    Returns:
        tuple: (normalized_multiplicand, normalized_multiplier, is_result_negative)
            - normalized_multiplicand: unchanged multiplicand value
            - normalized_multiplier: absolute value of multiplier
            - is_result_negative: True if final result should be negative

    Examples:
        >>> _validate_multiplication_inputs(5, -3)
        (5, 3, True)
        >>> _validate_multiplication_inputs(4, 2)
        (4, 2, False)
    """
    if multiplier < 0:
        return multiplicand, -multiplier, True
    return multiplicand, multiplier, False
