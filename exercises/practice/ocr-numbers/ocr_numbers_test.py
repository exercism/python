# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/ocr-numbers/canonical-data.json
# File last updated on 2023-07-19

import unittest

from ocr_numbers import (
    convert,
)


class OcrNumbersTest(unittest.TestCase):
    def test_recognizes_0(self):
        self.assertEqual(convert([" _ ", "| |", "|_|", "   "]), "0")

    def test_recognizes_1(self):
        self.assertEqual(convert(["   ", "  |", "  |", "   "]), "1")

    def test_unreadable_but_correctly_sized_inputs_return(self):
        self.assertEqual(convert(["   ", "  _", "  |", "   "]), "?")

    def test_input_with_a_number_of_lines_that_is_not_a_multiple_of_four_raises_an_error(
        self,
    ):
        with self.assertRaises(ValueError) as err:
            convert([" _ ", "| |", "   "])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "Number of input lines is not a multiple of four"
        )

    def test_input_with_a_number_of_columns_that_is_not_a_multiple_of_three_raises_an_error(
        self,
    ):
        with self.assertRaises(ValueError) as err:
            convert(["    ", "   |", "   |", "    "])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "Number of input columns is not a multiple of three"
        )

    def test_recognizes_110101100(self):
        self.assertEqual(
            convert(
                [
                    "       _     _        _  _ ",
                    "  |  || |  || |  |  || || |",
                    "  |  ||_|  ||_|  |  ||_||_|",
                    "                           ",
                ]
            ),
            "110101100",
        )

    def test_garbled_numbers_in_a_string_are_replaced_with(self):
        self.assertEqual(
            convert(
                [
                    "       _     _           _ ",
                    "  |  || |  || |     || || |",
                    "  |  | _|  ||_|  |  ||_||_|",
                    "                           ",
                ]
            ),
            "11?10?1?0",
        )

    def test_recognizes_2(self):
        self.assertEqual(convert([" _ ", " _|", "|_ ", "   "]), "2")

    def test_recognizes_3(self):
        self.assertEqual(convert([" _ ", " _|", " _|", "   "]), "3")

    def test_recognizes_4(self):
        self.assertEqual(convert(["   ", "|_|", "  |", "   "]), "4")

    def test_recognizes_5(self):
        self.assertEqual(convert([" _ ", "|_ ", " _|", "   "]), "5")

    def test_recognizes_6(self):
        self.assertEqual(convert([" _ ", "|_ ", "|_|", "   "]), "6")

    def test_recognizes_7(self):
        self.assertEqual(convert([" _ ", "  |", "  |", "   "]), "7")

    def test_recognizes_8(self):
        self.assertEqual(convert([" _ ", "|_|", "|_|", "   "]), "8")

    def test_recognizes_9(self):
        self.assertEqual(convert([" _ ", "|_|", " _|", "   "]), "9")

    def test_recognizes_string_of_decimal_numbers(self):
        self.assertEqual(
            convert(
                [
                    "    _  _     _  _  _  _  _  _ ",
                    "  | _| _||_||_ |_   ||_||_|| |",
                    "  ||_  _|  | _||_|  ||_| _||_|",
                    "                              ",
                ]
            ),
            "1234567890",
        )

    def test_numbers_separated_by_empty_lines_are_recognized_lines_are_joined_by_commas(
        self,
    ):
        self.assertEqual(
            convert(
                [
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
                    "         ",
                ]
            ),
            "123,456,789",
        )
