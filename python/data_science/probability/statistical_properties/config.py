"""
Data Classes and Configuration

This module provides data classes for configuring and capturing results from
statistical property tests in probability theory. It contains configuration
parameters and structured result containers for empirical verification of
mathematical properties like linearity, additivity, variance scaling, and
transformations of random variables.

The classes facilitate:
- Test configuration with customizable sample sizes and tolerance thresholds
- Structured result objects for different statistical property tests
- Statistical analysis with confidence intervals and error measurements
- Interpretation of test results based on configurable quality thresholds

These components support the statistical verification framework that empirically
validates theoretical mathematical properties through sampling and analysis.
"""


from dataclasses import dataclass
from typing import Optional


@dataclass
class TestConfiguration:
    """ Configuration for statistical property tests """
    sample_size: int = 10000
    confidence_level: float = 0.95
    tolerance_excellent: float = 0.01
    tolerance_good: float = 0.05
    tolerance_acceptable: float = 0.1
    random_seed: Optional[int] = None


@dataclass
class StatisticalAnalysis:
    """
    Statistical analysis results from empirical testing.

    Contains metrics related to the statistical validation of theoretical properties,
    including standard deviation and confidence interval calculations.

    Attributes:
        sample_size: Number of samples used in the analysis
        sample_standard_deviation: Standard deviation of the sample data
        margin_of_error_95_percent: Margin of error at the 95% confidence level
        confidence_level: Confidence level as a formatted string
    """
    sample_size: int
    sample_standard_deviation: float
    margin_of_error_95_percent: float
    confidence_level: str = '95%'

@dataclass
class AdditivityTestResult:
    """
    Results from testing the additivity property of expectation: E[X + Y] = E[X] + E[Y].

    Contains both theoretical and empirical calculations along with error analysis
    and statistical validation metrics.

    Attributes:
        property: Mathematical property being tested
        theoretical_sum: Expected value based on mathematical theory
        empirical_sum: Value calculated from empirical sampling
        absolute_error: Absolute difference between theoretical and empirical values
        relative_error_percent: Percentage error relative to theoretical value
        components: Dictionary containing intermediate calculation components
        statistical_analysis: Statistical metrics of the empirical results
        independence_analysis: Analysis of variable independence (correlation)
        test_passed: Boolean indicating if the test passed at the specified confidence level
        interpretation: Quality assessment based on configured tolerance thresholds
    """
    property: str
    theoretical_sum: float
    empirical_sum: float
    absolute_error: float
    relative_error_percent: float
    components: dict
    statistical_analysis: StatisticalAnalysis
    independence_analysis: dict
    test_passed: bool
    interpretation: dict

@dataclass
class LinearityTestResult:
    """
    Results from testing the linearity property of expectation: E[aX + bY] = aE[X] + bE[Y].

    Contains comparison of theoretical calculations against empirical results.

    Attributes:
        property: Mathematical property being tested
        theoretical: Expected value based on mathematical theory
        empirical: Value calculated from empirical sampling
        error: Absolute difference between theoretical and empirical values
        individual_means: Dictionary containing mean values of individual variables
        scalar_multipliers: Dictionary containing the scalar coefficients used
    """
    property: str
    theoretical: float
    empirical: float
    error: float
    individual_means: dict
    scalar_multipliers: dict

@dataclass
class ConstantShiftTestResult:
    """
    Results from testing the constant shift property: E[X + a] = E[X] + a.

    Validates that adding a constant to a random variable shifts its expected
    value by exactly that constant.

    Attributes:
        property: Mathematical property being tested
        constant_shift: The constant value added to the random variable
        theoretical_mean: Original expected value based on theory
        theoretical_shifted_mean: Expected value after shifting
        empirical_shifted_mean: Empirically calculated mean after shifting
        absolute_error: Absolute difference between theoretical and empirical values
        relative_error_percent: Percentage error relative to theoretical value
        components: Dictionary containing intermediate calculation components
        statistical_analysis: Statistical metrics of the empirical results
        variance_analysis: Analysis of how variance is affected by the shift
        test_passed: Boolean indicating if the test passed at the specified confidence level
        interpretation: Quality assessment based on configured tolerance thresholds
    """
    property: str
    constant_shift: float
    theoretical_mean: float
    theoretical_shifted_mean: float
    empirical_shifted_mean: float
    absolute_error: float
    relative_error_percent: float
    components: dict
    statistical_analysis: StatisticalAnalysis
    variance_analysis: dict
    test_passed: bool
    interpretation: dict


@dataclass
class TransformationTestResult:
    """
    Results from testing transformation properties like E[g(X)] vs g(E[X]).

    Tests how applying a function to a random variable affects its expected value,
    relevant for understanding Jensen's inequality and convexity properties.

    Attributes:
        transformation: Description of the transformation function applied
        e_gx: Empirical calculation of E[g(X)]
        g_ex: Value of g(E[X])
        difference: Difference between E[g(X)] and g(E[X])
        jensen_inequality_holds: Whether Jensen's inequality is satisfied for this function
                                (None if the function's convexity is unclear)
    """
    transformation: str
    e_gx: float
    g_ex: float
    difference: float
    jensen_inequality_holds: Optional[bool]


@dataclass
class VarianceTestResult:
    """
    Results from testing variance properties such as Var[aX + b] = a²Var[X].

    Validates mathematical properties of the variance operator through
    comparison of theoretical calculations and empirical sampling.

    Attributes:
        property: Mathematical property being tested
        theoretical_variance: Expected variance based on mathematical theory
        empirical_variance: Variance calculated from empirical sampling
        error: Absolute difference between theoretical and empirical values
        additional_info: Additional information specific to the variance property test
    """
    property: str
    theoretical_variance: float
    empirical_variance: float
    error: float
    additional_info: dict


