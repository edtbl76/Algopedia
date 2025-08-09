import unittest
from search.graph.graph_breadth_first_search import bfs
from data_structures.Graph import Graph
from data_structures.Vertex import Vertex


class TestGraphBreadthFirstSearch(unittest.TestCase):
    """Test cases for graph breadth-first search implementation."""

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

        # Graph for testing shortest path property of BFS
        #    1 --- 2 --- 5
        #    |           |
        #    |           |
        #    3 --- 4 --- 6
        self.path_graph = Graph(directed=False)
        self.pv1 = Vertex(1)
        self.pv2 = Vertex(2)
        self.pv3 = Vertex(3)
        self.pv4 = Vertex(4)
        self.pv5 = Vertex(5)
        self.pv6 = Vertex(6)
        
        self.path_graph.add_vertex(self.pv1)
        self.path_graph.add_vertex(self.pv2)
        self.path_graph.add_vertex(self.pv3)
        self.path_graph.add_vertex(self.pv4)
        self.path_graph.add_vertex(self.pv5)
        self.path_graph.add_vertex(self.pv6)
        
        self.path_graph.add_edge(self.pv1, self.pv2)
        self.path_graph.add_edge(self.pv1, self.pv3)
        self.path_graph.add_edge(self.pv2, self.pv5)
        self.path_graph.add_edge(self.pv3, self.pv4)
        self.path_graph.add_edge(self.pv4, self.pv6)
        self.path_graph.add_edge(self.pv5, self.pv6)

    def test_bfs_single_vertex(self):
        """Test BFS when the graph has only one vertex."""
        # Target is the only vertex
        path = bfs(self.single_vertex_graph, self.vertex1, self.vertex1)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 1)
        self.assertEqual(path[0], self.vertex1)

    def test_bfs_target_not_in_graph(self):
        """Test BFS when the target vertex is not in the graph."""
        # Create a vertex that's not in the graph
        non_existent_vertex = Vertex(99)
        path = bfs(self.directed_graph, self.v1, non_existent_vertex)
        self.assertIsNone(path)

    def test_bfs_directed_graph(self):
        """Test BFS in a directed graph."""
        # Test finding a vertex that's directly connected
        path = bfs(self.directed_graph, self.v1, self.v3)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 2)
        self.assertEqual(path[0], self.v1)
        self.assertEqual(path[1], self.v3)
        
        # Test finding a vertex that requires traversing multiple edges
        path = bfs(self.directed_graph, self.v1, self.v4)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0], self.v1)
        self.assertEqual(path[1], self.v2)
        self.assertEqual(path[2], self.v4)
        
        # Test finding a vertex that can be reached through multiple paths
        path = bfs(self.directed_graph, self.v1, self.v5)
        self.assertIsNotNone(path)
        # BFS should find the shortest path, which is either through v2 or v3
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0], self.v1)
        # The second vertex could be either v2 or v3 depending on the order of exploration
        self.assertTrue(path[1] in [self.v2, self.v3])
        self.assertEqual(path[2], self.v5)

    def test_bfs_undirected_graph(self):
        """Test BFS in an undirected graph."""
        # Test finding a vertex that's directly connected
        path = bfs(self.undirected_graph, self.uv1, self.uv3)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 2)
        self.assertEqual(path[0], self.uv1)
        self.assertEqual(path[1], self.uv3)
        
        # Test finding a vertex that requires traversing multiple edges
        path = bfs(self.undirected_graph, self.uv1, self.uv4)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0], self.uv1)
        self.assertEqual(path[1], self.uv2)
        self.assertEqual(path[2], self.uv4)
        
        # Test finding a vertex that can be reached through multiple paths
        path = bfs(self.undirected_graph, self.uv1, self.uv5)
        self.assertIsNotNone(path)
        # BFS should find the shortest path, which is either through uv2 or uv3
        self.assertEqual(len(path), 3)
        self.assertEqual(path[0], self.uv1)
        # The second vertex could be either uv2 or uv3 depending on the order of exploration
        self.assertTrue(path[1] in [self.uv2, self.uv3])
        self.assertEqual(path[2], self.uv5)

    def test_bfs_cyclic_graph(self):
        """Test BFS in a graph with cycles."""
        # Test that cycle protection prevents infinite loops
        path = bfs(self.cyclic_graph, self.cv1, self.cv4)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], self.cv1)
        self.assertEqual(path[-1], self.cv4)
        
        # Test finding a vertex that's part of the cycle
        path = bfs(self.cyclic_graph, self.cv2, self.cv5)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], self.cv2)
        self.assertEqual(path[-1], self.cv5)

    def test_bfs_shortest_path(self):
        """Test that BFS finds the shortest path in terms of number of edges."""
        # From pv1 to pv6, there are two paths:
        # 1. pv1 -> pv2 -> pv5 -> pv6 (3 edges)
        # 2. pv1 -> pv3 -> pv4 -> pv6 (3 edges)
        # Both are shortest paths with 3 edges
        path = bfs(self.path_graph, self.pv1, self.pv6)
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 4)  # 4 vertices = 3 edges
        self.assertEqual(path[0], self.pv1)
        self.assertEqual(path[-1], self.pv6)
        
        # The middle vertices should form one of the two possible shortest paths
        if path[1] == self.pv2:
            self.assertEqual(path[2], self.pv5)
        else:
            self.assertEqual(path[1], self.pv3)
            self.assertEqual(path[2], self.pv4)


if __name__ == '__main__':
    unittest.main()