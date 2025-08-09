import unittest
from data_structures.Graph import Graph
from data_structures.Vertex import Vertex


class TestGraph(unittest.TestCase):
    """
    Test cases for the Graph class implementation.
    
    These tests verify the functionality of the Graph class including:
    - Initialization (directed and undirected)
    - Adding vertices
    - Adding edges
    - Finding paths
    - Edge cases
    """

    def test_initialization_directed(self):
        """Test initialization of a directed graph"""
        graph = Graph(directed=True)
        self.assertTrue(graph.directed)
        self.assertEqual(graph.vertices, {})

    def test_initialization_undirected(self):
        """Test initialization of an undirected graph"""
        graph = Graph(directed=False)
        self.assertFalse(graph.directed)
        self.assertEqual(graph.vertices, {})

    def test_initialization_default(self):
        """Test initialization with default parameters"""
        graph = Graph()
        self.assertFalse(graph.directed)  # Default should be undirected
        self.assertEqual(graph.vertices, {})

    def test_add_vertex(self):
        """Test adding a vertex to the graph"""
        graph = Graph()
        vertex = Vertex("A")
        
        # Add vertex
        graph.add_vertex(vertex)
        
        # Verify vertex was added
        self.assertIn(vertex.value, graph.vertices)
        self.assertEqual(graph.vertices[vertex.value], vertex)

    def test_add_multiple_vertices(self):
        """Test adding multiple vertices to the graph"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_vertex(vertex3)
        
        # Verify vertices were added
        self.assertEqual(len(graph.vertices), 3)
        self.assertIn("A", graph.vertices)
        self.assertIn("B", graph.vertices)
        self.assertIn("C", graph.vertices)

    def test_add_vertex_overwrite(self):
        """Test overwriting an existing vertex"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("A")  # Same value as vertex1
        
        # Add first vertex
        graph.add_vertex(vertex1)
        self.assertEqual(graph.vertices["A"], vertex1)
        
        # Overwrite with second vertex
        graph.add_vertex(vertex2)
        self.assertEqual(graph.vertices["A"], vertex2)
        self.assertEqual(len(graph.vertices), 1)  # Still only one vertex

    def test_add_edge_directed(self):
        """Test adding an edge in a directed graph"""
        graph = Graph(directed=True)
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        
        # Add edge
        graph.add_edge(vertex1, vertex2)
        
        # Verify edge was added in one direction only
        self.assertIn(vertex2, graph.vertices["A"].edges)
        self.assertNotIn(vertex1, graph.vertices["B"].edges)

    def test_add_edge_undirected(self):
        """Test adding an edge in an undirected graph"""
        graph = Graph(directed=False)
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        
        # Add edge
        graph.add_edge(vertex1, vertex2)
        
        # Verify edge was added in both directions
        self.assertIn(vertex2, graph.vertices["A"].edges)
        self.assertIn(vertex1, graph.vertices["B"].edges)

    def test_add_edge_with_weight(self):
        """Test adding an edge with a custom weight"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        
        # Add edge with weight
        graph.add_edge(vertex1, vertex2, weight=5)
        
        # Verify edge weight
        self.assertEqual(graph.vertices["A"].edges[vertex2].weight, 5)
        self.assertEqual(graph.vertices["B"].edges[vertex1].weight, 5)  # Undirected graph

    def test_add_multiple_edges(self):
        """Test adding multiple edges"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_vertex(vertex3)
        
        # Add edges
        graph.add_edge(vertex1, vertex2)
        graph.add_edge(vertex1, vertex3)
        graph.add_edge(vertex2, vertex3)
        
        # Verify edges
        self.assertIn(vertex2, graph.vertices["A"].edges)
        self.assertIn(vertex3, graph.vertices["A"].edges)
        self.assertIn(vertex1, graph.vertices["B"].edges)
        self.assertIn(vertex3, graph.vertices["B"].edges)
        self.assertIn(vertex1, graph.vertices["C"].edges)
        self.assertIn(vertex2, graph.vertices["C"].edges)

    def test_find_path_direct(self):
        """Test finding a direct path between vertices"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add vertices and edge
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_edge(vertex1, vertex2)
        
        # Find path
        self.assertTrue(graph.find_path(vertex1, vertex2))
        self.assertTrue(graph.find_path(vertex2, vertex1))  # Undirected

    def test_find_path_indirect(self):
        """Test finding an indirect path through multiple vertices"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        vertex4 = Vertex("D")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_vertex(vertex3)
        graph.add_vertex(vertex4)
        
        # Add edges to form a path A -> B -> C -> D
        graph.add_edge(vertex1, vertex2)
        graph.add_edge(vertex2, vertex3)
        graph.add_edge(vertex3, vertex4)
        
        # Find path
        self.assertTrue(graph.find_path(vertex1, vertex4))
        self.assertTrue(graph.find_path(vertex4, vertex1))  # Undirected

    def test_find_path_nonexistent(self):
        """Test finding a nonexistent path"""
        graph = Graph(directed=True)  # Directed graph
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_vertex(vertex3)
        
        # Add edge from A to B only
        graph.add_edge(vertex1, vertex2)
        
        # No path from B to C or from C to A
        self.assertFalse(graph.find_path(vertex2, vertex3))
        self.assertFalse(graph.find_path(vertex3, vertex1))

    def test_find_path_cycle(self):
        """Test finding a path in a graph with cycles"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_vertex(vertex3)
        
        # Add edges to form a cycle A -> B -> C -> A
        graph.add_edge(vertex1, vertex2)
        graph.add_edge(vertex2, vertex3)
        graph.add_edge(vertex3, vertex1)
        
        # Find path
        self.assertTrue(graph.find_path(vertex1, vertex3))
        self.assertTrue(graph.find_path(vertex2, vertex1))
        self.assertTrue(graph.find_path(vertex3, vertex2))

    def test_find_path_self_loop(self):
        """Test finding a path from a vertex to itself"""
        graph = Graph()
        vertex = Vertex("A")
        
        # Add vertex
        graph.add_vertex(vertex)
        
        # Add self-loop
        graph.add_edge(vertex, vertex)
        
        # Find path
        self.assertTrue(graph.find_path(vertex, vertex))

    def test_find_path_disconnected(self):
        """Test finding a path in a disconnected graph"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        vertex4 = Vertex("D")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_vertex(vertex3)
        graph.add_vertex(vertex4)
        
        # Add edges to form two disconnected components: A-B and C-D
        graph.add_edge(vertex1, vertex2)
        graph.add_edge(vertex3, vertex4)
        
        # No path between components
        self.assertFalse(graph.find_path(vertex1, vertex3))
        self.assertFalse(graph.find_path(vertex2, vertex4))
        
    def test_find_path_invalid_vertices(self):
        """Test finding a path with vertices not in the graph"""
        graph = Graph()
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")  # Not added to graph
        
        # Add only two vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        graph.add_edge(vertex1, vertex2)
        
        # Try to find path with vertex not in graph
        # This should raise a KeyError since vertex3 is not in the graph
        with self.assertRaises(KeyError):
            graph.find_path(vertex1, vertex3)
            
        with self.assertRaises(KeyError):
            graph.find_path(vertex3, vertex1)
    
    def test_directed_graph_with_bidirectional_edges(self):
        """Test a directed graph with manually added bidirectional edges"""
        graph = Graph(directed=True)
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        
        # Add edges in both directions manually
        graph.add_edge(vertex1, vertex2)
        graph.add_edge(vertex2, vertex1)
        
        # Verify both edges exist
        self.assertIn(vertex2, graph.vertices["A"].edges)
        self.assertIn(vertex1, graph.vertices["B"].edges)
        
        # Verify paths exist in both directions
        self.assertTrue(graph.find_path(vertex1, vertex2))
        self.assertTrue(graph.find_path(vertex2, vertex1))
    
    def test_edge_weight_consistency_undirected(self):
        """Test that edge weights are consistent in both directions for undirected graphs"""
        graph = Graph(directed=False)
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add vertices
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)
        
        # Add edge with weight
        graph.add_edge(vertex1, vertex2, weight=7)
        
        # Verify weight is the same in both directions
        self.assertEqual(graph.vertices["A"].get_edge_weight(vertex2), 7)
        self.assertEqual(graph.vertices["B"].get_edge_weight(vertex1), 7)
        
        # Change weight in one direction
        graph.vertices["A"].add_edge(vertex2, weight=10)
        
        # In an undirected graph implementation, this should not affect the other direction
        # This test verifies the current behavior, which may need to be fixed if consistency is required
        self.assertEqual(graph.vertices["A"].get_edge_weight(vertex2), 10)
        self.assertEqual(graph.vertices["B"].get_edge_weight(vertex1), 7)
    
    def test_complete_graph(self):
        """Test creating and verifying a complete graph where every vertex connects to every other vertex"""
        graph = Graph()
        
        # Create vertices
        vertices = [Vertex(str(i)) for i in range(5)]  # 5 vertices labeled 0-4
        
        # Add vertices to graph
        for vertex in vertices:
            graph.add_vertex(vertex)
            
        # Connect every vertex to every other vertex (complete graph)
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if i != j:  # Don't connect to self
                    graph.add_edge(vertices[i], vertices[j])
        
        # Verify each vertex has edges to all other vertices
        for i in range(len(vertices)):
            # Each vertex should have n-1 edges (to all vertices except itself)
            self.assertEqual(len(graph.vertices[str(i)].edges), len(vertices) - 1)
            
            # Verify paths exist between all pairs of vertices
            for j in range(len(vertices)):
                if i != j:
                    self.assertTrue(graph.find_path(vertices[i], vertices[j]))
    
    def test_large_graph(self):
        """Test creating and using a larger graph structure"""
        graph = Graph()
        
        # Create a larger number of vertices
        num_vertices = 20
        vertices = [Vertex(str(i)) for i in range(num_vertices)]
        
        # Add vertices to graph
        for vertex in vertices:
            graph.add_vertex(vertex)
            
        # Create a ring structure: each vertex connects to next vertex in sequence
        for i in range(num_vertices):
            next_idx = (i + 1) % num_vertices  # Wrap around to first vertex
            graph.add_edge(vertices[i], vertices[next_idx])
        
        # Verify structure
        for i in range(num_vertices):
            next_idx = (i + 1) % num_vertices
            
            # Each vertex should connect to exactly one other vertex
            self.assertEqual(len(graph.vertices[str(i)].edges), 2)  # In undirected graph, each vertex has 2 edges
            
            # Verify connection to next vertex
            self.assertIn(vertices[next_idx], graph.vertices[str(i)].edges)
            
            # Verify path exists to all other vertices (can traverse the ring)
            for j in range(num_vertices):
                if i != j:
                    self.assertTrue(graph.find_path(vertices[i], vertices[j]))


if __name__ == '__main__':
    unittest.main()