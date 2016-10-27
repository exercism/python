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
        self.assertEqual('0', number([" _ ",
                                      "| |",
                                      "|_|",
                                      "   "]))

    def test_1(self):
        self.assertEqual('1', number(["   ",
                                      "  |",
                                      "  |",
                                      "   "]))

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
        self.assertEqual([" _ ",
                          "| |",
                          "|_|",
                          "   "], grid('0'))

    def test_grid1(self):
        self.assertEqual(["   ",
                          "  |",
                          "  |",
                          "   "], grid('1'))

    def test_0010110(self):
        self.assertEqual('0010110', number([" _  _     _        _ ",
                                            "| || |  || |  |  || |",
                                            "|_||_|  ||_|  |  ||_|",
                                            "                     "]))

    def test_3186547290(self):
        digits = '3186547290'
        self.assertEqual(digits, number([" _     _  _  _     _  _  _  _ ",
                                         " _|  ||_||_ |_ |_|  | _||_|| |",
                                         " _|  ||_||_| _|  |  ||_  _||_|",
                                         "                              "]))

    def test_Lost(self):
        digits = '4815162342'
        self.assertEqual(digits, number(["    _     _     _  _  _     _ ",
                                         "|_||_|  ||_   ||_  _| _||_| _|",
                                         "  ||_|  | _|  ||_||_  _|  ||_ ",
                                         "                              "]))

    def test_garble_middle(self):
        self.assertEqual('12?45', number(["    _  _     _ ",
                                          "  | _|  ||_||_ ",
                                          "  ||_  _|  | _|",
                                          "               "]))

    def test_grid3186547290(self):
        digits = '3186547290'
        self.assertEqual([" _     _  _  _     _  _  _  _ ",
                          " _|  ||_||_ |_ |_|  | _||_|| |",
                          " _|  ||_||_| _|  |  ||_  _||_|",
                          "                              "], grid(digits))

    def test_invalid_grid(self):
        self.assertRaises(ValueError, grid, '123a')

if __name__ == '__main__':
    unittest.main()
