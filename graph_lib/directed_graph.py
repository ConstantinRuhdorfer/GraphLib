from __future__ import annotations
from typing import List

import os

from graph_lib.graph import Graph
from graph_lib.directed_edge import DirectedEdge
from graph_lib.vertex import Vertex


class DirectedGraph(Graph):

    def __init__(self, verticies: List[Vertex], edges: List[DirectedEdge]):
        """
        Constructs a directed Graph.

        :param vertecies: List of vertecies
        :param edges: List of directed edges
        """
        super().__init__(verticies, edges)

    @classmethod
    def from_file(cls: DirectedGraph, file: str) -> Graph:
        """
        Constructs a directed graph from a file of the form:

        <number of vertecies>
        <vertecie a of edge 1> <vertecie b of edge 1>
        ...

        :param file: Path to the file (can either be a relative path from
                     the current cwd or an absolute one).
        :return: a directed Graph object.
        """
        if not os.path.isabs(file):
            file = f'{os.getcwd()}/{file}'

        vertecies: List = []
        edges: List[DirectedEdge] = []

        with open(file, 'r') as f:
            for i, line in enumerate(f):
                if i == 0:
                    num_verticies = int(line)
                    vertecies = [Vertex(x) for x in range(num_verticies)]
                    continue
                input_vertecies = line.split()
                edges.append(DirectedEdge(vertecies[int(input_vertecies[0])],
                                          vertecies[int(input_vertecies[1])],
                                          i-1))
        return cls(vertecies, edges)

    def insert_edge(self, edge: DirectedEdge) -> None:
        """
        Inserts a edge to the graph.
        If the vertecies do not already exist they are added to the graph.
        Performs health checks, e.g. no same vertex/edge ids.

        :param edge: The edge to add.
        :return: None
        """
        for elem in self.edges:
            if elem == edge:
                raise ValueError(f'Edge id already exists in the graph.')

        try:
            self.insert_vertex(edge.vertex_a)
        except ValueError:
            pass

        try:
            self.insert_vertex(edge.vertex_b)
        except ValueError:
            pass

        if edge.id > self._current_highest_edge_id:
            self._current_highest_edge_id = edge.id
        self.edges.append(edge)

    def create_edge(self, vertex_a: Vertex, vertex_b: Vertex,
                    edge_id: int = None) -> DirectedEdge:
        """
        Creates an edge and adds it to the graph.

        :param vertex_a: Vertex
        :param vertex_b: Vertex
        :param edge_id: A edge id. If None one is automatically assigned.
                        Defaults to None.
        :return: Created Edge
        """
        if edge_id is None:
            edge_id = self.get_free_edge_id()

        new_edge = DirectedEdge(vertex_a, vertex_b, edge_id)
        self.insert_edge(new_edge)
        return new_edge

    def get_edge_by_id(self, edge_id: int) -> DirectedEdge:
        """
        Gets a vertex from the graph by id.

        :param edge_id: The id to be searched.
        :return: The found vertex
        """
        for edge in self.edges:
            if edge.id == edge_id:
                return edge
        raise ValueError(f'{edge_id} does not exist in {self.edges}')

    def create_vertex(self, contained_edges: List[DirectedEdge] = None,
                      vertex_id: int = None) -> Vertex:
        """
        Creates a vertex and inserts it into the graph.
        If the vertex has edges assaigned to it they are
        also added to the graph.

        :param contained_edges: List of directed edges on the vertex.
                                Note: They will be added to the graph.
        :param vertex_id: A vertex id. If None one is automatically assigned.
                          Defaults to None.
        :return: Created Vertex
        """
        return super().create_vertex(contained_edges, vertex_id)

    def __str__(self) -> str:
        return f'Directed Graph with {self.num_verticies}' \
            f' number of vertecies and edges {self.edges}'
