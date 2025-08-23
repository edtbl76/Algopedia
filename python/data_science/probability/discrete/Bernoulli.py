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
"""
from random import random
from typing import Union, Optional, List, Sequence, Iterator

from data_science.probability.random_variable import DiscreteRandomVariable
from data_science.probability.utilities import validate_probability


class BernoulliDistribution(DiscreteRandomVariable[int]):
    """
    Bernoulli Distribution Implementation

    A discrete probability distribution for a random variable which takes value 1
    with probability p and value 0 with probability (1-p).

    Models binary outcomes such as success/failure, heads/tails, or yes/no events.
    """

    def __init__(self, probability: float) -> None:
        """
        Initialize a new Bernoulli distribution with the given probability of success.

        Args:
            probability: The probability of success (value 1). Must be between 0 and 1.

        Raises:
            ValueError: If probability is not between 0 and 1 (inclusive).
        """
        validate_probability(probability)
        self._probability: float = float(probability)

    @property
    def probability(self) -> float:
        """
        Gets the probability of success (value 1) for the distribution.

        Returns:
            float: The probability parameter p
        """
        return self._probability

    def pmf(self, k:int) -> float:
        """
        Calculates the probability mass function (PMF) value at the given point.

        For Bernoulli distribution:
            P(X = 1) = p
            P(X = 0) = 1-p
            P(X = k) = 0 for all other k

        Args:
            k: The value to calculate the probability for (0 or 1)

        Returns:
            float: The probability at the given value
        """
        if not isinstance(k, int) or k not in [0, 1]:
            return 0.0

        # Direct computation: if k=1, return p, otherwise return (1-p)
        return self.probability if k == 1 else (1 - self.probability)


    @property
    def mean(self) -> float:
        """
        Calculates the expected value (mean) of the Bernoulli distribution.

        For Bernoulli distribution:
            E[X] = p

        The mean represents the long-run average proportion of successes
        if the experiment is repeated many times.

        Returns:
            float: The mean (expected value) of the distribution
        """
        return self.probability


    @property
    def variance(self) -> float:
        """
        Calculates the variance of the Bernoulli distribution.

        For Bernoulli distribution:
            Var(X) = p(1-p)

        The variance reaches its maximum value of 0.25 when p = 0.5,
        and approaches 0 as p approaches either 0 or 1.

        Returns:
            float: The variance of the distribution
        """
        return self.probability * (1 - self.probability)

    def cdf(self, value: int) -> float:
        """
        Calculates the cumulative distribution function (CDF) at the given value.

        For Bernoulli distribution:
            F(x) = 0           if x < 0
            F(x) = 1-p         if 0 ≤ x < 1
            F(x) = 1           if x ≥ 1

        Args:
            value: The value to calculate the cumulative probability for

        Returns:
            float: The probability P(X ≤ value)
        """
        if value < 0:
            return 0.0
        elif value < 1:
            return 1.0 - self.probability
        else:
            return 1.0

    def sample(self, size: Optional[int] = None) -> Union[int, List[int]]:
        """
        Generates random samples from the Bernoulli distribution.

        Uses the inverse transform sampling method:
        - Generate uniform random number u between 0 and 1
        - Return 1 if u < p, otherwise return 0

        Args:
            size: Number of samples to generate (None for a single sample)

        Returns:
            A single sample (if size is None) or a list of samples
        """
        if size is None:
            # Generate a single sample
            return 1 if random() < self.probability else 0
        else:
            # Generate multiple samples
            return [1 if random() < self.probability else 0 for _ in range(size)]

    def support(self) -> Iterator[int]:
        """
        Returns the support of the random variable.

        For Bernoulli distribution, the support is always {0, 1}.
        These are the only values that have non-zero probability.

        Returns:
            Iterators[int]: The set of values that the random variable can take
            (Finite Support)
        """
        return iter([0, 1])

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

        return abs(self.probability - other.probability) < self._EPSILON

    def __hash__(self) -> int:
        """
        Make the distribution hashable for use in sets and dictionaries
        """
        return hash(self.probability / self._EPSILON)








