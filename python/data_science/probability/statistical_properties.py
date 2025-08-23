"""
Statistical Properties and Mathematical Operations on Random Variables

This module demonstrates and implements key mathematical properties of expectation
and variance operators, providing both theoretical insights and practical utilities
for working with probability distributions.

Mathematical Properties Implemented:
- Linearity of Expectation: E[aX + bY] = aE[X] + bE[Y]
- Variance Transformations: Var[aX + b] = a²Var[X]
- Covariance Properties: Var[X + Y] = Var[X] + Var[Y] + 2Cov[X,Y]
- Moment Generating Functions and their applications
"""
from typing import Callable, Sequence, Any, Tuple, List

from data_science.probability.random_variable import RandomVariable
from data_science.probability.utilities import is_convex_approx


class ExpectationOperator:
    """
    Demonstrates mathy properties of the expectation operator E[·].
    """

    @staticmethod
    def additivity(random_variable_x: RandomVariable, random_variable_y: RandomVariable,
                   joint_sampler: Callable[[int], Tuple[List[float], List[float]]],
                   sample_size: int = 50000) -> dict:
        """
        Tests the fundamental property of expectation: E(X + Y) = E(X) + E(Y)

        This property holds regardless of whether X and Y are independent or dependent,
        making it one of the most important and powerful properties in probability theory.

        Mathematical Foundation:
            For any random variables X and Y (independent or dependent):
            E[X + Y] = E[X] + E[Y]

            This is a consequence of the linearity of expectation, which states that
            expectation is a linear operator over the space of random variables.

        Args:
            random_variable_x: First random variable X
            random_variable_y: Second random variable Y
            joint_sampler: Function that generates paired samples (x_i, y_i) from the joint distribution
            sample_size: Number of samples to use for empirical verification

        Returns:
            dict: Comprehensive analysis comparing theoretical and empirical results

        Example:
            >>> bernoulli = BernoulliDistribution(0.3)
            >>> poisson = PoissonDistribution(2.5)
            >>> def sampler(n): return (bernoulli.sample(n), poisson.sample(n))
            >>> result = additivity(bernoulli, poisson, sampler)
            >>> print(f"Error: {result['absolute_error']:.6f}")
        """
        # Theoretical calculation using linearity property
        theoretical_e_x = random_variable_x.mean
        theoretical_e_y = random_variable_y.mean
        theoretical_sum = theoretical_e_x + theoretical_e_y

        # Generate paired samples from joint distribution
        samples_x, samples_y = joint_sampler(sample_size)

        # Validate that the samples are lists
        if not isinstance(samples_x, list):
            samples_x = [samples_x]
        if not isinstance(samples_y, list):
            samples_y = [samples_y]

        # Empirical calculation of individual expectations
        empirical_e_x = sum(samples_x) / len(samples_x)
        empirical_e_y = sum(samples_y) / len(samples_y)
        empirical_sum = empirical_e_x + empirical_e_y

        # Empirical calculation of E[X + Y] directly
        sum_samples = [x + y for x, y in zip(samples_x, samples_y)]
        empirical_sum_direct = sum(sum_samples) / len(sum_samples)

        # Calculate absolute error
        absolute_error = abs(theoretical_sum - empirical_sum)
        relative_error = absolute_error / abs(theoretical_sum) if theoretical_e_x != 0 else float('inf')

        # Additional verification: empirical E[X] + empirical E[Y] vs empirical E[X + Y]
        empirical_additivity_error = abs(empirical_sum - empirical_sum_direct)

        # Statistical confidence measures
        sample_standard_deviation = (
                (sum((s - empirical_sum_direct) ** 2 for s in sum_samples) / len(sum_samples)) ** 0.5)
        # 95% confidence interval
        margin_of_error_95 = 1.96 * sample_standard_deviation / (len(sum_samples) ** 0.5)

        # Independence test for informational purposes (calculate sample correlation coefficient)
        mean_x_sample = sum(samples_x) / len(samples_x)
        mean_y_sample = sum(samples_y) / len(samples_y)

        numerator = sum((x - mean_x_sample) + (y - mean_y_sample) for x,y in zip(samples_x, samples_y))
        denominator_x = sum((x - mean_x_sample)**2 for x in samples_x)**0.5
        denominator_y = sum((y - mean_y_sample)**2 for y in samples_y)**0.5

        correlation = numerator / (denominator_x * denominator_y) if denominator_x != 0 and denominator_y != 0 else 0
        independent = abs(correlation) < 1e-6

        return {
            'property': 'E(X + Y) = E(X) + E(Y)',
            'theoretical E(X + Y)': theoretical_sum,
            'empirical E(X + Y)': empirical_sum,
            'absolute_error': absolute_error,
            'relative_error_percent': relative_error * 100,

            # Component Analysis
            'components' : {
                'theoretical E(X)': theoretical_e_x,
                'theoretical E(Y)': theoretical_e_y,
                'empirical E(X)': empirical_e_x,
                'empirical E(Y)': empirical_e_y,
                'empirical sum of expectations E(X + Y)': empirical_sum_direct,
            },

            # Statistical measures
            'statistical_analysis': {
                'sample_size': sample_size,
                'sample_standard_deviation': sample_standard_deviation,
                'margin_of_error_95_percent': margin_of_error_95,
                'empirical_additivity_error': empirical_additivity_error
            },

            # Independence analysis (informational)
            'independence_analysis': {
                'sample_correlation': correlation,
                'likely_independent': independent,
                'note': 'Linearity holds regardless of independence'
            },

            # Test interpretation
            'test_passed': absolute_error < margin_of_error_95,
            'confidence_level': '95%',
            'interpretation': {
                'excellent': absolute_error < 0.01,
                'good': 0.01 <= absolute_error < 0.05,
                'acceptable': 0.05 <= absolute_error < 0.1,
                'poor': absolute_error >= 0.1
            }

        }

    @staticmethod
    def linearity(random_variable_x: RandomVariable, random_variable_y: RandomVariable,
                             a: float, b: float,
                             joint_sampler: Callable[[int], Tuple[Sequence[Any], Sequence[Any]]],
                             sample_size: int = 10000) -> dict:
        """
        Demonstrates linearity of expectation: E[aX + bY] = aE[X] + bE[Y]

        This property holds regardless of whether X and Y are independent,
        making it one of the most powerful tools in probability theory.

        Args:
            random_variable_x: First random variable X
            random_variable_y: Second random variable Y
            a: Scalar multiplier for X
            b: Scalar multiplier for Y
            joint_sampler: Function to generate paired samples from (X,Y)
            sample_size: Number of samples to use for empirical verification

        Returns:
            dict: Comparison of theoretical vs empirical results
        """
        # Theoretical calculation using linearity property
        theoretical_mean = a * random_variable_x.mean + b * random_variable_y.mean

        # Empirical verification through sampling
        samples_x, samples_y = joint_sampler(sample_size)
        empirical_combined = [a * x + b * y for x, y in zip(samples_x, samples_y)]
        empirical_mean = sum(empirical_combined) / len(empirical_combined)

        return {
            'property': 'E[aX + bY] = aE[X] + bE[Y]',
            'theoretical': theoretical_mean,
            'empirical': empirical_mean,
            'error': abs(theoretical_mean - empirical_mean),
            'individual_means': {'E[X]': random_variable_x.mean, 'E[Y]': random_variable_y.mean},
            'scalar_multipliers': {'a': a, 'b': b}
        }

    @staticmethod
    def constant_shift(random_variable: RandomVariable, a: float, sample_size: int = 50000) -> dict:
        """
        Tests the property of expectation with constant shift: E[X + a] = E[X] + a

        This property demonstrates that the expectation operator is translation-invariant:
        adding a constant to a random variable shifts its expected value by exactly that constant.

        Mathematical Foundation:
            For any random variable X and constant a:
            E[X + a] = E[X] + a

            This follows from the linearity of expectation, where the constant 'a'
            can be viewed as a degenerate random variable that always takes the value 'a'.

            Proof outline:
            E[X + a] = ∫(x + a)f(x)dx = ∫xf(x)dx + ∫af(x)dx = E[X] + a∫f(x)dx = E[X] + a

            Key insight: Constants "pass through" the expectation operator unchanged.

        Args:
            random_variable: Random variable X to test
            a: Constant to add to the random variable
            sample_size: Number of samples for empirical verification

        Returns:
            dict: Comprehensive analysis of the constant shift property

        Example:
            >>> poisson = PoissonDistribution(3.0)
            >>> result = constant_shift(poisson, 5.0)
            >>> print(f"E[X] = {result['original_mean']:.3f}")
            >>> print(f"E[X + 5] = {result['theoretical_shifted_mean']:.3f}")
            >>> print(f"Error: {result['absolute_error']:.6f}")
        """
        # Theoretical calculation
        theoretical_mean = random_variable.mean
        theoretical_shifted_mean = theoretical_mean + a

        # Generate samples from the original distribution
        samples = random_variable.sample(sample_size)
        if not isinstance(samples, list):
            samples = [samples]

        # Empirical calculation
        empirical_mean = sum(samples) / len(samples)

        # Apply constant shift to samples
        shifted_samples = [ x + a for x in samples ]
        empirical_shifted_mean = sum(shifted_samples) / len(shifted_samples)

        # Calculate errors
        absolute_error = abs(theoretical_shifted_mean - empirical_shifted_mean)
        relative_error = (
                absolute_error / abs(theoretical_shifted_mean)) if theoretical_shifted_mean != 0 else float('inf')

        # Alternate verification: empirical E[X] + a vs. empirical E[X + a]
        empirical_shift_verification = empirical_mean + a
        empirical_shift_error = abs(empirical_shifted_mean - empirical_shift_verification)

        # Statistical Measures
        sample_standard_deviation = (
                (sum((s - empirical_shifted_mean) ** 2 for s in shifted_samples) / len(shifted_samples)) ** 0.5)
        # 95% confidence interval
        margin_of_error_95 = 1.96 * sample_standard_deviation / (len(shifted_samples) ** 0.5)

        # Variance verification (should remain unchanged0
        theoretical_variance = random_variable.variance
        empirical_variance_shifted = (
                sum((s - empirical_shifted_mean) ** 2 for s in shifted_samples) / len(shifted_samples))
        variance_shift_error = abs(theoretical_variance - empirical_variance_shifted)

        return {
            # Primary test results
            'property': 'E[X + a] = E[X] + a',
            'constant_shift': a,
            'theoretical_mean': theoretical_mean,
            'theoretical_shifted_mean': theoretical_shifted_mean,
            'empirical_shifted_mean': empirical_shifted_mean,
            'absolute_error': absolute_error,
            'relative_error_percent': relative_error * 100,

            # Component analysis
            'components': {
                'empirical_mean': empirical_mean,
                'empirical_shift_verification': empirical_shift_verification,
                'empirical_shift_error': empirical_shift_error
            },

            # Statistical analysis
            'statistical_analysis': {
                'sample_size': sample_size,
                'sample_standard_deviation': sample_standard_deviation,
                'margin_of_error_95_percent': margin_of_error_95
            },

            # Variance preservation check
            'variance_analysis': {
                'theoretical_variance': theoretical_variance,
                'empirical_variance_shifted': empirical_variance_shifted,
                'variance_shift_error': variance_shift_error,
                'variance_preserved': variance_shift_error < 0.01,
                'note': 'Variance should remain unchanged under constant shift'
            },

            # Test results
            'test_passed': absolute_error < margin_of_error_95,
            'confidence_level': '95%',
            'interpretation': {
                'excellent': absolute_error < 0.01,
                'good': 0.01 <= absolute_error < 0.05,
                'acceptable': 0.05 <= absolute_error < 0.1,
                'poor': absolute_error >= 0.1
            }
        }

    @staticmethod
    def transformation_properties(random_variable: RandomVariable,
                                  transform_function: Callable[[float], float],
                                  transform_name: str) -> dict:
        """
        Explores E[g(X)] for various transformation functions g.

        Note: In general, E[g(X)] ≠ g(E[X]) (Jensen's inequality)

        Args:
            random_variable: Random variable X
            transform_function: Transformation function g
            transform_name: Description of the transformation

        Returns:
            dict: Analysis of E[g(X)] vs g(E[X])
        """
        # Sample from the distribution
        samples = random_variable.sample(10000)
        if not isinstance(samples, list):
            samples = [samples]

        # Calculate E[g(X)] empirically
        transformed_samples = [transform_function(x) for x in samples]
        e_gx = sum(transformed_samples) / len(transformed_samples)

        # Calculate g(E[X]) theoretically
        g_ex = transform_function(random_variable.mean)

        return {
            'transformation': transform_name,
            'E[g(X)]': e_gx,
            'g(E[X])': g_ex,
            'difference': e_gx - g_ex,
            'jensen_inequality_holds': e_gx >= g_ex if is_convex_approx(transform_function) else None
        }


class VarianceOperator:
    """
    Demonstrates mathy properties of the variance operator Var[·].

    Note: The variance operator is not a linear transformation of the mean.
    """


    @staticmethod
    def scaling_property(random_variable: RandomVariable, a: float, b: float) -> dict:
        """
        Demonstrates variance scaling: Var[aX + b] = a²Var[X]

        Key insight: Adding a constant (b) doesn't change variance,
        but scaling by (a) multiplies variance by a².

        Args:
            random_variable: Random variable X
            a: Scale factor
            b: Shift constant

        Returns:
            dict: Theoretical vs empirical variance calculations
        """
        # Theoretical calculation using scaling property
        theoretical_variance = a ** 2 * random_variable.variance

        # Empirical verification
        samples = random_variable.sample(10000)
        if not isinstance(samples, list):
            samples = [samples]

        transformed_samples = [a * x + b for x in samples]
        empirical_mean = sum(transformed_samples) / len(transformed_samples)
        empirical_variance = sum((x - empirical_mean) ** 2 for x in transformed_samples) / len(transformed_samples)


        return {
            'property': 'Var[aX + b] = a²Var[X]',
            'theoretical_variance': theoretical_variance,
            'empirical_variance': empirical_variance,
            'error': abs(theoretical_variance - empirical_variance),
            'scale_factor': a,
            'shift_constant': b,
            'note':'Shift constant does not affect variance'
        }

    @staticmethod
    def sum_property(random_variable_x: RandomVariable, random_variable_y: RandomVariable,
                     joint_sampler: Callable[[int], Tuple[List[float], List[float]]]) -> dict:
        """
        Demonstrates: Var[X + Y] = Var[X] + Var[Y] + 2Cov[X,Y]

        For independent variables, Cov[X,Y] = 0, so Var[X + Y] = Var[X] + Var[Y]

        Args:
            random_variable_x: First random variable
            random_variable_y: Second random variable
            joint_sampler: Function to generate paired samples

        Returns:
            dict: Analysis of variance additivity
        """
        # Generate samples to estimate covariance
        samples_x, samples_y = joint_sampler(10000)

        # Calculater empirical covariance
        mean_x = sum(samples_x) / len(samples_x)
        mean_y = sum(samples_y) / len(samples_y)
        covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(samples_x, samples_y)) / len(samples_x)

        # Theoretical variance of sum
        theoretical_sum_variance = random_variable_x.variance + random_variable_y.variance + 2 * covariance

        # Empirical variance of sum
        sum_samples = [x + y for x, y in zip(samples_x, samples_y)]
        empirical_sum_mean = sum(sum_samples) / len(sum_samples)
        empirical_sum_variance = sum((s - empirical_sum_mean) ** 2 for s in sum_samples) / len(sum_samples)

        return {
            'property': 'Var[X + Y] = Var[X] + Var[Y] + 2Cov[X,Y]',
            'variance_x': random_variable_x.variance,
            'variance_y': random_variable_y.variance,
            'covariance': covariance,
            'theoretical_sum_variance': theoretical_sum_variance,
            'empirical_sum_variance': empirical_sum_variance,
            'error': abs(theoretical_sum_variance - empirical_sum_variance),
            'independence_assumption': abs(covariance) < 1e-6
        }


    @staticmethod
    def constant_shift_invariance(random_variable: RandomVariable, a: float, sample_size: int = 50000) -> dict:
        """
        Tests the variance invariance property under constant shift: Var[X + a] = Var[X]

        This property demonstrates that variance is translation-invariant: adding a constant
        to a random variable does not change its variance. This occurs because variance
        measures spread around the mean, and shifting all values by the same constant
        preserves the relative distances between values.

        Mathematical Foundation:
            For any random variable X and constant a:
            Var[X + a] = Var[X]

            Proof:
            Var[X + a] = E[(X + a - E[X + a])²]
                       = E[(X + a - (E[X] + a))²]    [by linearity of expectation]
                       = E[(X - E[X])²]              [constant cancels out]
                       = Var[X]

            Key insight: Constants shift the mean but preserve deviations from the mean.

        Geometric Interpretation:
            Adding a constant translates the entire distribution along the x-axis
            without changing its shape or spread. The variance measures the "width"
            of the distribution, which remains unchanged under translation.

        Args:
            random_variable: Random variable X to test
            a: Constant to add to the random variable
            sample_size: Number of samples for empirical verification

        Returns:
            dict: Comprehensive analysis of variance invariance under constant shift

        Example:
            >>> binomial = BinomialDistribution(20, 0.3)
            >>> result = constant_shift_invariance(binomial, 10.0)
            >>> print(f"Var[X] = {result['original_variance']:.3f}")
            >>> print(f"Var[X + 10] = {result['empirical_shifted_variance']:.3f}")
            >>> print(f"Invariance preserved: {result['invariance_preserved']}")
        """
        # Theoretical variance (should remain unchanged)
        theoretical_variance = random_variable.variance
        theoretical_shifted_variance = theoretical_variance

        # Generate samples from the original distribution
        samples = random_variable.sample(sample_size)
        if not isinstance(samples, list):
            samples = [samples]

        # Calculate empirical variance of original samples
        empirical_mean = sum(samples) / len(samples)
        empirical_variance = sum((x - empirical_mean) ** 2 for x in samples) / len(samples)

        # Apply constant shift and calculate the variance of the shifted samples
        shifted_samples = [x + a for x in samples]
        shifted_mean = sum(shifted_samples) / len(shifted_samples)
        empirical_shifted_variance = sum((x - shifted_mean) ** 2 for x in shifted_samples) / len(shifted_samples)

        # Calculate errors
        absolute_error = abs(theoretical_shifted_variance - empirical_shifted_variance)
        relative_error = (
                absolute_error / theoretical_shifted_variance) if theoretical_shifted_variance != 0 else float('inf')


        # Empirical consistency check: empirical Var[X] vs. empirical Var[X + a]
        empirical_invariance_error = abs(empirical_variance - empirical_shifted_variance)

        # Statistical measures
        # Uses Bessel's correction for sample variance estimation
        sample_variance_bessel_correction = (
                sum((x - shifted_mean) ** 2 for x in shifted_samples) / (len(shifted_samples) - 1))
        sample_standard_deviation = sample_variance_bessel_correction ** 0.5

        # Confidence intervals are more complicated for variance, but we can use still get an approximate
        # estimate using normal approximation.
        margin_of_error_95 = 1.96 * sample_standard_deviation / (len(shifted_samples) ** 0.5)

        # Mean shift verification (should equal our 'a' constant)
        theoretical_mean_shift = a
        empirical_mean_shift = shifted_mean - empirical_mean
        mean_shift_error = abs(theoretical_mean_shift - empirical_mean_shift)

        # Standard deviation preservation (should remain unchanged)
        standard_deviation = random_variable.standard_deviation
        empirical_shifted_standard_deviation = empirical_shifted_variance ** 0.5
        standard_deviation_error = abs(standard_deviation - empirical_shifted_standard_deviation)

        return {
            # Primary test results
            'property': 'Var[X + a] = Var[X]',
            'constant_shift': a,
            'theoretical_variance': theoretical_variance,
            'theoretical_shifted_variance': theoretical_shifted_variance,
            'empirical_shifted_variance': empirical_shifted_variance,
            'absolute_error': absolute_error,
            'relative_error_percent': relative_error * 100,

            # Component analysis
            'components': {
                'empirical_variance': empirical_variance,
                'empirical_invariance_error': empirical_invariance_error,
                'variance_preservation_ratio': empirical_shifted_variance / empirical_variance if empirical_variance != 0 else float(
                    'inf')
            },

            # Mean shift verification
            'mean_analysis': {
                'theoretical_mean_shift': theoretical_mean_shift,
                'empirical_mean_shift': empirical_mean_shift,
                'mean_shift_error': mean_shift_error,
                'mean_shift_correct': mean_shift_error < 0.01,
                'note': 'Mean should shift by exactly the constant value'
            },

            # Standard deviation preservation
            'std_analysis': {
                'standard_deviation': standard_deviation,
                'empirical_shifted_standard_deviation': empirical_shifted_standard_deviation,
                'std_preservation_error': standard_deviation_error,
                'std_preserved': standard_deviation_error < 0.01,
                'note': 'Standard deviation should remain unchanged'
            },

            # Statistical measures
            'statistical_analysis': {
                'sample_size': sample_size,
                'sample_std_corrected (Bessel)': sample_standard_deviation,
                'margin_of_error_95_percent': margin_of_error_95
            },

            # Test results
            'invariance_preserved': empirical_invariance_error < 0.01,
            'test_passed': absolute_error < margin_of_error_95,
            'confidence_level': '95%',
            'interpretation': {
                'excellent': absolute_error < 0.01,
                'good': 0.01 <= absolute_error < 0.05,
                'acceptable': 0.05 <= absolute_error < 0.1,
                'poor': absolute_error >= 0.1
            },

        }



