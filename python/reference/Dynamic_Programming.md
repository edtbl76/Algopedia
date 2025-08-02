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


### Memoization vs. Tabulation

| Characteristic | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|----------------|------------------------|------------------------|
| **Approach** | Recursive with caching | Iterative with table filling |
| **Direction** | Starts from main problem, breaks down | Starts from base cases, builds up |
| **Implementation** | Uses recursion + storage (hash map/array) | Uses loops + storage (array/table) |
| **Memory Usage** | Only stores computed subproblems | Stores all subproblems (even unused ones) |
| **Space Complexity** | Often more space-efficient | May use more space for complete table |
| **Call Stack** | Uses recursion stack (risk of overflow) | No recursion stack overhead |
| **Computation** | Lazy evaluation (computes only when needed) | Eager evaluation (computes all subproblems) |
| **Code Readability** | More intuitive, mirrors recursive structure | Less intuitive initially, but more structured |
| **Performance** | Slight overhead from function calls | Generally faster due to iterative nature |
| **Debugging** | Can be harder to debug due to recursion | Easier to debug with step-by-step iteration |
| **Base Cases** | Handled naturally in recursive calls | Must be explicitly initialized |
| **Order Dependency** | Automatic (handled by recursion) | Must carefully determine computation order |
| **Stack Overflow Risk** | Yes (deep recursion) | No (iterative approach) |
| **When to Use** | When only some subproblems need solving | When most/all subproblems need solving |

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



