"""
Base classes and interfaces for random variables
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, Union, Sequence, Callable, Any, Dict, Iterator

# Type variable for the value type of the random variable
T = TypeVar("T")

class RandomVariable(Generic[T], ABC):
    """
    Abstract base class for random variables.

    A random variable is a variable whose value is subject to chance variations described by
    a probability distribution.
    """

    # Numerical tolerance for floating-point comparisons
    _EPSILON = 1e-10

    @property
    @abstractmethod
    def mean(self) -> float:
        """
        Expected value (mean) of the random variable.

        The expected value E[X] is the long-run average value of the random variable
        over many independent repetitions of an experiment. It is calculated as:

        For discrete random variables:
            E[X] = ∑(x_i * P(X = x_i)) for all possible values x_i

        For continuous random variables:
            E[X] = ∫(x * f(x) dx) over the support of X

        where f(x) is the probability density function.

        Returns:
            float: The expected value E[X]
        """
        pass

    @property
    @abstractmethod
    def variance(self) -> float:
        """
        Variance of the random variable.

        The variance measures how far a set of values are spread out from their mean.
        It is calculated as:

        Var[X] = E[(X - E[X])²] = E[X²] - (E[X])²

        where E[X] is the expected value of X and E[X²] is the expected value
        of the square of X.


        Returns:
            float: The variance Var[X]
        """
        pass

    @property
    def standard_deviation(self) -> float:
        """
        Standard deviation of the random variable.

        The standard deviation is the square root of the variance and measures
        the amount of variation or dispersion of a set of values from their mean.

        σ = √Var[X]

        Returns:
            float: The standard deviation σ
        """
        return self.variance ** 0.5


    @abstractmethod
    def cdf(self, value: T) -> float:
        """
        Calculates the cumulative distribution function (CDF) of the random variable.

        The CDF gives the probability that the random variable X takes a value
        less than or equal to x:

        F(x) = P(X ≤ x)

        For discrete random variables:
            F(x) = ∑(P(X = t)) for all t ≤ x

        For continuous random variables:
            F(x) = ∫(f(t) dt) from -∞ to x

        where f(t) is the probability density function.

        Args:
            value: The value to calculate the cumulative probability for

        Returns:
            float: The probability P(X ≤ value)
        """
        pass

    @abstractmethod
    def sample(self, size: Optional[int]) -> Union[T, Sequence[T]]:
        """
        Generates random samples from the distribution.

        Sampling involves drawing values from the probability distribution,
        typically using techniques specific to each distribution type.

        Args:
            size: Number of samples to generate (None for a single sample)

        Returns:
            A single sample or sequence of samples from the distribution
        """
        pass


class DiscreteRandomVariable(RandomVariable[T], ABC):
    """
    Abstract base class for discrete random variables.

    A discrete random variable can only take on a countable number of distinct values.
    Examples include:
    - Number of coin flips until first heads (geometric distribution)
    - Number of successes in n trials (binomial distribution)
    - Count of events in a fixed time interval (Poisson distribution)
    """

    @abstractmethod
    def pmf(self, value: T) -> float:
        """
        Calculates the probability mass function (PMF): P(X = value)

        The PMF gives the probability that a discrete random variable equals
        exactly a certain value. For a discrete random variable X:

        P(X = x) = PMF(x)

        The PMF must satisfy:
        1. P(X = x) ≥ 0 for all x
        2. ∑(P(X = x)) = 1 over all possible values x

        Args:
            value: The value to calculate the probability for

        Returns:
            float: The probability at the given value
        """
        pass

    @abstractmethod
    def support(self) -> Iterator[T]:
        """
        Returns an iterator over the support of the random variable.

        For finite support, iterates through all possible values.
        For infinite support, generates values indefinitely.


        In probability theory, the support of a random variable X is the smallest
        closed set of values such that the probability of X taking a value outside
        the set is zero.

        For discrete random variables, the support is the set of all possible
        values that have non-zero probability:

        support(X) = {x : P(X = x) > 0}

        Examples:
        - For a fair die: {1, 2, 3, 4, 5, 6}
        - For a Bernoulli random variable: {0, 1}
        - For a Poisson random variable: {0, 1, 2, ...}

        Returns:
            Iterator[T]: The set of values that the random variable can take
        """
        pass


class ContinuousRandomVariable(RandomVariable[T], ABC):
    """
    Abstract base class for continuous random variables.

    A continuous random variable can take on any value in a range or interval.
    Examples include:
    - Time until next event (exponential distribution)
    - Normally distributed measurements (normal distribution)
    - Waiting times (gamma distribution)
    """

    @abstractmethod
    def pdf(self, value: T) -> float:
        """
        Calculates the probability density function (PDF) at the given value.

        For a continuous random variable, the PDF f(x) gives the relative likelihood
        that the value of X equals x. Unlike PMF, the PDF doesn't directly give
        probabilities, but rather:

        P(a ≤ X ≤ b) = ∫(f(x) dx) from a to b

        The PDF must satisfy:
        1. f(x) ≥ 0 for all x
        2. ∫(f(x) dx) = 1 over the entire domain

        Args:
            value: The value to calculate the probability density for

        Returns:
            float: The probability density at the given value
        """
        pass

    @abstractmethod
    def quantile(self, p: float) -> float:
        """
        Calculates the quantile function (inverse of CDF) at probability p.

        The quantile function Q(p) returns the value x such that:

        P(X ≤ x) = p

        Mathematically, Q(p) = F^(-1)(p) where F is the CDF.

        Quantiles have specific names for certain values of p:
        - Q(0.5): Median
        - Q(0.25), Q(0.75): First and third quartiles
        - Q(0.01), Q(0.99): 1st and 99th percentiles

        Args:
            p: Probability value between 0 and 1

        Returns:
            float: The value x such that P(X ≤ x) = p

        Raises:
            ValueError: If p is not in the range [0, 1]
        """
        pass


class ParametricDistribution(ABC):
    """
    Mixin for distributions that have parameters.

    A mixin is a class that provides methods or properties to be used by other classes
    without being considered a base class. This mixin adds parameter-related
    functionality to distribution classes.

    In probability theory, parametric distributions are defined by a fixed set of
    parameters that completely determine their behavior. Examples include:
    - Normal distribution: parameters μ (mean) and σ² (variance)
    - Poisson distribution: parameter λ (rate)
    - Exponential distribution: parameter λ (rate)
    """

    @property
    @abstractmethod
    def parameters(self) -> Dict[str, Any]:
        """
        Gets the parameters of the distribution.

        Parameters are values that define the specific instance of a probability
        distribution. They control the shape, location, and scale of the distribution.

        Example parameters for common distributions:
        - Normal distribution: mean (μ), standard deviation (σ)
        - Binomial distribution: number of trials (n), success probability (p)
        - Poisson distribution: rate (λ)

        Returns:
            Dict[str, Any]: A dictionary of parameter names and their values
        """
        pass


# Helper functions for working with random variables

def expected_value(random_variable: RandomVariable) -> float:
    """
    Calculates the expected value (mean) of a random variable.

    The expected value represents the long-run average value of
    repeated samples from a distribution.

    For discrete random variables:
    E[X] = ∑(x_i * P(X = x_i)) for all possible values x_i

    For continuous random variables:
    E[X] = ∫(x * f(x) dx) over the support of X

    Args:
        random_variable: The random variable to calculate the expected value for

    Returns:
        float: The expected value E[X]
    """
    return random_variable.mean


def variance(random_variable: RandomVariable) -> float:
    """
    Calculates the variance of a random variable.

    Variance measures how far a set of values are spread out from their mean.

    Var[X] = E[(X - E[X])²] = E[X²] - (E[X])²

    Args:
        random_variable: The random variable to calculate the variance for

    Returns:
        float: The variance Var[X]
    """
    return random_variable.variance


def covariance(rv_x: RandomVariable, rv_y: RandomVariable,
               joint_sampler: Callable[[int], tuple[Sequence[Any], Sequence[Any]]]) -> float:
    """
    Calculates the covariance between two random variables.

    Covariance measures how much two random variables vary together.

    Cov[X, Y] = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]

    Properties:
    - Cov[X, Y] > 0: X and Y tend to move in the same direction
    - Cov[X, Y] < 0: X and Y tend to move in opposite directions
    - Cov[X, Y] = 0: X and Y have no linear relationship
    - Cov[X, X] = Var[X]

    Args:
        rv_x: First random variable
        rv_y: Second random variable
        joint_sampler: Function that returns paired samples from the joint distribution

    Returns:
        float: The covariance Cov[X, Y]
    """
    # Implementation would use Monte Carlo sampling to estimate covariance
    # This is a placeholder for the interface
    pass

