"""
Dijkstra's shortest path algorithm.

This module implements Dijkstra's algorithm for finding the shortest paths from a
source vertex to all other vertices in a weighted graph with non-negative edge weights.

Dijkstra's algorithm is a greedy algorithm that maintains a priority queue of vertices
ordered by their tentative distance from the source. It repeatedly extracts the vertex
with minimum distance and relaxes all its outgoing edges, potentially updating the
shortest distances to neighboring vertices.

The algorithm guarantees optimal shortest paths because it processes vertices in order
of their actual shortest distance from the source, ensuring that when a vertex is
processed, its shortest path has been found.

Key properties:
- Works only with non-negative edge weights
- Produces a shortest path tree from the source vertex
- Time complexity: O((V + E) log V) using binary heap
- Space complexity: O(V) for distance tracking and priority queue

"""
import math
from heapq import heappop, heappush
from typing import Dict

from data_structures.Graph import Graph
from data_structures.Vertex import Vertex

# Constant representing infinite distance for unreachable vertices
# Using a very large integer instead of trying to convert math.inf to int
INFINITY = float('inf')


def dijkstra(graph: Graph, start: Vertex) -> Dict[Vertex, int]:
    """
    Find shortest paths from a source vertex to all other vertices using Dijkstra's algorithm.

    This implementation uses a binary min-heap (priority queue) to efficiently extract
    the vertex with minimum tentative distance. The algorithm maintains the invariant
    that once a vertex is extracted from the priority queue, its shortest distance
    from the source has been determined.

    Algorithm steps:
    1. Initialize all distances to infinity except source (distance 0)
    2. Add source vertex to priority queue with distance 0
    3. While priority queue is not empty:
       a. Extract vertex with minimum distance
       b. Skip if we've already found a better path (lazy deletion)
       c. For each neighbor, attempt to relax the edge
       d. If relaxation improves distance, update and add to queue

    Time Complexity: O((V + E) log V)
        - V vertices are extracted from the priority queue: O(V log V)
        - Each edge is relaxed at most once: O(E log V) for heap operations
        - Overall: O((V + E) log V)

    Space Complexity: O(V)
        - Distance dictionary: O(V)
        - Priority queue: O(V) in worst case
        - No additional data structures scale with input size

    Args:
        graph: The input graph containing vertices and weighted edges
        start: The source vertex from which to compute shortest paths

    Returns:
        Dictionary mapping each vertex to its shortest distance from the source.
        Unreachable vertices will have distance INFINITY.

    Raises:
        KeyError: If start vertex is not in the graph

    Note:
        This implementation assumes all edge weights are non-negative.
        Negative edge weights would require the Bellman-Ford algorithm instead.
    """

    # Init distance dict w/ all vertices set to the infinity constant.
    # Only vertices that are reachable from source/start will be updated w/ finite distances.
    distances: Dict[Vertex, int] = {vertex: INFINITY for vertex in graph.vertices.values()}

    # Initialize priority queue with source vertex and distance 0
    distances[start] = 0

    # Priority queue stores tuples of (distance, vertex)
    # Python's heapq module uses min-heap, so minimum distance vertices are extracted first.
    unexplored_vertices = [(0, start)]

    # Main algo loop. We process vertices in increasing order of their distance from the source.
    while unexplored_vertices:
        # Extract vertex w/ minimum tentative distance from priority queue
        # This vertex should now have its final shortest distance determined
        current_distance, current_vertex = heappop(unexplored_vertices)

        # Lazy deletion: skip irrelevant vertices in priority queue
        # This is a common optimization to avoid processing vertices when we've already found a better path.
        if current_distance > distances[current_vertex]:
            continue

        # Edge relaxation: examines all outgoing edges from current vertex
        for neighbor in current_vertex.get_edges():

            # get edge weight from current vertex to neighbor
            edge_weight = current_vertex.get_edge_weight(neighbor)

            # calculates candidate / potential new distance through the current vertex
            new_distance = current_distance + edge_weight

            # Relaxation step: updates distance if a better path is found.
            if new_distance < distances[neighbor]:
                # updates shortest distance for neighbor
                distances[neighbor] = new_distance

                # Add neighbor to priority queue w/ updated distance
                # NOTE: we don't remove old entries (lazy deletion approach)
                heappush(unexplored_vertices, (new_distance, neighbor))

    # Returns mapping of vertices their shortest distances from the source.
    return distances
