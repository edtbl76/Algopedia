"""
Traveling Salesperson Problem (TSP) Implementation using Nearest Neighbor Heuristic.

The Traveling Salesperson Problem is a classic optimization problem in computer science
and operations research. Given a list of cities and the distances between each pair of
cities, the goal is to find the shortest possible route that visits each city exactly
once and returns to the starting city.

Problem Classification:
    - NP-hard optimization problem
    - No known polynomial-time algorithm for optimal solution
    - Heuristic approaches provide good approximate solutions

This module implements the Nearest Neighbor heuristic, which is a greedy algorithm that:
1. Starts at a given (or random) vertex
2. Repeatedly moves to the nearest unvisited neighbor
3. Attempts to return to the starting vertex to complete the circuit

While not guaranteed to find the optimal solution, the nearest neighbor heuristic is:
    - Simple to understand and implement
    - Fast execution: O(n²) time complexity
    - Provides reasonable approximations for many practical cases
    - Good starting point for more sophisticated algorithms

Typical applications include:
    - Route planning and logistics
    - Circuit board drilling optimization
    - DNA sequencing
    - Job scheduling problems
"""
import random
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from data_structures.Graph import Graph
from data_structures.Vertex import Vertex

@dataclass
class TSPResult:
    """
    Container class for Traveling Salesperson Problem results.

    This dataclass encapsulates all relevant information about a TSP solution,
    providing a clean interface for accessing results and enabling easy
    comparison between different algorithm runs or heuristics.

    The class serves as a data transfer object (DTO) that maintains
    immutability and provides clear structure for TSP solution data.

    Attributes:
        path: Ordered list of vertices representing the tour path
        total_distance: Sum of all edge weights in the path
        circuit_completed: True if algorithm successfully returned to start vertex

    Usage:
        result = TSPResult(path=[v1, v2, v3, v1], total_distance=25, circuit_completed=True)
        print(f"Tour length: {result.total_distance}")
    """

    path: List[Vertex]
    total_distance: int
    circuit_completed: bool



def traveling_salesperson(graph: Graph, start_vertex: Optional[Vertex] = None, verbose: bool = True) -> Optional[TSPResult]:
    """
    Solve the Traveling Salesperson Problem using the nearest neighbor heuristic.

    This greedy algorithm constructs a tour by repeatedly selecting the nearest
    unvisited neighbor from the current position. While not optimal, it provides
    a reasonable approximation with good computational efficiency.

    Algorithm Steps:
        1. Initialize at start vertex (or choose randomly)
        2. Mark current vertex as visited and add to path
        3. While unvisited vertices remain:
           a. Find all unvisited neighbors of current vertex
           b. Select neighbor with minimum edge weight
           c. Move to selected neighbor and add to path
        4. Attempt to return to starting vertex to complete circuit

    Time Complexity: O(n²) where n is the number of vertices
        - Outer loop executes O(n) times (once per vertex)
        - Finding nearest neighbor requires O(n) comparisons
        - Total: O(n) × O(n) = O(n²)

    Space Complexity: O(n) for auxiliary data structures
        - O(n) for visited vertices tracking dictionary
        - O(n) for path storage list
        - O(n) for temporary neighbor weight dictionary

    Approximation Quality:
        - Worst case: Can be arbitrarily bad compared to optimal
        - Average case: Often within 25% of optimal for Euclidean instances
        - Best case: Can find optimal solution for some graph structures

    Args:
        graph: The graph containing vertices and weighted edges to traverse
        start_vertex: Vertex to begin the tour from. If None, chooses randomly
        verbose: Whether to print progress messages and final results to console

    Returns:
        TSPResult containing the path, total distance, and completion status,
        or None if the input graph contains no vertices

    Raises:
        No exceptions raised directly. Handles disconnected graphs gracefully
        by returning partial solutions with circuit_completed=False

    Example:
        >>> graph = create_sample_graph()
        >>> result = traveling_salesperson(graph, verbose=False)
        >>> print(f"Distance: {result.total_distance}")
        Distance: 42
    """
    # Edge case: empty graph or no vertices has no solution.
    if not graph.vertices:
        return None

    # Initialize data structures (algorithm state) - O(n) space for tracking
    # - path is the "tour path accumulator"
    # - visited_vertices is a dictionary tracking visited vertices - O(n)
    # - total_distance is the running total of edge weights in the path
    path = []
    visited_vertices = {vertex: False for vertex in graph.vertices.values()}
    total_distance = 0

    # Choose starting vertex: user provider or random
    # Random selection is O(n)
    current_vertex = start_vertex or random.choice(list(graph.vertices.values()))
    path.append(current_vertex)
    visited_vertices[current_vertex] = True


    # Special case for single vertex graph
    if len(graph.vertices) == 1:
        return TSPResult(path, 0, True)

    # Main TSP Loop: visit all vertices using nearest neighbor heuristic
    # Outer loop: O(n) iterations, one per vertex
    while not _has_visited_all_vertices(visited_vertices):
        # Find all unvisited neighbors of current vertex
        # O(degree) where degree ≤ n-1
        unvisited_neighbors = _find_unvisited_neighbors(graph, current_vertex, visited_vertices)

        # Handle disconnected graph case - algorithm gets stuck
        if not unvisited_neighbors:
            _log_disconnected_warning(current_vertex, visited_vertices, verbose)
            break

        # Get nearest neighbor - O(degree) to find minimum weight edge
        nearest_vertex, nearest_weight = _find_nearest_neighbor(unvisited_neighbors)

        # Move to nearest neighbor - O(1) lookup and list append
        current_vertex = nearest_vertex
        visited_vertices[nearest_vertex] = True
        path.append(nearest_vertex)
        total_distance += nearest_weight


    # Attempt to close the circuit by returning to starting vertex
    circuit_completed, return_weight  = _try_complete_circuit(graph, current_vertex, path)
    if circuit_completed:
        # Don't forget to add the weight of the return edge!
        total_distance += return_weight

    # Create (DTO) and log result
    result = TSPResult(path, total_distance, circuit_completed)
    _log_result(result, verbose)

    return result


### Helper Functions ###


def _has_visited_all_vertices(visited_vertices: Dict[Vertex, bool]) -> bool:
    """
    Check if all vertices in the graph have been visited.

    Uses the built-in all() function for efficient evaluation that short-circuits
    on the first False value encountered, providing better average performance
    than manual iteration.

    Time Complexity: O(n) worst case, O(1) best case with short-circuiting
    Space Complexity: O(1) - no additional storage required

    Args:
        visited_vertices: Dictionary mapping each vertex to its visited status

    Returns:
        True if all vertices have been visited (all values are True),
        False if any vertex remains unvisited
    """
    # all() built-in function checks if every element in the iterable is True
    # Short-circuits immediately on first False value for efficiency
    # Replaces manual for-loop: "for v in visited_vertices.values(): if not v: return False"
    return all(visited_vertices.values())

def _find_unvisited_neighbors(graph: Graph, current_vertex: Vertex, visited_vertices:
                              Dict[Vertex, bool]) -> Dict[Vertex, int]:
    """
    Find all unvisited neighboring vertices and their edge weights.

    Constructs a dictionary of reachable unvisited vertices from the current
    position, along with the edge weights needed to reach them. This enables
    the nearest neighbor selection in the next step.

    Time Complexity: O(degree) where degree is the number of outgoing edges
        - Iterates through all edges from current vertex: O(degree)
        - Dictionary lookup for visited status: O(1) per edge
        - Edge weight lookup: O(1) per edge

    Space Complexity: O(degree) for the neighbors dictionary in worst case
        - Each unvisited neighbor creates one dictionary entry
        - Maximum size is the vertex degree

    Args:
        graph: The graph containing vertex and edge information
        current_vertex: The vertex from which to find neighbors  
        visited_vertices: Dictionary tracking which vertices have been visited

    Returns:
        Dictionary mapping unvisited neighbor vertices to their edge weights.
        Empty dictionary if no unvisited neighbors exist (disconnected case)
    """
    neighbors = {}
    # Gets adjacent vertices
    current_edges = graph.vertices[current_vertex.value].get_edges()

    # Cycle through each outgoing edge from the current vertex
    for edge in current_edges:
        # Ignore visited neighbors
        if not visited_vertices[edge]:
            weight = graph.vertices[current_vertex.value].get_edge_weight(edge)
            #
            # IMPLEMENTATION DETAIL:
            #
            # This syntax (as opposed to "if weight") includes edges w/ weight 0 (valid)
            # but excludes None (no edge exists)
            if weight is not None:
                neighbors[edge] = weight

    return neighbors

def _find_nearest_neighbor(neighbors: Dict[Vertex, int]) -> Tuple[Vertex, int]:
    """
    Identify the neighbor vertex with the minimum edge weight (nearest neighbor).

    Implements the core greedy choice of the nearest neighbor heuristic by
    selecting the unvisited neighbor that can be reached with minimum cost.
    This greedy selection is what makes the algorithm fast but not optimal.

    Time Complexity: O(k) where k is the number of unvisited neighbors
        - min() function must compare all dictionary values: O(k)
        - Dictionary lookup for selected vertex: O(1)

    Space Complexity: O(1) - only stores references to selected vertex and weight

    Args:
        neighbors: Dictionary mapping neighbor vertices to their edge weights.
                  Must be non-empty (caller should check for disconnected case)

    Returns:
        Tuple containing (nearest_vertex, edge_weight) where nearest_vertex
        is the vertex with minimum edge weight and edge_weight is that minimum cost

    Note:
        If multiple neighbors have the same minimum weight, min() returns one
        arbitrarily based on vertex comparison. This can affect solution quality
        but doesn't impact algorithm correctness.
    """
    # minimum weight is the nearest neighbor
    nearest_vertex = min(neighbors, key=neighbors.get)
    return nearest_vertex, neighbors[nearest_vertex]

def _try_complete_circuit(graph: Graph, current_vertex: Vertex, path: List[Vertex]) -> Tuple[bool, int]:
    """
      Attempt to complete the TSP circuit by adding an edge back to the starting vertex.

      A valid TSP solution requires returning to the starting vertex to form a complete
      circuit/cycle. This function checks if such a return edge exists and adds it to
      the path if possible. If no return edge exists, the result is a partial tour.

      Time Complexity: O(1) - constant time operations
          - Path indexing to get start vertex: O(1)
          - Edge weight lookup: O(1) via hash table
          - List append operation: O(1) amortized

      Space Complexity: O(1) - no additional data structures allocated
          - Only local variables for edge weight and return values

      Args:
          graph: The graph containing vertex and edge connectivity information
          current_vertex: The last vertex visited in the tour path
          path: The current tour path. Modified in-place if circuit completion succeeds

      Returns:
          Tuple (circuit_completed, return_weight) where:
          - circuit_completed: True if return edge exists and circuit is closed
          - return_weight: Weight of the return edge if it exists, 0 otherwise

      Side Effects:
          If a return edge exists, appends the starting vertex to the path to
          complete the circuit. This modifies the input path list in-place.

      Example:
          Path before: [A, B, C, D]
          Path after:  [A, B, C, D, A] (if edge D→A exists)
      """
    # calculates the weight of the edge from current_vertex to start_vertex (origin)
    start_vertex = path[0]
    return_weight = graph.vertices[current_vertex.value].get_edge_weight(start_vertex)

    # Check if this edge exists
    if return_weight is not None:
        # This is the magical step of the TSP algorithm: this closes the circuit.
        path.append(start_vertex)
        return True, return_weight

    # Close but no cigar: return partial solution with circuit_completed=False
    # Almost only counts in horseshoes and hand grenades, but still...
    return False, 0

def _log_disconnected_warning(current_vertex: Vertex, visited_vertices: Dict[Vertex, bool], verbose: bool) -> None:
    """
    Log a warning message when the algorithm gets stuck due to graph disconnectedness.

    This situation occurs when the current vertex has no unvisited neighbors,
    but unvisited vertices still exist elsewhere in the graph. This indicates
    the graph is not strongly connected, making a complete TSP tour impossible.

    Time Complexity: O(n) where n is the number of vertices
        - Counting unvisited vertices requires iteration through all vertices: O(n)
        - Print operations are O(1) each

    Space Complexity: O(1) - only local variables for counting

    Args:
        current_vertex: The vertex where the algorithm got stuck
        visited_vertices: Dictionary tracking visited status of all vertices
        verbose: Flag controlling whether to output warning messages

    Side Effects:
        Prints warning messages to console if verbose=True. No output if verbose=False
        to support silent execution modes.

    Note:
        This diagnostic information helps users understand why their TSP solution
        is incomplete and suggests checking graph connectivity as a potential fix.
    """
    if verbose:
        # Count unvisited vertices for diagnostic purposes
        unvisited_count = sum(1 for visited in visited_vertices.values() if not visited)
        print(f'Warning: Stuck at vertex {current_vertex} with no unvisited neighbors.')
        print(f'Graph may not be fully connected. {unvisited_count} vertices remain unvisited.')


def _log_result(result: TSPResult, verbose: bool) -> None:
    """
    Output the final TSP algorithm results in a human-readable format.

    Provides comprehensive feedback about the algorithm's performance including
    success status, tour quality metrics, and the complete path taken. This
    information is valuable for debugging, analysis, and understanding solution quality.

    Time Complexity: O(n) where n is the path length
        - List comprehension for path formatting: O(n)
        - Print operations: O(1) each
        - String formatting: O(n) for path representation

    Space Complexity: O(n) for temporary string representations of the path

    Args:
        result: TSPResult object containing all solution information
        verbose: Flag controlling console output. No output when False

    Side Effects:
        Prints formatted results to console when verbose=True:
        - Success/failure status message
        - Total distance traveled
        - Complete vertex path with readable vertex values

    Output Format Examples:
        Success case:
        "Traveling Salesperson circuit completed."
        "Total distance traveled: 42"
        "Final path: ['A', 'B', 'C', 'D', 'A']"

        Failure case:
        "Warning: Traveling Salesperson circuit could not be completed."
        "Partial path distance: 28"
        "Final path: ['A', 'B', 'C', 'D']"
    """
    if not verbose:
        return

    # Some basic reporting / metrics
    if result.circuit_completed:
        print("Traveling Salesperson circuit completed.")
        print(f"Total distance traveled: {result.total_distance}")
    else:
        print("Warning: Traveling Salesperson circuit could not be completed.")
        print(f"Partial path distance: {result.total_distance}")

    # Display the path in a human-readable representations of vertices
    print(f"Final path: {[str(v.value) for v in result.path]}")



# Legacy compatibility function
def traveling_salesperson_legacy(graph: Graph) -> Optional[Tuple[List[Vertex], int]]:
    """
    Legacy interface for backward compatibility with existing code.

    Provides the original function signature and return format to ensure
    existing code continues to work without modification after the API
    was enhanced with the TSPResult dataclass and additional parameters.

    This wrapper function demonstrates the adapter pattern, allowing old
    and new interfaces to coexist during transition periods.

    Time Complexity: O(n²) - same as main algorithm (just a thin wrapper)
    Space Complexity: O(n) - same as main algorithm plus minimal wrapper overhead

    Args:
        graph: The graph to solve TSP on (same as main function)

    Returns:
        Tuple (path, total_distance) in the original format, or None if
        the graph is empty. Equivalent to accessing result.path and
        result.total_distance from the new interface.

    Example:
        >>> # Old code continues to work unchanged
        >>> path, distance = traveling_salesperson_legacy(graph)
        >>> print(f"Legacy result: {distance}")

    Note:
        This function runs in silent mode (verbose=False) and uses random
        start vertex selection to match the original behavior exactly.
    """
    result = traveling_salesperson(graph, verbose=False)
    return (result.path, result.total_distance) if result else None
