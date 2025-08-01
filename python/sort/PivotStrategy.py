import random
from enum import Enum
from typing import List, Any


class PivotStrategy(Enum):
    """Enumeration of available pivot selection strategies."""
    MIDPOINT = "midpoint"
    RANDOM = "random"
    FIRST = "first"
    LAST = "last"
    MEDIAN_OF_THREE = "median_of_three"


class PivotSelector:
    """Handles pivot index selection based on strategy."""

    @staticmethod
    def select_pivot_index(values: List[Any], start: int, end: int,
                           strategy: PivotStrategy) -> int:
        """
        Select pivot index based on the specified strategy.

        Args:
            values: The list being partitioned
            start: Starting index (inclusive)
            end: Ending index (inclusive)
            strategy: The pivot selection strategy to use

        Returns:
            int: Index of the selected pivot element
        """
        if strategy == PivotStrategy.FIRST:
            return start
        elif strategy == PivotStrategy.LAST:
            return end
        elif strategy == PivotStrategy.MIDPOINT:
            return start + (end - start) // 2
        elif strategy == PivotStrategy.RANDOM:
            return random.randint(start, end)
        elif strategy == PivotStrategy.MEDIAN_OF_THREE:
            return PivotSelector._median_of_three_index(values, start, end)
        else:
            raise ValueError(f"Unknown pivot strategy: {strategy}")

    @staticmethod
    def _median_of_three_index(values: List[Any], start: int, end: int) -> int:
        """Find the index of the median among first, middle, and last elements."""
        mid = start + (end - start) // 2
        # Sort the three candidates to find median
        candidates = [(start, values[start]), (mid, values[mid]), (end, values[end])]
        candidates.sort(key=lambda x: x[1])
        return candidates[1][0]  # Return index of median value
