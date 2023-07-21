# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pascals-triangle/canonical-data.json
# File last updated on 2023-07-19

import sys
import unittest

from pascals_triangle import (
    rows,
)

TRIANGLE = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
]


class PascalsTriangleTest(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(rows(0), TRIANGLE[:0])

    def test_single_row(self):
        self.assertEqual(rows(1), TRIANGLE[:1])

    def test_two_rows(self):
        self.assertEqual(rows(2), TRIANGLE[:2])

    def test_three_rows(self):
        self.assertEqual(rows(3), TRIANGLE[:3])

    def test_four_rows(self):
        self.assertEqual(rows(4), TRIANGLE[:4])

    def test_five_rows(self):
        self.assertEqual(rows(5), TRIANGLE[:5])

    def test_six_rows(self):
        self.assertEqual(rows(6), TRIANGLE[:6])

    def test_ten_rows(self):
        self.assertEqual(rows(10), TRIANGLE[:10])

    # Additional tests for this track
    def test_negative_rows_are_invalid(self):
        with self.assertRaises(ValueError) as err:
            rows(-1)
            self.assertEqual(type(err.exception), ValueError)
            self.assertEqual(err.exception.args[0], "number of rows is negative")

    def test_solution_is_recursive(self):
        with self.assertRaises(RecursionError) as err:
            rows(sys.getrecursionlimit() + 10)
            self.assertEqual(type(err.exception), RecursionError)
            self.assertEqual(
                err.exception.args[0][:32], "maximum recursion depth exceeded"
            )
