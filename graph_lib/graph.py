from __future__ import annotations
from typing import List
import os

from graph_lib.edge import Edge
from graph_lib.vertex import Vertex


class Graph:

    def __init__(self, verticies: List[Vertex], edges: List[Edge]):
        """
        Constructs a Graph.

        :param vertecies: List of vertecies
        :param edges: List of edges
        """
        self.num_verticies = len(verticies)
        self.verticies = verticies
        self.edges = edges
        self.num_edges = len(edges)

        self._current_highest_vertex_id = self._calc_highest_id(verticies)
        self._current_highest_edge_id = self._calc_highest_id(edges)

    @classmethod
    def from_file(cls: Graph, file: str) -> Graph:
        """
        Constructs a graph from a file of the form:

        <number of vertecies>
        <vertecie a of edge 1> <vertecie b of edge 1>
        ...

        :param file: Path to the file (can either be a relative path from
                     the current cwd or an absolute one).
        :return: a Graph object.
        """
        if not os.path.isabs(file):
            file = f'{os.getcwd()}/{file}'

        vertecies: List = []
        edges: List[Edge] = []

        with open(file, 'r') as f:
            for i, line in enumerate(f):
                if i == 0:
                    num_verticies = int(line)
                    vertecies = [Vertex(x) for x in range(num_verticies)]
                    continue
                input_vertecies = line.split()
                edges.append(Edge(vertecies[int(input_vertecies[0])],
                                  vertecies[int(input_vertecies[1])],
                                  i-1))
        return cls(vertecies, edges)

    def insert_edge(self, edge: Edge) -> None:
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
                    edge_id: int = None) -> Edge:
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

        new_edge = Edge(vertex_a, vertex_b, edge_id)
        self.insert_edge(new_edge)
        return new_edge

    def get_edge_by_id(self, edge_id: int) -> Edge:
        """
        Gets a vertex from the graph by id.

        :param edge_id: The id to be searched.
        :return: The found vertex
        """
        for edge in self.edges:
            if edge.id == edge_id:
                return edge
        raise ValueError(f'{edge_id} does not exist in {self.edges}')

    def insert_vertex(self, vertex: Vertex) -> None:
        """
        Inserts a vertex into the graph.
        Performs health checks, e.g. no same vertex ids in a graph.

        :param vertex: The vertex to add.
        :return: None
        """

        for elem in self.verticies:
            if elem.id == vertex.id:
                raise ValueError(f'Vertex id already exists in the graph.')

        if vertex.id > self._current_highest_vertex_id:
            self._current_highest_vertex_id = vertex.id
        self.verticies.append(vertex)

    def create_vertex(self, contained_edges: List = None,
                      vertex_id: int = None) -> Vertex:
        """
        Creates a vertex and inserts it into the graph.
        If the vertex has edges assaigned to it they are
        also added to the graph.

        :param contained_edges: List of edges on the vertex.
                                Note: They will be added to the graph.
        :param vertex_id: A vertex id. If None one is automatically assigned.
                          Defaults to None.
        :return: Created Vertex
        """
        if vertex_id is None:
            vertex_id = self.get_free_vertex_id()

        if contained_edges is not None:
            for edge in contained_edges:
                self.insert_edge(edge)
            new_vertex = Vertex(vertex_id, contained_edges)
        else:
            new_vertex = Vertex(vertex_id)

        self.insert_vertex(new_vertex)
        return new_vertex

    def get_vertex_by_id(self, vertex_id: int) -> Vertex:
        """
        Gets a vertex from the graph by id.

        :param vertex_id: The id to be searched.
        :return: The found vertex
        """
        for vertex in self.verticies:
            if vertex.id == vertex_id:
                return vertex
        raise ValueError(f'{vertex_id} does not exist in {self.vertecies}')

    def get_free_edge_id(self) -> int:
        """
        Returns a free edge id and marks it as used.

        :return: A edge id.
        """
        self._current_highest_edge_id = self._current_highest_edge_id + 1
        return self._current_highest_edge_id

    def get_free_vertex_id(self) -> int:
        """
        Returns a free vertex id and marks it as used.

        :return: A vertex id.
        """
        self._current_highest_vertex_id = self._current_highest_vertex_id + 1
        return self._current_highest_vertex_id

    def _calc_highest_id(self, list: List) -> int:
        """
        Takes in list of elements with an id property
        and returns the highest one.

        :param list: The list to check
        :return: The highest id as int
        """
        highest = -1
        for elem in list:
            try:
                assert(isinstance(elem.id, int))
                highest = elem.id if elem.id > highest else highest
            except AttributeError:
                raise AttributeError(
                    f'Element {elem} needs to have an integer id property')
        return highest

    def __eq__(self, other: Graph) -> bool:
        """
        Comapres two graphs by edges, verticies and direction.

        :param other: The graph to compare to
        :return: Equality as boolean
        """
        if isinstance(other, self.__class__):
            if self.num_verticies != other.num_verticies:
                return False
            if len(self.edges) != len(other.edges):
                return False
            return (self.edges == other.edges
                    and self.verticies == other.verticies)
        return False

    def __str__(self) -> str:
        return f'Graph with {self.num_verticies}' \
            f' number of vertecies and edges {self.edges}'
