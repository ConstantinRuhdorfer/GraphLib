from __future__ import annotations
from typing import List
import os

from graph_lib.edge import Edge
from graph_lib.vertex import Vertex


class Graph:

    def __init__(self, verticies: List, edges: List, directed: bool = False):
        """
        Constructs a Graph.

        :param vertecies: List of vertecies
        :param edges: List of edges
        :param directed: Wether the graph is directed. Defaults to False.
        """

        self.num_verticies = len(verticies)
        self.verticies = verticies
        self.edges = edges
        self.num_edges = len(edges)
        self.directed = directed

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
                                  vertecies[int(input_vertecies[1])], i))

        return cls(vertecies, edges)

    def __eq__(self, other: Graph) -> bool:
        """
        Comapres two graphs by edges and verticies.

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
        return f'Graph with {self.num_verticies} number of vertecies'
        + f'and edges {self.edges}'
