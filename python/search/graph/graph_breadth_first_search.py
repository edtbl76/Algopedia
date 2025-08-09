"""
Graph Breadth-First Search (BFS) Implementation

Breadth-First Search is a graph traversal algorithm that explores vertices in order
of their distance from the starting vertex. It visits all vertices at distance k
before visiting any vertex at distance k+1, making it ideal for finding shortest
paths in unweighted graphs.

Key characteristics:
- Explores vertices level by level (breadth-first)
- Guarantees shortest path in unweighted graphs
- Uses a queue (FIFO) data structure for vertex ordering
- Requires cycle detection in graphs (unlike trees)
- Time complexity: O(V + E) where V = vertices, E = edges
- Space complexity: O(V) for visited set and queue storage

This implementation stores complete paths during traversal for immediate path
reconstruction when the target is found, trading memory efficiency for simplicity.
"""

from collections import deque
from typing import List

from data_structures.Graph import Graph
from data_structures.Vertex import Vertex


def bfs(graph: Graph, start: Vertex, target: Vertex) -> List[Vertex] | None:
    """
    Perform BFS to find the shortest path between two vertices

    This function implements BFS using a queue to maintain exploration order and
    stores complete paths during traversal. It explores the graph level by level,
    ensuring the first path found to the target is the shortest path in terms of
    number of edges.

    Algorithm:
    1. Handle base case: if start equals target, return single-vertex path
    2. Initialize queue with (start_vertex, path_to_start) tuple
    3. Initialize visited set for cycle protection
    4. While queue is not empty:
       a. Dequeue next (vertex, path) pair
       b. Skip if vertex already visited (cycle protection)
       c. Mark vertex as visited
       d. Explore all unvisited neighbors:
          - Create new path by extending current path
          - If neighbor is target, return complete path
          - Otherwise, enqueue (neighbor, new_path) for later exploration
    5. If queue empties without finding target, return None

    Args:
        graph: The Graph object to search within
        start: The starting Vertex for the search
        target: The target Vertex to find a path to

    Returns:
        List of Vertex objects representing shortest path from start to target,
        or None if no path exists

    Time Complexity: O(V + E) where V is number of vertices and E is number of edges
                    - Each vertex is visited at most once: O(V)
                    - Each edge is examined at most once: O(E)
                    - Path operations are O(L) where L is path length, bounded by V
                    - Overall: O(V + E)

    Space Complexity: O(V × L) where V is vertices and L is average path length
                     - O(V) for visited set (stores all processed vertices)
                     - O(V × L) for frontier queue (stores paths for unprocessed vertices)
                     - In worst case L can be O(V), making space O(V²)
                     - Practical space is often much better for sparse graphs

    Examples:
        >>> graph = Graph()
        >>> v1, v2, v3 = Vertex(1), Vertex(2), Vertex(3)
        >>> graph.add_vertex(v1); graph.add_vertex(v2); graph.add_vertex(v3)
        >>> graph.add_edge(v1, v2); graph.add_edge(v2, v3)
        >>> path = bfs(graph, v1, v3)
        >>> [v.value for v in path] if path else None
        [1, 2, 3]
    """
    # Base case: start equals target - return single-vertex path - O(1)
    if start == target:
        return [start]

    # Initialize BFS data structures - O(1)
    # Frontier queue (vertex, path_to_vertex) tuples for level-order exploration
    frontier = deque([(start, [start])])

    # Visited set prevents cycles and redundant exploration  - O(1) per lookup/insert
    visited = set()

    # Main BFS loop - O(V + E) overall
    # (Where V = number of vertices and E = number of edges)
    while frontier:
        # Dequeue next vertex and path to it - O(1)
        current_vertex, current_path = frontier.popleft()

        # Cycle protection: skip already processed vertices - O(1) set lookup
        if current_vertex in visited:
            continue

        # Mark vertex as visited - O(1) set insertion
        visited.add(current_vertex)

        # Get neighbors using proper graph vertex access - O(1) dict lookup + O(d) where d is the vertex degree
        neighbors = graph.vertices[current_vertex.value].get_edges()

        # Explore all unvisited neighbors - O(d) where d is the vertex degree
        for neighbor in neighbors:

            # Only process unvisited neighbors to avoid cycles - O(1) set lookup
            if neighbor not in visited:
                # Extend current path to include neighbor - O(L) where L is current path length
                new_path = current_path + [neighbor]

                # Check if target found - O(1) list lookup
                if neighbor == target:
                    return new_path

                # Enqueue neighbor for next level of exploration - O(1) deque append
                frontier.append((neighbor, new_path))

    # Target not found after exploring all reachable vertices - O(1)
    return None


