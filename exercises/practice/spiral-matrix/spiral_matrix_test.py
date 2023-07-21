# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/spiral-matrix/canonical-data.json
# File last updated on 2023-07-19

import unittest

from spiral_matrix import (
    spiral_matrix,
)


class SpiralMatrixTest(unittest.TestCase):
    def test_empty_spiral(self):
        self.assertEqual(spiral_matrix(0), [])

    def test_trivial_spiral(self):
        self.assertEqual(spiral_matrix(1), [[1]])

    def test_spiral_of_size_2(self):
        self.assertEqual(spiral_matrix(2), [[1, 2], [4, 3]])

    def test_spiral_of_size_3(self):
        self.assertEqual(spiral_matrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_spiral_of_size_4(self):
        self.assertEqual(
            spiral_matrix(4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        )

    def test_spiral_of_size_5(self):
        self.assertEqual(
            spiral_matrix(5),
            [
                [1, 2, 3, 4, 5],
                [16, 17, 18, 19, 6],
                [15, 24, 25, 20, 7],
                [14, 23, 22, 21, 8],
                [13, 12, 11, 10, 9],
            ],
        )
