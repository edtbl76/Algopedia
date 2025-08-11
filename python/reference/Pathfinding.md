
# Pathfinding

Pathfinding algorithms are computational methods used to find the shortest or most efficient path between two points in a graph or grid, while navigating around obstacles and considering various constraints [[8]](https://www.graphable.ai/blog/pathfinding-algorithms/).

## Overview

The goal of pathfinding algorithms is to explore a graph structure to find the optimal route from a starting point to a destination point. These algorithms are fundamental in computer science and have applications in:

- Game development (NPC movement, player navigation)
- Robotics and autonomous vehicles
- Network routing
- GPS navigation systems
- AI planning systems

## Core Algorithms

### Breadth-First Search (BFS)

**Description**: BFS explores nodes level by level, visiting all neighbors of the current node before moving to the next level [[4]](https://www.puppygraph.com/blog/depth-first-search-vs-breadth-first-search).

**Characteristics**:
- Guarantees shortest path in unweighted graphs
- Uses a queue data structure (FIFO)
- Explores nodes in order of distance from start
- Complete and optimal for unweighted graphs

**Time Complexity**: O(V + E) where V is vertices and E is edges
**Space Complexity**: O(V)

**Use Cases**: Shortest path in unweighted graphs, level-order traversal

### Depth-First Search (DFS)

**Description**: DFS explores as far as possible along each branch before backtracking [[4]](https://www.puppygraph.com/blog/depth-first-search-vs-breadth-first-search).

**Characteristics**:
- Uses a stack data structure (LIFO)
- Does not guarantee shortest path
- Memory efficient for deep graphs
- May get stuck in infinite loops without cycle detection

**Time Complexity**: O(V + E)
**Space Complexity**: O(V) in worst case

**Use Cases**: Maze solving, topological sorting, cycle detection

### Dijkstra's Algorithm

**Description**: Finds the shortest path in weighted graphs with non-negative edge weights [[7]](http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html).

**Characteristics**:
- Guarantees shortest path
- Explores nodes in order of distance from start
- Uses priority queue for efficiency
- Works with weighted graphs
- Similar to BFS but considers edge weights

**Time Complexity**: O((V + E) log V) with binary heap
**Space Complexity**: O(V)

**Use Cases**: Network routing protocols, GPS navigation, social networks

### A* (A-Star) Algorithm

**Description**: An extension of Dijkstra's algorithm that uses a heuristic function to guide the search toward the goal more efficiently [[7]](http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html).

**Characteristics**:
- Combines actual cost (g) and heuristic estimate (h)
- Formula: f(n) = g(n) + h(n)
- Optimal if heuristic is admissible (never overestimates)
- More efficient than Dijkstra's when good heuristic exists

**Time Complexity**: O(b^d) where b is branching factor and d is depth
**Space Complexity**: O(b^d)

**Use Cases**: Game pathfinding, robotics navigation, puzzle solving

## Algorithm Comparison

| Algorithm | Optimal | Complete | Time Complexity | Space Complexity | Best For |
|-----------|---------|----------|-----------------|------------------|----------|
| BFS | Yes (unweighted) | Yes | O(V + E) | O(V) | Unweighted shortest path |
| DFS | No | Yes (finite) | O(V + E) | O(V) | Memory-constrained scenarios |
| Dijkstra | Yes | Yes | O((V + E) log V) | O(V) | Weighted shortest path |
| A* | Yes (admissible h) | Yes | O(b^d) | O(b^d) | Informed search with heuristic |

## Choosing the Right Algorithm

### Use BFS when:
- Graph is unweighted
- Need guaranteed shortest path
- Memory is not a major constraint

### Use DFS when:
- Memory is limited
- Don't need shortest path
- Exploring all possibilities

### Use Dijkstra when:
- Graph has weighted edges
- Need guaranteed shortest path
- No good heuristic available

### Use A* when:
- Graph has weighted edges
- Good heuristic function available
- Need optimal solution efficiently

## Implementation Considerations

### Heuristic Functions for A*
- **Manhattan Distance**: |x1-x2| + |y1-y2| (grid with 4-directional movement)
- **Euclidean Distance**: √((x1-x2)² + (y1-y2)²) (grid with 8-directional movement)
- **Chebyshev Distance**: max(|x1-x2|, |y1-y2|) (grid with diagonal movement)

### Performance Optimizations
- **Bidirectional Search**: Search from both start and goal simultaneously
- **Jump Point Search**: Optimization for uniform-cost grids
- **Hierarchical Pathfinding**: Multi-level approach for large maps
- **Path Smoothing**: Post-processing to create more natural paths

## Common Challenges

1. **Dynamic Environments**: Handling moving obstacles and changing costs
2. **Memory Constraints**: Managing large search spaces efficiently
3. **Real-time Requirements**: Balancing optimality with computation time
4. **Multi-agent Pathfinding**: Coordinating multiple entities without collisions

## References

- Stanford CS Theory - Introduction to A* [[7]](http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html)
- Graphable AI - Pathfinding Algorithms Overview [[8]](https://www.graphable.ai/blog/pathfinding-algorithms/)
- PuppyGraph - DFS vs BFS Guide [[4]](https://www.puppygraph.com/blog/depth-first-search-vs-breadth-first-search)


