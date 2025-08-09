import unittest
from data_structures.Vertex import Vertex, Edge


class TestEdge(unittest.TestCase):
    """
    Test cases for the Edge class implementation.
    
    These tests verify the functionality of the Edge class including:
    - Initialization with default and custom weights
    - Target reference integrity
    """
    
    def test_edge_initialization(self):
        """Test initialization of an Edge with default weight"""
        vertex = Vertex("target")
        edge = Edge(target=vertex)
        
        self.assertEqual(edge.target, vertex)
        self.assertEqual(edge.weight, 1)  # Default weight
    
    def test_edge_initialization_with_weight(self):
        """Test initialization of an Edge with custom weight"""
        vertex = Vertex("target")
        edge = Edge(target=vertex, weight=10)
        
        self.assertEqual(edge.target, vertex)
        self.assertEqual(edge.weight, 10)
    
    def test_edge_with_zero_weight(self):
        """Test initialization of an Edge with zero weight"""
        vertex = Vertex("target")
        edge = Edge(target=vertex, weight=0)
        
        self.assertEqual(edge.target, vertex)
        self.assertEqual(edge.weight, 0)
    
    def test_edge_with_negative_weight(self):
        """Test initialization of an Edge with negative weight"""
        vertex = Vertex("target")
        edge = Edge(target=vertex, weight=-5)
        
        self.assertEqual(edge.target, vertex)
        self.assertEqual(edge.weight, -5)


class TestVertex(unittest.TestCase):
    """
    Test cases for the Vertex class implementation.
    
    These tests verify the functionality of the Vertex class including:
    - Initialization
    - Adding edges
    - Getting edges
    - Getting edge weights
    - Edge cases
    """

    def test_initialization(self):
        """Test initialization of a Vertex with different value types"""
        # Test with integer value
        vertex_int = Vertex(42)
        self.assertEqual(vertex_int.value, 42)
        self.assertEqual(vertex_int.edges, {})
        
        # Test with string value
        vertex_str = Vertex("test")
        self.assertEqual(vertex_str.value, "test")
        self.assertEqual(vertex_str.edges, {})
        
        # Test with None value
        vertex_none = Vertex(None)
        self.assertIsNone(vertex_none.value)
        self.assertEqual(vertex_none.edges, {})

    def test_add_edge(self):
        """Test adding an edge to a vertex"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add edge with default weight
        vertex1.add_edge(vertex2)
        
        # Verify edge was added
        self.assertIn(vertex2, vertex1.edges)
        self.assertEqual(vertex1.edges[vertex2].target, vertex2)
        self.assertEqual(vertex1.edges[vertex2].weight, 1)
        
        # Verify no edge was added in the opposite direction (not bidirectional)
        self.assertNotIn(vertex1, vertex2.edges)

    def test_add_edge_with_weight(self):
        """Test adding an edge with a custom weight"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add edge with custom weight
        vertex1.add_edge(vertex2, weight=5)
        
        # Verify edge was added with correct weight
        self.assertIn(vertex2, vertex1.edges)
        self.assertEqual(vertex1.edges[vertex2].target, vertex2)
        self.assertEqual(vertex1.edges[vertex2].weight, 5)

    def test_add_multiple_edges(self):
        """Test adding multiple edges from a single vertex"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        vertex4 = Vertex("D")
        
        # Add multiple edges with different weights
        vertex1.add_edge(vertex2, weight=2)
        vertex1.add_edge(vertex3, weight=3)
        vertex1.add_edge(vertex4, weight=4)
        
        # Verify all edges were added correctly
        self.assertEqual(len(vertex1.edges), 3)
        self.assertEqual(vertex1.edges[vertex2].weight, 2)
        self.assertEqual(vertex1.edges[vertex3].weight, 3)
        self.assertEqual(vertex1.edges[vertex4].weight, 4)

    def test_add_edge_to_self(self):
        """Test adding an edge from a vertex to itself (self-loop)"""
        vertex = Vertex("A")
        
        # Add self-loop
        vertex.add_edge(vertex, weight=10)
        
        # Verify self-loop was added
        self.assertIn(vertex, vertex.edges)
        self.assertEqual(vertex.edges[vertex].target, vertex)
        self.assertEqual(vertex.edges[vertex].weight, 10)

    def test_overwrite_edge(self):
        """Test overwriting an existing edge"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add edge with initial weight
        vertex1.add_edge(vertex2, weight=5)
        self.assertEqual(vertex1.edges[vertex2].weight, 5)
        
        # Overwrite with new weight
        vertex1.add_edge(vertex2, weight=10)
        self.assertEqual(vertex1.edges[vertex2].weight, 10)

    def test_get_edges(self):
        """Test getting all edges from a vertex"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        
        # Add edges
        vertex1.add_edge(vertex2)
        vertex1.add_edge(vertex3)
        
        # Get edges
        edges = vertex1.get_edges()
        
        # Verify edges list
        self.assertEqual(len(edges), 2)
        self.assertIn(vertex2, edges)
        self.assertIn(vertex3, edges)

    def test_get_edges_empty(self):
        """Test getting edges from a vertex with no edges"""
        vertex = Vertex("A")
        
        # Get edges from vertex with no edges
        edges = vertex.get_edges()
        
        # Verify empty list
        self.assertEqual(edges, [])

    def test_get_edge_weight(self):
        """Test getting the weight of an edge"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Add edge with weight
        vertex1.add_edge(vertex2, weight=7)
        
        # Get edge weight
        weight = vertex1.get_edge_weight(vertex2)
        
        # Verify weight
        self.assertEqual(weight, 7)

    def test_get_edge_weight_nonexistent(self):
        """Test getting the weight of a nonexistent edge"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        
        # Get weight of nonexistent edge
        weight = vertex1.get_edge_weight(vertex2)
        
        # Verify None is returned
        self.assertIsNone(weight)
        
    def test_complex_vertex_values(self):
        """Test vertices with complex values like lists, dicts, and objects"""
        # List value
        list_value = [1, 2, 3]
        vertex_list = Vertex(list_value)
        self.assertEqual(vertex_list.value, list_value)
        
        # Dictionary value
        dict_value = {"key": "value", "number": 42}
        vertex_dict = Vertex(dict_value)
        self.assertEqual(vertex_dict.value, dict_value)
        
        # Object value
        class TestObject:
            def __init__(self, name):
                self.name = name
                
        obj = TestObject("test_object")
        vertex_obj = Vertex(obj)
        self.assertEqual(vertex_obj.value, obj)
        self.assertEqual(vertex_obj.value.name, "test_object")
        
    def test_edge_with_complex_vertex(self):
        """Test adding edges between vertices with complex values"""
        vertex1 = Vertex([1, 2, 3])
        vertex2 = Vertex({"name": "vertex2"})
        
        # Add edge
        vertex1.add_edge(vertex2, weight=5)
        
        # Verify edge
        self.assertIn(vertex2, vertex1.edges)
        self.assertEqual(vertex1.edges[vertex2].weight, 5)
        self.assertEqual(vertex1.edges[vertex2].target.value, {"name": "vertex2"})
        
    def test_multiple_edges_with_different_weights(self):
        """Test adding multiple edges with different weights including zero and negative"""
        vertex1 = Vertex("A")
        vertex2 = Vertex("B")
        vertex3 = Vertex("C")
        vertex4 = Vertex("D")
        
        # Add edges with various weights
        vertex1.add_edge(vertex2, weight=0)  # Zero weight
        vertex1.add_edge(vertex3, weight=-3)  # Negative weight
        vertex1.add_edge(vertex4, weight=5)  # Positive weight
        
        # Verify edges
        self.assertEqual(vertex1.get_edge_weight(vertex2), 0)
        self.assertEqual(vertex1.get_edge_weight(vertex3), -3)
        self.assertEqual(vertex1.get_edge_weight(vertex4), 5)


if __name__ == '__main__':
    unittest.main()