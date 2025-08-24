class StatisticalTestError(Exception):
    """ Base class for statistical test errors """
    pass

class InvalidSampleError(StatisticalTestError):
    """ Raised when a sample is invalid for statistical tests """
    pass

class InsufficientDataError(StatisticalTestError):
    """ Raised when a sample size is insufficient for statistical tests """
    pass


