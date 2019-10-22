import unittest

from graph_lib.vertex import Vertex
import graph_lib.edge as e


class TestVertex(unittest.TestCase):

    def setUp(self) -> None:
        """
        Setup constants for tests here.

        :return: None
        """
        pass

    def test_add_edge(self) -> None:
        a = Vertex(2, [])
        b = Vertex(3, [])
        test_edge = e.Edge(a, b, 1, False)

        actual = Vertex(1, [])
        actual.add_edge(test_edge)
        expected = [test_edge]
        self.assertEqual(expected, actual.edges)

    def tearDown(self) -> None:
        """
        Things to do on test suite completion.
        :return: None
        """
        pass
