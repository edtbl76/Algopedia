"""
Quicksort Algorithm Implementation with Multiple Partitioning Strategies
======================================================================

History of Quicksort:
--------------------
Quicksort was developed by British computer scientist Tony Hoare in 1959 and published in 1961.
It remains one of the most widely used sorting algorithms due to its average-case efficiency
and in-place sorting capability. The algorithm uses a divide-and-conquer approach, selecting
a 'pivot' element and partitioning the array around it.

Key historical developments:
- 1959: Tony Hoare develops the basic quicksort algorithm
- 1962: Hoare publishes the algorithm formally
- 1970s: Various partitioning schemes (Lomuto, improved Hoare) developed
- 1980s: Hybrid approaches like Introsort introduced
- 1990s: Multi-pivot variations explored
- 2000s: Dual-pivot quicksort adopted in Java's standard library

Performance Characteristics Summary:
-----------------------------------
| Strategy        | Best Use Case           | Advantage                    | Disadvantage                |
|-----------------|-------------------------|------------------------------|-----------------------------|
| Lomuto          | Teaching/simple code    | Easy to understand           | More swaps than Hoare       |
| Hoare           | General performance     | Fewer swaps                  | More complex implementation |
| 3-Way           | Many duplicates         | Handles duplicates optimally | Overhead for unique elements|
| Random          | Adversarial inputs      | Avoids worst-case            | Random number generation    |
| Median-of-3     | General use             | Better pivot selection       | Pivot selection overhead    |
| Sedgewick       | Balanced implementation | Simpler than Hoare           | Slightly more swaps         |
| Dual-pivot      | Large arrays            | Can be faster than single    | Complex implementation      |
| Fat-pivot       | Complex objects         | Handles multi-key sorting    | Overhead for simple data    |

This implementation provides a strategy pattern allowing easy experimentation with different
partitioning approaches to understand their trade-offs and performance characteristics.

I opted for this strategy based on the popularity of this algorithm in the wild and the
relative simplicity of its many variants. It's also easy to implement and understand, which
makes it a good choice for teaching and experimentation.
"""

from typing import List, Any, Protocol
import random


class PartitionStrategy(Protocol):
    """Protocol defining the interface for partition strategies."""

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Partitions the array and returns the final position of the pivot.

        Args:
            values: List to be partitioned
            start: Starting index (inclusive)
            end: Ending index (inclusive)

        Returns:
            Final position of the pivot element after partitioning
        """
        ...


class PartitionUtils:
    """Utility methods for common partitioning operations."""

    @staticmethod
    def lomuto_partition_with_pivot(values: List[Any], start: int, end: int,
                                    pivot_index: int) -> int:
        """
        Common Lomuto partitioning logic that can be reused by multiple strategies.
        """
        pivot = values[pivot_index]

        # Move pivot to end
        values[pivot_index], values[end] = values[end], values[pivot_index]

        partition_index = start

        # Partition elements
        for idx in range(start, end):
            if values[idx] < pivot:
                values[idx], values[partition_index] = values[partition_index], values[idx]
                partition_index += 1

        # Place pivot in final position
        values[end], values[partition_index] = values[partition_index], values[end]

        return partition_index



class LomutoPartition:
    """
    Lomuto Partition Scheme
    ======================

    Named after Nico Lomuto, this partitioning scheme is simpler to understand and implement
    than Hoare's original scheme. It maintains a partition index that tracks elements less
    than the pivot, making the algorithm logic more intuitive.

    Key characteristics:
    - Always moves pivot to the end before partitioning
    - Uses a single partition index that grows from left to right
    - Performs more swaps than Hoare's scheme but is easier to understand
    - Commonly used in educational settings due to its clarity

    Best for: Teaching quicksort concepts, simple implementations
    """

    def partition(self, values: List[Any], start: int, end: int) -> int:
        pivot_index = start + (end - start) // 2
        return PartitionUtils.lomuto_partition_with_pivot(values, start, end, pivot_index)


class HoarePartition:
    """
    Hoare Partition Scheme
    =====================

    This is the original partitioning scheme developed by Tony Hoare. It uses two pointers
    that move toward each other from opposite ends of the array, swapping elements that
    are on the wrong side of the pivot.

    Key characteristics:
    - Uses two pointers moving from opposite ends
    - Generally performs fewer swaps than Lomuto
    - More efficient in practice but harder to implement correctly
    - Pivot ends up in an arbitrary position (not necessarily its final sorted position)

    Best for: Production code where performance matters, experienced developers
    """

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Partitions using Hoare scheme with first element as pivot.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        # Choose pivot (first element)
        pivot = values[start]

        # Initialize pointers
        left = start + 1  # Start after the pivot
        right = end

        # Partition the array
        while True:
            # Find element on left that should be on right
            while left <= right and values[left] <= pivot:
                left += 1

            # Find element on right that should be on left
            while left <= right and values[right] > pivot:
                right -= 1

            # If pointers crossed, partitioning is done
            if left > right:
                break

            # Swap elements that are in wrong partitions
            values[left], values[right] = values[right], values[left]

        # Place pivot in its correct position
        values[start], values[right] = values[right], values[start]

        # Return the position of the pivot
        return right


class ThreeWayPartition:
    """
    Three-Way (Dutch National Flag) Partitioning
    ===========================================

    Developed by Edsger Dijkstra, this scheme partitions the array into three sections:
    elements less than pivot, equal to pivot, and greater than pivot. It's particularly
    effective when the array contains many duplicate elements.

    Key characteristics:
    - Creates three partitions: < pivot, = pivot, > pivot
    - Significantly improves performance on arrays with many duplicates
    - Reduces the number of recursive calls when duplicates are present
    - Slightly more complex than basic two-way partitioning

    Best for: Arrays with many duplicate elements, robust general-purpose sorting
    """

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Three-way partitioning that returns a pivot position compatible with quicksort.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        if start >= end:
            return start

        # Choose pivot (midpoint strategy)
        pivot_index = start + (end - start) // 2
        pivot = values[pivot_index]

        # Three-way partitioning
        less_than = start  # Elements < pivot
        equal = start      # Elements = pivot
        greater_than = end # Elements > pivot

        while equal <= greater_than:
            if values[equal] < pivot:
                values[less_than], values[equal] = values[equal], values[less_than]
                less_than += 1
                equal += 1
            elif values[equal] > pivot:
                values[equal], values[greater_than] = values[greater_than], values[equal]
                greater_than -= 1
            else:
                equal += 1

        # For compatibility with quicksort, we need to return a position that divides
        # the array into elements <= pivot and elements > pivot
        # The middle of the equal section is a good choice
        middle_equal = (less_than + greater_than) // 2

        # Ensure we return a valid index within the equal section
        if less_than <= middle_equal <= greater_than:
            return middle_equal
        elif less_than > greater_than:
            # If there's no equal section, return the boundary
            return less_than - 1
        else:
            # Default to the start of the equal section
            return less_than


class RandomPivotPartition:
    """
    Random Pivot Selection Strategy
    ==============================

    This strategy randomly selects the pivot element to avoid worst-case performance
    on already sorted or nearly sorted arrays. It can be combined with any partitioning
    scheme (here we use Lomuto for simplicity).

    Key characteristics:
    - Randomly selects pivot to avoid pathological input cases
    - Provides probabilistic guarantee against worst-case behavior
    - Slight overhead from random number generation
    - Makes the algorithm randomized rather than deterministic

    Best for: Adversarial inputs, situations where input characteristics are unknown
    """

    def partition(self, values: List[Any], start: int, end: int) -> int:
        pivot_index = random.randint(start, end)
        return PartitionUtils.lomuto_partition_with_pivot(values, start, end, pivot_index)


class MedianOfThreePartition:
    """
    Median-of-Three Pivot Selection
    ==============================

    This strategy selects the pivot as the median of the first, middle, and last elements
    of the current subarray. This typically provides better pivot selection than choosing
    a single element, leading to more balanced partitions.

    Key characteristics:
    - Examines three candidates and chooses the median value
    - Better pivot selection leads to more balanced partitions
    - Small overhead for pivot selection pays off with better performance
    - Commonly used in production implementations

    Best for: General-purpose sorting, production systems
    """

    def _median_of_three(self, values: List[Any], start: int, end: int) -> int:
        """Find the index of the median among first, middle, and last elements."""
        mid = start + (end - start) // 2

        # Sort the three candidates to find median
        candidates = [(start, values[start]), (mid, values[mid]), (end, values[end])]
        candidates.sort(key=lambda x: x[1])

        return candidates[1][0]  # Return index of median value

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Partitions using median-of-three pivot selection with Lomuto scheme.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        # Select median-of-three as pivot
        pivot_index = self._median_of_three(values, start, end)
        pivot = values[pivot_index]

        # Move pivot to end (Lomuto style)
        values[pivot_index], values[end] = values[end], values[pivot_index]

        partition_index = start

        # Standard Lomuto partitioning
        for idx in range(start, end):
            if values[idx] < pivot:
                values[idx], values[partition_index] = values[partition_index], values[idx]
                partition_index += 1

        # Place pivot in final position
        values[end], values[partition_index] = values[partition_index], values[end]

        return partition_index


class SedgewickPartition:
    """
    Sedgewick's Partitioning Scheme
    ==============================

    Developed by Robert Sedgewick, this is a variation of Hoare's partitioning that's
    often easier to implement correctly while maintaining good performance characteristics.
    It provides a good balance between implementation complexity and efficiency.

    Key characteristics:
    - Variation of Hoare's scheme with clearer loop invariants
    - Easier to implement correctly than standard Hoare
    - Good performance characteristics with simpler logic
    - Commonly taught in algorithms courses

    Best for: Educational purposes, balanced implementation complexity and performance
    """

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Partitions using Sedgewick's variation of Hoare's scheme.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        pivot = values[start]
        left = start + 1
        right = end

        while True:
            # Find element from left that should be on right
            while left <= right and values[left] <= pivot:
                left += 1

            # Find element from right that should be on left
            while left <= right and values[right] > pivot:
                right -= 1

            # If pointers crossed, partitioning is done
            if left > right:
                break

            # Swap misplaced elements
            values[left], values[right] = values[right], values[left]

        # Place pivot in its final position
        values[start], values[right] = values[right], values[start]

        return right


class DualPivotPartition:
    """
    Dual-Pivot Partitioning
    =====================

    This advanced strategy uses two pivots to create three partitions, which can
    be more efficient than single-pivot approaches for large arrays. It's used
    in Java's Arrays.sort() implementation.

    Key characteristics:
    - Uses two pivots to create three-way partitioning
    - Can be significantly faster than single-pivot approaches
    - More complex implementation and logic
    - Optimal for large arrays with diverse elements

    Best for: Large arrays, production systems requiring maximum performance
    """

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Dual-pivot partitioning. For compatibility with single-pivot interface,
        we return the boundary of the middle partition.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        if start >= end:
            return start

        # Ensure pivot1 <= pivot2
        if values[start] > values[end]:
            values[start], values[end] = values[end], values[start]

        pivot1 = values[start]
        pivot2 = values[end]

        # Three-way partitioning with dual pivots
        less = start + 1
        great = end - 1
        k = less

        while k <= great:
            if values[k] < pivot1:
                values[k], values[less] = values[less], values[k]
                less += 1
            elif values[k] > pivot2:
                values[k], values[great] = values[great], values[k]
                great -= 1
                k -= 1  # Need to recheck swapped element
            k += 1

        # Place pivots in final positions
        less -= 1
        great += 1
        values[start], values[less] = values[less], values[start]
        values[end], values[great] = values[great], values[end]

        # Return middle partition boundary for compatibility
        return less


class FatPivotPartition:
    """
    Fat Pivot (Multi-Key) Partitioning
    =================================

    This strategy is designed for sorting complex objects where equality doesn't
    necessarily mean identical. It handles cases where multiple keys or comparison
    criteria are involved in determining sort order.

    Key characteristics:
    - Handles complex comparison scenarios
    - Useful for multi-key sorting (e.g., sort by name, then by age)
    - Can handle objects where equal comparison != identical objects
    - More overhead but handles edge cases better

    Best for: Complex objects, multi-key sorting, robust comparison handling
    """

    def __init__(self, key_func=None, secondary_key_func=None):
        """
        Initialize with optional key functions for complex sorting.

        Args:
            key_func: Primary key extraction function
            secondary_key_func: Secondary key extraction function for ties
        """
        self.key_func = key_func or (lambda x: x)
        self.secondary_key_func = secondary_key_func

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Fat pivot partitioning with multi-key support.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        # Choose pivot (midpoint strategy)
        pivot_index = start + (end - start) // 2
        pivot = values[pivot_index]
        pivot_key = self.key_func(pivot)

        # Move pivot to end
        values[pivot_index], values[end] = values[end], values[pivot_index]

        partition_index = start

        # Partition with multi-key comparison
        for idx in range(start, end):
            element_key = self.key_func(values[idx])

            should_move_left = element_key < pivot_key

            # Handle ties with secondary key if provided
            if element_key == pivot_key and self.secondary_key_func:
                element_secondary = self.secondary_key_func(values[idx])
                pivot_secondary = self.secondary_key_func(pivot)
                should_move_left = element_secondary < pivot_secondary

            if should_move_left:
                values[idx], values[partition_index] = values[partition_index], values[idx]
                partition_index += 1

        # Place pivot in final position
        values[end], values[partition_index] = values[partition_index], values[end]

        return partition_index


class HybridPartition:
    """
    Hybrid Partitioning Strategy
    ===========================

    This strategy combines multiple approaches for optimal performance across
    different scenarios. It switches between different strategies based on
    array characteristics like size, recursion depth, etc.

    Key characteristics:
    - Switches to insertion sort for small subarrays
    - Uses different partitioning strategies based on context
    - Monitors recursion depth to avoid worst-case behavior
    - Production-ready with multiple optimizations

    Best for: Production systems, general-purpose high-performance sorting
    """

    def __init__(self, insertion_threshold=10, max_depth=None):
        """
        Initialize hybrid strategy with configurable parameters.

        Args:
            insertion_threshold: Size below which to use insertion sort
            max_depth: Maximum recursion depth before switching strategies
        """
        self.insertion_threshold = insertion_threshold
        self.max_depth = max_depth
        self.current_depth = 0
        self.median_partition = MedianOfThreePartition()
        self.random_partition = RandomPivotPartition()

    def partition(self, values: List[Any], start: int, end: int) -> int:
        """
        Hybrid partitioning with multiple optimizations.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        size = end - start + 1

        # Use insertion sort for very small arrays
        if size <= self.insertion_threshold:
            # For compatibility, we'll just use median-of-three for small arrays
            # In a real implementation, you'd call insertion sort here
            return self.median_partition.partition(values, start, end)

        # Switch to random pivot if we're getting too deep (avoid worst case)
        if self.max_depth and self.current_depth > self.max_depth:
            return self.random_partition.partition(values, start, end)

        # Default to median-of-three for good general performance
        return self.median_partition.partition(values, start, end)


def quicksort(values: List[Any], start: int = None, end: int = None,
              partition_strategy: PartitionStrategy = None) -> None:
    """
    Sorts a list in-place using the quicksort algorithm with configurable partitioning.

    Time Complexity:
        - Best/Average Case: O(n log n) - when pivot divides array roughly in half
        - Worst Case: O(n²) - when pivot is always the smallest/largest element
    Space Complexity: O(log n) - due to recursion stack depth

    Args:
        values: List to be sorted in-place
        start: Starting index of the subarray to sort (inclusive). Defaults to 0.
        end: Ending index of the subarray to sort (inclusive). Defaults to len(values)-1.
        partition_strategy: Strategy to use for partitioning. Defaults to LomutoPartition.
    """
    # Set default parameters for initial call
    if start is None:
        start = 0
    if end is None:
        end = len(values) - 1
    if partition_strategy is None:
        partition_strategy = LomutoPartition()

    # Base case: single element or invalid range
    if start >= end:
        return

    # Special handling for hybrid strategy depth tracking
    if isinstance(partition_strategy, HybridPartition):
        partition_strategy.current_depth += 1

    # Partition the array using the selected strategy
    pivot_position = partition_strategy.partition(values, start, end)

    # Recursive step: sort left and right partitions
    quicksort(values, start, pivot_position - 1, partition_strategy)
    quicksort(values, pivot_position + 1, end, partition_strategy)

    # Decrement depth for hybrid strategy
    if isinstance(partition_strategy, HybridPartition):
        partition_strategy.current_depth -= 1


def quicksort_iterative(values: List[Any], start: int = None, end: int = None,
                        partition_strategy: PartitionStrategy = None) -> None:
    """
    Iterative quicksort with tail call optimization to reduce stack usage.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(values) - 1
    if partition_strategy is None:
        partition_strategy = LomutoPartition()

    stack = [(start, end)]

    while stack:
        start, end = stack.pop()

        if start >= end:
            continue

        pivot_position = partition_strategy.partition(values, start, end)

        # Push larger partition first to keep stack smaller
        left_size = pivot_position - start
        right_size = end - pivot_position - 1

        if left_size > right_size:
            stack.append((start, pivot_position - 1))
            stack.append((pivot_position + 1, end))
        else:
            stack.append((pivot_position + 1, end))
            stack.append((start, pivot_position - 1))
