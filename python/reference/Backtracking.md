# Backtracking 

Backtracking is a systematic algorithmic approach (i.e., intelligent brute-force) for solving computational problems by 
exploring potential solutions incrementally and abandoning paths that cannot lead to valid solutions. 

It's less naive than exhaustive searches, because it uses _constraint checking_ and _early pruning_ as a means of 
excluding impossible scenarios. 


## Core Concept

1. **Building solutions step-by-step** - Constructing partial solutions incrementally
2. **Testing constraints** - Checking if the current partial solution can potentially lead to a complete valid solution
3. **Backtracking on failure** - When a partial solution fails, it "backs up" to the previous decision point and tries alternative paths
4. **Pruning the search space** - Eliminating entire branches of possibilities early when they're guaranteed to fail

## How It Works

Think of backtracking like navigating a maze:
- You move forward step by step
- When you hit a dead end, you retrace your steps to the last decision point
- You try a different path from that point
- You continue until you find the exit or exhaust all possibilities

## Algorithm Pattern

```python
def backtrack(partial_solution, problem_constraints):
    # Base case: check if we have a complete solution
    if is_complete(partial_solution):
        return partial_solution
    
    # Try all possible next choices
    for choice in get_possible_choices(partial_solution):
        # Make the choice (add to partial solution)
        partial_solution.append(choice)
        
        # Check if this choice could lead to a valid solution
        if is_valid(partial_solution, problem_constraints):
            # Recursively try to complete the solution
            result = backtrack(partial_solution, problem_constraints)
            if result is not None:
                return result
        
        # Backtrack: remove the choice and try the next one
        partial_solution.pop()
    
    # No valid solution found from this state
    return None
```


## Key Characteristics

- **Systematic exploration**: Ensures all possibilities are considered
- **Early termination**: Stops exploring paths that can't succeed
- **Memory efficient**: Only stores the current path, not all possibilities
- **Recursive nature**: Naturally implemented with recursion

## Common Applications

1. **N-Queens Problem** - Place N queens on a chessboard so none attack each other
2. **Sudoku Solver** - Fill a 9×9 grid following Sudoku rules
3. **Graph Coloring** - Color graph vertices so no adjacent vertices share colors
4. **Subset Sum** - Find subsets that sum to a target value
5. **Permutations/Combinations** - Generate all arrangements or selections
6. **Maze Solving** - Find paths through a maze

## Advantages
- **Complete**: Finds a solution if one exists
- **Optimal for constraint problems**: Excellent for problems with many constraints
- **Space efficient**: O(depth) space complexity instead of storing all possibilities

## Disadvantages
- **Can be slow**: Worst-case time complexity is often exponential
- **May explore many invalid paths**: Without good pruning, it can be inefficient

