"""
Unit tests for the Traveling Salesperson Problem implementation.

This module contains tests for the Traveling Salesperson Problem (TSP) implementation
using the nearest neighbor heuristic. The tests cover various scenarios including:

1. Simple complete graphs - Tests basic functionality on small complete graphs
2. Larger complete graphs - Tests scalability on larger graphs
3. Disconnected graphs - Tests behavior when not all vertices are reachable
4. Empty graphs - Tests edge case of empty input
5. Single vertex graphs - Tests trivial case with only one vertex
6. Undirected graphs - Tests behavior on undirected graphs
7. Zero-weight edges - Tests handling of zero-weight edges

Each test verifies different aspects of the algorithm including:
- Correct path construction
- Proper circuit completion
- Accurate distance calculation
- Appropriate handling of edge cases

These tests ensure the TSP implementation is robust and behaves as expected
across a wide range of input scenarios.
"""

import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.Greedy.TravelingSalesperson import traveling_salesperson, TSPResult
from data_structures.Graph import Graph
from data_structures.Vertex import Vertex


class TestTravelingSalesperson(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create vertices for simple graph
        self.vertex_a = Vertex('A')
        self.vertex_b = Vertex('B')
        self.vertex_c = Vertex('C')
        self.vertex_d = Vertex('D')
        
        # Create vertices for complex graph
        self.vertex_1 = Vertex('1')
        self.vertex_2 = Vertex('2')
        self.vertex_3 = Vertex('3')
        self.vertex_4 = Vertex('4')
        self.vertex_5 = Vertex('5')

    def test_simple_complete_graph(self):
        """
        Test TSP on a simple complete graph where all vertices are connected.
        
        This test creates a small complete directed graph with 3 vertices (A, B, C)
        where every vertex has an edge to every other vertex. It verifies that:
        1. The algorithm returns a valid TSPResult
        2. The circuit is successfully completed
        3. The path contains all vertices exactly once (except start vertex)
        4. The path starts and ends with the same vertex
        """
        # Create a complete directed graph
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_a)
        graph.add_vertex(self.vertex_b)
        graph.add_vertex(self.vertex_c)
        
        # Add edges with weights to make a complete graph
        graph.add_edge(self.vertex_a, self.vertex_b, 1)
        graph.add_edge(self.vertex_a, self.vertex_c, 4)
        graph.add_edge(self.vertex_b, self.vertex_a, 2)
        graph.add_edge(self.vertex_b, self.vertex_c, 2)
        graph.add_edge(self.vertex_c, self.vertex_a, 3)
        graph.add_edge(self.vertex_c, self.vertex_b, 5)
        
        # Get the vertex from the graph for the start vertex
        start_vertex = graph.vertices['A']
        
        # Run TSP algorithm with a fixed start vertex for deterministic testing
        result = traveling_salesperson(graph, start_vertex, verbose=False)
        
        # Check result properties
        self.assertIsNotNone(result)
        self.assertIsInstance(result, TSPResult)
        self.assertTrue(result.circuit_completed)
        
        # Check path properties
        self.assertEqual(len(result.path), 4)  # 3 vertices + return to start
        self.assertEqual(result.path[0], graph.vertices['A'])  # Start vertex
        self.assertEqual(result.path[-1], graph.vertices['A'])  # End vertex (circuit)
        
        # Verify all vertices are visited exactly once (except start vertex which appears twice)
        vertices_in_path = set(result.path)
        self.assertEqual(len(vertices_in_path), 3)
        self.assertIn(graph.vertices['A'], vertices_in_path)
        self.assertIn(graph.vertices['B'], vertices_in_path)
        self.assertIn(graph.vertices['C'], vertices_in_path)

    def test_larger_complete_graph(self):
        """
        Test TSP on a larger complete graph.
        
        This test creates a larger complete directed graph with 5 vertices (1-5)
        with varying edge weights. It verifies that:
        1. The algorithm scales to handle larger graphs
        2. The circuit is successfully completed
        3. The path contains all vertices exactly once (except start vertex)
        4. The path starts and ends with the same vertex
        
        This test is important for verifying the algorithm's performance on
        more complex inputs.
        """
        # Create a complete directed graph
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_1)
        graph.add_vertex(self.vertex_2)
        graph.add_vertex(self.vertex_3)
        graph.add_vertex(self.vertex_4)
        graph.add_vertex(self.vertex_5)
        
        # Add edges with weights to make a complete graph
        # From vertex 1
        graph.add_edge(self.vertex_1, self.vertex_2, 10)
        graph.add_edge(self.vertex_1, self.vertex_3, 15)
        graph.add_edge(self.vertex_1, self.vertex_4, 20)
        graph.add_edge(self.vertex_1, self.vertex_5, 25)
        
        # From vertex 2
        graph.add_edge(self.vertex_2, self.vertex_1, 10)
        graph.add_edge(self.vertex_2, self.vertex_3, 35)
        graph.add_edge(self.vertex_2, self.vertex_4, 25)
        graph.add_edge(self.vertex_2, self.vertex_5, 30)
        
        # From vertex 3
        graph.add_edge(self.vertex_3, self.vertex_1, 15)
        graph.add_edge(self.vertex_3, self.vertex_2, 35)
        graph.add_edge(self.vertex_3, self.vertex_4, 30)
        graph.add_edge(self.vertex_3, self.vertex_5, 5)
        
        # From vertex 4
        graph.add_edge(self.vertex_4, self.vertex_1, 20)
        graph.add_edge(self.vertex_4, self.vertex_2, 25)
        graph.add_edge(self.vertex_4, self.vertex_3, 30)
        graph.add_edge(self.vertex_4, self.vertex_5, 10)
        
        # From vertex 5
        graph.add_edge(self.vertex_5, self.vertex_1, 25)
        graph.add_edge(self.vertex_5, self.vertex_2, 30)
        graph.add_edge(self.vertex_5, self.vertex_3, 5)
        graph.add_edge(self.vertex_5, self.vertex_4, 10)
        
        # Get the vertex from the graph for the start vertex
        start_vertex = graph.vertices['1']
        
        # Run TSP algorithm with a fixed start vertex for deterministic testing
        result = traveling_salesperson(graph, start_vertex, verbose=False)
        
        # Check result properties
        self.assertIsNotNone(result)
        self.assertTrue(result.circuit_completed)
        
        # Check path properties
        self.assertEqual(len(result.path), 6)  # 5 vertices + return to start
        self.assertEqual(result.path[0], graph.vertices['1'])  # Start vertex
        self.assertEqual(result.path[-1], graph.vertices['1'])  # End vertex (circuit)
        
        # Verify all vertices are visited exactly once (except start vertex which appears twice)
        vertices_in_path = set(result.path)
        self.assertEqual(len(vertices_in_path), 5)
        self.assertIn(graph.vertices['1'], vertices_in_path)
        self.assertIn(graph.vertices['2'], vertices_in_path)
        self.assertIn(graph.vertices['3'], vertices_in_path)
        self.assertIn(graph.vertices['4'], vertices_in_path)
        self.assertIn(graph.vertices['5'], vertices_in_path)

    def test_disconnected_graph(self):
        """
        Test TSP on a disconnected graph where a complete circuit is impossible.
        
        This test creates a directed graph with 4 vertices where:
        - Vertex D is completely disconnected (no edges to/from it)
        - Vertices A, B, C form a path without a return edge to complete the circuit
        
        It verifies that:
        1. The algorithm handles disconnected graphs gracefully
        2. The circuit_completed flag is correctly set to False
        3. The unreachable vertex D is not included in the path
        4. The path contains only the reachable vertices
        
        This test is crucial for verifying the algorithm's behavior in non-ideal
        graph conditions.
        """
        # Create a disconnected directed graph
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_a)
        graph.add_vertex(self.vertex_b)
        graph.add_vertex(self.vertex_c)
        graph.add_vertex(self.vertex_d)
        
        # Add edges with weights (D is unreachable)
        graph.add_edge(self.vertex_a, self.vertex_b, 1)
        graph.add_edge(self.vertex_b, self.vertex_c, 2)
        # No return edge from C to A to break the circuit
        # No edges to or from vertex D
        
        # Get the vertex from the graph for the start vertex
        start_vertex = graph.vertices['A']
        
        # Run TSP algorithm with a fixed start vertex
        result = traveling_salesperson(graph, start_vertex, verbose=False)
        
        # Check result properties
        self.assertIsNotNone(result)
        self.assertFalse(result.circuit_completed)  # Circuit should not be completed
        
        # Check path properties - should contain only A, B, C (not D)
        self.assertLessEqual(len(result.path), 3)  # At most 3 vertices in path
        self.assertEqual(result.path[0], graph.vertices['A'])  # Start vertex
        
        # Verify D is not in the path (unreachable)
        self.assertNotIn(graph.vertices['D'], result.path)

    def test_empty_graph(self):
        """
        Test TSP on an empty graph.
        
        This test creates an empty graph with no vertices and verifies that:
        1. The algorithm returns None for an empty graph
        
        This test is important for verifying the algorithm's behavior with
        edge case inputs and ensuring it doesn't crash on empty input.
        """
        # Create an empty graph
        graph = Graph(directed=True)
        
        # Run TSP algorithm
        result = traveling_salesperson(graph, verbose=False)
        
        # Check result properties
        self.assertIsNone(result)  # Should return None for empty graph

    def test_single_vertex_graph(self):
        """
        Test TSP on a graph with a single vertex.
        
        This test creates a graph with a single vertex and verifies that:
        1. The algorithm handles the trivial case correctly
        2. The circuit_completed flag is set to True (trivial circuit)
        3. The path contains only the single vertex
        4. The total distance is 0 (no edges traversed)
        
        This test is important for verifying the algorithm's behavior with
        minimal valid input and ensuring edge cases are handled properly.
        """
        # Create a graph with a single vertex
        graph = Graph(directed=True)
        
        # Add vertex to the graph
        graph.add_vertex(self.vertex_a)
        
        # Get the vertex from the graph
        start_vertex = graph.vertices['A']
        
        # Run TSP algorithm
        result = traveling_salesperson(graph, start_vertex, verbose=False)
        
        # Check result properties
        self.assertIsNotNone(result)
        self.assertTrue(result.circuit_completed)  # Single vertex is a trivial circuit
        
        # Check path properties
        self.assertEqual(len(result.path), 1)  # Only one vertex
        self.assertEqual(result.path[0], graph.vertices['A'])
        self.assertEqual(result.total_distance, 0)  # No distance traveled

    def test_undirected_graph(self):
        """
        Test TSP on an undirected graph.
        
        This test creates an undirected graph with 4 vertices (A, B, C, D)
        connected in a cycle. It verifies that:
        1. The algorithm works correctly on undirected graphs
        2. The circuit is successfully completed
        3. The path contains all vertices exactly once (except start vertex)
        4. The path starts and ends with the same vertex
        
        This test is important for verifying the algorithm's flexibility
        to work with both directed and undirected graphs.
        """
        # Create an undirected graph
        graph = Graph(directed=False)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_a)
        graph.add_vertex(self.vertex_b)
        graph.add_vertex(self.vertex_c)
        graph.add_vertex(self.vertex_d)
        
        # Add edges with weights
        graph.add_edge(self.vertex_a, self.vertex_b, 1)
        graph.add_edge(self.vertex_b, self.vertex_c, 2)
        graph.add_edge(self.vertex_c, self.vertex_d, 3)
        graph.add_edge(self.vertex_d, self.vertex_a, 4)
        
        # Get the vertex from the graph
        start_vertex = graph.vertices['A']
        
        # Run TSP algorithm with a fixed start vertex
        result = traveling_salesperson(graph, start_vertex, verbose=False)
        
        # Check result properties
        self.assertIsNotNone(result)
        self.assertTrue(result.circuit_completed)
        
        # Check path properties
        self.assertEqual(len(result.path), 5)  # 4 vertices + return to start
        self.assertEqual(result.path[0], graph.vertices['A'])  # Start vertex
        self.assertEqual(result.path[-1], graph.vertices['A'])  # End vertex (circuit)
        
        # Verify all vertices are visited exactly once (except start vertex which appears twice)
        vertices_in_path = set(result.path)
        self.assertEqual(len(vertices_in_path), 4)
        self.assertIn(graph.vertices['A'], vertices_in_path)
        self.assertIn(graph.vertices['B'], vertices_in_path)
        self.assertIn(graph.vertices['C'], vertices_in_path)
        self.assertIn(graph.vertices['D'], vertices_in_path)

    def test_zero_weight_edges(self):
        """
        Test TSP with zero-weight edges.
        
        This test creates a directed graph with 3 vertices (A, B, C) where
        all edges have zero weight. It verifies that:
        1. The algorithm handles zero-weight edges correctly
        2. The circuit is successfully completed
        3. The path contains all vertices exactly once (except start vertex)
        4. The total distance is correctly calculated as 0
        
        This test is important for verifying the algorithm's behavior with
        edge weights of 0, ensuring they are treated as valid edges and not
        as missing connections.
        """
        # Create a directed graph with zero-weight edges
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_a)
        graph.add_vertex(self.vertex_b)
        graph.add_vertex(self.vertex_c)
        
        # Add edges with weights (including zero)
        graph.add_edge(self.vertex_a, self.vertex_b, 0)
        graph.add_edge(self.vertex_b, self.vertex_c, 0)
        graph.add_edge(self.vertex_c, self.vertex_a, 0)
        
        # Get the vertex from the graph
        start_vertex = graph.vertices['A']
        
        # Run TSP algorithm with a fixed start vertex
        result = traveling_salesperson(graph, start_vertex, verbose=False)
        
        # Check result properties
        self.assertIsNotNone(result)
        self.assertTrue(result.circuit_completed)
        
        # Check path properties
        self.assertEqual(len(result.path), 4)  # 3 vertices + return to start
        self.assertEqual(result.path[0], graph.vertices['A'])  # Start vertex
        self.assertEqual(result.path[-1], graph.vertices['A'])  # End vertex (circuit)
        self.assertEqual(result.total_distance, 0)  # Total distance should be 0


if __name__ == '__main__':
    unittest.main()