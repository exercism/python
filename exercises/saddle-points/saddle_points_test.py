"""Tests for the saddle-points exercise

Implementation note:
The saddle_points function must validate the input matrix and raise a
ValueError with a meaningful error message if the matrix turns out to be
irregular.
"""
import unittest

from saddle_points import saddle_points


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class SaddlePointTest(unittest.TestCase):
    def test_one_saddle(self):
        inp = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        self.assertEqual(saddle_points(inp), set([(1, 0)]))

    def test_empty_matrix(self):
        self.assertEqual(saddle_points([]), set())

    def test_no_saddle(self):
        inp = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
        self.assertEqual(saddle_points(inp), set())

    def test_mult_saddle(self):
        inp = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
        ans = set([(0, 1), (1, 1), (2, 1)])
        self.assertEqual(saddle_points(inp), ans)

    def test_indentify_saddle_bottom_right_corner(self):
        inp = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
        ans = set([(2, 2)])
        self.assertEqual(saddle_points(inp), ans)

    # Additional tests for this track

    def test_irregular_matrix(self):
        inp = [[3, 2, 1], [0, 1], [2, 1, 0]]
        with self.assertRaises(ValueError):
            saddle_points(inp)


if __name__ == '__main__':
    unittest.main()
