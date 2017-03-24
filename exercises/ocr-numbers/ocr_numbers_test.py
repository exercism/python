"""Tests for the ocr-numbers exercise

Implementation note:
Both ocr.grid and ocr.number should validate their input
and raise ValueErrors with meaningful error messages
if necessary.
"""

import unittest

from ocr_numbers import grid, number


class OcrTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(number([" _ ",
                                 "| |",
                                 "|_|",
                                 "   "]), '0')

    def test_1(self):
        self.assertEqual(number(["   ",
                                 "  |",
                                 "  |",
                                 "   "]), '1')

    def test_garbage(self):
        self.assertEqual(number([" _ ",
                                 " _|",
                                 "  |",
                                 "   "]), '?')

    def test_last_line_nonblank(self):
        self.assertEqual(number(["   ",
                                 "  |",
                                 "  |",
                                 "| |"]), '?')

    def test_unknown_char(self):
        self.assertEqual(number([" - ",
                                 " _|",
                                 " X|",
                                 "   "]), '?')

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
        self.assertEqual(grid('0'), [" _ ",
                                     "| |",
                                     "|_|",
                                     "   "])

    def test_grid1(self):
        self.assertEqual(grid('1'), ["   ",
                                     "  |",
                                     "  |",
                                     "   "])

    def test_0010110(self):
        self.assertEqual(
            number([
                " _  _     _        _ ",
                "| || |  || |  |  || |",
                "|_||_|  ||_|  |  ||_|",
                "                     "
            ]), '0010110')

    def test_3186547290(self):
        digits = '3186547290'
        self.assertEqual(
            number([
                " _     _  _  _     _  _  _  _ ",
                " _|  ||_||_ |_ |_|  | _||_|| |",
                " _|  ||_||_| _|  |  ||_  _||_|",
                "                              "
            ]), digits)

    def test_Lost(self):
        digits = '4815162342'
        self.assertEqual(
            number([
                "    _     _     _  _  _     _ ",
                "|_||_|  ||_   ||_  _| _||_| _|",
                "  ||_|  | _|  ||_||_  _|  ||_ ",
                "                              "
            ]), digits)

    def test_garble_middle(self):
        self.assertEqual(
            number([
                "    _  _     _ ",
                "  | _|  ||_||_ ",
                "  ||_  _|  | _|",
                "               "
            ]), '12?45')

    def test_grid3186547290(self):
        digits = '3186547290'
        self.assertEqual(
            grid(digits), [
                " _     _  _  _     _  _  _  _ ",
                " _|  ||_||_ |_ |_|  | _||_|| |",
                " _|  ||_||_| _|  |  ||_  _||_|",
                "                              "
            ])

    def test_invalid_grid(self):
        self.assertRaises(ValueError, grid, '123a')


if __name__ == '__main__':
    unittest.main()
