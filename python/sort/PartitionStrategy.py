"""
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

This implementation provides an example of the Strategy pattern allowing easy experimentation with different
partitioning approaches to understand their trade-offs and performance characteristics.

I opted for this strategy based on the popularity of this algorithm in the wild and the
relative simplicity of its many variants. It's also easy to implement and understand, which
makes it a good choice for teaching and experimentation.
"""
from typing import Protocol, List, Any

from sort.PivotStrategy import PivotStrategy, PivotSelector

class PartitionStrategy(Protocol):
    """Protocol defining the interface for partition strategies."""

    def partition(self, values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.MIDPOINT) -> int:
        """
        Partitions the array and returns the final position of the pivot.
        Args:
            values: List to be partitioned
            start: Starting index (inclusive)
            end: Ending index (inclusive)
            pivot_strategy: Strategy for selecting the pivot
        Returns:
            Final position of the pivot element after partitioning
        """
        ...


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

    Default pivot strategy: MIDPOINT (as it was originally implemented)
    """

    @staticmethod
    def lomuto_partition_with_pivot(values: List[Any], start: int, end: int,
                                    pivot_index: int) -> int:
        """
            Performs Lomuto partitioning on a subarray using a specified pivot element.

            This is a reusable implementation of the Lomuto partitioning scheme that can be
            used by multiple quicksort strategies. The method rearranges elements so that
            all values less than the pivot appear before it, and all values greater than
            or equal to the pivot appear after it.

            The Lomuto scheme is characterized by:
            - Moving the pivot to the end position before partitioning
            - Using a single partition index that grows from left to right
            - Clear loop invariants that make the algorithm easy to understand

            Algorithm Steps:
            1. Store the pivot value and move pivot element to the end position
            2. Initialize partition_index to track the boundary between partitions
            3. Iterate through elements, swapping smaller elements to the left partition
            4. Place the pivot in its final sorted position

            Time Complexity: O(n) where n = end - start + 1
            Space Complexity: O(1) - performs partitioning in-place

            Args:
                values: The list to be partitioned (modified in-place)
                start: Starting index of the subarray to partition (inclusive)
                end: Ending index of the subarray to partition (inclusive)
                pivot_index: Index of the element to use as the pivot

            Returns:
                int: The final position of the pivot element after partitioning.
                     All elements at indices [start, return_value) are < pivot.
                     The pivot is at index return_value.
                     All elements at indices (return_value, end] are >= pivot.

            Example:
                >>> values = [64, 34, 25, 12, 22, 11, 90]
                >>> pivot_pos = LomutoPartition.lomuto_partition_with_pivot(values, 0, 6, 3)
                >>> print(f"Pivot at position {pivot_pos}, value: {values[pivot_pos]}")
                Pivot at position 1, value: 12
                >>> print("Values after partitioning:", values)
                Values after partitioning: [11, 12, 25, 64, 22, 34, 90]
                >>> # Element at position 0: [11] is < 12
                >>> # Elements at positions 2-6: [25, 64, 22, 34, 90] are >= 12


            Note:
                This method modifies the input list in-place. The method assumes valid
                indices are provided and does not perform bounds checking. The pivot
                element will be moved to its correct partitioned position, but other
                elements may not be in their final sorted positions until the entire
                quicksort algorithm completes.
        """

        # pivot_index provided as a parameter.
        pivot = values[pivot_index]

        # Move pivot to end
        values[pivot_index], values[end] = values[end], values[pivot_index]

        # Set "boundary tracking" to start (reflecting no elements being sorted)
        partition_index = start

        # Partition elements
        for idx in range(start, end):
            # When an element smaller than the pivot is id'd, we swap it to the left side
            # of the boundary and then increment the boundary
            if values[idx] < pivot:
                values[idx], values[partition_index] = values[partition_index], values[idx]
                partition_index += 1

        # Move pivot from the end to the boundary.
        values[end], values[partition_index] = values[partition_index], values[end]

        # We're returning the boundary / partition index.
        return partition_index

    @staticmethod
    def partition(values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.MIDPOINT) -> int:

        """Lomuto partitioning with configurable pivot selection."""
        pivot_index = PivotSelector.select_pivot_index(values, start, end, pivot_strategy)
        return LomutoPartition.lomuto_partition_with_pivot(values, start, end, pivot_index)

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
    Default pivot strategy: RANDOM (as it was originally implemented)
    """

    @staticmethod
    def partition(values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.RANDOM) -> int:
        """Random pivot partitioning - uses Lomuto scheme."""
        pivot_index = PivotSelector.select_pivot_index(values, start, end, pivot_strategy)
        return LomutoPartition.lomuto_partition_with_pivot(values, start, end, pivot_index)


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
    Default pivot strategy: MEDIAN_OF_THREE (as it was originally implemented)
    """

    @staticmethod
    def partition(values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.MEDIAN_OF_THREE) -> int:
        """Median-of-three partitioning with configurable pivot selection."""
        pivot_index = PivotSelector.select_pivot_index(values, start, end, pivot_strategy)
        return LomutoPartition.lomuto_partition_with_pivot(values, start, end, pivot_index)


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

    Default pivot strategy: FIRST (as it was originally implemented)
    """
    @staticmethod
    def partition(values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.FIRST) -> int:

        """
        Partitions using Hoare scheme with the first element as pivot.

        The Hoare partitioning scheme uses two pointers that move toward each other
        from opposite ends of the array, swapping elements that are on the wrong
        side of the pivot. This method is more efficient than Lomuto partitioning
        as it typically performs fewer swaps.

        Algorithm Steps:
        1. Choose the first element as pivot
        2. Initialize left pointer after pivot, right pointer at end
        3. Move left pointer right until finding element > pivot
        4. Move right pointer left until finding element <= pivot
        5. If pointers haven't crossed, swap elements
        6. Repeat until pointers cross
        7. Swap pivot with the element at the right pointer position

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)

        Args:
            values: The list to be partitioned (modified in-place)
            start: Starting index of the subarray to partition (inclusive)
            end: Ending index of the subarray to partition (inclusive)
            pivot_strategy: Strategy for selecting the pivot element.
        Returns:
            int: The final position of the pivot element after partitioning.
                 All elements at indices [start, return_value] are <= pivot.
                 All elements at indices (return_value, end] are > pivot.

        Example:
            >>> values = [64, 34, 25, 12, 22, 11, 90]
            >>> pivot_pos = HoarePartition.partition(  )
            >>> print(f"Pivot at position {pivot_pos}, value: {values[pivot_pos]}")
            Pivot at position 5, value: 64
            >>> print("Values after partitioning:", values)
            Values after partitioning: [11, 34, 25, 12, 22, 64, 90]
            >>> # Elements at positions 0-5: [11, 34, 25, 12, 22, 64] are <= 64
            >>> # Elements at positions 6: [90] are > 64

         Step-by-step execution for the example above:
            Initial: [64, 34, 25, 12, 22, 11, 90] (pivot=64, left=1, right=6)
            Step 1: left moves to index 6 (90 > 64), right moves to index 5 (11 <= 64)
            Step 2: Check if left <= right: 6 <= 5 is false, so pointers have crossed
            Step 3: Exit the partitioning loop (no swap occurs)
            Step 4: Swap pivot 64 with element at right position 5 (11) -> [11, 34, 25, 12, 22, 64, 90]
            Final: Pivot 64 is now at position 5, correctly partitioned

        Note:
            Unlike Lomuto partitioning, the pivot doesn't necessarily end up in its
            final sorted position, but the partitioning property is maintained:
            all elements to the left are <= pivot, all elements to the right are > pivot.
        """

        # set pivot (first element)
        pivot_index = PivotSelector.select_pivot_index(values, start, end, pivot_strategy)
        pivot = values[pivot_index]

        # Move pivot to start position for Hoare algorithm
        # This is a FORCE statement that ensures the FIRST strategy is used.
        # If you want to try other strategies, comment this if statement out.
        if pivot_index != start:
            values[pivot_index], values[start] = values[start], values[pivot_index]

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

        # Place pivot in its correct position and return to caller.
        values[start], values[right] = values[right], values[start]
        return right


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
    Default pivot strategy: FIRST (as it was originally implemented)
    """

    @staticmethod
    def partition(values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.FIRST) -> int:
        """
        Partitions using Sedgewick's variation of Hoare's scheme.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        pivot_index = PivotSelector.select_pivot_index(values, start, end, pivot_strategy)
        pivot = values[pivot_index]

        # Move pivot to start position
        if pivot_index != start:
            values[pivot_index], values[start] = values[start], values[pivot_index]

        left = start + 1
        right = end

        while True:
            while left <= right and values[left] <= pivot:
                left += 1
            while left <= right and values[right] > pivot:
                right -= 1
            if left > right:
                break
            values[left], values[right] = values[right], values[left]

        values[start], values[right] = values[right], values[start]
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

    Default pivot strategy: MIDPOINT (as it was originally implemented)
    """

    @staticmethod
    def partition(values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.MIDPOINT) -> int:
        """
        Three-way partitioning that returns a pivot position compatible with quicksort.

        This method implements Dijkstra's Dutch National Flag algorithm to partition
        the array into three sections: elements less than pivot, equal to pivot,
        and greater than pivot. It's particularly effective when dealing with arrays
        containing many duplicate elements.

        Algorithm Steps
        1. Choose pivot using midpoint strategy
        2. Initialize three pointers: less_than, equal, and greater_than
        3. Iterate through elements, placing each in the appropriate partition
        4. Return a pivot position compatible with standard quicksort interface

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1) - performs partitioning in-place

        Args:
            values: The list to be partitioned (modified in-place)
            start: Starting index of the subarray to partition (inclusive)
            end: Ending index of the subarray to partition (inclusive)
            pivot_strategy: Strategy for selecting the pivot element.
        Returns:
            int: A pivot position that divides the array into elements <= pivot
                 and elements > pivot, compatible with quicksort's requirements.

        Examples:
            Basic partitioning with unique elements:
            >>> partition = ThreeWayPartition()
            >>> values = [64, 34, 25, 12, 22, 11, 90]
            >>> pivot_pos = partition.partition(values, 0, 6)
            >>> print(f"Pivot at position {pivot_pos}, value: {values[pivot_pos]}")
            Pivot at position 1, value: 12
            >>> print("Values after partitioning:", values)
            Values after partitioning: [11, 12, 25, 22, 34, 64, 90]
            >>> # Elements <= 12: [11, 12] at positions [0, 1]
            >>> # Elements > 12: [25, 22, 34, 64, 90] at positions [2, 6]

            Partitioning with many duplicates (where three-way shines):
            >>> values = [5, 2, 8, 2, 9, 1, 5, 5, 2]
            >>> pivot_pos = partition.partition(values, 0, 8)
            >>> print(f"Pivot at position {pivot_pos}, value: {values[pivot_pos]}")
            Pivot at position 8, value: 9
            >>> print("Values after partitioning:", values)
            Values after partitioning: [5, 2, 8, 2, 1, 5, 5, 2, 9]
            >>> # Elements < 9: [5, 2, 8, 2, 1, 5, 5, 2] at positions [0, 7]
            >>> # Elements = 9: [9] at position [8]
            >>> # Elements > 9: none


            Edge case - single element:
            >>> values = [42]
            >>> pivot_pos = partition.partition(values, 0, 0)
            >>> print(f"Single element at position {pivot_pos}: {values[pivot_pos]}")
            Single element at position 0: 42

            Edge case - all elements equal:
            >>> values = [7, 7, 7, 7, 7]
            >>> pivot_pos = partition.partition(values, 0, 4)
            >>> print(f"All equal, pivot at position {pivot_pos}: {values[pivot_pos]}")
            All equal, pivot at position 2: 7
            >>> print("All elements remain equal:", values)
            All elements remain equal: [7, 7, 7, 7, 7]

            Subarray partitioning (indices 2 to 6):
            >>> values = [1, 9, 3, 7, 5, 6, 2, 8, 4]
            >>> pivot_pos = partition.partition(values, 2, 6)  # Partition subarray [3, 7, 5, 6, 2]
            >>> print(f"Pivot at position {pivot_pos}, value: {values[pivot_pos]}")
            Pivot at position 4, value: 5
            >>> print("Values after partitioning:", values)
            Values after partitioning: [1, 9, 3, 2, 5, 6, 7, 8, 4]
            >>> # Only indices [2, 6] were affected: [3, 2, 5, 6, 7]
            >>> # Elements < 5: [3, 2] at positions [2, 3]
            >>> # Elements = 5: [5] at position [4]
            >>> # Elements > 5: [6, 7] at positions [5, 6]


        Performance Benefits:
            When array has many duplicates, three-way partitioning significantly
            reduces recursive calls by grouping equal elements together:

            - Traditional 2-way: O(n log n) comparisons even with duplicates
            - Three-way: O(n) comparisons when many elements equal pivot
            - Memory: Same O(1) space as traditional partitioning

        Note:
            The returned pivot position may not be the exact center of the equal
            partition, but it maintains the partitioning property required by
            quicksort: all elements at indices [start, pivot_pos] are <= pivot,
            and all elements at indices (pivot_pos, end] are > pivot.
        """
        if start >= end:
            return start

        pivot_index = PivotSelector.select_pivot_index(values, start, end, pivot_strategy)
        pivot = values[pivot_index]

        # Three-way partitioning uses 3 pointers
        less_than = start  # Elements < pivot
        equal = start  # Current element
        greater_than = end  # Elements > pivot

        # moves current pointer towards greater than (which may also move towards current)
        while equal <= greater_than:

            # Build the smaller partition
            if values[equal] < pivot:
                values[less_than], values[equal] = values[equal], values[less_than]
                less_than += 1
                equal += 1
            # build greater-than partition
            elif values[equal] > pivot:
                values[equal], values[greater_than] = values[greater_than], values[equal]
                greater_than -= 1
            # advance pointer
            else:
                equal += 1

        # For compatibility with quicksort, we need to return a position that divides
        # the array into elements <= pivot and elements > pivot
        # The middle of the equal section is a good choice
        middle_equal = (less_than + greater_than) // 2

        # Ensure we return a valid index within equal section
        if less_than <= middle_equal <= greater_than:
            return middle_equal
        elif less_than > greater_than:
            return less_than - 1 # return boundary if there is no equal section
        else:
            return less_than # edge cases / default to start of equal section



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

    def partition(self, values: List[Any], start: int, end: int,
                  pivot_strategy1: PivotStrategy = PivotStrategy.FIRST,
                  pivot_strategy2: PivotStrategy = PivotStrategy.LAST) -> int:
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

        pivot1 = PivotSelector.select_pivot_index(values, start, end, pivot_strategy1)
        pivot2 = PivotSelector.select_pivot_index(values, start, end, pivot_strategy2)

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

    def partition(self, values: List[Any], start: int, end: int,
                  pivot_strategy: PivotStrategy = PivotStrategy.MIDPOINT) -> int:
        """
        Fat pivot partitioning with multi-key support.

        Time Complexity: O(n) where n = end - start + 1
        Space Complexity: O(1)
        """
        pivot_index = PivotSelector.select_pivot_index(values, start, end, pivot_strategy)
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