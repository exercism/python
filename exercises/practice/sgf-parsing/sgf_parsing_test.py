import unittest

from sgf_parsing import (
    parse,
    SgfTree,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class SgfParsingTest(unittest.TestCase):
    def test_empty_input(self):
        input_string = ""
        with self.assertRaises(ValueError) as err:
            parse(input_string)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "tree missing")

    def test_tree_with_no_nodes(self):
        input_string = "()"
        with self.assertRaises(ValueError) as err:
            parse(input_string)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "tree with no nodes")

    def test_node_without_tree(self):
        input_string = ";"
        with self.assertRaises(ValueError) as err:
            parse(input_string)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "tree missing")

    def test_node_without_properties(self):
        input_string = "(;)"
        expected = SgfTree()
        self.assertEqual(parse(input_string), expected)

    def test_single_node_tree(self):
        input_string = "(;A[B])"
        expected = SgfTree(properties={"A": ["B"]})
        self.assertEqual(parse(input_string), expected)

    def test_multiple_properties(self):
        input_string = "(;A[b]C[d])"
        expected = SgfTree(properties={"A": ["b"], "C": ["d"]})
        self.assertEqual(parse(input_string), expected)

    def test_properties_without_delimiter(self):
        input_string = "(;A)"
        with self.assertRaises(ValueError) as err:
            parse(input_string)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "properties without delimiter")

    def test_all_lowercase_property(self):
        input_string = "(;a[b])"
        with self.assertRaises(ValueError) as err:
            parse(input_string)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "property must be in uppercase")

    def test_upper_and_lowercase_property(self):
        input_string = "(;Aa[b])"
        with self.assertRaises(ValueError) as err:
            parse(input_string)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "property must be in uppercase")

    def test_two_nodes(self):
        input_string = "(;A[B];B[C])"
        expected = SgfTree(properties={"A": ["B"]}, children=[SgfTree({"B": ["C"]})])
        self.assertEqual(parse(input_string), expected)

    def test_two_child_trees(self):
        input_string = "(;A[B](;B[C])(;C[D]))"
        expected = SgfTree(
            properties={"A": ["B"]},
            children=[SgfTree({"B": ["C"]}), SgfTree({"C": ["D"]})],
        )
        self.assertEqual(parse(input_string), expected)

    def test_multiple_property_values(self):
        input_string = "(;A[b][c][d])"
        expected = SgfTree(properties={"A": ["b", "c", "d"]})
        self.assertEqual(parse(input_string), expected)

    def test_escaped_property(self):
        input_string = "(;A[\\]b\nc\nd\t\te \n\\]])"
        expected = SgfTree(properties={"A": ["]b\nc\nd  e \n]"]})
        self.assertEqual(parse(input_string), expected)
