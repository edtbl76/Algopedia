"""
Statistical Utilities for Empirical Testing

This module provides utility classes for validating sample data, performing
statistical calculations, and analyzing test results in the context of
statistical property verification. It supports the empirical testing framework
by offering robust data validation, comprehensive statistical computations,
and standardized result interpretation.

The module is organized into three main utility classes:
- SampleValidator: Ensures data integrity and proper formatting
- StatisticalCalculations: Performs core statistical computations
- TestResultAnalyzer: Interprets results and provides quality assessments

These utilities are designed to be stateless and thread-safe, making them
suitable for use across multiple statistical property tests.
"""
from typing import List, Tuple

from data_science.probability.statistical_properties.config import TestConfiguration
from data_science.probability.statistical_properties.enums import TestInterpretation


class SampleValidator:
    """
    Validates and normalizes sample data for statistical analysis.

    This utility class ensures that sample data is properly formatted and
    validated before being used in statistical calculations. It handles
    common data format issues and provides consistent data structures
    for downstream processing.

    All methods are static to support stateless operation and can be
    used independently without class instantiation.
    """

    @staticmethod
    def ensure_list(samples) -> List[float]:
        """
        Ensures that samples is properly formatted as a list of floats.

        Converts single values to single-element lists and handles None values
        gracefully. This normalization ensures consistent data structure for
        statistical calculations that expect list inputs.

        Args:
            samples: Sample data that may be a single value, list, or None

        Returns:
            List of floats representing the sample data
        """
        if not isinstance(samples, list):
            return [samples] if samples is not None else []
        return samples

    @staticmethod
    def validate_sample_pairs(samples_x: List[float], samples_y: List[float]) -> Tuple[List[float], List[float]]:
        """
        Validate and normalize paired samples for joint statistical analysis.

        Ensures both sample lists are properly formatted and have matching lengths,
        which is essential for computing joint statistics like covariance and
        correlation coefficients.

        Args:
            samples_x: Sample data for the first random variable
            samples_y: Sample data for the second random variable

        Returns:
            Tuple containing validated and normalized sample pairs

        Raises:
            ValueError: If the sample pairs have different lengths

        Example:
            >>> x_samples = [1.0, 2.0, 3.0]
            >>> y_samples = [4.0, 5.0, 6.0]
            >>> validated_x, validated_y = SampleValidator.validate_sample_pairs(x_samples, y_samples)
            >>> len(validated_x) == len(validated_y)
            True
        """
        samples_x = SampleValidator.ensure_list(samples_x)
        samples_y = SampleValidator.ensure_list(samples_y)

        if len(samples_x) != len(samples_y):
            raise ValueError("Sample pairs must have the same length.")

        return samples_x, samples_y


class StatisticalCalculations:
    """
    Utility class for fundamental statistical calculations.

    Provides a comprehensive set of statistical functions commonly needed
    for empirical verification of mathematical properties. All calculations
    use numerically stable algorithms and handle edge cases gracefully.

    The class focuses on descriptive statistics, correlation measures, and
    confidence interval calculations that are essential for statistical
    hypothesis testing and property verification.
    """

    @staticmethod
    def mean(samples: List[float]) -> float:
        """
        Calculate the arithmetic mean (average) of a list of samples.

        Computes the sample mean using the standard formula: sum(x_i) / n.
        Handles empty lists gracefully by returning 0.0.

        Args:
            samples: List of numerical sample values

        Returns:
            The arithmetic mean of the samples

        """
        return sum(samples) / len(samples) if samples else 0.0

    @staticmethod
    def variance(samples: List[float], mean: float = None) -> float:
        """
        Calculate the population variance of a list of samples.

        Computes variance using the formula: Σ(x_i - μ)² / n where μ is the mean.
        This is the population variance (divides by n, not n-1). If the mean
        is not provided, it will be calculated from the samples.

        Args:
            samples: List of numerical sample values
            mean: Pre-calculated mean value (optional, will be computed if None)

        Returns:
            The population variance of the samples


        Note:
            Uses population variance (n denominator) rather than sample variance
            (n-1 denominator) as this is typically used for theoretical comparisons.
        """
        if not samples:
            return 0.0

        if mean is None:
            mean = StatisticalCalculations.mean(samples)

        return sum((x - mean) ** 2 for x in samples) / len(samples)

    @staticmethod
    def standard_deviation(samples: List[float], mean: float = None) -> float:
        """
        Calculate the standard deviation of a list of samples.

        Computes standard deviation as the square root of variance. Uses
        population standard deviation for consistency with variance calculation.

        Args:
            samples: List of numerical sample values
            mean: Pre-calculated mean value (optional, will be computed if None)

        Returns:
            The standard deviation of the samples

        """
        return StatisticalCalculations.variance(samples, mean) ** 0.5


    @staticmethod
    def covariance(samples_x: List[float], samples_y: List[float], mean_x: float = None, mean_y: float = None) -> float:
        """
        Calculate the covariance between two lists of samples.

        Computes sample covariance using the formula: Σ(x_i - μ_x)(y_i - μ_y) / n.
        Covariance measures how much two variables vary together. Positive values
        indicate variables tend to move in the same direction, negative values
        indicate opposite directions, and zero indicates no linear relationship.

        Args:
            samples_x: First set of sample values
            samples_y: Second set of sample values
            mean_x: Pre-calculated mean of X samples (optional)
            mean_y: Pre-calculated mean of Y samples (optional)

        Returns:
            The covariance between the two sample sets

        Note:
            Returns 0.0 if samples have different lengths or are empty.

        """
        if len(samples_x) != len(samples_y) or not samples_x or not samples_y:
            return 0.0

        if mean_x is None:
            mean_x = StatisticalCalculations.mean(samples_x)

        if mean_y is None:
            mean_y = StatisticalCalculations.mean(samples_y)

        return sum((x - mean_x) * (y - mean_y) for x, y in zip(samples_x, samples_y)) / len(samples_x)


    @staticmethod
    def correlation_coefficient(samples_x: List[float], samples_y: List[float],
                                mean_x: float = None, mean_y: float = None) -> float:
        """
        Calculate the Pearson correlation coefficient between two sample sets.

        Computes the correlation coefficient using the formula:
        r = Cov(X,Y) / (σ_X * σ_Y)

        The correlation coefficient ranges from -1 to 1, where:
        - 1 indicates perfect positive linear correlation
        - 0 indicates no linear correlation
        - -1 indicates perfect negative linear correlation

        Args:
            samples_x: First set of sample values
            samples_y: Second set of sample values
            mean_x: Pre-calculated mean of X samples (optional)
            mean_y: Pre-calculated mean of Y samples (optional)

        Returns:
            The Pearson correlation coefficient between the sample sets

        Note:
            Returns 0.0 if samples have different lengths, are empty, or if
            either variable has zero standard deviation.

        """
        if len(samples_x) != len(samples_y) or not samples_x or not samples_y:
            return 0.0

        if mean_x is None:
            mean_x = StatisticalCalculations.mean(samples_x)

        if mean_y is None:
            mean_y = StatisticalCalculations.mean(samples_y)

        numerator = StatisticalCalculations.covariance(samples_x, samples_y, mean_x, mean_y)
        denominator_x = StatisticalCalculations.standard_deviation(samples_x, mean_x)
        denominator_y = StatisticalCalculations.standard_deviation(samples_y, mean_y)

        return numerator / (denominator_x * denominator_y) if denominator_x != 0 and denominator_y != 0 else 0.0

    @staticmethod
    def confidence_interval_95(samples: List[float], mean: float = None) -> float:
        """
        Calculate the margin of error for a 95% confidence interval.

        Computes the margin of error using the formula:
        margin = 1.96 * (σ / √n)

        This assumes a large sample size where the Central Limit Theorem applies
        and the sampling distribution of the mean is approximately normal.
        The value 1.96 corresponds to the 95% confidence level.

        Args:
            samples: List of sample values
            mean: Pre-calculated mean value (optional, will be computed if None)

        Returns:
            The margin of error for the 95% confidence interval


        Note:
            Returns 0.0 for empty sample lists. For small sample sizes (n < 30),
            a t-distribution would be more appropriate, but this implementation
            uses the normal approximation for simplicity.
        """
        if not samples:
            return 0.0

        if mean is None:
            mean = StatisticalCalculations.mean(samples)

        sample_standard_deviation = StatisticalCalculations.standard_deviation(samples, mean)
        return 1.96 * sample_standard_deviation / (len(samples) ** 0.5)


class TestResultAnalyzer:
    """
    Analyzes test results and provides standardized interpretations.

    This utility class provides methods for interpreting statistical test
    results according to predefined tolerance thresholds. It helps standardize
    the quality assessment of empirical test results across different
    statistical property tests.

    The analyzer uses configurable tolerance levels to categorize test
    performance and provides both individual assessments and comprehensive
    interpretation frameworks.
    """

    @staticmethod
    def interpret_error(error: float, config: TestConfiguration) -> TestInterpretation:
        """
        Interpret the magnitude of an error value using configured tolerance thresholds.

        Classifies the error into one of four quality categories based on the
        configured tolerance levels in the TestConfiguration. This provides
        a standardized way to assess test result quality across different
        statistical property tests.

        Args:
            error: The absolute error value to interpret
            config: TestConfiguration containing tolerance thresholds

        Returns:
            TestInterpretation enum value indicating the quality category

        Quality Categories:
        - EXCELLENT: Error below the excellent tolerance threshold
        - GOOD: Error between excellent and good tolerance thresholds
        - ACCEPTABLE: Error between good and acceptable tolerance thresholds
        - POOR: Error above the acceptable tolerance threshold

        Example:
            >>> config = TestConfiguration(tolerance_excellent=0.01, tolerance_good=0.05)
            >>> TestResultAnalyzer.interpret_error(0.005, config)
            <TestInterpretation.EXCELLENT: 'excellent'>
        """
        if error < config.tolerance_excellent:
            return TestInterpretation.EXCELLENT
        elif error < config.tolerance_good:
            return TestInterpretation.GOOD
        elif error < config.tolerance_acceptable:
            return TestInterpretation.ACCEPTABLE
        else:
            return TestInterpretation.POOR

    @staticmethod
    def create_interpretation_result(config: TestConfiguration) -> dict:
        """
        Create a comprehensive interpretation framework dictionary.

        Generates a dictionary that maps quality categories to their
        corresponding error threshold ranges. This provides a complete
        reference for interpreting test results and can be included
        in test result objects for documentation purposes.

        Args:
            config: TestConfiguration containing tolerance thresholds

        Returns:
            Dictionary mapping interpretation categories to threshold descriptions

        Example:
            >>> config = TestConfiguration(tolerance_excellent=0.01, tolerance_good=0.05, tolerance_acceptable=0.1)
            >>> result = TestResultAnalyzer.create_interpretation_result(config)
            >>> result['excellent']
            'error < 0.01'
            >>> result['poor']
            'error >= 0.1'
        """
        return {
            TestInterpretation.EXCELLENT.value: f"error < {config.tolerance_excellent}",
            TestInterpretation.GOOD.value: f"{config.tolerance_excellent} <= error < {config.tolerance_good}",
            TestInterpretation.ACCEPTABLE.value: f"{config.tolerance_good} <= error < {config.tolerance_acceptable}",
            TestInterpretation.POOR.value: f"error >= {config.tolerance_acceptable}"
        }

