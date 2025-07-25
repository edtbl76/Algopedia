
# Sorting Algorithms Comparison

This document compares the sorting algorithms implemented in the `sort/` directory.

## Overview

The sorting algorithms directory contains three main implementations:
- **Bubble Sort** (`bubble_sort.py`)
- **Merge Sort** (`merge_sort.py`) 
- **Quick Sort** (`quicksort.py`)

## Merge Sort (`merge_sort.py`)

### Algorithm Description
Merge sort is a divide-and-conquer algorithm invented by John von Neumann in 1945. It was one of the first algorithms to achieve O(n log n) time complexity in the worst case, making it significantly more efficient than earlier O(n²) algorithms.

### Key Characteristics
- **Time Complexity**: O(n log n) in all cases (best, average, worst)
- **Space Complexity**: O(n) - requires additional space for temporary arrays
- **Stability**: Stable - maintains relative order of equal elements
- **Strategy**: Divide-and-conquer approach

### Implementation Features
The merge sort implementation includes several optimizations:

1. **Index-based iteration**: Uses indices instead of `pop(0)` operations to maintain O(1) access time
2. **Stability preservation**: Uses `<=` comparison to ensure stable sorting
3. **Slice-based extension**: Efficiently handles remaining elements using list slicing

### Functions
- `merge_sort(values: List[Any]) -> List[Any]`: Main sorting function
- `_merge(left_side: List[Any], right_side: List[Any]) -> List[Any]`: Merges two sorted lists

## Quick Sort (`quicksort.py`)

### Algorithm Description
Quick sort is a highly efficient divide-and-conquer sorting algorithm that works by selecting a 'pivot' element and partitioning the array around it.

### Key Characteristics
- **Time Complexity**: 
  - Best/Average: O(n log n)
  - Worst: O(n²)
- **Space Complexity**: O(log n) average case due to recursion
- **Stability**: Not stable (can change relative order of equal elements)

### Implementation Features
The quicksort implementation provides multiple partitioning strategies:

#### Partitioning Strategies
1. **LomutoPartition**: Simple partitioning scheme
2. **HoarePartition**: Original Hoare partitioning method
3. **ThreeWayPartition**: Handles duplicate elements efficiently
4. **RandomPivotPartition**: Uses random pivot selection
5. **MedianOfThreePartition**: Selects pivot as median of three elements
6. **SedgewickPartition**: Sedgewick's partitioning variant
7. **DualPivotPartition**: Uses two pivots for partitioning
8. **FatPivotPartition**: Specialized for datasets with many duplicates
9. **HybridPartition**: Combines multiple strategies based on array characteristics

### Functions
- `quicksort()`: Recursive implementation
- `quicksort_iterative()`: Iterative implementation using a stack

## Bubble Sort (`bubble_sort.py`)

### Algorithm Description
Bubble sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.

### Key Characteristics
- **Time Complexity**: O(n²) in worst and average cases, O(n) in best case
- **Space Complexity**: O(1) - sorts in-place
- **Stability**: Stable when implemented with proper comparison
- **Strategy**: Simple comparison and swap

### Implementation
- `bubble_sort_basic(values: List[Any]) -> None`: Basic in-place bubble sort implementation

## Comparison Summary

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stable | In-Place |
|-----------|-----------|--------------|------------|------------------|---------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |

## When to Use Each Algorithm

### Merge Sort
- **Best for**: Large datasets where consistent performance is required
- **Advantages**: Guaranteed O(n log n) performance, stable sorting
- **Disadvantages**: Requires additional memory space

### Quick Sort
- **Best for**: General-purpose sorting when average-case performance matters
- **Advantages**: Fast average performance, in-place sorting, multiple optimization strategies
- **Disadvantages**: Worst-case O(n²) performance, not stable

### Bubble Sort
- **Best for**: Educational purposes, very small datasets, or when simplicity is paramount
- **Advantages**: Simple implementation, adaptive (efficient for nearly sorted data)
- **Disadvantages**: Poor performance on large datasets

## Advanced Features

### Quick Sort Partitioning Strategies
The quicksort implementation stands out for its comprehensive collection of partitioning strategies, each optimized for different scenarios:

- **Random pivot** helps avoid worst-case performance on sorted data
- **Median-of-three** improves pivot selection
- **Three-way partitioning** efficiently handles arrays with many duplicate values
- **Dual-pivot** can provide better performance in certain cases
- **Hybrid approach** adapts strategy based on array characteristics

This makes the quicksort implementation highly versatile and suitable for various input patterns and performance requirements.