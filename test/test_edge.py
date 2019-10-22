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
        e = Edge(a, b, 0, False)
        self.assertTrue(e in a.edges,
                        f'{e} with {e.id} should be in the eges of a {a}:'
                        + f'\n {a.edges}')

    def test_get_partner_vertex(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e = Edge(a, b, 0, False)
        expected = a
        actual = e.get_partner_vertex(b)
        self.assertEqual(expected, actual)

    def test_is_part_true(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e = Edge(a, b, 0, False)
        self.assertTrue(e.is_part(a), f'{a} should be a part of {e}')

    def test_is_part_false(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        c = v.Vertex(2)
        e = Edge(a, b, 0, False)
        self.assertFalse(e.is_part(c), f'{c} should not be a part of {e}')

    def test_equal_fail_directed(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e1 = Edge(a, b, 0, False)
        e2 = Edge(a, b, 0, True)
        self.assertNotEqual(e1, e2)

    def test_equal(self):
        a = v.Vertex(1)
        b = v.Vertex(2)
        e1 = Edge(a, b, 0, False)
        e2 = Edge(a, b, 1, False)
        self.assertEqual(e1, e2)

    def tearDown(self) -> None:
        """
        Things to do on test suite completion.
        :return: None
        """
        pass
