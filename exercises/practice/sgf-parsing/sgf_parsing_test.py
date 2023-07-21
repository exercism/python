# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/sgf-parsing/canonical-data.json
# File last updated on 2023-07-19

import unittest

from sgf_parsing import (
    parse,
    SgfTree,
)


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

    def test_within_property_values_whitespace_characters_such_as_tab_are_converted_to_spaces(
        self,
    ):
        input_string = "(;A[hello\t\tworld])"
        expected = SgfTree(properties={"A": ["hello  world"]})
        self.assertEqual(parse(input_string), expected)

    def test_within_property_values_newlines_remain_as_newlines(self):
        input_string = "(;A[hello\n\nworld])"
        expected = SgfTree(properties={"A": ["hello\n\nworld"]})
        self.assertEqual(parse(input_string), expected)

    def test_escaped_closing_bracket_within_property_value_becomes_just_a_closing_bracket(
        self,
    ):
        input_string = "(;A[\\]])"
        expected = SgfTree(properties={"A": ["]"]})
        self.assertEqual(parse(input_string), expected)

    def test_escaped_backslash_in_property_value_becomes_just_a_backslash(self):
        input_string = "(;A[\\\\])"
        expected = SgfTree(properties={"A": ["\\"]})
        self.assertEqual(parse(input_string), expected)

    def test_opening_bracket_within_property_value_doesn_t_need_to_be_escaped(self):
        input_string = "(;A[x[y\\]z][foo]B[bar];C[baz])"
        expected = SgfTree(
            properties={"A": ["x[y]z", "foo"], "B": ["bar"]},
            children=[SgfTree({"C": ["baz"]})],
        )
        self.assertEqual(parse(input_string), expected)

    def test_semicolon_in_property_value_doesn_t_need_to_be_escaped(self):
        input_string = "(;A[a;b][foo]B[bar];C[baz])"
        expected = SgfTree(
            properties={"A": ["a;b", "foo"], "B": ["bar"]},
            children=[SgfTree({"C": ["baz"]})],
        )
        self.assertEqual(parse(input_string), expected)

    def test_parentheses_in_property_value_don_t_need_to_be_escaped(self):
        input_string = "(;A[x(y)z][foo]B[bar];C[baz])"
        expected = SgfTree(
            properties={"A": ["x(y)z", "foo"], "B": ["bar"]},
            children=[SgfTree({"C": ["baz"]})],
        )
        self.assertEqual(parse(input_string), expected)

    def test_escaped_tab_in_property_value_is_converted_to_space(self):
        input_string = "(;A[hello\\\tworld])"
        expected = SgfTree(properties={"A": ["hello world"]})
        self.assertEqual(parse(input_string), expected)

    def test_escaped_newline_in_property_value_is_converted_to_nothing_at_all(self):
        input_string = "(;A[hello\\\nworld])"
        expected = SgfTree(properties={"A": ["helloworld"]})
        self.assertEqual(parse(input_string), expected)

    def test_escaped_t_and_n_in_property_value_are_just_letters_not_whitespace(self):
        input_string = "(;A[\\t = t and \\n = n])"
        expected = SgfTree(properties={"A": ["t = t and n = n"]})
        self.assertEqual(parse(input_string), expected)

    def test_mixing_various_kinds_of_whitespace_and_escaped_characters_in_property_value(
        self,
    ):
        input_string = "(;A[\\]b\nc\\\nd\t\te\\\\ \\\n\\]])"
        expected = SgfTree(properties={"A": ["]b\ncd  e\\ ]"]})
        self.assertEqual(parse(input_string), expected)
