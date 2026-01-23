# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/line-up/canonical-data.json
# File last updated on 2026-01-23

import unittest

from line_up import (
    line_up,
)


class LineUpTest(unittest.TestCase):
    def test_format_smallest_non_exceptional_ordinal_numeral_4(self):
        self.assertEqual(
            line_up("Gianna", 4),
            "Gianna, you are the 4th customer we serve today. Thank you!",
        )

    def test_format_greatest_single_digit_non_exceptional_ordinal_numeral_9(self):
        self.assertEqual(
            line_up("Maarten", 9),
            "Maarten, you are the 9th customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_5(self):
        self.assertEqual(
            line_up("Petronila", 5),
            "Petronila, you are the 5th customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_6(self):
        self.assertEqual(
            line_up("Attakullakulla", 6),
            "Attakullakulla, you are the 6th customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_7(self):
        self.assertEqual(
            line_up("Kate", 7),
            "Kate, you are the 7th customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_8(self):
        self.assertEqual(
            line_up("Maximiliano", 8),
            "Maximiliano, you are the 8th customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_1(self):
        self.assertEqual(
            line_up("Mary", 1),
            "Mary, you are the 1st customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_2(self):
        self.assertEqual(
            line_up("Haruto", 2),
            "Haruto, you are the 2nd customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_3(self):
        self.assertEqual(
            line_up("Henriette", 3),
            "Henriette, you are the 3rd customer we serve today. Thank you!",
        )

    def test_format_smallest_two_digit_non_exceptional_ordinal_numeral_10(self):
        self.assertEqual(
            line_up("Alvarez", 10),
            "Alvarez, you are the 10th customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_11(self):
        self.assertEqual(
            line_up("Jacqueline", 11),
            "Jacqueline, you are the 11th customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_12(self):
        self.assertEqual(
            line_up("Juan", 12),
            "Juan, you are the 12th customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_13(self):
        self.assertEqual(
            line_up("Patricia", 13),
            "Patricia, you are the 13th customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_21(self):
        self.assertEqual(
            line_up("Washi", 21),
            "Washi, you are the 21st customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_62(self):
        self.assertEqual(
            line_up("Nayra", 62),
            "Nayra, you are the 62nd customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_100(self):
        self.assertEqual(
            line_up("John", 100),
            "John, you are the 100th customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_101(self):
        self.assertEqual(
            line_up("Zeinab", 101),
            "Zeinab, you are the 101st customer we serve today. Thank you!",
        )

    def test_format_non_exceptional_ordinal_numeral_112(self):
        self.assertEqual(
            line_up("Knud", 112),
            "Knud, you are the 112th customer we serve today. Thank you!",
        )

    def test_format_exceptional_ordinal_numeral_123(self):
        self.assertEqual(
            line_up("Yma", 123),
            "Yma, you are the 123rd customer we serve today. Thank you!",
        )
