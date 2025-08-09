import unittest
from search.graph.graph_depth_first_search import GraphDepthFirstSearch, dfs
from data_structures.Graph import Graph
from data_structures.Vertex import Vertex


class TestGraphDepthFirstSearch(unittest.TestCase):
    """Test cases for graph depth-first search implementation."""

    def setUp(self):
        """Set up common test data."""
        # Empty graph
        self.empty_graph = Graph()

        # Single vertex graph
        self.single_vertex_graph = Graph()
        self.vertex1 = Vertex(1)
        self.single_vertex_graph.add_vertex(self.vertex1)

        # Simple directed graph
        #    1 --> 2 --> 4
        #    |     |
        #    v     v
        #    3 --> 5
        self.directed_graph = Graph(directed=True)
        self.v1 = Vertex(1)
        self.v2 = Vertex(2)
        self.v3 = Vertex(3)
        self.v4 = Vertex(4)
        self.v5 = Vertex(5)
        
        self.directed_graph.add_vertex(self.v1)
        self.directed_graph.add_vertex(self.v2)
        self.directed_graph.add_vertex(self.v3)
        self.directed_graph.add_vertex(self.v4)
        self.directed_graph.add_vertex(self.v5)
        
        self.directed_graph.add_edge(self.v1, self.v2)
        self.directed_graph.add_edge(self.v1, self.v3)
        self.directed_graph.add_edge(self.v2, self.v4)
        self.directed_graph.add_edge(self.v2, self.v5)
        self.directed_graph.add_edge(self.v3, self.v5)

        # Simple undirected graph
        #    1 --- 2 --- 4
        #    |     |
        #    |     |
        #    3 --- 5
        self.undirected_graph = Graph(directed=False)
        self.uv1 = Vertex(1)
        self.uv2 = Vertex(2)
        self.uv3 = Vertex(3)
        self.uv4 = Vertex(4)
        self.uv5 = Vertex(5)
        
        self.undirected_graph.add_vertex(self.uv1)
        self.undirected_graph.add_vertex(self.uv2)
        self.undirected_graph.add_vertex(self.uv3)
        self.undirected_graph.add_vertex(self.uv4)
        self.undirected_graph.add_vertex(self.uv5)
        
        self.undirected_graph.add_edge(self.uv1, self.uv2)
        self.undirected_graph.add_edge(self.uv1, self.uv3)
        self.undirected_graph.add_edge(self.uv2, self.uv4)
        self.undirected_graph.add_edge(self.uv2, self.uv5)
        self.undirected_graph.add_edge(self.uv3, self.uv5)

        # Graph with a cycle
        #    1 --> 2 --> 3
        #    ^           |
        #    |           v
        #    5 <-- 4 <-- 6
        self.cyclic_graph = Graph(directed=True)
        self.cv1 = Vertex(1)
        self.cv2 = Vertex(2)
        self.cv3 = Vertex(3)
        self.cv4 = Vertex(4)
        self.cv5 = Vertex(5)
        self.cv6 = Vertex(6)
        
        self.cyclic_graph.add_vertex(self.cv1)
        self.cyclic_graph.add_vertex(self.cv2)
        self.cyclic_graph.add_vertex(self.cv3)
        self.cyclic_graph.add_vertex(self.cv4)
        self.cyclic_graph.add_vertex(self.cv5)
        self.cyclic_graph.add_vertex(self.cv6)
        
        self.cyclic_graph.add_edge(self.cv1, self.cv2)
        self.cyclic_graph.add_edge(self.cv2, self.cv3)
        self.cyclic_graph.add_edge(self.cv3, self.cv6)
        self.cyclic_graph.add_edge(self.cv6, self.cv4)
        self.cyclic_graph.add_edge(self.cv4, self.cv5)
        self.cyclic_graph.add_edge(self.cv5, self.cv1)  # Creates a cycle

    def test_search_single_vertex(self):
        """Test search when the graph has only one vertex."""
        # Target is the only vertex
        result = GraphDepthFirstSearch.search(self.single_vertex_graph, self.vertex1, self.vertex1)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertIn(self.vertex1, result)

    def test_search_target_not_in_graph(self):
        """Test search when the target vertex is not in the graph."""
        # Create a vertex that's not in the graph
        non_existent_vertex = Vertex(99)
        result = GraphDepthFirstSearch.search(self.directed_graph, self.v1, non_existent_vertex)
        self.assertIsNone(result)

    def test_search_directed_graph(self):
        """Test search in a directed graph."""
        # Test finding a vertex that's directly connected
        result = GraphDepthFirstSearch.search(self.directed_graph, self.v1, self.v3)
        self.assertIsNotNone(result)
        self.assertIn(self.v1, result)
        self.assertIn(self.v3, result)
        
        # Test finding a vertex that requires traversing multiple edges
        result = GraphDepthFirstSearch.search(self.directed_graph, self.v1, self.v4)
        self.assertIsNotNone(result)
        self.assertIn(self.v1, result)
        self.assertIn(self.v2, result)
        self.assertIn(self.v4, result)
        
        # Test finding a vertex that can be reached through multiple paths
        result = GraphDepthFirstSearch.search(self.directed_graph, self.v1, self.v5)
        self.assertIsNotNone(result)
        self.assertIn(self.v1, result)
        self.assertIn(self.v5, result)
        # Note: We can't assert the exact path since DFS might take different paths

    def test_search_undirected_graph(self):
        """Test search in an undirected graph."""
        # Test finding a vertex that's directly connected
        result = GraphDepthFirstSearch.search(self.undirected_graph, self.uv1, self.uv3)
        self.assertIsNotNone(result)
        self.assertIn(self.uv1, result)
        self.assertIn(self.uv3, result)
        
        # Test finding a vertex that requires traversing multiple edges
        result = GraphDepthFirstSearch.search(self.undirected_graph, self.uv1, self.uv4)
        self.assertIsNotNone(result)
        self.assertIn(self.uv1, result)
        self.assertIn(self.uv4, result)
        
        # Test finding a vertex that can be reached through multiple paths
        result = GraphDepthFirstSearch.search(self.undirected_graph, self.uv1, self.uv5)
        self.assertIsNotNone(result)
        self.assertIn(self.uv1, result)
        self.assertIn(self.uv5, result)

    def test_search_cyclic_graph(self):
        """Test search in a graph with cycles."""
        # Test that cycle protection prevents infinite loops
        result = GraphDepthFirstSearch.search(self.cyclic_graph, self.cv1, self.cv4)
        self.assertIsNotNone(result)
        self.assertIn(self.cv1, result)
        self.assertIn(self.cv4, result)
        
        # Test finding a vertex that's part of the cycle
        result = GraphDepthFirstSearch.search(self.cyclic_graph, self.cv2, self.cv5)
        self.assertIsNotNone(result)
        self.assertIn(self.cv2, result)
        self.assertIn(self.cv5, result)

    def test_dfs_convenience_function(self):
        """Test the dfs convenience function."""
        # Test that dfs function returns the same result as GraphDepthFirstSearch.search
        class_result = GraphDepthFirstSearch.search(self.directed_graph, self.v1, self.v4)
        func_result = dfs(self.directed_graph, self.v1, self.v4)
        
        # Both should be not None
        self.assertIsNotNone(class_result)
        self.assertIsNotNone(func_result)
        
        # Both should contain the same vertices
        self.assertEqual(class_result, func_result)


if __name__ == '__main__':
    unittest.main()