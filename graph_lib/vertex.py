from __future__ import annotations
from typing import List

from graph_lib.edge import Edge


class Vertex:

    def __init__(self, vertex_id: int, edges: List = []):
        """
        Constructs a Vertex.

        :param vertex_id: Vertex id.
        """

        self.id: int = vertex_id
        self.edges: List = edges
        self.num_edges: int = len(edges)

    def add_edge(self, edge: Edge) -> None:
        """
        Appends an edge to the vertex if it does not exist yet.

        :param edge: The edge to add.
        :return: None
        """
        if edge not in self.edges:
            self.edges.append(edge)
            self.num_edges = self.num_edges + 1

    def __eq__(self, other: Vertex) -> bool:
        """
        Compares two vertecies by id and edges.

        :param other: Vertex to compare against
        :return: Equality as boolean
        """
        if isinstance(other, self.__class__):
            return self.id == other.id and self.edges == other.edges
        return False

    def __str__(self) -> str:
        return f'Id {self.id} with {self.num_edges} edges: {self.edges}\n'
