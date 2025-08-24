"""
Expectation Operator Implementation

This module implements and empirically verifies the mathematical properties of
the expectation operator E[·] on random variables. It provides methods to test
key properties of expected values through both theoretical calculations and
empirical sampling verification.

Key mathematical properties tested include:
- Additivity: E[X + Y] = E[X] + E[Y] (regardless of independence)
- Linearity: E[aX + bY] = aE[X] + bE[Y] (for constants a, b)
- Constant Shift: E[X + a] = E[X] + a (for constant a)
- Transformation Properties: Exploring how E[g(X)] relates to g(E[X])

Each property is verified both theoretically and empirically using statistical
sampling, with comprehensive error analysis and statistical validation metrics.
"""
from typing import Callable, Tuple, List

from data_science.probability.random_variable import RandomVariable
from data_science.probability.statistical_properties.base import StatisticalProperty
from data_science.probability.statistical_properties.config import AdditivityTestResult, StatisticalAnalysis, \
    LinearityTestResult, ConstantShiftTestResult, TransformationTestResult
from data_science.probability.statistical_properties.exceptions import StatisticalTestError
from data_science.probability.statistical_properties.utils import SampleValidator, StatisticalCalculations, \
    TestResultAnalyzer
from data_science.probability.utilities import is_convex_approx


class ExpectationOperator(StatisticalProperty):
    """
    Demonstrates mathematical properties of the expectation operator E[·]

    This class demonstrates and validates fundamental mathematical properties
    of expectation through empirical sampling and statistical analysis. It
    inherits from StatisticalProperty to leverage shared testing configurations
    and utilities.
    """

    def additivity(self, random_variable_x: RandomVariable, random_variable_y: RandomVariable,
                   joint_sampler: Callable[[int], Tuple[List[float], List[float]]]) -> AdditivityTestResult:
        """
        Tests the fundamental additivity property of expectation: E(X + Y) = E(X) + E(Y)

        This property holds regardless of whether X and Y are independent or dependent,
        making it one of the most important and powerful properties in probability theory.
        The test compares theoretical calculations with empirical sampling results to
        validate the property within statistical confidence bounds.

        Args:
            random_variable_x: First random variable X
            random_variable_y: Second random variable Y
            joint_sampler: Function that generates paired samples from the joint distribution
                           of X and Y, accepting sample_size as parameter

        Returns:
            AdditivityTestResult containing theoretical and empirical results,
            error metrics, and statistical analysis

        Raises:
            StatisticalTestError: If sampling or calculation errors occur

        Example:
            >>> normal_x = NormalDistribution(mean=2.0, std_dev=1.0)
            >>> normal_y = NormalDistribution(mean=3.0, std_dev=2.0)
            >>> def joint_sampler(n): return (normal_x.sample(n), normal_y.sample(n))
            >>> result = expectation.additivity(normal_x, normal_y, joint_sampler)
            >>> print(f"Theoretical: {result.theoretical_sum}, Empirical: {result.empirical_sum}")
        """

        try:
            # Calculate theoretical values
            theoretical_results = self._calculate_theoretical_additivity(
                random_variable_x, random_variable_y)

            # Generate and validate samples
            samples_x, samples_y = self._generate_and_validate_samples(
                joint_sampler, self.config.sample_size)

            # Calculate empirical values
            empirical_results = self._calculate_empirical_additivity(
                samples_x, samples_y)

            # Perform statistical analysis
            statistical_results = self._statistical_analysis(
                samples_x, samples_y, theoretical_results, empirical_results)

            # Build result object
            return self._build_additivity_result(
                theoretical_results, empirical_results, statistical_results)

        except Exception as e:
            raise StatisticalTestError(f"Additivity test failed: {e}")

    @staticmethod
    def _calculate_theoretical_additivity(random_variable_x: RandomVariable,
                                          random_variable_y: RandomVariable) -> dict:
        """
        Calculate theoretical expectations for additivity property.

        Computes E[X], E[Y], and E[X+Y] based on theoretical properties.

        Args:
            random_variable_x: First random variable X
            random_variable_y: Second random variable Y

        Returns:
            Dictionary with theoretical expectation values
        """

        return {
            'e_x': random_variable_x.mean,
            'e_y': random_variable_y.mean,
            'e_sum': random_variable_x.mean + random_variable_y.mean
        }

    @staticmethod
    def _generate_and_validate_samples(joint_sampler: Callable,
                                       sample_size: int) -> Tuple[List[float], List[float]]:
        """
        Generate and validate paired samples from joint distribution.

        Uses the provided sampler function to generate paired samples and
        validates them to ensure they are properly formatted for analysis.

        Args:
            joint_sampler: Function that generates paired samples
            sample_size: Number of samples to generate

        Returns:
            Tuple of validated sample lists (samples_x, samples_y)
        """
        samples_x, samples_y = joint_sampler(sample_size)
        return SampleValidator.validate_sample_pairs(samples_x, samples_y)

    @staticmethod
    def _calculate_empirical_additivity(samples_x: List[float],
                                        samples_y: List[float]) -> dict:
        """
        Calculate empirical expectations and sums from samples.

        Computes empirical E[X], E[Y], E[X]+E[Y], and E[X+Y] directly from
        the provided samples.

        Args:
            samples_x: List of samples for random variable X
            samples_y: List of samples for random variable Y

        Returns:
            Dictionary with empirical calculations and sample data
        """
        empirical_e_x = StatisticalCalculations.mean(samples_x)
        empirical_e_y = StatisticalCalculations.mean(samples_y)
        empirical_sum = empirical_e_x + empirical_e_y

        # Direct calculation of E[X + Y]
        sum_samples = [x + y for x, y in zip(samples_x, samples_y)]
        empirical_sum_direct = StatisticalCalculations.mean(sum_samples)

        return {
            'empirical_e_x': empirical_e_x,
            'empirical_e_y': empirical_e_y,
            'empirical_sum': empirical_sum,
            'empirical_sum_direct': empirical_sum_direct,
            'sum_samples': sum_samples
        }

    @staticmethod
    def _statistical_analysis(samples_x: List[float], samples_y: List[float],
                              theoretical: dict, empirical: dict) -> dict:
        """
        Perform comprehensive statistical analysis on the samples and results.

        Calculates error metrics, statistical measures, and performs independence
        analysis by measuring correlation between samples.

        Args:
            samples_x: List of samples for random variable X
            samples_y: List of samples for random variable Y
            theoretical: Dictionary with theoretical calculations
            empirical: Dictionary with empirical calculations

        Returns:
            Dictionary with statistical analysis results
        """
        # Error calculations
        absolute_error = abs(theoretical['e_sum'] - empirical['empirical_sum'])
        relative_error = absolute_error / abs(theoretical['e_sum']) if theoretical['e_sum'] != 0 else float('inf')

        # Statistical measures
        sample_standard_deviation = StatisticalCalculations.standard_deviation(empirical['sum_samples'])
        margin_of_error_95 = StatisticalCalculations.confidence_interval_95(empirical['sum_samples'])

        # Independence Analysis
        correlation = StatisticalCalculations.correlation_coefficient(samples_x, samples_y)

        return {
            'absolute_error': absolute_error,
            'relative_error': relative_error,
            'sample_standard_deviation': sample_standard_deviation,
            'margin_of_error_95': margin_of_error_95,
            'correlation': correlation,
            'independent': abs(correlation) < 1e-6
        }

    def _build_additivity_result(self, theoretical: dict, empirical: dict,
                                 statistical: dict) -> AdditivityTestResult:
        """
        Assemble the final additivity test result object.

        Constructs a structured AdditivityTestResult object with all components
        of the test including theoretical and empirical values, error analysis,
        and test interpretation.

        Args:
            theoretical: Dictionary with theoretical calculations
            empirical: Dictionary with empirical calculations
            statistical: Dictionary with statistical analysis

        Returns:
            Structured AdditivityTestResult object
        """
        components = {
            'theoretical E(X)': theoretical['e_x'],
            'theoretical E(Y)': theoretical['e_y'],
            'empirical E(X)': empirical['empirical_e_x'],
            'empirical E(Y)': empirical['empirical_e_y'],
            'empirical sum of expectations E(X + Y)': empirical['empirical_sum_direct'],
        }

        statistical_analysis = StatisticalAnalysis(
            sample_size=self.config.sample_size,
            sample_standard_deviation=statistical['sample_standard_deviation'],
            margin_of_error_95_percent=statistical['margin_of_error_95']
        )

        independence_analysis = {
            'sample_correlation': statistical['correlation'],
            'likely_independent': statistical['independent'],
            'note': 'Linearity holds regardless of independence'
        }

        interpretation = TestResultAnalyzer.create_interpretation_result(self.config)

        return AdditivityTestResult(
            property='E(X + Y) = E(X) + E(Y)',
            theoretical_sum=theoretical['e_sum'],
            empirical_sum=empirical['empirical_sum'],
            absolute_error=statistical['absolute_error'],
            relative_error_percent=statistical['relative_error'] * 100,
            components=components,
            statistical_analysis=statistical_analysis,
            independence_analysis=independence_analysis,
            test_passed=statistical['absolute_error'] < statistical['margin_of_error_95'],
            interpretation=interpretation
        )

    def linearity(self, random_variable_x: RandomVariable, random_variable_y: RandomVariable,
                  a: float, b: float,
                  joint_sampler: Callable[[int], Tuple[List[float], List[float]]]) -> LinearityTestResult:
        """
        Demonstrates the linearity property of expectation: E[aX + bY] = aE[X] + bE[Y]

        This property is a generalization of additivity, showing that expectation
        is a linear operator with respect to both addition and scalar multiplication.
        It holds for any constants a and b, regardless of whether X and Y are independent.

        Args:
            random_variable_x: First random variable X
            random_variable_y: Second random variable Y
            a: Scalar multiplier for X
            b: Scalar multiplier for Y
            joint_sampler: Function that generates paired samples from the joint
                           distribution of X and Y

        Returns:
            LinearityTestResult containing theoretical and empirical results with
            error metrics

        Raises:
            StatisticalTestError: If sampling or calculation errors occur

        Example:
            >>> uniform_x = UniformDistribution(0, 1)
            >>> uniform_y = UniformDistribution(1, 2)
            >>> def sampler(n): return (uniform_x.sample(n), uniform_y.sample(n))
            >>> result = expectation.linearity(uniform_x, uniform_y, 2.0, 3.0, sampler)
            >>> print(f"Error: {result.error:.6f}")
        """
        try:
            # Theoretical calculation
            theoretical_mean = a * random_variable_x.mean + b * random_variable_y.mean

            # Empirical Verification
            samples_x, samples_y = joint_sampler(self.config.sample_size)
            empirical_combined = [a * x + b * y for x, y in zip(samples_x, samples_y)]
            empirical_mean = StatisticalCalculations.mean(empirical_combined)

            return LinearityTestResult(
                property='E[aX + bY] = aE[X] + bE[Y]',
                theoretical=theoretical_mean,
                empirical=empirical_mean,
                error=abs(theoretical_mean - empirical_mean),
                individual_means={'E[X]': random_variable_x.mean, 'E[Y]': random_variable_y.mean},
                scalar_multipliers={'a': a, 'b': b}
            )
        except Exception as e:
            raise StatisticalTestError(f"Linearity test failed: {e}")

    def constant_shift(self, random_variable: RandomVariable, a: float) -> ConstantShiftTestResult:
        """
        Tests the constant shift property of expectation: E[X + a] = E[X] + a

        This property demonstrates that adding a constant to a random variable
        shifts its expected value by exactly that constant. This is a special
        case of linearity and is particularly useful for understanding how
        translations affect probability distributions.

        Args:
            random_variable: Random variable X
            a: Constant value to add to X

        Returns:
            ConstantShiftTestResult containing detailed analysis of the property

        Raises:
            StatisticalTestError: If sampling or calculation errors occur

        Example:
            >>> exponential = ExponentialDistribution(rate=2.0)
            >>> result = expectation.constant_shift(exponential, 5.0)
            >>> print(f"Original mean: {result.theoretical_mean}")
            >>> print(f"Shifted mean: {result.empirical_shifted_mean}")
        """
        try:
            # Theoretical calculation
            theoretical_mean = random_variable.mean
            theoretical_shifted_mean = theoretical_mean + a

            # Generate and validate samples
            samples = SampleValidator.ensure_list(random_variable.sample(self.config.sample_size))

            # Empirical calculation
            empirical_mean = StatisticalCalculations.mean(samples)
            shifted_samples = [x + a for x in samples]
            empirical_shifted_mean = StatisticalCalculations.mean(shifted_samples)

            # Calculate errors
            absolute_error = abs(theoretical_shifted_mean - empirical_shifted_mean)
            relative_error = (
                    absolute_error / abs(theoretical_shifted_mean)) if theoretical_shifted_mean != 0 else float('inf')

            # Statistical analysis
            sample_standard_deviation = StatisticalCalculations.standard_deviation(samples)
            margin_of_error_95 = StatisticalCalculations.confidence_interval_95(samples)

            # Variance analysis
            theoretical_variance = random_variable.variance
            empirical_variance = StatisticalCalculations.variance(shifted_samples, empirical_shifted_mean)
            variance_shift_error = abs(theoretical_variance - empirical_variance)

            # Build components
            components = {
                'empirical_mean': empirical_mean,
                'empirical_shift_verification': empirical_mean + a,
                'empirical_shift_error': abs(empirical_shifted_mean - (empirical_mean + a))
            }

            statistical_analysis = StatisticalAnalysis(
                sample_size=self.config.sample_size,
                sample_standard_deviation=sample_standard_deviation,
                margin_of_error_95_percent=margin_of_error_95
            )

            variance_analysis = {
                'theoretical_variance': theoretical_variance,
                'empirical_variance_shifted': empirical_variance,
                'variance_shift_error': variance_shift_error,
                'variance_preserved': variance_shift_error < self.config.tolerance_excellent,
                'note': 'Variance should remain unchanged under constant shift'
            }

            interpretation = TestResultAnalyzer.create_interpretation_result(self.config)

            return ConstantShiftTestResult(
                property='E[X + a] = E[X] + a',
                constant_shift=a,
                theoretical_mean=theoretical_mean,
                theoretical_shifted_mean=theoretical_shifted_mean,
                empirical_shifted_mean=empirical_shifted_mean,
                absolute_error=absolute_error,
                relative_error_percent=relative_error * 100,
                components=components,
                statistical_analysis=statistical_analysis,
                variance_analysis=variance_analysis,
                test_passed=absolute_error < margin_of_error_95,
                interpretation=interpretation
            )
        except Exception as e:
            raise StatisticalTestError(f"Constant shift test failed: {e}")

    def transformation_properties(self, random_variable: RandomVariable,
                                  transform_function: Callable[[float], float],
                                  transform_name: str) -> TransformationTestResult:
        """
        Explores the relationship between E[g(X)] and g(E[X]) for transformation function g.

        This method investigates how applying a function to a random variable affects
        its expected value. It tests Jensen's inequality which states that for convex
        functions g, E[g(X)] ≥ g(E[X]), and for concave functions, E[g(X)] ≤ g(E[X]).

        Args:
            random_variable: Random variable X to transform
            transform_function: Transformation function g to apply to X
            transform_name: Descriptive name of the transformation

        Returns:
            TransformationTestResult containing the comparison between E[g(X)] and g(E[X])

        Raises:
            StatisticalTestError: If sampling or calculation errors occur

        Example:
            >>> normal = NormalDistribution(mean=0, std_dev=1)
            >>> square = lambda x: x**2
            >>> result = expectation.transformation_properties(normal, square, "square")
            >>> print(f"E[g(X)]: {result.e_gx:.4f}, g(E[X]): {result.g_ex:.4f}")
            >>> print(f"Jensen's inequality holds: {result.jensen_inequality_holds}")
        """
        try:
            # Sample from the distribution
            samples = SampleValidator.ensure_list(random_variable.sample(self.config.sample_size))

            # Calculate E[g(X)] empirically
            transformed_samples = [transform_function(x) for x in samples]
            e_gx = StatisticalCalculations.mean(transformed_samples)

            # Calculate g(E[X]) theoretically
            g_ex = transform_function(random_variable.mean)

            return TransformationTestResult(
                transformation=transform_name,
                e_gx=e_gx,
                g_ex=g_ex,
                difference=e_gx - g_ex,
                jensen_inequality_holds=e_gx >= g_ex if is_convex_approx(transform_function) else None
            )
        except Exception as e:
            raise StatisticalTestError(f"Transformation test failed: {e}")