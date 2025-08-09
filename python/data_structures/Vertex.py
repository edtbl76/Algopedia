"""
Vertex and Edge classes for graph data structure implementation.

A Vertex represents a node in a graph that can store any value and maintain
connections (edges) to other vertices.

Each edge has a target vertex and an
optional weight, enabling representation of both weighted and unweighted graphs.
"""

from dataclasses import dataclass
from typing import Optional, Any, Dict

@dataclass
class Edge:
    """
    Represents a directed edge from one vertex to another.

    An edge connects the current vertex to a target vertex with an optional
    weight value. This implementation supports weighted graphs where edges
    can have associated costs or distances.
    """
    target: 'Vertex'
    weight: int = 1
    #label: str = ''


class Vertex:
    """
    Represents a vertex (node) in a graph data structure.

    A vertex can store any value and maintains a dictionary of outgoing edges
    to other vertices. The edges are stored using the target vertex as the key,
    allowing for O(1) lookup, addition, and weight retrieval operations.
    """
    def __init__(self, value: Optional[Any]) -> None:
        """
        Initialize a new vertex with a given value.
        The edges dictionary is used to map outgoing edges to target vertices.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            value: The data value to store in this vertex. Can be any type or None.
        """
        self.value = value
        self.edges: Dict['Vertex', Edge] = {}

    def add_edge(self, vertex: 'Vertex', weight: int = 1) -> None:
        """
        Add an edge from this vertex to the target vertex.

        Time Complexity: O(1) - Dictionary insertion
        Space Complexity: O(1) - Single edge storage

        Args:
            vertex: The target vertex to connect to
            weight: The weight/cost of the edge (default: 1)
        """
        self.edges[vertex] = Edge(target=vertex, weight=weight)

    def get_edges(self) -> list['Vertex']:
        """
        Get a list of all vertices that this vertex has edges to.

        Time Complexity: O(n) where n is the number of outgoing edges
        Space Complexity: O(n) for the returned list

        Returns:
            A list of target vertices connected by outgoing edges
        """
        return list(self.edges.keys())

    def get_edge_weight(self, vertex: 'Vertex') -> Optional[int]:
        """
        Get the weight of the edge to a specific target vertex.

        Time Complexity: O(1) - Dictionary lookup
        Space Complexity: O(1)

        Args:
            vertex: The target vertex to check the edge weight for

        Returns:
            The weight of the edge to the target vertex, or None if no edge exists
        """
        edge = self.edges.get(vertex)
        return edge.weight if edge else None

