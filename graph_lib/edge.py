from __future__ import annotations

import graph_lib.vertex as v


class Edge:

    def __init__(self, a: v.Vertex, b: v.Vertex, edge_id: int):
        """
        Constructs a edge.

        :param a: Vertex
        :param b: Vertex
        """

        self.vertex_a = a
        self.vertex_b = b
        self.id = edge_id

        a.add_edge(self)
        b.add_edge(self)

    def get_partner_vertex(self, given: v.Vertex) -> v.Vertex:
        """
        For a edge x <-> y returns the partner to the given vertex,
        e.g. given x returns y.

        :param given: Vertex
        :return: Vertex
        """

        if self.vertex_a == given:
            return self.vertex_b
        elif self.vertex_b == given:
            return self.vertex_a
        else:
            raise ValueError(
                f'Given: {given}'
                + f'is not in {self.vertex_a} <-> {self.vertex_b}')

    def is_part(self, vertex: v.Vertex) -> bool:
        """
        Checks wether the vertex is part of the edge.

        :param vertex: Vertex to check.
        :return: Bool
        """
        return vertex is self.vertex_a or vertex is self.vertex_b

    def __eq__(self, other: Edge) -> bool:
        """
        Compares two edges by the ids of the vertecies.

        :param other: Edge to compare against
        :return: Equality as boolean
        """
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False

    def __str__(self) -> str:
        return f'Id {self.id}: {self.vertex_a.id} <-> {self.vertex_b.id}\n'
