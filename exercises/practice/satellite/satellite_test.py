# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/satellite/canonical-data.json
# File last updated on 2025-12-30

import unittest

from satellite import (
    tree_from_traversals,
)


class SatelliteTest(unittest.TestCase):
    def test_empty_tree(self):
        preorder = []
        inorder = []

        expected = {}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_one_item(self):
        preorder = ["a"]
        inorder = ["a"]

        expected = {"v": "a", "l": {}, "r": {}}
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_many_items(self):
        preorder = ["a", "i", "x", "f", "r"]
        inorder = ["i", "a", "f", "x", "r"]

        expected = {
            "v": "a",
            "l": {"v": "i", "l": {}, "r": {}},
            "r": {
                "v": "x",
                "l": {"v": "f", "l": {}, "r": {}},
                "r": {"v": "r", "l": {}, "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_reject_traversals_of_different_length(self):
        preorder = ["a", "b"]
        inorder = ["b", "a", "r"]

        with self.assertRaises(ValueError) as err:
            tree_from_traversals(preorder, inorder)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "traversals must have the same length")

    def test_reject_inconsistent_traversals_of_same_length(self):
        preorder = ["x", "y", "z"]
        inorder = ["a", "b", "c"]

        with self.assertRaises(ValueError) as err:
            tree_from_traversals(preorder, inorder)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "traversals must have the same elements"
        )

    def test_reject_traversals_with_repeated_items(self):
        preorder = ["a", "b", "a"]
        inorder = ["b", "a", "a"]

        with self.assertRaises(ValueError) as err:
            tree_from_traversals(preorder, inorder)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "traversals must contain unique items")

    def test_a_degenerate_binary_tree(self):
        preorder = ["a", "b", "c", "d"]
        inorder = ["d", "c", "b", "a"]

        expected = {
            "v": "a",
            "l": {
                "v": "b",
                "l": {"v": "c", "l": {"v": "d", "l": {}, "r": {}}, "r": {}},
                "r": {},
            },
            "r": {},
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_another_degenerate_binary_tree(self):
        preorder = ["a", "b", "c", "d"]
        inorder = ["a", "b", "c", "d"]

        expected = {
            "v": "a",
            "l": {},
            "r": {
                "v": "b",
                "l": {},
                "r": {"v": "c", "l": {}, "r": {"v": "d", "l": {}, "r": {}}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)

    def test_tree_with_many_more_items(self):
        preorder = ["a", "b", "d", "g", "h", "c", "e", "f", "i"]
        inorder = ["g", "d", "h", "b", "a", "e", "c", "i", "f"]

        expected = {
            "v": "a",
            "l": {
                "v": "b",
                "l": {
                    "v": "d",
                    "l": {"v": "g", "l": {}, "r": {}},
                    "r": {"v": "h", "l": {}, "r": {}},
                },
                "r": {},
            },
            "r": {
                "v": "c",
                "l": {"v": "e", "l": {}, "r": {}},
                "r": {"v": "f", "l": {"v": "i", "l": {}, "r": {}}, "r": {}},
            },
        }
        self.assertEqual(tree_from_traversals(preorder, inorder), expected)
