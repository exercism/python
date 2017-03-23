"""Tests for the series exercise

Implementation note:
The slices function should raise a ValueError with a meaningful error
message if its length argument doesn't fit the series.
"""
import unittest

from series import slices


class SeriesTest(unittest.TestCase):
    def test_slices_of_one(self):
        self.assertEqual(
            slices("01234", 1),
            [[0], [1], [2], [3], [4]], )

    def test_slices_of_two(self):
        self.assertEqual(
            slices("97867564", 2),
            [[9, 7], [7, 8], [8, 6], [6, 7], [7, 5], [5, 6], [6, 4]], )

    def test_slices_of_three(self):
        self.assertEqual(
            slices("97867564", 3),
            [[9, 7, 8], [7, 8, 6], [8, 6, 7], [6, 7, 5], [7, 5, 6], [5, 6, 4]],
        )

    def test_slices_of_four(self):
        self.assertEqual(
            slices("01234", 4),
            [[0, 1, 2, 3], [1, 2, 3, 4]], )

    def test_slices_of_five(self):
        self.assertEqual(
            slices("01234", 5),
            [[0, 1, 2, 3, 4]], )

    def test_overly_long_slice(self):
        with self.assertRaises(ValueError):
            slices("012", 4)

    def test_overly_short_slice(self):
        with self.assertRaises(ValueError):
            slices("01234", 0)


if __name__ == '__main__':
    unittest.main()
