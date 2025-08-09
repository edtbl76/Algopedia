"""
Graph Depth-First Search Implementation

Depth-First Search (DFS) is a fundamental graph traversal algorithm that explores
as far as possible along each branch before backtracking. This module provides
a recursive implementation of DFS for finding target vertices in graph structures.

DFS follows these principles:
1. Start at a source vertex and mark it as visited
2. Recursively visit all unvisited adjacent vertices
3. Backtrack when no unvisited adjacent vertices remain
4. Continue until all reachable vertices are explored or target is found

This implementation is particularly useful for:
- Path finding between two vertices
- Graph connectivity analysis
- Cycle detection (with modifications)
- Topological sorting (with modifications)

The algorithm uses a visited set to prevent infinite loops in cyclic graphs
and maintains the complete traversal path for analysis purposes.
"""
from typing import Optional

from data_structures.Graph import Graph
from data_structures.Vertex import Vertex


class GraphDepthFirstSearch:
    """
    A utility class for performing depth-first search operations on graphs.

    This class encapsulates DFS functionality and provides a clean interface
    for graph traversal operations. The implementation uses recursive traversal
    with cycle detection to safely navigate both directed and undirected graphs.

    The class maintains no internal state, making it thread-safe and suitable
    for multiple concurrent searches on different graphs.

    Implementation Details:
    - Uses recursive approach for natural call stack management
    - Employs visited set for O(1) cycle detection
    - Returns complete traversal path for further analysis
    - Supports both weighted and unweighted graphs through vertex abstraction
    """

    @staticmethod
    def search(graph: Graph, start_vertex: Vertex, target_vertex: Vertex,
               visited: Optional[set[Vertex]] = None) -> Optional[set[Vertex]]:
        """
        Perform recursive depth-first search to locate a target vertex in a graph.

        This method implements the classic DFS algorithm using recursion. It explores
        each branch of the graph as deeply as possible before backtracking, maintaining
        a visited set to prevent cycles and infinite loops.

        Algorithm Steps:
        1. Initialize visited set if not provided (first call)
        2. Mark current vertex as visited
        3. Check if current vertex matches target (base case)
        4. Recursively explore each unvisited neighbor
        5. Return visited set if target found, None otherwise

        Time Complexity: O(V + E) where V = number of vertices, E = number of edges
        - Each vertex is visited at most once: O(V)
        - Each edge is examined at most once: O(E)
        - Combined traversal complexity: O(V + E)

        Space Complexity: O(V) for visited set and recursion stack
        - Visited set stores at most V vertices: O(V)
        - Recursion stack depth is at most V in worst case: O(V)
        - Total auxiliary space: O(V)

        Args:
            graph: The Graph object to search within
            start_vertex: The Vertex to begin the search from
            target_vertex: The Vertex to locate in the graph
            visited: Optional set of already visited vertices (used in recursion)

        Returns:
            set[Vertex]: Complete set of visited vertices if target is found
            None: If target vertex is not reachable from start vertex

        Raises:
            No explicit exceptions, but may raise if graph access fails

        Example:
            >>> searcher = GraphDepthFirstSearch()
            >>> result = searcher.search(my_graph, vertex_a, vertex_b)
            >>> if result:
            >>>     print(f"Found target! Visited {len(result)} vertices")
        """

        # Initialize visited set on first call if not provided
        if not visited:
            visited = set()


        # Cycle protection, mark current vertex as visited
        visited.add(start_vertex)

        # Base case: target found
        if start_vertex == target_vertex:
            return visited


        # Recursive case: explore all unvisited neighbors:
        # Get neighbors through graph's vertex lookup and edge traversal.
        current_graph_vertex = graph.vertices[start_vertex.value]

        for neighbor in current_graph_vertex.get_edges():
            # Skip already visited vertices to prevent infinite loops
            if neighbor not in visited:
                # Recursive DFS search for target vertex on unvisited neighbors
                path = GraphDepthFirstSearch.search(graph, neighbor, target_vertex, visited)

                # If target found, return complete path by propagating the result up.
                if path:
                    return path

        # Target not found in any reachable path from this vertex.
        return None


# Convenience function for backward compatibility and simpler usage
def dfs(graph: Graph, start_vertex: Vertex, target_vertex: Vertex, 
        visited: Optional[set[Vertex]] = None) -> Optional[set[Vertex]]:
    """
    Convenience wrapper function for depth-first search.

    This function provides a simpler interface to the DFS functionality
    without requiring class instantiation. It delegates to the main
    GraphDepthFirstSearch implementation.

    Time Complexity: O(V + E) - same as GraphDepthFirstSearch.search
    Space Complexity: O(V) - same as GraphDepthFirstSearch.search

    Args:
        graph: The graph to search in
        start_vertex: The vertex to start the search from
        target_vertex: The target vertex to find
        visited: Set of already visited vertices (used for recursion)

    Returns:
        Set of visited vertices if target is found, None if not found
    """
    return GraphDepthFirstSearch.search(graph, start_vertex, target_vertex, visited)



