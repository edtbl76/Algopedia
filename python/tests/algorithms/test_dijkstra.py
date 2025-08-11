import unittest
import sys
import os
import math

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.Greedy.Dijkstras import dijkstra, INFINITY
from data_structures.Graph import Graph
from data_structures.Vertex import Vertex


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create vertices for simple graph
        self.vertex_a = Vertex('A')
        self.vertex_b = Vertex('B')
        self.vertex_c = Vertex('C')
        self.vertex_d = Vertex('D')
        
        # Create vertices for complex graph
        self.vertex_s = Vertex('S')  # Source
        self.vertex_t = Vertex('T')  # Target
        self.vertex_x = Vertex('X')
        self.vertex_y = Vertex('Y')
        self.vertex_z = Vertex('Z')

    def test_simple_graph(self):
        """Test Dijkstra's algorithm on a simple graph."""
        # Create a simple directed graph
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_a)
        graph.add_vertex(self.vertex_b)
        graph.add_vertex(self.vertex_c)
        
        # Add edges with weights
        graph.add_edge(self.vertex_a, self.vertex_b, 1)
        graph.add_edge(self.vertex_b, self.vertex_c, 2)
        graph.add_edge(self.vertex_a, self.vertex_c, 4)
        
        # Run Dijkstra's algorithm from vertex A
        distances = dijkstra(graph, self.vertex_a)
        
        # Check distances
        self.assertEqual(distances[self.vertex_a], 0)
        self.assertEqual(distances[self.vertex_b], 1)
        self.assertEqual(distances[self.vertex_c], 3)  # Should be 3 (A->B->C) not 4 (A->C)

    def test_complex_graph(self):
        """Test Dijkstra's algorithm on a more complex graph."""
        # Create a complex directed graph
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_s)
        graph.add_vertex(self.vertex_t)
        graph.add_vertex(self.vertex_x)
        graph.add_vertex(self.vertex_y)
        graph.add_vertex(self.vertex_z)
        
        # Add edges with weights
        graph.add_edge(self.vertex_s, self.vertex_t, 10)
        graph.add_edge(self.vertex_s, self.vertex_y, 5)
        graph.add_edge(self.vertex_t, self.vertex_x, 1)
        graph.add_edge(self.vertex_t, self.vertex_y, 2)
        graph.add_edge(self.vertex_y, self.vertex_t, 3)
        graph.add_edge(self.vertex_y, self.vertex_x, 9)
        graph.add_edge(self.vertex_y, self.vertex_z, 2)
        graph.add_edge(self.vertex_x, self.vertex_z, 4)
        graph.add_edge(self.vertex_z, self.vertex_x, 6)
        
        # Run Dijkstra's algorithm from vertex S
        distances = dijkstra(graph, self.vertex_s)
        
        # Check distances
        self.assertEqual(distances[self.vertex_s], 0)
        self.assertEqual(distances[self.vertex_t], 8)  # S->Y->T (5+3)
        self.assertEqual(distances[self.vertex_x], 9)  # S->Y->T->X (5+3+1)
        self.assertEqual(distances[self.vertex_y], 5)  # S->Y (5)
        self.assertEqual(distances[self.vertex_z], 7)  # S->Y->Z (5+2)

    def test_undirected_graph(self):
        """Test Dijkstra's algorithm on an undirected graph."""
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
        graph.add_edge(self.vertex_c, self.vertex_d, 1)
        graph.add_edge(self.vertex_a, self.vertex_d, 6)
        
        # Run Dijkstra's algorithm from vertex A
        distances = dijkstra(graph, self.vertex_a)
        
        # Check distances
        self.assertEqual(distances[self.vertex_a], 0)
        self.assertEqual(distances[self.vertex_b], 1)
        self.assertEqual(distances[self.vertex_c], 3)  # A->B->C (1+2)
        self.assertEqual(distances[self.vertex_d], 4)  # A->B->C->D (1+2+1)

    def test_unreachable_vertices(self):
        """Test Dijkstra's algorithm with unreachable vertices."""
        # Create a directed graph with unreachable vertices
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_a)
        graph.add_vertex(self.vertex_b)
        graph.add_vertex(self.vertex_c)
        graph.add_vertex(self.vertex_d)
        
        # Add edges with weights (D is unreachable)
        graph.add_edge(self.vertex_a, self.vertex_b, 1)
        graph.add_edge(self.vertex_b, self.vertex_c, 2)
        # No edges to vertex D
        
        # Run Dijkstra's algorithm from vertex A
        distances = dijkstra(graph, self.vertex_a)
        
        # Check distances
        self.assertEqual(distances[self.vertex_a], 0)
        self.assertEqual(distances[self.vertex_b], 1)
        self.assertEqual(distances[self.vertex_c], 3)  # A->B->C (1+2)
        self.assertEqual(distances[self.vertex_d], INFINITY)  # Unreachable

    def test_single_vertex_graph(self):
        """Test Dijkstra's algorithm on a graph with a single vertex."""
        # Create a graph with a single vertex
        graph = Graph(directed=True)
        
        # Add vertex to the graph
        graph.add_vertex(self.vertex_a)
        
        # Run Dijkstra's algorithm from vertex A
        distances = dijkstra(graph, self.vertex_a)
        
        # Check distances
        self.assertEqual(distances[self.vertex_a], 0)
        self.assertEqual(len(distances), 1)

    def test_zero_weight_edges(self):
        """Test Dijkstra's algorithm with zero-weight edges."""
        # Create a directed graph with zero-weight edges
        graph = Graph(directed=True)
        
        # Add vertices to the graph
        graph.add_vertex(self.vertex_a)
        graph.add_vertex(self.vertex_b)
        graph.add_vertex(self.vertex_c)
        
        # Add edges with weights (including zero)
        graph.add_edge(self.vertex_a, self.vertex_b, 0)
        graph.add_edge(self.vertex_b, self.vertex_c, 0)
        graph.add_edge(self.vertex_a, self.vertex_c, 1)
        
        # Run Dijkstra's algorithm from vertex A
        distances = dijkstra(graph, self.vertex_a)
        
        # Check distances
        self.assertEqual(distances[self.vertex_a], 0)
        self.assertEqual(distances[self.vertex_b], 0)
        self.assertEqual(distances[self.vertex_c], 0)  # A->B->C (0+0)

    def test_negative_edge_weights(self):
        """Test Dijkstra's algorithm with negative edge weights (not supported)."""
        # This test is for documentation purposes only
        # Dijkstra's algorithm doesn't work with negative edge weights
        # The implementation should handle this gracefully or document the limitation
        pass


if __name__ == '__main__':
    unittest.main()