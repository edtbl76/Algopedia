"""
Combinatorics Module

Provides efficient implementations for calculating binomial coefficients (n choose k).
Multiple algorithmic approaches accommodate different use cases, from simple calculations
to scenarios requiring extensive caching.
"""
from enum import Enum
from functools import lru_cache
from typing import Dict, Tuple, Optional

from algorithms.Combinatorics.utils.optimization import optimize_k
from algorithms.Combinatorics.utils.validation import validate_inputs


class BinomialMethod(Enum):
    """
    Available binomial coefficient calculation methods.

    ITERATIVE:
    - Direct multiplicative computation
    - O(min(k, n-k)) time
    - O(1) space

    MEMOIZED:
    - Recursive with manual caching
    - O(n*k) time/space worst case

    TABULATION:
    - Bottom-up DP building Pascal's triangle
    - O(n*k) time/space

    RECURSIVE:
    - Pure recursive (educational only)
    - O(2^n) time
    - O(n) space

    RECURSIVE_LRU_CACHE:
    - Recursive with automatic LRU cache,
    - O(n*k) time/space

    Recommendations:
    - Single calculations: ITERATIVE
    - Repeated calculations: RECURSIVE_LRU_CACHE or MEMOIZED
    - Pascal's triangle: TABULATION
    - Educational: RECURSIVE (small inputs only)
    """
    ITERATIVE = "iterative"
    MEMOIZED = "memoized"
    TABULATION = "tabulation"
    RECURSIVE = "recursive"
    RECURSIVE_LRU_CACHE = "recursive_lru_cache"


def binomial_coefficient(n: int, k: int, method: BinomialMethod = BinomialMethod.ITERATIVE) -> int:
    """
    Calculate the binomial coefficient C(n, k) = n! / (k! * (n-k)!)

    Unified interface for computing binomial coefficients using different algorithms.
    Default ITERATIVE method provides optimal O(min(k, n-k)) performance for most cases.

    Args:
        n: Total number of items (non-negative)
        k: Number of items to choose (0 ≤ k ≤ n)
        method: Calculation method (see BinomialMethod enum)

    Returns:
        int: The binomial coefficient C(n, k)

    Raises:
        ValueError: If n < 0, k < 0, k > n, or method unsupported
    """
    validate_inputs(n, k)

    # Base Cases (Mathematical extreme: there is exactly one way each to choose 0/all items from a set)
    if k == 0 or k == n:
        return 1

    # Method dispatch table - maps enum values to corresponding implementation functions\
    # clean separation of concerns and easy extension for new methods -- provided they all have the same return type
    method_dispatch_map = {
         BinomialMethod.ITERATIVE: _binomial_iterative,
         BinomialMethod.MEMOIZED: _binomial_memoized,
         BinomialMethod.TABULATION: _binomial_tabulation,
         BinomialMethod.RECURSIVE: _binomial_recursive,
         BinomialMethod.RECURSIVE_LRU_CACHE: _binomial_recursive_lru
    }

    # Validate method selection
    if method not in method_dispatch_map:
        raise ValueError(f"Unsupported method: {method}")

    # Dispatches selection to the appropriate implementation function
    return method_dispatch_map[method](n, k)


def _binomial_iterative(n: int, k:int) -> int:
    """
    Calculate binomial coefficient using optimized iterative approach.

    Uses multiplicative formula C(n,k) = ∏(i=0 to k-1) [(n-i)/(i+1)] with
    symmetry optimization and immediate division to prevent overflow.

    Time: O(min(k, n-k)), Space: O(1)
    """

    # Symmetry optimization (reduces computational complexity from O(k) to O(min(k, n-k))
    k = optimize_k(n, k)

    # Multiplicative formula
    result = 1

    # This syntax is explicit and important.
    # The immediate division for each multiplication operation is used to prevent overflow.
    # Placing these operations on separate lines are at risk of overflow.
    for i in range(k):
        # multiplying the result by (n - i) and dividing by (i + 1) maintains ==> result *= (n - i) // (i + 1)
        result = result * (n - i) // (i + 1)

    return result


def _binomial_memoized(n: int, k: int, memo: Optional[Dict[Tuple[int, int], int]] = None) -> int:
    """
    Calculate binomial coefficient using recursive memoization.

    Implements Pascal's identity C(n,k) = C(n-1,k-1) + C(n-1,k) with dictionary
    caching to avoid redundant computation.

    Time: O(n*k) worst case, O(1) cached
    Space: O(n*k) for cache + O(n) recursion stack

    Args:
        memo: Optional cache dict for reuse across calls
    """
    if memo is None:
        memo = {}

    if (n, k) in memo:
        return memo[(n, k)]

    # Base Cases (Mathematical extreme: there is exactly one way each to choose 0/all items from a set)
    # (Note: These terminate recursion)
    if k == 0 or k == n:
        return 1

    # Recursive computation using Pascal's identity: C(n,k) = C(n-1,k-1) + C(n-1,k)
    # This breaks the problem into two smaller, overlapping subproblems
    # _binomial_memoized(n - 1, k - 1, memo): Choose item n, then choose k-1 from remaining n -1
    # _binomial_memoized(n - 1, k, memo): Don't Choose item n, choose k from remaining n - 1
    result = _binomial_memoized(n - 1, k - 1, memo) + _binomial_memoized(n - 1, k, memo)

    memo[(n, k)] = result
    return result

def _binomial_tabulation(n: int, k: int) -> int:
    """
    Calculate binomial coefficient using bottom-up dynamic programming (tabulation).

    This method implements the tabulation approach to dynamic programming, building
    a 2D table that represents a portion of Pascal's triangle. Unlike memoization
    (top-down), tabulation works bottom-up, systematically filling the table from
    base cases to the target value. This approach guarantees that all dependencies
    are computed before they are needed.

    Pascal's Triangle Foundation:
        The algorithm builds Pascal's triangle where entry (i,j) represents C(i,j):

        Row 0:           1
        Row 1:         1   1
        Row 2:       1   2   1
        Row 3:     1   3   3   1
        Row 4:   1   4   6   4   1

        Each entry equals the sum of the two entries above it, implementing
        Pascal's identity: C(i,j) = C(i-1,j-1) + C(i-1,j)

    Space Optimization:
        The implementation applies the symmetry property C(n,k) = C(n,n-k) to
        reduce space complexity. By using min(k, n-k), we build only the left
        half of Pascal's triangle, cutting space requirements roughly in half.

    Table Construction Strategy:
        1. Initialize table[i][0] = 1 for all rows (base case: choosing 0 items)
        2. Fill each row using values from the previous row
        3. Use Pascal's identity for interior entries
        4. Boundary conditions prevent array out-of-bounds access

    Time: O(n*k)
    Space: O(n*k)

    Args:
        n: Total number of items (pre-validated)
        k: Number of items to choose (pre-validated)

    Returns:
        int: The binomial coefficient C(n,k)

    Memory Layout:
        table[i][j] represents C(i,j) where:
        • i ranges from 0 to n (row index)
        • j ranges from 0 to k (column index)
        • Entry dependencies: table[i][j] depends on table[i-1][j-1] and table[i-1][j]
    """
    # Symmetry optimization (reduces computational complexity from O(k) to O(min(k, n-k))
    k = optimize_k(n, k)

    # Initialize 2D table - table[i][j] will store C(i,j)
    # Dimensions: (n+1) rows × (k+1) columns
    # Extra row/column for 0-indexing convenience with 1-based mathematical notation
    table = [[0] * (k + 1) for _ in range(n + 1)]

    # Fill base cases: C(i,0) = 1 for all i
    # Combinatorial interpretation: exactly one way to choose 0 items from any set
    for i in range(n + 1):
        table[i][0] = 1

    # Build table bottom-up using Pascal's identity
    # For each position (i,j), compute C(i,j) = C(i-1,j-1) + C(i-1,j)
    #
    # We start from row 1 (base case row 0 was already filled)
    for i in range(1, n + 1):
        # Structure the range so we avoid out-of-bounds and impossible calculations.
        for j in range(1, min(i + 1, k + 1)):

            # Pascal's identity: ways to choose j from i items equals:
            # (ways to choose j-1 from first i - 1, then take the ith) +
            # (ways to choose j from first i - 1, then take the ith)
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

    # Return the computed binomial coefficient C(n,k) from the final table position
    return table[n][k]


def _binomial_recursive(n: int, k: int) -> int:
    """
    Calculate binomial coefficient using pure recursion (educational only).

    Direct implementation of Pascal's identity. Exponential time complexity
    makes it impractical for n > 20. Use for teaching or small inputs only.

    Time: O(2^n), Space: O(n) recursion stack
    """

    # Base cases - mathematical extrema. These terminate recursion and provide foundation for Pascal's identity.
    # C(n,0) = 1, there is exactly one way to choose no items from a set
    # C(n,n) = 1, there is exactly one way to choose all items from a set.
    if k == 0 or k == n:
        return 1

    # Recursive decomposition using Pascal's identity
    # C(n,k) = C(n-1,k-1) + C(n-1,k)
    #
    # Mathy interpretation
    # When selecting k items from n items, we hape the option to:
    # 1. Include the nth item, then choose from the remaining n-1 items (_binomial_recursive(n - 1, k - 1))
    # 2. Exclude the nth item, then choose from the remaining n-1 items (_binomial_recursive(n - 1, k))
    #
    # The total number of ways to choose k items from n items is the sum of the two:
    # C(n-1,k-1) + C(n-1,k)
    return _binomial_recursive(n - 1, k - 1) + _binomial_recursive(n - 1, k)


@lru_cache(maxsize=None)
def _binomial_recursive_lru(n: int, k: int) -> int:
    """
    Calculate binomial coefficient using recursive approach with LRU cache.

    This implementation combines the mathy elegance of the recursive approach
    with the performance benefits of automatic memoization provided by Python's
    functools.lru_cache decorator.

    The LRU (Least Recently Used) cache automatically manages memory by evicting old entries when the cache reaches
    its size limit, though we use maxsize=None for unlimited caching in this case.

    LRU Cache Mechanism:
        The @lru_cache decorator intercepts function calls and:
        1. Checks if the arguments (n,k) have been seen before
        2. If cached, returns the stored result immediately (O(1))
        3. If not cached, executes the function and stores the result
        4. Manages cache size automatically using LRU eviction policy

    Comparison with Manual Memoization:
        Advantages of LRU cache:
        • Automatic cache management (no manual dictionary handling)
        • Built-in cache statistics and monitoring capabilities
        • Thread-safe implementation for concurrent use
        • Optimized C implementation for better performance
        • Automatic memory management with configurable size limits

        Disadvantages:
        • Less control over cache behavior and eviction policies
        • Global cache shared across all calls to this function
        • Cannot easily customize cache key generation or storage format

    Mathematical Foundation:
        Identical to _binomial_recursive(), implementing Pascal's identity:
        C(n,k) = C(n-1,k-1) + C(n-1,k)

        The recursion tree structure remains the same, but overlapping
        subproblems are now cached, eliminating redundant computations.

    Cache Performance Analysis:
        • First call to C(n,k): O(n*k) time to build complete cache
        • Subsequent identical calls: O(1) time from cache lookup
        • Related calls: Benefit from partial cache overlap
        • Memory usage: O(n*k) for storing unique subproblem results


    Time: O(n*k)
    Space: O(n*k) recursion stack
    Args:
        n: Total number of items (pre-validated)
        k: Number of items to choose (pre-validated)

    Returns:
        int: The binomial coefficient C(n,k)

    Cache Configuration:
        • maxsize=None: Unlimited cache size (no automatic eviction)
        • Alternative: Set maxsize=128 or other value for bounded cache
        • Cache statistics available via function.cache_info()
        • Cache can be cleared manually via function.cache_clear()
    """
    # Base cases - identical to recursive version
    # These terminate the recursion and provide foundation values
    if k == 0 or k == n:
        return 1

    # Recursive implementation using Pascal's identity
    # The @lru_cache decorator automatically handles memoization
    # Each recursive call is cached, eliminating redundant computation
    return _binomial_recursive_lru(n - 1, k - 1) + _binomial_recursive_lru(n - 1, k)








