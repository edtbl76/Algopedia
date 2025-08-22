"""
Bernoulli Distribution

This module implements the Bernoulli distribution, a discrete probability distribution
for a random variable which takes value 1 with probability p and value 0 with probability (1-p).

Mathematical Definition:
The probability mass function (PMF) of a Bernoulli distribution is:
    P(X = k) = p^k * (1-p)^(1-k) for k ∈ {0, 1}

Where:
    - X is the random variable
    - k is the outcome (0 or 1)
    - p is the probability of success (0 ≤ p ≤ 1)

Properties:
    - Mean (Expected Value): E[X] = p
    - Variance: Var(X) = p(1-p)
    - Standard Deviation: σ = √(p(1-p))

Historical Context:
Named after Swiss mathematician Jacob Bernoulli (1654-1705), who studied this distribution
in his work "Ars Conjectandi" (published posthumously in 1713). The Bernoulli distribution
forms the foundation for the binomial distribution and is fundamental in probability theory.
Bernoulli's work laid the groundwork for the law of large numbers and modern probability theory.

Applications:
- Coin flips (heads/tails)
- Success/failure experiments
- Binary classification problems
- Quality control (pass/fail)
- Medical trials (cure/no cure)
"""
import math
from typing import Union


class BernoulliDistribution:
    """
    Bernoulli Distribution Implementation

    This class provides a complete implementation of the Bernoulli distribution,
    offering efficient computation of probability mass function, mean, and variance.

    Implementation Details:
    - Uses direct mathematical formulas for O(1) computation complexity
    - Validates input parameters to ensure mathematical correctness
    - Implements properties as cached computations for efficiency

    The implementation follows standard probability theory conventions and provides
    type hints for better code maintainability and IDE support.

    """

    # Class constant for numerical toleran ce
    _EPISION = 1e-10


    def __init__(self, probability: float) -> None:
        """
        Initialize a new Bernoulli distribution with the given probability of success.

            Time Complexity: O(1)
            Space Complexity: O(1)

        Args:
            probability (Union[int, float]): The probability of success for the distribution.
                                           Must be a numeric value between 0 and 1 (inclusive).

        Raises:
            TypeError: If probability is not a numeric value (int or float).
            ValueError: If probability is not between 0 and 1 (inclusive).

        """
        self._validate_probability(probability)
        self._probability:float = float(probability)

    @property
    def probability(self) -> float:
        """
        Get the probability of success for the distribution.
        """
        return self._probability

    def pmf(self, k:int) -> float:
        """
        Probability Mass Function (PMF) for Bernoulli distribution.

        Computes P(X = k) using the formula: p^k * (1-p)^(1-k)

        Time Complexity: O(1) - Direct formula evaluation
        Space Complexity: O(1) - No additional storage required

        Args:
            k (int): The value of the random variable. Must be 0 or 1.

        Returns:
            float: The probability mass function value for the given k.
                  Returns p if k=1, (1-p) if k=0.

        Raises:
            ValueError: If k is not 0 or 1.
        """
        self._validate_pmf_input(k)

        # Direct computation: if k=1, return p, otherwise return (1-p)
        return self.probability if k == 1 else (1 - self.probability)


    @property
    def mean(self) -> float:
        """
        Calculate the mean (expected value) of the Bernoulli distribution.

        The expected value E[X] = p for Bernoulli distribution.

        Time Complexity: O(1) - Direct property access
        Space Complexity: O(1) - No additional storage

        Returns:
            float: The mean of the Bernoulli distribution (p).
                  Represents the expected value of the random variable.

        Mathematical Derivation:
            E[X] = 0 * P(X=0) + 1 * P(X=1) = 0 * (1-p) + 1 * p = p

        """
        return self.probability


    @property
    def variance(self) -> float:
        """
        Calculate the variance of the Bernoulli distribution.

        Uses the closed-form formula: Var(X) = p(1-p)

        Time Complexity: O(1) - Single multiplication operation
        Space Complexity: O(1) - No additional storage

        Returns:
            The variance of the Bernoulli distribution (p * (1 - p)).
            Maximum variance occurs at p = 0.5 with value 0.25.

        Note:
            The variance reaches its maximum when p = 0.5 (fair coin),
            and approaches 0 as p approaches 0 or 1 (certain outcomes).
        """
        return self.probability * (1 - self.probability)


    @property
    def standard_deviation(self) -> float:
        """
        Calculate the standard deviation of the Bernoulli distribution.

        Uses the formula: σ = √(p(1-p))

        Time Complexity: O(1) - Square root operation
        Space Complexity: O(1) - No additional storage

        Returns:
            The standard deviation of the Bernoulli distribution.
        """
        return math.sqrt(self.variance)



    def sample(self, random_value: float) -> int:
        """
        Generate a random sample from the Bernoulli distribution.

        Args:
            random_value: A random value between 0 and 1.

        Returns:
            1 if random_value is less than probability, 0 otherwise.

        Raises:
            TypeError: If random_value is not numeric.
            ValueError: If random_value is not between 0 and 1.
        """
        BernoulliDistribution._validate_random_value(random_value)
        return 1 if random_value < self._probability else 0


    def cdf(self, k: int) -> float:
        """
        Cumulative Distribution Function (CDF) for Bernoulli distribution.

        Args:
            k: The value at which to evaluate the CDF.

        Returns:
            The cumulative probability P(X ≤ k).
        """
        if k < 0:
            return 0.0
        elif k == 0:
            return 1.0 - self.probability
        else:
            return 1.0


    def __str__(self) -> str:
        """
        String representation of the Bernoulli distribution.
        """
        return f"Bernoulli Distribution (p = {self.probability})"

    def __repr__(self):
        """
        Detailed string representation of the Bernoulli distribution
        """
        return (f"BernoulliDistribution(probability={self.probability}, "
                f"variance={self.variance}, mean={self.mean}, standard_deviation={self.standard_deviation})")


    def __eq__(self, other: object) -> bool:
        """
        Checks equality between two Bernoulli distributions.
        """
        if not isinstance(other, BernoulliDistribution):
            return False

        return abs(self.probability - other.probability) < self._EPISION

    def __hash__(self) -> int:
        """
        Make the distribution hashable for use in sets and dictionaries
        """
        return hash(self.probability / self._EPISION)

### Helper Methods ###\

    @staticmethod
    def _validate_probability(probability: Union[int, float]) -> None:
        """
        Validate the probability parameter.
        """
        if not 0 <= probability <= 1:
            raise ValueError("Probability must be between 0 and 1 (inclusive)")


    @staticmethod
    def _validate_pmf_input(k: int) -> None:
        """
        Validates input for PMF method
        """
        if not isinstance(k, int) or k not in [0, 1]:
            raise ValueError("Input must be 0 or 1")

    @staticmethod
    def _validate_random_value(random_value: Union[int, float]) -> None:
        """
        Validate random value(s) for sampling

        Args:
            random_value: A random value between 0 and 1 for sampling

        Raises:
            ValueError: If random_value is not in range [0, 1]
        """
        if not 0 <= random_value <= 1:
            raise ValueError("Random value must be between 0 and 1")
