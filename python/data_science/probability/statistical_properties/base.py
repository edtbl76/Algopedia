from data_science.probability.statistical_properties.config import TestConfiguration


class StatisticalProperty:
    """
    Abstract base class for statistical properties of random variables.

    This class serves as a foundation for implementing statistical operators
    like expectation, variance, and other probability-related computations.
    Classes that inherit from this should implement specific statistical
    properties and mathematical operations on random variables.

    Attributes:
        config (TestConfiguration): Configuration settings for statistical tests,
            including sample size, confidence levels, and tolerance thresholds.
            If not provided, a default configuration is used.
    """

    def __init__(self, config: TestConfiguration = None) -> None:
        """
        Initialize a statistical property with configuration settings.

        Args:
            config (TestConfiguration, optional): Configuration for statistical tests.
                If None, a default TestConfiguration is created.
        """
        self.config = config or TestConfiguration()






