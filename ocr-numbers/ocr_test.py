"""Tests for the ocr-numbers exercise

Implementation note:
Both ocr.grid and ocr.number should validate their input
and raise ValueErrors with meaningful error messages
if necessary.
"""

import os
import unittest

from ocr import grid, number


ZERO = [
    " _ ",
    "| |",
    "|_|",
    "   "
]

ONE = [
    "   ",
    "  |",
    "  |",
    "   "
]

class OcrTest(unittest.TestCase):

    def test_0(self):
        self.assertEqual('0', number(ZERO))

    def test_1(self):
        self.assertEqual('1', number(ONE))

    def test_garbage(self):
        self.assertEqual('?', number([" _ ",
                                      " _|",
                                      "  |",
                                      "   "]))

    def test_last_line_nonblank(self):
        self.assertEqual('?', number(["   ",
                                      "  |",
                                      "  |",
                                      "| |"]))

    def test_unknown_char(self):
        self.assertEqual('?', number([" - ",
                                      " _|",
                                      " X|",
                                      "   "]))

    def test_too_short_row(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " |",
                                               "   "])

    def test_insufficient_rows(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " X|"])

    def test_grid0(self):
        self.assertEqual(ZERO, grid('0'))

    def test_grid1(self):
        self.assertEqual(ONE, grid('1'))


if __name__ == '__main__':
    unittest.main()
