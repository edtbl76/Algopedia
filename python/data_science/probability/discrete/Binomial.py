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
import random
from typing import Union, Optional, List, Iterator

from data_science.probability.random_variable import DiscreteRandomVariable
from data_science.probability.utilities import validate_probability, validate_positive_integer, log_binomial_coefficient


class BinomialDistribution(DiscreteRandomVariable[int]):
    """
    Binomial Distribution Implementation

    A discrete probability distribution that models the number of successes
    in a fixed number of independent trials, each with the same probability of success.

    Examples include:
    - Number of heads in n coin flips
    - Number of defective items in a sample of n items
    - Number of successful patients in a clinical trial of n patients
    """

    def __init__(self, trials: int, probability: float) -> None:
        """
        Initializes a new Binomial distribution with the given parameters.

        Args:
            trials: Number of independent Bernoulli trials. Must be a positive integer.
            probability: Probability of success on each trial. Must be between 0 and 1.

        Raises:
            ValueError: If trials is not a positive integer or probability is invalid
        """
        validate_probability(probability)
        validate_positive_integer(trials)

        self._trials = trials
        self._probability = probability

    @property
    def trials(self) -> int:
        """
        Gets the number of trials parameter.

        Returns:
            int: The number of trials n
        """
        return self._trials

    @property
    def probability(self) -> float:
        """
        Gets the probability of success on each trial.

        Returns:
            float: The probability parameter p
        """
        return self._probability

    def pmf(self, k: int) -> float:
        """
        Calculates the probability mass function (PMF) at the given value.

        For Binomial distribution:
            P(X = k) = C(n,k) × p^k × (1-p)^(n-k)

        Where C(n,k) is the binomial coefficient ("n choose k").

        For values outside the support {0, 1, 2, ..., n}, returns 0.

        Args:
            k: The number of successes to calculate the probability for

        Returns:
            float: The probability of exactly 'value' successes
        """
        if not isinstance(k, int) or not (0 <= k <= self._trials):
            return 0.0

        # Handle the "all or nothing" edge cases. (Mathematical extrema)
        if k == 0:
            # P(X = 0) = (1-p)^n - probability of no success in all trials.
            return (1 - self._probability) ** self._trials
        elif k == self._trials:
            # P(X = n) = p^n - probability of all successes in all trials.
            return self._probability ** self._trials
        else:
            # Handle degenerate probabilities to avoid log(0)
            if self._probability == 0.0:
                # With p=0, only k=0 has mass (already handled above); others are 0
                return 0.0
            if self._probability == 1.0:
                # With p=1, only k=n has mass (already handled above); others are 0
                return 0.0

            # General case: use log-space computation for numerical stability
            # This prevents overflows when computing large factorials directly.

            # 1. ln(C(n,k)): The log of the number of ways to arrange k successes in n trials.
            log_combinations = log_binomial_coefficient(self._trials, k)

            # 2. k * ln(p): The log of the probability of k successes.
            log_prob_success = k * math.log(self._probability)

            # 3. (n-k) * ln(1-p): The log of the probability of (n-k) failures.
            log_prob_failure = (self._trials - k) * math.log(1 - self._probability)

            # Assemble the components to get the total log-probability.
            log_pmf = log_combinations + log_prob_success + log_prob_failure

            # Convert the logarithm back to probability using the exponential function.
            # P(X=k) = exp(ln(P(X=k)))
            return math.exp(log_pmf)

    @property
    def mean(self) -> float:
        """
        Calculates the expected value (mean) of the Binomial distribution.

        For Binomial distribution:
            E[X] = n × p

        This represents the average number of successes expected in n trials.

        Returns:
            float: The mean (expected value) of the distribution
        """
        return self._trials * self._probability

    @property
    def variance(self) -> float:
        """
        Calculates the variance of the Binomial distribution.

        For Binomial distribution:
            Var(X) = n × p × (1-p)

        The variance reaches its maximum when p = 0.5 and approaches 0
        as p approaches either 0 or 1.

        Returns:
            float: The variance of the distribution
        """
        return self._trials * self._probability * (1 - self._probability)

    def cdf(self, k: int) -> float:
        """
        Calculates the cumulative distribution function (CDF) at the given value.

        For Binomial distribution:
            F(x) = P(X ≤ x) = ∑(k=0 to ⌊x⌋) P(X = k)

        This gives the probability of obtaining at most 'value' successes in n trials.

        Args:
            k: The upper bound for the number of successes

        Returns:
            float: The probability P(X ≤ value)
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

    def sample(self, size: Optional[int] = None) -> Union[int, List[int]]:
        """
        Generates random samples from the Binomial distribution.

        Implementation uses a series of Bernoulli trials to simulate the binomial process:
        - For each trial, generate a random number between 0 and 1
        - Count the number of trials where the random number is less than p

        Args:
            size: Number of samples to generate (None for a single sample)

        Returns:
            A single sample (if size is None) or a list of samples
        """
        if size is None:
            # Generate a single sample by simulating n Bernoulli trials
            return sum(1 for _ in range(self._trials) if random.random() < self._probability)
        else:
            # Generate multiple samples
            return [sum(1 for _ in range(self._trials) if random.random() < self._probability)
                    for _ in range(size)]


    def support(self) -> Iterator[int]:
        """
        Returns an iterator over the support of the random variable.

        For Binomial distribution, the support is {0, 1, 2, ..., n},
        representing all possible numbers of successes in n trials.

        Since the support is finite, this iterator will yield exactly (n+1) values.

        Returns:
            Iterator[int]: An iterator over all possible values (0 to n inclusive)

        Example:
            >>> binomial = BinomialDistribution(3, 0.5)
            >>> list(binomial.support())
            [0, 1, 2, 3]
        """
        return iter(range(self._trials + 1))

    def __str__(self) -> str:
        """
        String representation of the Binomial distribution.
        """
        return f"Binomial Distribution (n = {self._trials}, p = {self._probability})"

    def __repr__(self) -> str:
        """
        Detailed string representation of the Binomial distribution.
        """
        return (f"BinomialDistribution(trials={self._trials}, probability={self._probability}, "
                f"mean={self.mean}, variance={self.variance}, "
                f"standard_deviation={self.standard_deviation})")

    def __eq__(self, other: object) -> bool:
        """
        Checks equality between two Binomial distributions.

        Two Binomial distributions are equal if they have the same number of trials
        and the same probability of success on each trial.

        Args:
            other: Object to compare with

        Returns:
            bool: True if the distributions are equal, False otherwise
        """
        if not isinstance(other, BinomialDistribution):
            return False

        return (self._trials == other._trials and
                abs(self._probability - other._probability) < self._EPSILON)

    def __hash__(self) -> int:
        """
        Makes the distribution hashable for use in sets and dictionaries.

        Returns:
            int: Hash value for the distribution
        """
        return hash((self._trials, round(self._probability / self._EPSILON)))





