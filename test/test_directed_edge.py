import unittest

import graph_lib.vertex as v
from graph_lib.directed_edge import DirectedEdge


class TestDirectedEdge(unittest.TestCase):

    def setUp(self) -> None:
        """
        Setup constants for tests here.

        :return: None
        """
        pass

    def test_automatic_add_vertex_to_edge(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e = DirectedEdge(a, b, 0)
        self.assertTrue(e in a.edges,
                        f'{e} with {e.id} should be in the eges of a {a}:'
                        + f'\n {a.edges}')

    def test_equal_directed(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e1 = DirectedEdge(a, b, 0)
        e2 = DirectedEdge(a, b, 0)
        self.assertEqual(e1, e2)

    def test_equal_fail_directed(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e1 = DirectedEdge(a, b, 0)
        e2 = DirectedEdge(b, a, 0)
        self.assertNotEqual(e1, e2)

    def tearDown(self) -> None:
        """
        Things to do on test suite completion.
        :return: None
        """
        pass
