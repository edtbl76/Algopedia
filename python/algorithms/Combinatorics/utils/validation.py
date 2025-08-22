"""
Validation utilities for combinatorial algorithms.
"""


def validate_inputs(n: int, k: int) -> None:
    """
    Validate inputs for combinatorial calculations (combinations and permutations).

    This function ensures that the mathematical preconditions for computing

    Mathematical Constraints:
        • n ≥ 0: Cannot have negative total items
        • k ≥ 0: Cannot choose negative number of items
        • k ≤ n: Cannot choose more items than available

    These constraints ensure that:
        1. The factorial operations n!, k!, and (n-k)! are well-defined
        2. The combinatorial interpretation makes sense
        3. All algorithmic implementations will produce valid results

    Args:
        n: Total number of items
        k: Number of items to arrange

    Raises:
        ValueError: If any constraint is violated

    Input Validation Strategy:
        The function performs fail-fast validation, checking constraints in
        order of logical dependency and providing specific error messages
        to aid in debugging and user understanding.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if k < 0:
        raise ValueError("k must be non-negative")
    if k > n:
        raise ValueError("k cannot be greater than n")

