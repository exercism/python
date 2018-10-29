"""Tests for the ocr-numbers exercise

Implementation note:
ocr.convert should validate its input and
raise ValueErrors with meaningful error messages
if necessary.
"""

import unittest

from ocr_numbers import convert


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class OcrNumbersTest(unittest.TestCase):
    def test_recognizes_0(self):
        self.assertEqual(convert([" _ ",
                                  "| |",
                                  "|_|",
                                  "   "]), '0')

    def test_recognizes_1(self):
        self.assertEqual(convert(["   ",
                                  "  |",
                                  "  |",
                                  "   "]), '1')

    def test_unreadable_but_correctly_sized(self):
        self.assertEqual(convert(["   ",
                                  "  _",
                                  "  |",
                                  "   "]), '?')

    def test_line_number_not_multiple_of_four(self):
        with self.assertRaisesWithMessage(ValueError):
            convert([" _ ",
                     "| |",
                     "   "])

    def test_col_number_not_multiple_of_three(self):
        with self.assertRaisesWithMessage(ValueError):
            convert(["    ",
                     "   |",
                     "   |",
                     "    "])

    def test_recognizes_110101100(self):
        input_grid = [
            "       _     _        _  _ ",
            "  |  || |  || |  |  || || |",
            "  |  ||_|  ||_|  |  ||_||_|",
            "                           "
        ]
        self.assertEqual(convert(input_grid), "110101100")

    def test_garbled_numbers_in_string(self):
        input_grid = [
            "       _     _           _ ",
            "  |  || |  || |     || || |",
            "  |  | _|  ||_|  |  ||_||_|",
            "                           "
        ]
        self.assertEqual(convert(input_grid), "11?10?1?0")

    def test_recognizes_2(self):
        self.assertEqual(convert([" _ ",
                                  " _|",
                                  "|_ ",
                                  "   "]), "2")

    def test_recognizes_3(self):
        self.assertEqual(convert([" _ ",
                                  " _|",
                                  " _|",
                                  "   "]), "3")

    def test_recognizes_4(self):
        self.assertEqual(convert(["   ",
                                  "|_|",
                                  "  |",
                                  "   "]), "4")

    def test_recognizes_5(self):
        self.assertEqual(convert([" _ ",
                                  "|_ ",
                                  " _|",
                                  "   "]), "5")

    def test_recognizes_6(self):
        self.assertEqual(convert([" _ ",
                                  "|_ ",
                                  "|_|",
                                  "   "]), "6")

    def test_recognizes_7(self):
        self.assertEqual(convert([" _ ",
                                  "  |",
                                  "  |",
                                  "   "]), "7")

    def test_recognizes_8(self):
        self.assertEqual(convert([" _ ",
                                  "|_|",
                                  "|_|",
                                  "   "]), "8")

    def test_recognizes_9(self):
        self.assertEqual(convert([" _ ",
                                  "|_|",
                                  " _|",
                                  "   "]), "9")

    def test_recognizes_string_of_decimal_numbers(self):
        input_grid = [
            "    _  _     _  _  _  _  _  _ ",
            "  | _| _||_||_ |_   ||_||_|| |",
            "  ||_  _|  | _||_|  ||_| _||_|",
            "                              "
        ]
        self.assertEqual(convert(input_grid), "1234567890")

    def test_recognizes_numbers_separated_by_empty_lines(self):
        input_grid = [
            "    _  _ ",
            "  | _| _|",
            "  ||_  _|",
            "         ",
            "    _  _ ",
            "|_||_ |_ ",
            "  | _||_|",
            "         ",
            " _  _  _ ",
            "  ||_||_|",
            "  ||_| _|",
            "         "
        ]
        self.assertEqual(convert(input_grid), "123,456,789")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
