"""
Optimization Utilities for Combinatorics
"""

def optimize_k(n: int, k: int) -> int:
    """
    Optimize k using the symmetry property C(n,k) = C(n,n-k).

    This function exploits one of the most important mathematical properties
    of combinatorics: symmetry. The symmetry property states that
    choosing k items from n is equivalent to choosing (n-k) items from n,
    since choosing k items to include is the same as choosing (n-k) items to exclude.

    Mathematical Foundation of Symmetry:
        C(n,k) = n! / (k! * (n-k)!) = n! / ((n-k)! * k!) = C(n,n-k)

        Proof by algebraic manipulation:
        • The factorial expressions are identical when k and (n-k) are swapped
        • This is because multiplication is commutative: k! * (n-k)! = (n-k)! * k!
        • The numerator n! remains unchanged

    Combinatorial Interpretation:
        The symmetry has a natural combinatorial explanation:
        • Choosing k items to include from n items
        • Is equivalent to choosing (n-k) items to exclude from n items
        • These represent the same partition of the n items

        Example: From 5 people, choosing 2 to form a committee is the same as
        choosing 3 to NOT be on the committee. Both result in the same 2-person committee.

    Computational Benefits:
        By always computing C(n, min(k, n-k)), we ensure:

        1. Reduced Time Complexity:
           • Iterative method: O(min(k, n-k)) vs O(k)
           • When k > n/2, we compute O(n-k) instead of O(k)
           • Maximum iterations reduced from n to n/2

        2. Reduced Space Complexity:
           • Tabulation method: O(n * min(k, n-k)) vs O(n * k)
           • For large k, this can halve memory usage
           • Cache efficiency improved due to smaller parameter ranges

        3. Numerical Stability:
           • Smaller intermediate values reduce overflow risk
           • Fewer multiplication operations reduce accumulated rounding errors
           • More balanced computation trees in recursive approaches

    Time Complexity: O(1)
        • Single comparison and arithmetic operation
        • No loops, recursion, or complex data structures
        • Constant time regardless of input size

    Space Complexity: O(1)
        • Uses only primitive variables for computation
        • No additional data structures allocated
        • Memory usage independent of input parameters

    Args:
        n: Total number of items (assumed valid from prior validation)
        k: Number of items to choose (assumed valid from prior validation)

    Returns:
        int: The smaller of k or (n-k), maintaining mathematical equivalence
             while optimizing computational efficiency

    Mathematical Guarantee:
        The returned value k' satisfies:
        • C(n,k') = C(n,k) (mathematical correctness preserved)
        • k' ≤ n/2 (optimization achieved)
        • 0 ≤ k' ≤ n (validity maintained)
    """
    # Return the minimum of k and (n-k) to exploit symmetry
    # This ensures we always compute the "smaller half" of the binomial coefficient
    # Mathematical equivalence: C(n,k) = C(n,n-k) guarantees correctness
    return min(k, n - k)
