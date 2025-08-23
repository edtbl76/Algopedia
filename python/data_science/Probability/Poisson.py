"""
Poisson Distribution Module

The Poisson distribution is a discrete probability distribution that models the number of events occurring
in a fixed interval of time or space when these events happen with a known average rate and independently of the time
since the last event.

Mathematical Foundation:
    The Poisson distribution is characterized by a single parameter λ (lambda),
    which represents both the mean and variance of the distribution. The
    probability mass function is given by:

    P(X = k) = (λ^k * e^(-λ)) / k!

    where:
    - k is the number of events (non-negative integer)
    - λ is the average rate parameter (positive real number)
    - e is Euler's number (≈ 2.71828)

Common Applications:
    - Number of phone calls received by a call center per hour
    - Number of defects in manufacturing per unit time
    - Number of particles emitted by radioactive decay per second
    - Number of network packet arrivals per time unit
    - Number of earthquakes in a region per year

Key Properties:
    - Domain: Non-negative integers {0, 1, 2, 3, ...}
    - Parameter space: λ > 0
    - Mean: E[X] = λ
    - Variance: Var(X) = λ
    - Standard deviation: σ = √λ

"""
import math


class PoissonDistribution:
    """
    Poisson Distribution for modeling discrete count events.

    Models the number of events occurring in a fixed interval with a known 
    average rate λ (lambda). Used for rare events that happen independently.

    Key Properties:
        - Mean = Variance = λ
        - Domain: Non-negative integers {0, 1, 2, ...}
        - Parameter: λ > 0 (average event rate)

    Common Applications:
        - Phone calls per hour, defects per unit time
        - Network packets, radioactive decay events
        - Queue arrivals, failure rates

    Numerical Features:
        - Automatic log-space computation for large λ or k values
        - Handles edge cases gracefully (returns 0.0 for invalid inputs)
        - Optimized for typical use cases with fallbacks for extremes

    Thread Safety:
        Immutable after initialization. Safe for concurrent reads in CPython (GIL).
        Other Python implementations may require explicit synchronization.
    """

    _ZERO_PROBABILITY = 0.0

    # Numerical stability thresholds for floating-point computation
    # These constants are based on IEEE 754 double-precision floating-point limitations
    # where Python's float type uses 64-bit representation with ~15-17 decimal digits of precision

    _OVERFLOW_THRESHOLD = 700
    # exp(700) ≈ 1.014 × 10^304, safely below IEEE 754 double-precision maximum (~1.798 × 10^308)
    # Values above ~709 cause exp() to overflow to infinity in 64-bit floating-point arithmetic
    # Conservative threshold provides safety margin for intermediate calculations

    _UNDERFLOW_THRESHOLD = -700
    # exp(-700) ≈ 10^-304, effectively zero in IEEE 754 double-precision representation
    # Probabilities smaller than this are negligible and can be safely returned as 0.0
    # Symmetric to overflow threshold for consistency in log-space calculations

    _LARGE_VALUE_THRESHOLD = 100

    # Combined threshold for detecting when both k and λ are moderately large
    # Prevents overflow in intermediate calculations like k*ln(λ) even when individual
    # values are below the main overflow threshold. Based on empirical testing of
    # numerical stability in the Poisson PMF computation

    def __init__(self, lambda_rate: float) -> None:
        """
        Initialize Poisson distribution with given rate parameter.

        Performs validation to ensure mathematical correctness and stores
        the rate parameter for subsequent probability calculations.

        Mathematical Constraint:
            λ > 0 is required because:
            - λ represents an average rate, which must be positive
            - The exponential term e^(-λ) must be well-defined and positive
            - Statistical interpretation requires a positive expected value

        Time Complexity: O(1)
            Single validation check and assignment operation

        Space Complexity: O(1)
            Stores only the rate parameter as instance variable

        Args:
            lambda_rate (float): Average rate of events (λ > 0)

        Raises:
            ValueError: If lambda_rate <= 0

        Example:
            >>> dist = PoissonDistribution(3.5)
            >>> dist.lambda_rate
            3.5
        """
        self._validate_lambda_rate(lambda_rate)
        self.lambda_rate = lambda_rate


    def pmf(self, k: int) -> float:
        """
        Compute Probability Mass Function P(X = k)

        Returns the probability of observing exactly k events.
        Uses direct computation for normal values, log-space for large values.

        Formula: P(X = k) = (λ^k * e^(-λ)) / k!

        where:
            - λ^k: Lambda raised to the power k
            - e^(-λ): Exponential decay term
            - k!: Factorial of k (number of ways to arrange k events)

        Algorithm Strategy:
            1. Validate input k for domain constraints
            2. Detect potential numerical instability scenarios
            3. For large values: use log-space computation to prevent overflow/underflow
            4. For normal ranges: use direct computation for optimal performance
            5. Handle edge cases gracefully with appropriate fallback mechanisms

        Numerical Stability Implementation:
            The method automatically switches between direct computation and log-space
            computation based on parameter values to prevent floating-point overflow,
            underflow, and precision loss. Log-space computation uses the identity:
            ln(P(X=k)) = k*ln(λ) - λ - ln(k!)

        Args:
            k: Number of events (non-negative integer)

        Returns:
            Probability of exactly k events (0.0 if invalid k)

        Time Complexity: O(log k)
        Space Complexity: O(1)


        Numerical Considerations:
            - Automatically handles large k or λ values using log-space computation
            - Prevents overflow in λ^k calculations before division occurs
            - Prevents underflow in exp(-λ) for very large λ values
            - Uses math.lgamma(k+1) = ln(k!) for numerical stability with large factorials
            - Returns 0.0 for cases where probability is negligibly small (< 10^-300)

        Args:
            k (int): Number of events (must be non-negative integer)

        Returns:
            float: Probability of exactly k events occurring
                  Returns 0.0 for invalid k values (k < 0) or negligibly small probabilities

        Example:
            >>> dist = PoissonDistribution(2.0)
            >>> dist.pmf(3)
            0.18044704431548356
            >>> dist.pmf(-1)  # Invalid k
            0.0
            >>> # Large value example - handled with log-space computation
            >>> big_dist = PoissonDistribution(500.0)
            >>> big_dist.pmf(500)  # Uses log-space automatically
            0.03568...
        """
        # Early return for invalid k values with zero probability
        if not self._validate_k_value(k):
            return self._ZERO_PROBABILITY
        
        
        # Detect numerical stability scenarios and switch to log-space computation
        # Three conditions: 
        # 1. k exceeds overflow threshold (prevents factorial-related overflow)
        # 2. λ exceeds overflow threshold (prevents exp(-λ) underflow to zero)
        # 3. Both k and λ are moderately large (prevents k*ln(λ) overflow)
        if (k > self._OVERFLOW_THRESHOLD or self.lambda_rate > self._OVERFLOW_THRESHOLD 
            or (k > self._LARGE_VALUE_THRESHOLD and self.lambda_rate > self._LARGE_VALUE_THRESHOLD)):
            
            
            return self._compute_pmf_log_space(k)
            
        # Standard direct computation for normal parameter ranges
        # This provides optimal performance for typical use cases. 
        try:
            # Compute individual terms of the Poisson PMF formula
            lambda_power_k = self.lambda_rate ** k  # λ^k term
            exponential_term = math.exp(-self.lambda_rate)  # e^(-λ) term
            factorial_k = math.factorial(k)  # k! term (denominator)

            # Assemble the final result
            result = (lambda_power_k * exponential_term) / factorial_k
            
            # Validate the result for potential numerical issues (NaN or infinity)
            if math.isnan(result) or math.isinf(result):
                result = self._ZERO_PROBABILITY

            return result
        
        except(OverflowError, ValueError):
            # Fallback to log-space computation if direct computation fails unexpectedly
            return self._compute_pmf_log_space(k)

    def cdf(self, k: int) -> float:
        """
        Compute Cumulative Distribution Function P(X ≤ k).

        Returns probability of observing k or fewer events by summing PMF values.
        Optimized to compute exponential term once rather than per PMF call.

        Formula: P(X ≤ k) = Σ(i=0 to k) (λ^i * e^(-λ)) / i!


        Algorithm Strategy:
            1. Validate input k for domain constraints
            2. Pre-compute e^(-λ) once for efficiency
            3. Iterate from i = 0 to k, computing PMF components directly
            4. Return total cumulative probability

        This approach optimizes performance by computing the expensive exponential
        term once rather than in each PMF call, while maintaining numerical accuracy.

        Args:
            k: Upper bound for cumulative probability (non-negative integer)

        Returns:
            Probability of k or fewer events (0.0 if invalid k)

        Time Complexity: O(k²) - due to k iterations × O(log k) per computation
        Space Complexity: O(1)


        Example:
            >>> dist = PoissonDistribution(2.0)
            >>> dist.cdf(3)
            0.857123460498547
            >>> dist.cdf(-1)  # Invalid k
            0.0
        
        # Edge case examples:
        >>> # Small λ: CDF rises quickly from 0
        >>> small_dist = PoissonDistribution(0.5)
        >>> small_dist.cdf(0)  # Probability of 0 or fewer events
        0.6065306597126334
        >>> small_dist.cdf(2)  # Most probability mass in first few values
        0.9856303364808416
        
        >>> # Large λ: CDF rises gradually, normal-like behavior
        >>> large_dist = PoissonDistribution(20.0)
        >>> large_dist.cdf(10)  # Well below mean
        0.010837026923297146
        >>> large_dist.cdf(20)  # Around the mean
        0.5594944670011475
    """
        # Early return for invalid k values with zero probability
        if not self._validate_k_value(k):
            return self._ZERO_PROBABILITY

        # Pre-compute the exponential term once for efficiency
        exponential_term = math.exp(-self.lambda_rate)
        
        # Accumulate probabilities from 0 to k (inclusive)
        cumulative_probability = 0.0
        
        for event_count in range(k + 1):
            # Compute PMF components directly without calling pmf()
            lambda_power_event_count = self.lambda_rate ** event_count
            factorial_event_count = math.factorial(event_count)
            pmf_value = (lambda_power_event_count * exponential_term) / factorial_event_count
            cumulative_probability += pmf_value
        
        return cumulative_probability

    def mean(self) -> float:
        """
        Compute the expected value (mean) of the Poisson distribution.

        For the Poisson distribution, the expected value equals the rate
        parameter λ. This is a fundamental property that makes the Poisson
        distribution particularly elegant and useful in practice.

        Mathematical Property:
            E[X] = λ

        Proof Outline:
            E[X] = Σ(k=0 to ∞) k * P(X = k)
                 = Σ(k=0 to ∞) k * (λ^k * e^(-λ)) / k!
                 = λ * e^(-λ) * Σ(k=1 to ∞) λ^(k-1) / (k-1)!
                 = λ * e^(-λ) * e^λ
                 = λ

        Time Complexity: O(1)
            Direct return of stored parameter value

        Space Complexity: O(1)
            No additional memory allocation

        Returns:
            float: Expected value of the distribution (equals λ)

        Example:
            >>> dist = PoissonDistribution(3.5)
            >>> dist.mean()
            3.5
        """
        return self.lambda_rate

    def variance(self) -> float:
        """
        Compute the variance of the Poisson distribution.

        For the Poisson distribution, the variance equals the rate parameter λ,
        which is the same as the mean. This equality is a unique property that
        distinguishes the Poisson distribution from other discrete distributions.

        Mathematical Property:
            Var(X) = λ

        Proof Outline:
            Var(X) = E[X²] - (E[X])²

            For Poisson distribution:
            E[X²] = E[X(X-1)] + E[X] = λ² + λ
            Therefore: Var(X) = (λ² + λ) - λ² = λ

        Practical Implications:
            - Standard deviation grows as √λ
            - Relative variability decreases as λ increases
            - For large λ, distribution approaches normal distribution

        Time Complexity: O(1)
            Direct return of stored parameter value

        Space Complexity: O(1)
            No additional memory allocation

        Returns:
            float: Variance of the distribution (equals λ)

        Example:
            >>> dist = PoissonDistribution(4.0)
            >>> dist.variance()
            4.0
        """
        return self.lambda_rate

    def standard_deviation(self) -> float:
        """
        Compute the standard deviation of the Poisson distribution.

        The standard deviation is the square root of the variance, which for
        the Poisson distribution equals √λ. This measure quantifies the
        typical deviation of observed values from the expected value.

        Mathematical Formula:
            σ = √(Var(X)) = √λ

        Statistical Interpretation:
            - Approximately 68% of observations fall within μ ± σ
            - Approximately 95% of observations fall within μ ± 2σ
            - As λ increases, absolute spread increases but relative spread decreases

        Numerical Implementation:
            Uses math.sqrt for accurate computation of the square root,
            which is more reliable than using fractional exponentiation.

        Time Complexity: O(1)
            Single square root computation using optimized math library

        Space Complexity: O(1)
            No additional memory allocation beyond return value

        Returns:
            float: Standard deviation of the distribution (equals √λ)

        Example:
            >>> dist = PoissonDistribution(9.0)
            >>> dist.standard_deviation()
            3.0
            >>> dist.standard_deviation() == math.sqrt(9.0)
            True
        """
        return math.sqrt(self.lambda_rate)

    ### Helper Methods ###
    
    def _compute_pmf_log_space(self, k: int) -> float:
        """
        Helper method to compute PMF using log-space computation for numerical stability.

        This method handles large k or λ values by computing ln(P(X=k)) and then
        converting back to probability space, preventing intermediate overflow/underflow.

        Args:
            k: Number of events (already validated)

        Returns:
            float: Probability computed in log-space, or 0.0 if negligibly small
        """
        try:
            # Log-space computation: ln(P(X=k)) = k*ln(λ) - λ - ln(k!)
            # This approach prevents intermediate overflow while maintaining precision
            k_times_ln_lambda = k * math.log(self.lambda_rate)  # k*ln(λ) term
            negative_lambda = -self.lambda_rate                 # -λ term
            negative_ln_k_factorial = -math.lgamma(k + 1)       # -ln(k!) term using lgamma(k+1)

            log_pmf = k_times_ln_lambda + negative_lambda + negative_ln_k_factorial

            # Convert back to probability space, handling underflow
            if log_pmf < self._UNDERFLOW_THRESHOLD:
                return self._ZERO_PROBABILITY

            return math.exp(log_pmf)


        except(OverflowError, ValueError):
            # if log computation fails, probability is negligibly small (< 10^-300), we'll nudge it to zero.
            return self._ZERO_PROBABILITY
        
        


    @staticmethod
    def _validate_lambda_rate(lambda_rate: float) -> None:
        """
        Validate that lambda rate parameter satisfies mathematical and computational constraints.

        Ensures the rate parameter meets the mathematical requirements for a valid
        Poisson distribution and provides warnings for edge cases that might affect
        computational performance or accuracy.

        Mathematical Requirements:
            λ > 0 is required because:
            - λ represents an average rate, which must be positive
            - The exponential term e^(-λ) must be well-defined and positive
            - Statistical interpretation requires a positive expected value
            - λ = 0 would make the distribution degenerate (not a proper Poisson)

        Computational Considerations:
            - Very small λ (< 1e-10) may cause precision issues
            - Very large λ (> 1000) will trigger log-space computation automatically
            - λ values near numerical limits are handled but may have reduced precision

        Time Complexity: O(1)
            Single series of validation checks and comparisons

        Space Complexity: O(1)
            No additional memory allocation

        Args:
            lambda_rate (float): Rate parameter to validate

        Raises:
            ValueError: If lambda_rate <= 0 or is not a valid number
            TypeError: If lambda_rate is not a numeric type

        Examples:
            >>> PoissonDistribution._validate_lambda_rate(2.5)
            # No exception - valid
            >>> PoissonDistribution._validate_lambda_rate(0)
            ValueError: Lambda rate must be positive, got 0
            >>> PoissonDistribution._validate_lambda_rate(-1.5)
            ValueError: Lambda rate must be positive, got -1.5
        """
        # Type validation
        if not isinstance(lambda_rate, (int, float)):
            raise TypeError(f"Lambda rate must be numeric, got {type(lambda_rate).__name__}")
        
        # Check for special float values
        if math.isnan(lambda_rate):
            raise ValueError("Lambda rate cannot be NaN")
        
        if math.isinf(lambda_rate):
            raise ValueError("Lambda rate cannot be infinite")
        
        # Mathematical constraint: λ > 0
        if lambda_rate <= 0:
            raise ValueError(f"Lambda rate must be positive, got {lambda_rate}")
        
        # Performance and accuracy warnings for edge cases
        if lambda_rate < 1e-10:
            import warnings
            warnings.warn(
                f"Very small lambda rate ({lambda_rate}) may cause numerical precision issues. "
                f"Consider using lambda >= 1e-10 for better accuracy.",
                UserWarning,
                stacklevel=3  # Point to the caller's code
            )
        
        if lambda_rate > 1000:
            import warnings
            warnings.warn(
                f"Large lambda rate ({lambda_rate}) will automatically use log-space computation "
                f"for numerical stability. This is handled transparently but may affect performance.",
                UserWarning,
                stacklevel=3
            )

    @staticmethod
    def _validate_k_value(k: int) -> bool:
        """
        Validate k value for probability calculations.

        Performs comprehensive validation of the k parameter to ensure it's suitable
        for Poisson distribution calculations. This method checks both mathematical
        validity and practical computational constraints.

        Mathematical Constraints:
            k ≥ 0 is required because:
            - Poisson distribution models count data (cannot be negative)
            - Factorial k! is undefined for negative integers
            - Physical interpretation requires non-negative event counts

        Computational Considerations:
            - Very large k values (k > 10000) may cause performance issues in CDF
            - k values near numerical limits may trigger log-space computation
            - Non-integer values are rejected to maintain mathematical correctness

        Time Complexity: O(1)
            Single series of validation checks

        Space Complexity: O(1)
            No memory allocation, returns primitive boolean

        Args:
            k (int): Number of events to validate

        Returns:
            bool: True if k is valid for computation, False otherwise

        Note:
            This method returns False for invalid k rather than raising
            an exception to enable graceful handling with zero probability
            return values in probability methods. However, it does provide
            warnings for edge cases that might cause performance issues.

        Examples:
            >>> PoissonDistribution._validate_k_value(5)
            True
            >>> PoissonDistribution._validate_k_value(-1)
            False
            >>> PoissonDistribution._validate_k_value(15000)  # Warning logged, but returns True
            True
        """
        # Basic type check - reject non-integers
        if not isinstance(k, int):
            return False
        
        # Mathematical constraint: k must be non-negative
        if k < 0:
            return False
        
        # Performance warning for very large k values in CDF calculations
        # These values are mathematically valid but may be computationally expensive
        if k > 10000:
            import warnings
            warnings.warn(
                f"Large k value ({k}) detected. CDF calculations may be slow. "
                f"Consider using approximations for k > 10000.",
                UserWarning,
                stacklevel=4  # Point to the actual calling code, not internal methods
            )
        
        # Extreme value warning - values that will likely trigger log-space computation
        if k > 100000:
            import warnings
            warnings.warn(
                f"Very large k value ({k}) will use log-space computation. "
                f"Results may have reduced precision for extremely large values.",
                UserWarning,
                stacklevel=4
            )
        
        return True