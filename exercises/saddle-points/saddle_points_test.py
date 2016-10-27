"""Tests for the saddle-points exercise

Implementation note:
The saddle_points function must validate the input matrix and raise a
ValueError with a meaningful error message if the matrix turns out to be
irregular.
"""
import unittest

from saddle_points import saddle_points


class SaddlePointTest(unittest.TestCase):
    def test_one_saddle(self):
        inp = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        self.assertEqual(set([(1, 0)]), saddle_points(inp))

    def test_no_saddle(self):
        self.assertEqual(set(), saddle_points([[2, 1], [1, 2]]))

    def test_mult_saddle(self):
        inp = [[5, 3, 5, 4], [6, 4, 7, 3], [5, 1, 5, 3]]
        ans = set([(0, 0), (0, 2), (2, 0), (2, 2)])
        self.assertEqual(ans, saddle_points(inp))

    def test_empty_matrix(self):
        self.assertEqual(set(), saddle_points([]))

    def test_irregular_matrix(self):
        inp = [[3, 2, 1], [0, 1], [2, 1, 0]]
        self.assertRaises(ValueError, saddle_points, inp)


if __name__ == '__main__':
    unittest.main()
