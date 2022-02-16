import unittest

from flatten_array import (
    flatten,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class FlattenArrayTest(unittest.TestCase):
    def test_empty(self):
        inputs = []
        expected = []
        self.assertEqual(flatten(inputs), expected)

    def test_no_nesting(self):
        inputs = [0, 1, 2]
        expected = [0, 1, 2]
        self.assertEqual(flatten(inputs), expected)

    def test_flattens_a_nested_array(self):
        inputs = [[[]]]
        expected = []
        self.assertEqual(flatten(inputs), expected)

    def test_flattens_array_with_just_integers_present(self):
        inputs = [1, [2, 3, 4, 5, 6, 7], 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(inputs), expected)

    def test_5_level_nesting(self):
        inputs = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
        expected = [0, 2, 2, 3, 8, 100, 4, 50, -2]
        self.assertEqual(flatten(inputs), expected)

    def test_6_level_nesting(self):
        inputs = [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(inputs), expected)

    def test_null_values_are_omitted_from_the_final_result(self):
        inputs = [1, 2, None]
        expected = [1, 2]
        self.assertEqual(flatten(inputs), expected)

    def test_consecutive_null_values_at_the_front_of_the_list_are_omitted_from_the_final_result(
        self,
    ):
        inputs = [None, None, 3]
        expected = [3]
        self.assertEqual(flatten(inputs), expected)

    def test_consecutive_null_values_in_the_middle_of_the_list_are_omitted_from_the_final_result(
        self,
    ):
        inputs = [1, None, None, 4]
        expected = [1, 4]
        self.assertEqual(flatten(inputs), expected)

    def test_6_level_nest_list_with_null_values(self):
        inputs = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
        expected = [0, 2, 2, 3, 8, 100, -2]
        self.assertEqual(flatten(inputs), expected)

    def test_all_values_in_nested_list_are_null(self):
        inputs = [None, [[[None]]], None, None, [[None, None], None], None]
        expected = []
        self.assertEqual(flatten(inputs), expected)


if __name__ == "__main__":
    unittest.main()
