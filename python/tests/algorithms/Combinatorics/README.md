# Combinatorics Tests

This directory contains tests for the Combinatorics module.

## Test Files

- `test_permutations.py`: Tests for permutation functions
- `test_combinations.py`: Tests for combination functions
- `utils/test_validation.py`: Tests for input validation utilities
- `utils/test_optimization.py`: Tests for optimization utilities

## Test Coverage

### Validation Tests
- Valid input combinations
- Error cases (negative n, negative k, k > n)
- Error message verification

### Optimization Tests
- Symmetry property C(n,k) = C(n,n-k)
- Boundary cases (k=0, k=n)
- Mathematical properties

### Combinations Tests
- Binomial coefficient calculation with different methods
- Mathematical properties (symmetry, Pascal's identity)
- Edge cases and large values

### Permutations Tests
- Permutation counting
- Permutation generation with different algorithms
- Permutation iteration
- Verification against Python's itertools.permutations
- Edge cases (empty list, single item)

All tests are passing successfully, providing good coverage of the functionality and mathematical properties of the combinatorics module.