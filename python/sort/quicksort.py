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

"""

from typing import List, Any

from sort.PartitionStrategy import PartitionStrategy, LomutoPartition, HybridPartition


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
