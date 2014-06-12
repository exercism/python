"""Tests for the series exercise

Implementation note:
The Series.slices method should raise a ValueError with a meaningful error
message if its argument isn't a valid slice length.
"""
import unittest

from series import Series


class SeriesTest(unittest.TestCase):
    def test_slices_of_one(self):
        self.assertEqual([[0], [1], [2], [3], [4]],
                         Series("01234").slices(1))

    def test_slices_of_two(self):
        self.assertEqual([[9, 7], [7, 8], [8, 6], [6, 7],
                          [7, 5], [5, 6], [6, 4]],
                         Series("97867564").slices(2))

    def test_slices_of_three(self):
        self.assertEqual([[9, 7, 8], [7, 8, 6], [8, 6, 7],
                          [6, 7, 5], [7, 5, 6], [5, 6, 4]],
                         Series("97867564").slices(3))

    def test_slices_of_four(self):
        self.assertEqual([[0, 1, 2, 3], [1, 2, 3, 4]],
                         Series("01234").slices(4))

    def test_slices_of_five(self):
        self.assertEqual([[0, 1, 2, 3, 4]],
                         Series("01234").slices(5))

    def test_overly_long_slice(self):
        self.assertRaises(ValueError, Series("012").slices, 4)

    def test_overly_short_slice(self):
        self.assertRaises(ValueError, Series("01234").slices, 0)


if __name__ == '__main__':
    unittest.main()
