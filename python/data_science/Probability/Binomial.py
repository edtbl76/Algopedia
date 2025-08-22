"""
Binomial Distribution

This module implements the Binomial distribution, a discrete probability distribution
that models the number of successes in a fixed number of independent Bernoulli trials,
where each trial has the same probability of success.

Mathematical Definition:
    The probability mass function (PMF) of a Binomial distribution is:

    P(X = k) = C(n,k) × p^k × (1-p)^(n-k)    for k ∈ {0, 1, 2, ..., n}

    Where:
        • X is the random variable (number of successes)
        • k is the observed number of successes (0 ≤ k ≤ n)
        • n is the total number of independent trials
        • p is the probability of success on each trial (0 ≤ p ≤ 1)
        • C(n,k) is the binomial coefficient "n choose k" = n!/(k!(n-k)!)

Key Terms:
    • Combination (C(n,k)): The number of ways to choose k items from n items without
      regard to order. Mathematically defined as n!/(k!(n-k)!), representing the
      binomial coefficient that counts the number of possible arrangements.

    • Numerical Stability: The property of an algorithm to produce accurate results
      even when dealing with very large or very small numbers that might cause
      floating-point overflow, underflow, or precision loss. In this implementation,
      we achieve stability by working in logarithmic space for large factorials.

Statistical Properties:
    • Mean (Expected Value): E[X] = np
    • Variance: Var(X) = np(1-p)
    • Standard Deviation: σ = √(np(1-p))
    • Mode: ⌊(n+1)p⌋ for most cases

Historical Context:
    The binomial distribution was first studied by Jacob Bernoulli in "Ars Conjectandi"
    (1713). It generalizes the Bernoulli distribution for multiple trials and forms
    the foundation for many statistical applications including hypothesis testing,
    quality control, and sampling theory.

Common Applications:
    • Quality control: Number of defective items in a production batch
    • Clinical trials: Number of successful treatments out of n patients
    • Survey research: Number of positive responses to yes/no questions
    • Marketing: Number of customers who make a purchase out of n contacts
    • A/B testing: Number of conversions in experimental groups

Implementation Notes:
    This implementation uses logarithmic computation for numerical stability
    when dealing with large factorials in binomial coefficients. This prevents
    overflow errors that would occur with direct factorial computation for large n.
"""

import math
from typing import Union


class BinomialDistribution:
    """
    Implementation of the Binomial Distribution

    This class provides a complete implementation of the Binomial distribution,
    offering efficient computation of probability mass function, mean, and variance
    and other statistical properties.

    Implementation Details:
    - uses mathematical formulas for computation
    - validates input parameters to ensure mathematical correctness
    - implements properties as cached computations for efficiency
    - uses logarithms for numerical stability in large combinations. (e.g. C(n,k))

    The implementation follows standard probability theory conventions and provides
    type hints for better code maintainability and IDE support.
    """

    # Class constant for numerical tolerance in floating-point comparisons
    _EPSILON = 1e-10

    def __init__(self, trials: int, probability: float) -> None:
        """
        Inits a new Binomial Distribution with the given parameters. I'm executing validation on the parameters
        at initialization of the class to ensure mathematical correctness.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            trials (int): Number of trials. Must be a positive integer.
            probability (float): Probability of success on each trial. Must be a float between 0 and 1 (inclusive).

        Raises:
            ValueError: If trials is not a positive integer, or probability is not a float between 0 and 1 (inclusive).
        """
        # mathematical validation occurs during initialization
        self._validate_trials(trials)
        self._validate_probability(probability)

        # Validated parameters are stored as private attributes.
        self._trials = trials
        self._probability = probability


    @property
    def trials(self) -> int:
        """ Get the number of trials. """
        return self._trials


    @property
    def probability(self) -> float:
        """ Get the probability of success on each trial. """
        return self._probability


    def pmf(self, k: int) -> float:
        """
        Probability Mass Function (PMF) for Binomial distribution.

        Computes P(X = k) using the formula: C(n,k) * p^k * (1-p)^(n-k)
        This represents the probability of getting exactly k successes out of n trials.

        Time Complexity: O(1) - for most cases, O(k) for large k due to combination calculations
        Space Complexity: O(1) - No additional storage required

        Args:
            k (int): The number of successes. Must be between 0 and n (inclusive). (This is the random variable X)

        Returns:
            float: The probability mass function value for the given k.
        """
        self._validate_pmf_input(k)

        # Handle the "all or nothing" edge cases. (Mathematical extrema)
        if k == 0:
            # P(X = 0) = (1-p)^n - probability of no success in all trials.
            return (1 - self._probability) ** self._trials
        elif k == self._trials:
            # P(X = n) = p^n - probability of all successes in all trials.
            return self._probability ** self._trials
        else:
            # General case: use log-space computation for numerical stability
            # This prevents overflows when computing large factorials directly.

            # Compute ln(P(X=k)) = ln(C(n,k)) + k * ln(p) + (n-k) * ln(1-p)
            log_pmf = (self._log_binomial_coefficient(self._trials, k) +    # ln(C(n,k))
                    k * math.log(self._probability) +                       # k * ln(p)
                    (self._trials - k) * math.log(1 - self._probability))   # (n-k) * ln(1-p)

            # Convert the logarithm back to probability using the exponential function.
            # P(X=k) = exp(ln(P(X=k)))
            return math.exp(log_pmf)


    @property
    def mean(self) -> float:
        """
        Calculate the mean (expected value) of the Binomial distribution.

        The expected value E[X] = np for Binomial distribution.
        This is the average number of successes expected out of n trials.

        Time Complexity: O(1) - Direct property access
        Space Complexity: O(1) - No additional storage

        Returns:
            float: The mean of the Binomial distribution (np).

        Mathematical Derivation:
            E[X] = sum(k * P(X=k)) for k in {0, 1, 2, ..., n}
            Through linearity of expectation: E[X] = n * p
        """
        # Direct computation: The mean is the number of trials multiplied by the probability.
        return self._trials * self._probability

    @property
    def variance(self) -> float:
        """
        Calculate the variance of the Binomial distribution.

        Uses the closed form-formula: Var(X) = np(1-p)
        This measures the spread of the distribution around the mean.

        Time Complexity: O(1) - Direct property access
        Space Complexity: O(1) - No additional storage

        Returns:
            float: The variance of the Binomial distribution (np(1-p)).

        NOTE: The variance reaches its maximum when p = 0.5 (fair coin). It appraoches 0 as p approaches 0 or 1
            (certain outcomes).
        """
        # Variance formula: np(1-p)
        # Maximum variance occurs at p = 0.5 (max uncertainty)
        return self._trials * self._probability * (1 - self._probability)


    @property
    def standard_deviation(self) -> float:
        """
        Calculate the standard deviation of the Binomial distribution.

        Uses the formula: σ = √(np(1-p))
        Standard deviation is the square root of the variance, giving a measure of the spread in the same units as the
        original data.

        Time Complexity: O(1) - Square root operation
        Space Complexity: O(1) - No additional storage

        Returns;
            float: the standard deviation of the Binomial distribution.
        """
        # Cheat! Standard deviation is just the square root of the variance, so we can think of this method
        # as a wrapper for variance.
        return math.sqrt(self.variance)

    def sample(self, random_values: list[float]) -> int:
        """
        Generate a random sample from the Binomial distribution.

        Simulates n Bernoulli trials with probability p and returns the number of successes. Each random value
        represents a single trail. If the result is < p, the trail was a success.

        Args:
            random_values: A list of random values between 0 and 1.

        Returns:
            int: The number of successes in the n trials.

        Raises:
            ValueError: If the length of random_values is not equal to n.
        """
        # We need to ensure that the lists are symmetrical
        if len(random_values) != self._trials:
            raise ValueError(f"Length of random_values must be {self._trials}")

        # Validate the random values before we start sampling.
        for value in random_values:
            self._validate_random_value(value)

        # Accumulate successes: for each trail, success occurs if the random value is < probability.
        # This simulates the Bernoulli trial outcome for each individual trial.
        return sum(1 for value in random_values if value < self._probability)


    def cdf(self, k: int) -> float:
        """
        Cumulative Distribution Function (CDF) for Binomial distribution.

        Computes P(X ≤ k) by summing PMF values from 0 to k.
        This gives the probability of getting k or fewer successes out of n trials.

        Args:
            k: The value at which to evaluate the CDF.

        Returns:
            float: The cumulative probability P(X ≤ k).
        """
        # Handle edge cases for k.
        if k < 0:
            # CDF(k) = 0 for k < 0 (you can't have negative successes!)
            return 0.0
        elif k > self._trials:
            # CDF(k) = 1 for k > n (you can't have more successes than trials!)
            return 1.0
        else:
            # This is just the sum of the PMF values from 0 to k. (i.e. the individual probabilities)
            # P(X ≤ k) = Σ P(X = i) for i = 0 to k
            return sum(self.pmf(i) for i in range(k + 1))

    def __str__(self) -> str:
        """ String representation of the Binomial distribution. """
        return f"Binomial Distribution (n = {self._trials}, p = {self._probability})"

    def __repr__(self) -> str:
        """
        Detailed string representation of the Binomial distribution.
        """
        return (f"BinomialDistribution(n={self._trials}, probability={self.probability}, "
                f"mean={self.mean}, variance={self.variance}, "
                f"standard_deviation={self.standard_deviation})")

    def __eq__(self, other: object) -> bool:
        """
        Checks equality between two Binomial distributions.
        """
        if not isinstance(other, BinomialDistribution):
            return False

        # Compares parameters w/ numerical tolerance (EPSILON)
        return (self._trials == other._trials and
                abs(self.probability - other.probability) < self._EPSILON)

    def __hash__(self) -> int:
        """
        Make the distribution hashable for use in sets and dictionaries.
        """
        # This creates a hash on discretized probability to handle floating point precision.
        return hash((self._trials, round(self.probability / self._EPSILON)))


    ### Helper Methods ###

    @staticmethod
    def _validate_trials(trials: Union[int, float]) -> None:
        """
        Validates the trials parameter.
        Ensures that trials is as positive integer (Per the definition of a Binomial Distribution).
        """
        if not isinstance(trials, int) or trials <= 0:
            raise ValueError("Trials must be a positive integer")


    @staticmethod
    def _validate_probability(probability: Union[int, float]) -> None:
        """
        Validates the probability parameter.
        Ensures that p is in the range [0, 1] (inclusive). (Per the definition of a valid probability)
        """
        if not 0 <= probability <= 1:
            raise ValueError("Probability must be between 0 and 1 (inclusive)")



    def _validate_pmf_input(self, k: int) -> None:
        """
        Validates input for PMF method.
        Ensures that k is in the range [0, n] (inclusive). (i.e it is non-negative and less than or equal to the
        number of trials)
        """
        if not isinstance(k, int) or not (0 <= k <= self._trials):
            raise ValueError(f"k must be a non-negative integer less than or equal to {self._trials}")


    @staticmethod
    def _validate_random_value(random_value: Union[int, float]) -> None:
        """
        Validate random value(s) for sampling:
        Ensures that each random value is between 0 and 1 for proper Bernoulli sampling.

        Args:
            random_value: A random value between 0 and 1 for sampling

        Raises:
            ValueError: If random_value is not between 0 and 1.
        """
        if not 0 <= random_value <= 1:
            raise ValueError("Random value must be between 0 and 1")


    @staticmethod
    def _log_binomial_coefficient(n:int, k:int) -> float:
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
        # Handle edge cases where combination equals 1 (ln(1) = 0)
        if k == 0 or k == n:
            return 0.0

        # Use the logarithmic identity: ln(C(n,k)) = ln(n!) - ln(k!) - ln((n-k)!)
        # Compute each factorial's logarithm using lgamma function:
        # - lgamma(m+1) = ln(m!) for positive integer m
        # - This avoids computing large factorials directly
        return (math.lgamma(n + 1) -        # ln(n!)
                math.lgamma(k + 1) -        # ln(k!)
                math.lgamma(n - k + 1))     # ln((n-k)!)



