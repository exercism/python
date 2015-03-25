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

    @unittest.skip("")
    def test_1(self):
        self.assertEqual('1', number(ONE))

    @unittest.skip("")
    def test_garbage(self):
        self.assertEqual('?', number([" _ ",
                                      " _|",
                                      "  |",
                                      "   "]))

    @unittest.skip("")
    def test_last_line_nonblank(self):
        self.assertEqual('?', number(["   ",
                                      "  |",
                                      "  |",
                                      "| |"]))

    @unittest.skip("")
    def test_unknown_char(self):
        self.assertEqual('?', number([" - ",
                                      " _|",
                                      " X|",
                                      "   "]))

    @unittest.skip("")
    def test_too_short_row(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " |",
                                               "   "])

    @unittest.skip("")
    def test_insufficient_rows(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " X|"])

    @unittest.skip("")
    def test_grid0(self):
        self.assertEqual(ZERO, grid('0'))

    @unittest.skip("")
    def test_grid1(self):
        self.assertEqual(ONE, grid('1'))


if __name__ == '__main__':
    unittest.main()
