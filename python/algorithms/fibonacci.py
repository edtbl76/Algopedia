from typing import Optional, Dict


def fibonacci_basic(n: int) -> int:
    """
    Calculate the nth Fibonacci number using basic recursion.

    This is a naive recursive implementation that demonstrates the classic
    Fibonacci algorithm but has exponential time complexity due to repeated
    calculations of the same subproblems.

    The Fibonacci sequence: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) for n>1

    Time Complexity: O(2^n) - exponential due to redundant calculations
    Space Complexity: O(n) - linear due to maximum recursion depth

    Args:
        n: A non-negative integer representing the position in Fibonacci sequence

    Returns:
        The nth Fibonacci number

    Examples:
        >>> fibonacci_basic(0)
        0
        >>> fibonacci_basic(1)
        1
        >>> fibonacci_basic(5)
        5
    """

    # Handle negative numbers by using absolute value
    n = abs(n)

    # Base cases: F(0) = 0 and F(1) = 1
    if n <= 1:
        return n

    # Recursive step: F(n) = F(n-1) + F(n-2) for n > 1
    return fibonacci_basic(n - 1) + fibonacci_basic(n - 2)



"""

    Sentinel object to detect when no memory dict was provided

    Sentinel Object Pattern Explanation:
    ------------------------------------
    Instead of using a mutable default argument like `memory: Dict[int, int] = {}`
    (which would create a shared dictionary across all function calls), we use
    a sentinel object `_SENTINEL` as the default value. This pattern:
    
    1. Avoids the "mutable default argument" anti-pattern where the same dict
       would be shared across all function calls
    2. Allows us to detect when no memory dict was explicitly provided
    3. Creates a fresh dictionary for each top-level call while allowing
       explicit memory dict passing for recursive calls
    4. Provides better control over when to initialize vs. reuse the cache
    
    Other patterns are the creation of a class or Extract Function refactoring, however
    these create indirection for this particular instance. 
"""
_SENTINEL = object()


def fibonacci_memoization(n: int, memory: Optional[Dict[int, int]] = _SENTINEL) -> int:
    """
    Calculate the nth Fibonacci number using memoization for optimal performance.

    This implementation uses dynamic programming with memoization to cache
    previously calculated results, reducing time complexity from exponential
    to linear. The sentinel object pattern is used to avoid the mutable
    default argument anti-pattern.

    Time Complexity: O(n) - each Fibonacci number is calculated only once
    Space Complexity: O(n) - for storing memoization cache and recursion stack

    Args:
        n: A non-negative integer representing the position in Fibonacci sequence
        memory: Optional dictionary for caching results. Uses sentinel pattern
                to detect when not provided and create a fresh cache.

    Returns:
        The nth Fibonacci number

    Examples:
        >>> fibonacci_memoization(0)
        0
        >>> fibonacci_memoization(10)
        55
        >>> # Using explicit memory dict
        >>> cache = {}
        >>> fibonacci_memoization(5, cache)
        5
        >>> len(cache)  # Cache now contains intermediate results
        6
    """

    # Handle negative numbers by using absolute value
    n = abs(n)

    # Initialize memory dict if sentinel was passed (no explicit memory provided)
    if memory is _SENTINEL:
        memory = {}

    # Base case: return cached result if already computed
    if n in memory:
        return memory[n]

    if n <= 1:
        # Base cases: F(0) = 0 and F(1) = 1
        result = n
    else:
        # Recursive step: F(n) = F(n-1) + F(n-2) for n > 1
        # Both recursive calls use the same memory dict to share cached results
        result = fibonacci_memoization(n - 1, memory) + fibonacci_memoization(n - 2, memory)

    # Cache the result before returning to avoid recalculation
    memory[n] = result
    return result

def fibonacci_iterative(n: int) -> int:
    """
    Calculate the nth Fibonacci number using iterative approach with dynamic array building.

    This implementation builds the Fibonacci sequence iteratively by maintaining
    a list of computed values, starting with the base cases [0, 1] and extending
    as needed. This approach provides O(n) time complexity while storing all
    intermediate results, making it memory-intensive but useful when multiple
    Fibonacci numbers might be needed.
    The Fibonacci sequence: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) for n>1

    Time Complexity: O(n) - builds sequence up to nth position
    Space Complexity: O(n) - stores all computed Fibonacci numbers up to n

    Args:
        n: A non-negative integer representing the position in Fibonacci sequence

    Returns:
        The nth Fibonacci number

    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(8)
        21
    """


    """
    
        Magic Number Elimination:
        ------------------------
        The initial values [0, 1] are extracted into a named constant to improve
        maintainability. In large codebases, magic numbers scattered throughout
        code become problematic because:
        - They're hard to locate and modify if the algorithm needs adjustment
        - Their meaning isn't immediately clear to other developers
        - They can be accidentally duplicated with slight variations
        - Testing and debugging becomes more difficult
        Using named constants makes the code self-documenting and centralizes
        these critical values for easier maintenance.
        
        I opted to add this as an example of production code. It's not necessary for a small example like this.
        
    """
    # Handle negative numbers by using absolute value
    n = abs(n)

    INITIAL_FIBONACCI_VALUES = [0, 1]
    fibonacci_sequence = INITIAL_FIBONACCI_VALUES.copy()

    last_computed_index = len(fibonacci_sequence) - 1

    if n <= last_computed_index:
        return fibonacci_sequence[n]

    while n > last_computed_index:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
        last_computed_index = len(fibonacci_sequence) - 1

    return fibonacci_sequence[n]


""" TODO - Implement additional Fibonacci algorithms
    - Tabulation (bottom-up dynamic programming): Build table from F(0) to F(n)
    - Matrix exponentiation: Use matrix multiplication for O(log n) complexity  
    - Binet's formula: Direct calculation using golden ratio (floating point precision issues)
    - Space-optimized iterative: O(1) space using only two variables
    
    Performance characteristics:
    - Tabulation: O(n) time, O(n) space - bottom-up approach, no recursion
    - Matrix exponentiation: O(log n) time, O(1) space - fastest for large n
    - Binet's formula: O(1) time, O(1) space - precision limited
    - Space-optimized: O(n) time, O(1) space - best space efficiency
"""


