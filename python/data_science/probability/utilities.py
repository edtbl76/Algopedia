"""
This is just a generic utilities file for helper functions.

- Calculate probability

"""
import math
from typing import Set, Any, Union, Callable


### Math Utilities

def calculate_probability(event: Set[Any], state_space: Set[Any]) -> float:
    """
    Calculate probability of an event in a discrete uniform probability space.

    Assumes all outcomes in the state space are equally likely, so probability
    is calculated as the ratio of favorable outcomes to total outcomes.

    Time Complexity: O(1) - uses built-in len() which is constant time for sets
    Space Complexity: O(1) - only stores scalar values

    Args:
        event (Set[Any]): Set of favorable outcomes
        state_space (Set[Any]): Complete set of all possible outcomes

    Returns:
        float: probability of the event (number between 0 and 1)

    Raises:
        ValueError: If state_space is empty (division by zero prevention)

    Note:
        This function assumes a uniform distribution where each outcome
        has equal probability of 1/|state_space|.
    """
    if len(state_space) == 0:
        raise ValueError("State space cannot be empty")

    # Classical probability: favorable outcomes / total outcomes
    return len(event) / len(state_space)


def binomial_coefficient(n: int, k: int) -> int:
    """
    Compute the binomial coefficient C(n,k) using an optimized iterative approach.
    
    Formula: C(n,k) = n!/(k!(n-k)!)
    
    This implementation uses the multiplicative formula with symmetry optimization
    and immediate division to prevent overflow, avoiding the computational expense
    and numerical instability of factorial calculations.
    
    Args:
        n: Total number of items (must be non-negative)
        k: Number of items to choose (must satisfy 0 ≤ k ≤ n)
        
    Returns:
        int: The binomial coefficient C(n,k)
        
    Raises:
        ValueError: If n < 0, k < 0, or k > n
        
    Examples:
        >>> binomial_coefficient(5, 2)
        10
        >>> binomial_coefficient(10, 0)
        1
        >>> binomial_coefficient(4, 4)
        1
        
    Time Complexity: O(min(k, n-k))
    Space Complexity: O(1)
    """
    # Input validation
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if k < 0:
        raise ValueError(f"k must be non-negative, got {k}")
    if k > n:
        raise ValueError(f"k cannot be greater than n, got k={k}, n={n}")
    
    # Base cases - mathematical extrema
    if k == 0 or k == n:
        return 1
    
    # Symmetry optimization: C(n,k) = C(n,n-k)
    # Use the smaller of k and n-k to minimize computations
    k = min(k, n - k)
    
    # Multiplicative formula: C(n,k) = ∏(i=0 to k-1) [(n-i)/(i+1)]
    # Perform division at each step to prevent integer overflow
    result = 1
    for i in range(k):
        # Critical: multiply first, then divide to maintain integer arithmetic
        # while preventing overflow by dividing at each step
        result = result * (n - i) // (i + 1)
    
    return result
    

def is_convex_approx(function: Callable[[float], float]) -> bool | None:
    """
    Approximate convexity check (uses second derivative)

    This is a very basic check.

    Convexity is a property of a function that is preserved by a monotonic transformation.
    """
    try:
        # Test convexity at a few points
        test_points = [0.0, 0.25, 0.5, 0.75, 1.0]
        htm = 0.001

        for x in test_points:
            second_derivative = (function(x + htm) - 2 * function(x) + function(x - htm)) / (htm ** 2)
            if second_derivative < -0.01:
                return False
        return True
    except:
        return



def log_binomial_coefficient(n:int, k:int) -> float:
    """
    Compute the natural logarithm of the binomial coefficient C(n,k).

    Uses log-gamma function for numerical stability with large numbers.
    This prevents overflow that would occur with direct factorial computation
    when n or k are large (e.g., n! for n > 170 overflows in standard float64).

    Numerical Stability Explanation:
    - Direct computation: C(n,k) = n!/(k!(n-k)!) can overflow for large n
    - Log-space computation: ln(C(n,k)) = ln(n!) - ln(k!) - ln((n-k)!)
    - Using lgamma: ln(m!) = lgamma(m+1) for any positive integer m
    - Final result: exp(ln(C(n,k))) gives us C(n,k) without intermediate overflow

    Args:
        n: total number of items (trials)
        k: number of items to choose (successes)

    Returns:
        float: natural logarithm of binomial coefficient C(n,k) (i.e. ln(C(n,k)))
    """
    if k < 0 or k > n:
        # ln(0) is -inf; callers typically guard before exponentiating.
        return float("-inf")

    # Handle edge cases where combination equals 1 (ln(1) = 0)
    if k == 0 or k == n:
        return 0.0

    # Apply symmetry for optimization, as C(n, k) = C(n, n-k)
    k = min(k, n - k)

    # The formula for ln(C(n,k)) is ln(n!) - (ln(k!) + ln((n-k)!))
    # We use math.lgamma(x + 1) which is equivalent to ln(x!)

    # 1. Calculate the log of the numerator's factorial
    log_n_factorial = math.lgamma(n + 1)

    # 2. Calculate the log of the denominator's factorials
    log_k_factorial = math.lgamma(k + 1)
    log_n_minus_k_factorial = math.lgamma(n - k + 1)

    # 3. Assemble the result by subtracting the denominator's parts from the numerator's
    log_coefficient = log_n_factorial - (log_k_factorial + log_n_minus_k_factorial)

    return log_coefficient


### Validation Methods

def validate_probability(probability: Union[int, float]) -> None:
    """
    Validates the probability parameter.

    Ensures that the probability is a number between 0 and 1 (inclusive).

    Args:
        probability: Value to validate

    Raises:
        ValueError: If probability is not between 0 and 1
        TypeError: If probability is not a number
    """
    if not isinstance(probability, (int, float)):
        raise TypeError(f"Probability must be numeric, got {type(probability).__name__}")

    if not 0 <= probability <= 1:
        raise ValueError(f"Probability must be between 0 and 1 (inclusive), got {probability}")

def validate_positive_float(value: float) -> None:
    if not isinstance(value, float) or value <= 0.0:
        raise ValueError(f"Value must be a positive float, got {value}")

def validate_positive_integer(value: int) -> None:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Value must be a positive integer, got {value}")