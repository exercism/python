# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/binary-search/canonical-data.json
# File last updated on 2023-07-20

import unittest

from binary_search import (
    find,
)


class BinarySearchTest(unittest.TestCase):
    def test_finds_a_value_in_an_array_with_one_element(self):

        self.assertEqual(find([6], 6), 0)

    def test_finds_a_value_in_the_middle_of_an_array(self):

        self.assertEqual(find([1, 3, 4, 6, 8, 9, 11], 6), 3)

    def test_finds_a_value_at_the_beginning_of_an_array(self):

        self.assertEqual(find([1, 3, 4, 6, 8, 9, 11], 1), 0)

    def test_finds_a_value_at_the_end_of_an_array(self):

        self.assertEqual(find([1, 3, 4, 6, 8, 9, 11], 11), 6)

    def test_finds_a_value_in_an_array_of_odd_length(self):

        self.assertEqual(
            find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144), 9
        )

    def test_finds_a_value_in_an_array_of_even_length(self):

        self.assertEqual(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21), 5)

    def test_identifies_that_a_value_is_not_included_in_the_array(self):

        with self.assertRaises(ValueError) as err:
            find([1, 3, 4, 6, 8, 9, 11], 7)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "value not in array")

    def test_a_value_smaller_than_the_array_s_smallest_value_is_not_found(self):

        with self.assertRaises(ValueError) as err:
            find([1, 3, 4, 6, 8, 9, 11], 0)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "value not in array")

    def test_a_value_larger_than_the_array_s_largest_value_is_not_found(self):

        with self.assertRaises(ValueError) as err:
            find([1, 3, 4, 6, 8, 9, 11], 13)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "value not in array")

    def test_nothing_is_found_in_an_empty_array(self):

        with self.assertRaises(ValueError) as err:
            find([], 1)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "value not in array")

    def test_nothing_is_found_when_the_left_and_right_bounds_cross(self):

        with self.assertRaises(ValueError) as err:
            find([1, 2], 0)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "value not in array")
