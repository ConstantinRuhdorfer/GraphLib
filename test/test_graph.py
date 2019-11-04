import unittest

from graph_lib.graph import Graph
import graph_lib.vertex as v
import graph_lib.edge as e


class TestGraph(unittest.TestCase):

    def setUp(self) -> None:
        """
        Setup constants for tests here.

        :return: None
        """
        self.test_file_path_small = "input/graph1.plain"
        self.test_file_path_big = f'/Users/ruhdocon/dev' + \
            f'/python_graph/input/graph4.plain'

    def test_basic_constructor(self):
        a, b = v.Vertex(1), v.Vertex(2)
        test_vertecies = [a, b]
        test_edges = [e.Edge(a, b, 1)]
        g = Graph(test_vertecies, test_edges)
        actual = (g.num_edges == 1
                  and g.num_verticies == 2
                  and test_vertecies == g.verticies
                  and test_edges == g.edges)
        self.assertTrue(actual,
                        f'Failed: Graph: {g.num_edges} == Test: 1'
                        + f'and Graph: {g.num_verticies} == Test: 2'
                        + f'and Test: {test_vertecies} == Graph: {g.verticies}'
                        + f'and Test: {test_edges} == Graph: {g.edges}')

    def test_graph_constructor_from_file(self):
        g = Graph.from_file(self.test_file_path_small)
        actual_vertecies = [elem.id for elem in g.verticies]
        actual_edges = [elem.id for elem in g.edges]
        actual_vertecies_len, actual_edges_len = len(
            actual_edges), len(actual_vertecies)

        actual = (actual_vertecies == [0, 1, 2, 3, 4, 5, 6, 7, 8]
                  and actual_edges == [0, 1, 2, 3, 4, 5, 6, 7, 8]
                  and actual_vertecies_len == 9
                  and actual_edges_len == 9)

        self.assertTrue(actual,
                        f'Failed: Graph: {g.num_edges}==Test: 9'
                        + f'and Graph: {g.num_verticies}==Test: 9'
                        + f'and Test: {actual_vertecies}==Graph: {g.verticies}'
                        + f'and Test: {actual_edges}==Graph: {g.edges}')

    def test_parser_for_number_of_vertecies(self):
        g = Graph.from_file(self.test_file_path_small)
        self.assertEqual(g.num_verticies, 9)

    def test_equal(self):
        g1 = Graph.from_file(self.test_file_path_big)
        g2 = Graph.from_file(self.test_file_path_big)
        self.assertEqual(g1, g2)

    def test_get_neighbours(self):
        g1 = Graph.from_file(self.test_file_path_small)
        actual = [elem.id for elem in g1.get_neighbours(g1.verticies[0])]
        expected = [1, 2, 6]
        self.assertEqual(actual, expected)

    def test_get_vertex_by_id(self):
        g = Graph.from_file(self.test_file_path_small)
        actual = g.get_vertex_by_id(2)
        expected = v.Vertex(2)
        self.assertEqual(actual, expected)

    def test_insert_vertex(self):
        g = Graph.from_file(self.test_file_path_small)
        vertex_id = g.get_free_vertex_id()
        expected = v.Vertex(vertex_id)
        g.insert_vertex(expected)
        actual = g.get_vertex_by_id(vertex_id)
        self.assertEqual(actual, expected)

    def test_create_vertex(self):
        g = Graph.from_file(self.test_file_path_small)
        expected = g.create_vertex()
        actual = g.get_vertex_by_id(expected.id)
        self.assertEqual(actual, expected)

    def test_get_edge_by_id(self):
        g = Graph.from_file(self.test_file_path_small)
        actual = g.get_edge_by_id(0)
        expected = e.Edge(v.Vertex(0), v.Vertex(1), 0)
        self.assertEqual(actual, expected)

    def test_insert_edge(self):
        g = Graph.from_file(self.test_file_path_small)
        edge_id = g.get_free_edge_id()
        expected = e.Edge(v.Vertex(12), v.Vertex(0), edge_id)
        g.insert_edge(expected)
        actual = g.get_edge_by_id(edge_id)
        self.assertEqual(actual, expected)

    def test_create_edge(self):
        g = Graph.from_file(self.test_file_path_small)
        expected = g.create_edge(v.Vertex(12), v.Vertex(37))
        actual = g.get_edge_by_id(expected.id)
        self.assertEqual(actual, expected)

    def tearDown(self) -> None:
        """
        Things to do on test suite completion.
        :return: None
        """
        pass
