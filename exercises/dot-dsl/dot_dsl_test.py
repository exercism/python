import unittest

from dot_dsl import Graph, Node, Edge, NODE, EDGE, ATTR


class DotDslTest(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()

        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_node(self):
        g = Graph([
            (NODE, "a", {})
        ])

        self.assertEqual(g.nodes, [Node("a")])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_node_with_keywords(self):
        g = Graph([
            (NODE, "a", {"color": "green"})
        ])

        self.assertEqual(g.nodes, [Node("a", {"color": "green"})])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_edge(self):
        g = Graph([
            (EDGE, "a", "b", {})
        ])

        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [Edge("a", "b", {})])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_attribute(self):
        g = Graph([
            (ATTR, "foo", "1")
        ])

        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {"foo": "1"})

    def test_graph_with_attributes(self):
        g = Graph([
            (ATTR, "foo", "1"),
            (ATTR, "title", "Testing Attrs"),
            (NODE, "a", {"color": "green"}),
            (NODE, "c", {}),
            (NODE, "b", {"label", "Beta!"}),
            (EDGE, "b", "c", {}),
            (EDGE, "a", "b", {"color": "blue"}),
            (ATTR, "bar", "true")
        ])

        self.assertEqual(g.nodes, [Node("a", {"color": "green"}),
                                   Node("c", {}),
                                   Node("b", {"label", "Beta!"})])
        self.assertEqual(g.edges, [Edge("b", "c", {}),
                                   Edge("a", "b", {"color": "blue"})])
        self.assertEqual(g.attrs, {
            "foo": "1",
            "title": "Testing Attrs",
            "bar": "true"
        })


if __name__ == '__main__':
    unittest.main()
