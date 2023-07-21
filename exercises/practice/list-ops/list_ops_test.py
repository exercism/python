# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/list-ops/canonical-data.json
# File last updated on 2023-07-19

import unittest

from list_ops import (
    append,
    concat,
    foldl,
    foldr,
    length,
    reverse,
    filter as list_ops_filter,
    map as list_ops_map,
)


class ListOpsTest(unittest.TestCase):
    def test_append_empty_lists(self):
        self.assertEqual(append([], []), [])

    def test_append_list_to_empty_list(self):
        self.assertEqual(append([], [1, 2, 3, 4]), [1, 2, 3, 4])

    def test_append_empty_list_to_list(self):
        self.assertEqual(append([1, 2, 3, 4], []), [1, 2, 3, 4])

    def test_append_non_empty_lists(self):
        self.assertEqual(append([1, 2], [2, 3, 4, 5]), [1, 2, 2, 3, 4, 5])

    def test_concat_empty_list(self):
        self.assertEqual(concat([]), [])

    def test_concat_list_of_lists(self):
        self.assertEqual(concat([[1, 2], [3], [], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_concat_list_of_nested_lists(self):
        self.assertEqual(
            concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]),
            [[1], [2], [3], [], [4, 5, 6]],
        )

    def test_filter_empty_list(self):
        self.assertEqual(list_ops_filter(lambda x: x % 2 == 1, []), [])

    def test_filter_non_empty_list(self):
        self.assertEqual(list_ops_filter(lambda x: x % 2 == 1, [1, 2, 3, 5]), [1, 3, 5])

    def test_length_empty_list(self):
        self.assertEqual(length([]), 0)

    def test_length_non_empty_list(self):
        self.assertEqual(length([1, 2, 3, 4]), 4)

    def test_map_empty_list(self):
        self.assertEqual(list_ops_map(lambda x: x + 1, []), [])

    def test_map_non_empty_list(self):
        self.assertEqual(list_ops_map(lambda x: x + 1, [1, 3, 5, 7]), [2, 4, 6, 8])

    def test_foldl_empty_list(self):
        self.assertEqual(foldl(lambda acc, el: el * acc, [], 2), 2)

    def test_foldl_direction_independent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5), 15)

    def test_foldl_direction_dependent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldl(lambda acc, el: el / acc, [1, 2, 3, 4], 24), 64)

    def test_foldr_empty_list(self):
        self.assertEqual(foldr(lambda acc, el: el * acc, [], 2), 2)

    def test_foldr_direction_independent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldr(lambda acc, el: el + acc, [1, 2, 3, 4], 5), 15)

    def test_foldr_direction_dependent_function_applied_to_non_empty_list(self):
        self.assertEqual(foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24), 9)

    def test_reverse_empty_list(self):
        self.assertEqual(reverse([]), [])

    def test_reverse_non_empty_list(self):
        self.assertEqual(reverse([1, 3, 5, 7]), [7, 5, 3, 1])

    def test_reverse_list_of_lists_is_not_flattened(self):
        self.assertEqual(
            reverse([[1, 2], [3], [], [4, 5, 6]]), [[4, 5, 6], [], [3], [1, 2]]
        )

    # Additional tests for this track

    def test_foldr_foldr_add_string(self):
        self.assertEqual(
            foldr(
                lambda acc, el: el + acc, ["e", "x", "e", "r", "c", "i", "s", "m"], "!"
            ),
            "exercism!",
        )

    def test_reverse_reverse_mixed_types(self):
        self.assertEqual(reverse(["xyz", 4.0, "cat", 1]), [1, "cat", 4.0, "xyz"])
