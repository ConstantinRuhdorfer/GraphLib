from __future__ import annotations

from graph_lib.edge import Edge


class DirectedEdge(Edge):
    """
    The direction of the edge goes:

    DirectedEdge.vertex_a -> DirectedEdge.vertex_b.
    """

    def __eq__(self, other: DirectedEdge) -> bool:
        """
        Compares two edges by the ids of the vertecies.

        :param other: DirectedEdge to compare against
        :return: Equality as boolean
        """
        if isinstance(other, self.__class__):
            return (self.vertex_a == other.vertex_a
                    and self.vertex_b == other.vertex_b)

    def __str__(self) -> str:
        return f'Edge Id {self.id}: ' \
            f'{self.vertex_a.id} -> {self.vertex_b.id}\n'
