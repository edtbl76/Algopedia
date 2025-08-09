"""
Graph data structure implementation supporting both directed and undirected graphs.

A Graph is a non-linear data structure consisting of vertices (nodes) and edges
that connect pairs of vertices. This implementation uses an adjacency list
representation where each vertex maintains its own list of outgoing edges,
providing efficient storage and traversal capabilities.

The graph supports:
- Both directed and undirected graphs
- Weighted edges
- Dynamic vertex and edge addition
- Path finding using depth-first search (DFS)
"""

from typing import Dict
from data_structures.Vertex import Vertex


class Graph:
    """
    A graph data structure using adjacency list representation.

    The graph maintains a dictionary mapping vertex values to Vertex objects,
    allowing for O(1) vertex lookup by value. Each vertex stores its own
    outgoing edges, providing an efficient adjacency list implementation.

    Implementation details:
    - Vertices are stored in a dictionary keyed by their values
    - Edges are managed by individual Vertex objects
    - Undirected graphs maintain bidirectional edges automatically
    - Supports weighted edges through the underlying Vertex/Edge structure
    """

    def __init__(self, directed: bool = False):
        """
        Initialize a new graph instance.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            directed: If True, creates a directed graph. If False, creates
                     an undirected graph where edges are bidirectional.
        """
        self.directed = directed
        self.vertices: Dict[any, Vertex] = {}

    def add_vertex(self, vertex: Vertex) -> None:
        """
        Add a vertex to the graph.

        The vertex is indexed by its value for O(1) lookup. If a vertex
        with the same value already exists, it will be replaced.

        Time Complexity: O(1) - Dictionary insertion
        Space Complexity: O(1) - Single vertex storage

        Args:
            vertex: The Vertex object to add to the graph
        """
        self.vertices[vertex.value] = vertex

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: int = 1) -> None:
        """
        Add an edge between two vertices in the graph.

        For directed graphs, creates a single edge from from_vertex to to_vertex.
        For undirected graphs, creates bidirectional edges between the vertices.
        Both vertices must already exist in the graph.

        Time Complexity: O(1) for directed graphs, O(1) for undirected graphs
        Space Complexity: O(1) for directed graphs, O(2) for undirected graphs

        Args:
            from_vertex: The source vertex of the edge
            to_vertex: The destination vertex of the edge
            weight: The weight/cost of the edge (default: 1)

        Note:
            This method assumes both vertices have already been added to the graph.
            No validation is performed to check vertex existence.
        """

        # Edge from source to destination
        self.vertices[from_vertex.value].add_edge(to_vertex, weight)
        if not self.directed:
            # Edge from destination to source (if undirected)
            self.vertices[to_vertex.value].add_edge(from_vertex, weight)

    def find_path(self, start_vertex: Vertex, end_vertex: Vertex) -> bool:
        """
        Determine if a path exists between two vertices using depth-first search.

        Uses an iterative DFS approach with a stack to avoid recursion limits.
        The algorithm explores as far as possible along each branch before
        backtracking, marking vertices as visited to prevent cycles.

        Time Complexity: O(V + E) where V is vertices and E is edges
                        - In worst case, visits all vertices and traverses all edges
        Space Complexity: O(V) for the stack and visited set
                         - Stack can grow up to V vertices in worst case
                         - Visited set stores up to V vertices

        Args:
            start_vertex: The vertex to start the search from
            end_vertex: The target vertex to find a path to

        Returns:
            True if a path exists from start_vertex to end_vertex, False otherwise

        Algorithm:
            1. Initialize stack with start vertex and empty visited set
            2. While stack is not empty:
               a. Pop vertex from stack and mark as visited
               b. If current vertex equals target, return True
               c. Add all unvisited neighbors to stack
            3. If stack becomes empty without finding target, return False
        """
        # Verify both vertices exist in the graph
        if start_vertex.value not in self.vertices or end_vertex.value not in self.vertices:
            raise KeyError("One or both vertices are not in the graph")

        # basic DFS stack for iterative traversal
        stack = [start_vertex]

        # Cycle protection. Set to track visited vertices.
        visited = set()

        while len(stack) > 0:

            # Pop vertex from stack and mark as visited
            vertex_to_check = stack.pop()
            visited.add(vertex_to_check)

            # If we find the end vertex --> Hit, you sank my battleship! (or return True, I guess)
            if vertex_to_check == end_vertex:
                return True

            # Get the actual vertex object from our graph to check its edges
            current_vertex = self.vertices[vertex_to_check.value]

            # Find all unvisited neighbors and add to stack for next iteration
            unvisited_neighbors = [vertex for vertex in current_vertex.get_edges() if vertex not in visited]
            stack.extend(unvisited_neighbors)

        # search is exhausted without finding the end vertex.
        return False


