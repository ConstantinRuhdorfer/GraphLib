import unittest

import graph_lib.vertex as v
from graph_lib.edge import Edge


class TestEdge(unittest.TestCase):

    def setUp(self) -> None:
        """
        Setup constants for tests here.

        :return: None
        """
        pass

    def test_automatic_add_vertex_to_edge(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e = Edge(a, b, 0)
        self.assertTrue(e in a.edges,
                        f'{e} with {e.id} should be in the eges of a {a}:'
                        + f'\n {a.edges}')

    def test_get_partner_vertex(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e = Edge(a, b, 0)
        expected = a
        actual = e.get_partner_vertex(b)
        self.assertEqual(expected, actual)

    def test_is_part_true(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e = Edge(a, b, 0)
        self.assertTrue(e.is_part(a), f'{a} should be a part of {e}')

    def test_is_part_false(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        c = v.Vertex(2)
        e = Edge(a, b, 0)
        self.assertFalse(e.is_part(c), f'{c} should not be a part of {e}')

    def tearDown(self) -> None:
        """
        Things to do on test suite completion.
        :return: None
        """
        pass
