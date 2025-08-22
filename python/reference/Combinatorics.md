# Combinatorics

## Definition

Combinatorics is a branch of mathematics that studies the counting, arrangement, and selection of objects within finite 
sets. It provides the mathematical foundation for analyzing discrete structures and is fundamental to probability theory, 
algorithm design, and computer science.


The two primary areas of combinatorics are:
- **Permutations**: Ordered arrangements where sequence matters
- **Combinations**: Unordered selections where sequence doesn't matter

---

## Mathematical Foundations

### Factorial Function
The factorial function is fundamental to both permutations and combinations:
- **Definition**: n! = n × (n-1) × (n-2) × ... × 2 × 1
- **Base Cases**: 0! = 1, 1! = 1
- **Growth**: Factorial function grows extremely rapidly (faster than exponential)

### Key Mathematical Relationship
Permutations and combinations are mathematically related:
**P(n,k) = C(n,k) × k!**

This relationship shows that permutations account for all possible orderings of each combination.

---

## Permutations: Ordered Arrangements

### Mathematical Definition
A permutation P(n,k) represents the number of ways to arrange k items from n total items where **order matters**.

**Formula**: P(n,k) = n! / (n-k)!

### Key Properties
- **P(n,0) = 1**: One way to arrange nothing
- **P(n,1) = n**: n ways to choose the first item
- **P(n,n) = n!**: All possible arrangements of n items
- **Recursive relation**: P(n,k) = n × P(n-1,k-1)

### Mathematical Examples
- P(5,3) = 5!/(5-3)! = 5!/2! = 120/2 = 60
- P(4,4) = 4!/0! = 24/1 = 24
- P(10,2) = 10!/8! = 10 × 9 = 90

### Real-World Applications
- **Scheduling**: Arranging tasks in a specific order
- **Passwords**: Creating passwords where character position matters
- **Racing**: Determining possible finish orders
- **Seating arrangements**: Organizing people in a line or around a table
- **Cryptography**: Key generation where sequence is critical
- **Algorithm analysis**: Analyzing worst-case input scenarios

### Algorithmic Approaches

#### Generation Methods
1. **Recursive Backtracking**
   - Time: O(P(n,k) × k)
   - Space: O(P(n,k) × k)
   - Best for: Small datasets, educational purposes

2. **Optimized Backtracking**
   - Time: O(P(n,k) × k)
   - Space: O(k + P(n,k) × k) - better recursion depth
   - Best for: Medium datasets with memory considerations

3. **Lexicographic Generation**
   - Time: O(n × n!) for full permutations
   - Space: O(n!)
   - Best for: When sorted order is required

4. **Heap's Algorithm**
   - Time: O(n!) - only works for k=n
   - Space: O(n!)
   - Best for: Full permutations of medium-large sets

5. **Iterator Pattern**
   - Time: O(P(n,k) × k) total, O(k) per iteration
   - Space: O(k) - only current permutation in memory
   - Best for: Large datasets, memory-constrained environments

#### Counting Method
- **Direct Calculation**: P(n,k) = n × (n-1) × ... × (n-k+1)
- Time: O(k), Space: O(1)
- Avoids factorial overflow by using multiplicative approach

---

## Combinations: Unordered Selections

### Mathematical Definition
A combination C(n,k) represents the number of ways to choose k items from n total items where **order doesn't matter**.

**Formula**: C(n,k) = n! / (k! × (n-k)!)

### Key Properties
- **Symmetry**: C(n,k) = C(n,n-k)
- **Pascal's Identity**: C(n,k) = C(n-1,k-1) + C(n-1,k)
- **Base Cases**: C(n,0) = C(n,n) = 1 for all n ≥ 0
- **Sum Property**: Σ C(n,k) for k=0 to n equals 2^n

### Mathematical Examples
- C(5,2) = 5!/(2!×3!) = 120/(2×6) = 10
- C(10,0) = 1 (one way to choose nothing)
- C(6,6) = 1 (one way to choose everything)

### Real-World Applications
- **Probability**: Binomial distributions, lottery calculations
- **Statistics**: Sampling without replacement
- **Team formation**: Choosing committee members
- **Game theory**: Analyzing possible game states
- **Genetics**: Calculating trait inheritance probabilities
- **Algorithm analysis**: Counting possible algorithm states

### Algorithmic Approaches

#### Computation Methods
1. **Iterative Approach**
   - Time: O(min(k, n-k)) - exploits symmetry
   - Space: O(1)
   - Best for: Single calculations, memory-constrained environments

2. **Memoized Recursion**
   - Time: O(n×k) worst case, O(1) for cached results
   - Space: O(n×k) for cache storage
   - Best for: Multiple calculations with overlapping subproblems

3. **Tabulation (Bottom-up DP)**
   - Time: O(n×k) - systematic computation
   - Space: O(n×k) - full table storage
   - Best for: Computing multiple related coefficients (Pascal's triangle)

4. **Pure Recursion**
   - Time: O(2^n) - exponential due to repeated subproblems
   - Space: O(n) - recursion stack depth
   - Best for: Educational purposes, small inputs only

5. **LRU Cached Recursion**
   - Time: O(n×k) worst case, O(1) for cached results
   - Space: O(n×k) - automatic cache management
   - Best for: Production code with repeated calculations

### Pascal's Triangle
Combinations form Pascal's Triangle, where each entry C(n,k) can be computed from the two entries above it:

Row 0: 1 
Row 1: 1 1 
Row 2: 1 2 1 
Row 3: 1 3 3 1 
Row 4: 1 4 6 4 1 
Row 5: 1 5 10 10 5 1

## Historical Context

### Ancient Origins
- **Chinese Mathematics**: Yang Hui's triangle (1261) - early form of Pascal's triangle
- **Persian Mathematics**: Omar Khayyam (11th century) - binomial theorem foundations

### Modern Development
- **Blaise Pascal & Pierre de Fermat** (17th century): Established modern combinatorial foundations
- **Pascal's Triangle**: Became cornerstone of combinatorial mathematics
- **Probability Theory**: Pascal and Fermat's correspondence laid groundwork for modern probability

## Key Differences: Permutations vs Combinations

| Aspect | Permutations | Combinations |
|--------|-------------|-------------|
| **Order Significance** | Order matters | Order doesn't matter |
| **Formula** | P(n,k) = n!/(n-k)! | C(n,k) = n!/(k!×(n-k)!) |
| **Example Result** | (A,B,C) ≠ (B,A,C) | {A,B,C} = {B,A,C} |
| **Relationship** | P(n,k) = C(n,k) × k! | C(n,k) = P(n,k) / k! |
| **Use Cases** | Sequences, arrangements | Groups, selections |

## Computational Considerations

### Performance Optimization
1. **Symmetry Exploitation**: Use C(n,k) = C(n,n-k) to minimize computation
2. **Overflow Prevention**: Use multiplicative formulas instead of factorial division
3. **Caching**: Implement memoization for repeated calculations
4. **Early Termination**: Handle base cases (k=0, k=n) immediately

### Algorithm Selection Guidelines
- **Single calculations**: Use iterative methods
- **Educational purposes**: Use recursive methods for clarity
- **Repeated calculations**: Use cached approaches
- **Memory constraints**: Use iterator patterns for generation
- **Large datasets**: Prefer O(1) space algorithms when possible

### Numerical Stability
- **Large Values**: Consider logarithmic computation for very large n,k
- **Integer Overflow**: Use appropriate data types or arbitrary precision arithmetic
- **Intermediate Results**: Perform division at each step to minimize overflow risk

## Complexity Analysis Summary

### Time Complexity Comparison
| Operation | Best Method | Time Complexity |
|-----------|-------------|-----------------|
| P(n,k) Count | Direct multiplication | O(k) |
| C(n,k) Count | Iterative with symmetry | O(min(k,n-k)) |
| Generate all P(n,k) | Heap's algorithm (k=n) | O(n!) |
| Generate all C(n,k) | Not typically done | - |
| Pascal's triangle row | Tabulation | O(n²) |

### Space Complexity Comparison
| Operation | Method | Space Complexity |
|-----------|--------|------------------|
| Count only | Direct calculation | O(1) |
| Generate all | Store results | O(result_count) |
| Memoization | Cache storage | O(n×k) |
| Iterator | Streaming | O(k) |

## Conclusion

Combinatorics provides essential mathematical tools for counting and arrangement problems across computer science and mathematics. Understanding the trade-offs between different algorithmic approaches allows for optimal implementation choices based on specific requirements such as memory constraints, performance needs, and problem characteristics.

The relationship between permutations and combinations (P(n,k) = C(n,k) × k!) demonstrates how ordered and unordered selections are mathematically connected, providing a foundation for more advanced topics in probability theory, algorithm analysis, and computational mathematics.
