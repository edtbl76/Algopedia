"""
Variance Operator Implementation

This module implements and empirically verifies the mathematical properties of
the variance operator Var[·] on random variables. Unlike the expectation operator,
variance is not a linear transformation and exhibits unique mathematical behaviors
that are essential to understanding probability theory and statistical analysis.

Key mathematical properties tested include:
- Scaling Property: Var[aX + b] = a²Var[X] (constant shifts don't affect variance)
- Sum Property: Var[X + Y] = Var[X] + Var[Y] + 2Cov[X,Y] (includes covariance term)
- Translation Invariance: Var[X + a] = Var[X] (constants preserve variance)

Each property is verified through both theoretical calculations and empirical
sampling, providing comprehensive validation of variance behavior under various
transformations and operations.
"""
from typing import Callable, Tuple, List

from data_science.probability.random_variable import RandomVariable
from data_science.probability.statistical_properties.base import StatisticalProperty
from data_science.probability.statistical_properties.config import VarianceTestResult
from data_science.probability.statistical_properties.exceptions import StatisticalTestError
from data_science.probability.statistical_properties.utils import StatisticalCalculations, SampleValidator


class VarianceOperator(StatisticalProperty):
    """
    Implementation of the variance operator Var[·]

    This class demonstrates and validates fundamental mathematical properties
    of variance through empirical sampling and statistical analysis. Unlike
    expectation, variance exhibits non-linear behavior that makes it particularly
    interesting for understanding probability distributions.

    The variance operator measures the spread or dispersion of a random variable
    around its mean, and its properties are crucial for understanding risk,
    uncertainty, and the behavior of sums of random variables.
    """

    def scaling_property(self, random_variable: RandomVariable, a: float, b: float) -> VarianceTestResult:
        """
        Tests the variance scaling property: Var[aX + b] = a²Var[X]

        This fundamental property demonstrates two key insights about variance:
        1. Adding a constant (b) does not change the variance (translation invariance)
        2. Scaling by a factor (a) multiplies variance by a² (quadratic scaling)

        The quadratic nature of variance scaling is what makes it different from
        expectation, which scales linearly. This property is essential for
        understanding how transformations affect the spread of distributions.

        Args:
            random_variable: Random variable X to test
            a: Scale factor applied to the random variable
            b: Shift constant added to the random variable

        Returns:
            VarianceTestResult containing theoretical and empirical variance
            calculations with detailed analysis

        Raises:
            StatisticalTestError: If sampling or calculation errors occur

        Mathematical Foundation:
            Var[aX + b] = E[(aX + b)²] - (E[aX + b])²
                        = E[a²X² + 2abX + b²] - (aE[X] + b)²
                        = a²E[X²] + 2abE[X] + b² - (a²(E[X])² + 2abE[X] + b²)
                        = a²E[X²] - a²(E[X])²
                        = a²(E[X²] - (E[X])²)
                        = a²Var[X]

        Example:
            >>> normal = NormalDistribution(mean=0, std_dev=1)
            >>> result = variance_op.scaling_property(normal, 3.0, 5.0)
            >>> print(f"Original variance: {normal.variance}")
            >>> print(f"Scaled variance (3X+5): {result.theoretical_variance}")
            >>> # Should show 9 * original_variance since 3² = 9
        """
        try:
            # Theoretical calculation
            theoretical_variance = a ** 2 * random_variable.variance

            # Empirical verification
            samples = SampleValidator.ensure_list(random_variable.sample(self.config.sample_size))

            transformed_samples = [a * x + b for x in samples]
            empirical_variance = StatisticalCalculations.variance(transformed_samples)

            additional_info = {
                'scale_factor': a,
                'shift_constant': b,
                'note': 'Shift constant does not affect variance'
            }

            return VarianceTestResult(
                property='Var[aX + b] = a²Var[X]',
                theoretical_variance=theoretical_variance,
                empirical_variance=empirical_variance,
                error=abs(theoretical_variance - empirical_variance),
                additional_info=additional_info
            )
        except Exception as e:
            raise StatisticalTestError(f"Variance scaling test failed: {e}")


    def sum_property(self, random_variable_x: RandomVariable, random_variable_y: RandomVariable,
                     joint_sampler: Callable[[int], Tuple[List[float], List[float]]]) -> VarianceTestResult:
        """
        Tests the variance sum property: Var[X + Y] = Var[X] + Var[Y] + 2Cov[X,Y]

        This property reveals the fundamental difference between variance and expectation
        when dealing with sums of random variables. Unlike expectation, which is always
        additive, variance includes a covariance term that depends on the relationship
        between the variables.

        Key insights:
        - For independent variables: Cov[X,Y] = 0, so Var[X + Y] = Var[X] + Var[Y]
        - For positively correlated variables: Cov[X,Y] > 0, increasing total variance
        - For negatively correlated variables: Cov[X,Y] < 0, reducing total variance

        Args:
            random_variable_x: First random variable X
            random_variable_y: Second random variable Y
            joint_sampler: Function that generates paired samples from the joint
                           distribution of X and Y

        Returns:
            VarianceTestResult containing analysis of variance additivity including
            covariance effects and independence assessment

        Raises:
            StatisticalTestError: If sampling or calculation errors occur

        Mathematical Foundation:
            Var[X + Y] = E[(X + Y)²] - (E[X + Y])²
                       = E[X² + 2XY + Y²] - (E[X] + E[Y])²
                       = E[X²] + 2E[XY] + E[Y²] - (E[X])² - 2E[X]E[Y] - (E[Y])²
                       = (E[X²] - (E[X])²) + (E[Y²] - (E[Y])²) + 2(E[XY] - E[X]E[Y])
                       = Var[X] + Var[Y] + 2Cov[X,Y]

        Example:
            >>> normal_x = NormalDistribution(mean=0, std_dev=2)
            >>> normal_y = NormalDistribution(mean=0, std_dev=3)
            >>> def independent_sampler(n): return (normal_x.sample(n), normal_y.sample(n))
            >>> result = variance_op.sum_property(normal_x, normal_y, independent_sampler)
            >>> print(f"Covariance: {result.additional_info['covariance']:.6f}")
            >>> print(f"Independent: {result.additional_info['independence_assumption']}")
        """
        try:
            # Generate samples
            samples_x, samples_y = joint_sampler(self.config.sample_size)
            samples_x, samples_y = SampleValidator.validate_sample_pairs(samples_x, samples_y)

            # Calculate empirical covariance
            covariance = StatisticalCalculations.covariance(samples_x, samples_y)

            # Theoretical variance of sum
            theoretical_sum_variance = random_variable_x.variance + random_variable_y.variance + 2 * covariance

            # Empirical variance of sum
            sum_samples = [x + y for x, y in zip(samples_x, samples_y)]
            empirical_sum_variance = StatisticalCalculations.variance(sum_samples)

            additional_info = {
                'variance_x': random_variable_x.variance,
                'variance_y': random_variable_y.variance,
                'covariance': covariance,
                'independence_assumption': abs(covariance) < 1e-6
            }

            return VarianceTestResult(
                property='Var[X + Y] = Var[X] + Var[Y] + 2Cov[X,Y]',
                theoretical_variance=theoretical_sum_variance,
                empirical_variance=empirical_sum_variance,
                error=abs(theoretical_sum_variance - empirical_sum_variance),
                additional_info=additional_info
            )
        except Exception as e:
            raise StatisticalTestError(f"Variance sum test failed: {e}")

    def constant_shift_invariance(self, random_variable: RandomVariable, a: float) -> VarianceTestResult:
        """
         Tests the variance invariance property under constant shift: Var[X + a] = Var[X]

         This property demonstrates that variance is translation-invariant: adding a
         constant to a random variable does not change its variance. This fundamental
         property occurs because variance measures spread around the mean, and shifting
         all values by the same constant preserves the relative distances.

         This is a special case of the scaling property where the scale factor is 1
         and only the shift constant is applied. It's important enough to test separately
         because it reveals the geometric interpretation of variance as a measure of
         "width" or "spread" that is preserved under translation.

         Args:
             random_variable: Random variable X to test
             a: Constant value to add to the random variable

         Returns:
             VarianceTestResult containing detailed analysis of variance preservation
             under constant shift, including empirical verification

         Raises:
             StatisticalTestError: If sampling or calculation errors occur

         Mathematical Foundation:
             Var[X + a] = E[(X + a - E[X + a])²]
                        = E[(X + a - (E[X] + a))²]    [by linearity of expectation]
                        = E[(X - E[X])²]              [constant cancels out]
                        = Var[X]

         Geometric Interpretation:
             Adding a constant translates the entire distribution along the x-axis
             without changing its shape or spread. The variance measures the "width"
             of the distribution, which remains unchanged under translation.

         Example:
             >>> binomial = BinomialDistribution(n=20, p=0.3)
             >>> result = variance_op.constant_shift_invariance(binomial, 100.0)
             >>> print(f"Original variance: {binomial.variance:.3f}")
             >>> print(f"Shifted variance: {result.empirical_variance:.3f}")
             >>> print(f"Invariance preserved: {result.additional_info['invariance_preserved']}")
        """
        try:
            # Theoretical variance (should remain unchanged)
            theoretical_variance = random_variable.variance

            # Generate samples
            samples = random_variable.sample(self.config.sample_size)
            samples = SampleValidator.ensure_list(samples)

            # Calculate empirical variances
            empirical_variance = StatisticalCalculations.variance(samples)
            shifted_samples = [x + a for x in samples]
            empirical_shifted_variance = StatisticalCalculations.variance(shifted_samples)

            # Additional analysis
            empirical_invariance_error = abs(empirical_variance - empirical_shifted_variance)

            additional_info = {
                'constant_shift': a,
                'empirical_variance_original': empirical_variance,
                'empirical_invariance_error': empirical_invariance_error,
                'invariance_preserved': empirical_invariance_error < self.config.tolerance_excellent,
                'variance_preservation_ratio': empirical_shifted_variance / empirical_variance if empirical_variance != 0 else float(
                    'inf')
            }

            return VarianceTestResult(
                property='Var[X + a] = Var[X]',
                theoretical_variance=theoretical_variance,
                empirical_variance=empirical_shifted_variance,
                error=abs(theoretical_variance - empirical_shifted_variance),
                additional_info=additional_info
            )
        except Exception as e:
            raise StatisticalTestError(f"Variance invariance test failed: {e}")
