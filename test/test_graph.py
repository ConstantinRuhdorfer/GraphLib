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
        test_edges = [e.Edge(a, b, 1, False)]
        g = Graph(test_vertecies, test_edges, False)
        actual = (g.num_edges == 1
                  and g.num_verticies == 2
                  and test_vertecies == g.verticies
                  and test_edges == g.edges)
        self.assertTrue(actual,
                        f'Failed: Graph: {g.num_edges} == Test: 1'
                        + f'and Graph: {g.num_verticies} == Test: 2'
                        + f'and Test: {test_vertecies} == Graph: {g.verticies}'
                        + f'and Test: {test_edges} == Graph: {g.edges}')

    def test_parser_for_number_of_vertecies(self):
        g = Graph.from_file(self.test_file_path_small, False)
        self.assertEqual(g.num_verticies, 9)

    def test_for_fail_on_different_directed(self):
        a, b = v.Vertex(1), v.Vertex(2)
        test_vertecies = [a, b]
        test_edges = [e.Edge(a, b, 1, False)]
        self.assertRaises(ValueError, lambda: Graph(
            test_vertecies, test_edges, True))

    def test_equal(self):
        g1 = Graph.from_file(self.test_file_path_big, False)
        g2 = Graph.from_file(self.test_file_path_big, False)
        self.assertEqual(g1, g2)

    def tearDown(self) -> None:
        """
        Things to do on test suite completion.
        :return: None
        """
        pass
