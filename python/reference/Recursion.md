# Recursion

Recursion, in computer science and programming, is a method of solving problems where the solution to a problem depends
on solutions to smaller instances of the same problem. Think of it like a set of Russian nesting dolls, where each doll 
contains a smaller version of itself until you reach the smallest, innermost doll. In programming, this translates to a 
function calling itself, either directly or indirectly, until a specific base case is reached.

---
## How Recursion Works

### **Breaking Down the Problem** 

A recursive function breaks a complex problem into smaller, simpler subproblems, each resembling the original problem.

### **Self-Calling Function** 

The key characteristic of a recursive function is that it calls itself to solve these smaller subproblems.

### **Base Case** 

Every recursive function must have a base case, which is a condition that stops the recursion and provides a direct 
solution without further recursive calls. Without a base case, the function would call itself indefinitely, possibly 
leading to a stack overflow error. 

---
## Advantages of Recursion

### **Concise Solutions** 

For certain problems, a recursive solution can be more concise and easier to understand than an iterative one.

### **Natural Fit for Certain Problems:** 

Recursion is particularly well-suited for problems involving data structures that are inherently recursive, (i.e., trees 
and graphs) or for algorithms like sorting and searching that can be easily broken into smaller, similar subproblems.

### **Simplicity / Readability** 

When applied appropriately, recursion can result in code that is easier to write and read.

---
## Disadvantages of Recursion

### **Increased Memory Usage** 

Each recursive call adds a new frame to the call stack, potentially leading to increased memory consumption.

### **Stack Overflow Risk** 

If the recursion doesn't have a properly defined base case, it can result in infinite recursion and a stack overflow 
error.

### **Performance Considerations** 

In some cases, recursive functions might be slower than their iterative counterparts due to the overhead of function 
calls. However, some languages optimize for tail recursion. 



### **Debugging Challenges** 

Tracing the execution flow of a recursive function can be more challenging compared to an iterative solution.


---
## Examples of Recursion

### **Factorial** 

Calculating the factorial of a number (n!) is a classic example where n! = n * (n-1)!, with a base case of 0! = 1.

### **Fibonacci Sequence** 

Generating the Fibonacci sequence (where each number is the sum of the two preceding ones) also lends itself well to a 
recursive approach, with base cases of fib(0) = 0 and fib(1) = 1. 

_(NOTE: This is usually performed w/ memoization)_

### **Tree Traversal** 

Algorithms for traversing tree data structures (like pre-order, in-order, and post-order traversal) often use recursion 
to visit each node and its children systematically.

### **Binary Search** 

This search algorithm efficiently finds a target value in a sorted array by repeatedly dividing the array in half 
using recursion.


---
## Special Notes

### Tail Recursion

Tail recursion is a special form of recursion where the recursive call is the very last operation performed
in the function. There are no additional steps after the recursive call returns. 

#### **Key Characteristics**

- Recursive Call is the final statement in the function
- NO additional operations. 
- The function essentially "passes through" the result directly. 

#### Importance. 

**TCO (Tail Call Optimization** 
Some languages optimize til recursion 
- reuses current stack frame instead of creating a new one
- converts recursion into iteration behind the scenes (more performant)
- eliminates risk of stack overflow
- reduces memory usage to O(1) instead of O(n)

TCO gives you the performance of iteration (and more!) w/ the conciseness of recursion, provided
the developers understand it. 

```python
# Tail recursive (optimizable)
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)  # Last operation

# Non-tail recursive 
def factorial_regular(n):
    if n <= 1:
        return 1
    return n * factorial_regular(n - 1)  # Multiplication happens AFTER recursive call

```