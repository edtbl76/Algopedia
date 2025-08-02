# Dynamic programming (DP) 

## Definition

Dynamic programming (DP) is a technique for solving complex problems by breaking them down into simpler, overlapping 
subproblems and storing the solutions to those subproblems to avoid recomputing them. It's especially useful for 
optimization problems, which aim to find the maximum or minimum solution given certain constraints

### Key Characteristics

**1. Optimal Substructure:**

The optimal solution to the overall problem can be constructed from the optimal solutions of its subproblems.

**2. Overlapping Subproblems:**

The same subproblems are encountered and solved repeatedly when solving a larger problem using a recursive approach. DP
addresses this by solving each subproblem only once and storing its result


## Approaches / Techniques

### **Top-Down Approach (Memoization):**

1. Starting with the main problem, we recursively break it down into subproblems
2. As each subproblem is solved, the solution is stored (hash-map, array, table, etc.)
3. Before computing solutions for a subproblem, we check to see if it has already been stored. If it has, we just reuse 
the previously computed vlue. 

This approach usually mirrors or outlines the natural recursive structure of the problem. 

### **Bottom-Up Approach (Tabulation):**

1. Start by solving the smallest subproblems first. 
2. Iteratively build up the solution to a larger problem
3. Solutions to subproblems are stored (hash-map, array, table, etc.)
4. Solutions to subproblems are used to compute solutions for increasingly larger subproblems


## Benefits

### **Efficiency**

Avoiding redundant calculations can significantly reduce the time complexity of
solving problems. (It is often used to reduce exponential time solutions down to 
polynomial time solutions.)

### **Optimization**

Systematic consideration and combining of optimal solutions of subproblems allows
DP to guarantee an optimal solution for problems with optimal substructure.

## Examples

Classic examples of problems solved using dynamic programming include:


### Fibonacci 

Calculating nth Fibonacci number efficiently by storing previously calculated 
values

### Backpack/Knapsack Problem

Maximizing the value of items placed in a knapsack w/ a limited weight capacity

### LCS (Longest Common Subsequence)

Finding the longest sequence of characters that appear in the same relative order
in two given strings. 

### SPF (Shortest Path First)

Algos like Floyd-Warshall and Bellman-Ford use DP to find shortest paths in a graph.



