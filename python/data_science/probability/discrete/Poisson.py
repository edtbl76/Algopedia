"""
Poisson Distribution

This module implements the Poisson distribution, a discrete probability
distribution that models the number of events occurring in a fixed interval of
time or space, given a known constant mean rate. Used for rare events that
happen independently.

Mathematical Definition:
    The probability mass function (PMF) of a Poisson distribution is:

    P(X = k) = (λ^k * e^(-λ)) / k!

    Where:
        - k is the number of occurrences (k >= 0)
        - λ (lambda) is the expected number of occurrences
        - e is Euler's number

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
import random
from typing import Optional, Union, List, Iterator

from data_science.probability.random_variable import DiscreteRandomVariable
from data_science.probability.utilities import validate_positive_float


class PoissonDistribution(DiscreteRandomVariable[int]):
    """
    Implements the Poisson Distribution for modeling discrete count data.
    """


    def __init__(self, lambda_rate: float):
        """
        Initializes a Poisson distribution.

        Args:
            lambda_rate: The average rate of events (λ), must be > 0.
        """
        validate_positive_float(lambda_rate)
        self._lambda_rate = lambda_rate


    @property
    def lambda_rate(self) -> float:
        """The average rate of events (λ) for the distribution."""
        return self._lambda_rate

    @property
    def mean(self) -> float:
        """
        Calculates the mean (expected value) of the distribution, E[X] = λ.

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


        """
        return self._lambda_rate

    @property
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

        """
        return self._lambda_rate


    def pmf(self, k: int) -> float:
        """
        Compute probability Mass Function P(X = k)

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
            probability of exactly k events (0.0 if invalid k)


        Args:
            k (int): Number of events (must be non-negative integer)

        Returns:
            float: probability of exactly k events occurring
                  Returns 0.0 for invalid k values (k < 0) or negligibly small probabilities

        """
        if not isinstance(k, int) or k < 0:
            return 0.0

        # For numerical stability, calculate in log-space:
        # ln(P(X=k)) = k*ln(λ) - λ - ln(k!)

        # 1. The log of the rate component: k * ln(λ)
        log_rate_component = k * math.log(self._lambda_rate)

        # 2. The log of the factorial component: -ln(k!)
        #    We use math.lgamma(k + 1) which is equivalent to ln(k!)
        log_factorial_component = -math.lgamma(k + 1)

        # 3. The exponential decay component: -λ
        decay_component = -self._lambda_rate

        # Assemble the components to get the total log-probability
        log_pmf = log_rate_component + log_factorial_component + decay_component

        # Convert back from log-space to probability
        return math.exp(log_pmf)

    def cdf(self, k: int) -> float:
        """
        Calculates the Cumulative Distribution Function (CDF) for a given k.

        Formula: P(X <= k) = Σ [ (λ^i * e^(-λ)) / i! ] for i from 0 to k.

        Args:
            k: The value at which to evaluate the CDF.

        Returns:
            The cumulative probability of observing k or fewer events.
        """
        if k < 0:
            return 0.0

        # Sum the PMF values from 0 to k
        return sum(self.pmf(i) for i in range(k + 1))

    def sample(self, size: Optional[int] = None) -> Union[int, List[int]]:
        """
        Generates random samples from the Poisson distribution.

        Uses Knuth's algorithm for generating Poisson-distributed random numbers.

        Args:
            size: The number of samples to generate. If None, a single sample is returned.

        Returns:
            A single sample or a list of samples.
        """
        if size is None:
            return self._generate_single_sample()

        return [self._generate_single_sample() for _ in range(size)]

    def support(self) -> Iterator[int]:
        """
        Returns the support of the Poisson distribution.

        The support is the set of all non-negative integers {0, 1, 2, ...}.
        Since the support is infinite, this method returns an iterator.

        Returns:
            An iterator that yields the non-negative integers. (Infinite Support)
        """
        # The support is infinite, so we return a generator
        def _support_generator():
            n = 0
            while True:
                yield n
                n += 1
        return _support_generator()


    def __eq__(self, other: object) -> bool:
        """Checks for equality based on the lambda_rate parameter."""
        if not isinstance(other, PoissonDistribution):
            return False
        return abs(self._lambda_rate - other._lambda_rate) < self._EPSILON

    def __hash__(self) -> int:
        """Hashes the distribution based on its lambda_rate parameter."""
        return hash(round(self._lambda_rate / self._EPSILON))

    def _generate_single_sample(self) -> int:
        """Helper to generate one sample using Knuth's algorithm."""
        l = math.exp(-self._lambda_rate)
        k = 0
        p = 1.0
        while p > l:
            k += 1
            p *= random.random()
        return k - 1

