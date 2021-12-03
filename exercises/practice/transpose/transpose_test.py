import unittest

from transpose import (
    transpose,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class TransposeTest(unittest.TestCase):
    def test_empty_string(self):
        lines = []
        expected = []
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_two_characters_in_a_row(self):
        lines = ["A1"]
        expected = ["A", "1"]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_two_characters_in_a_column(self):
        lines = ["A", "1"]
        expected = ["A1"]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_simple(self):
        lines = ["ABC", "123"]
        expected = ["A1", "B2", "C3"]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_single_line(self):
        lines = ["Single line."]
        expected = ["S", "i", "n", "g", "l", "e", " ", "l", "i", "n", "e", "."]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_first_line_longer_than_second_line(self):
        lines = ["The fourth line.", "The fifth line."]
        expected = [
            "TT",
            "hh",
            "ee",
            "  ",
            "ff",
            "oi",
            "uf",
            "rt",
            "th",
            "h ",
            " l",
            "li",
            "in",
            "ne",
            "e.",
            ".",
        ]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_second_line_longer_than_first_line(self):
        lines = ["The first line.", "The second line."]
        expected = [
            "TT",
            "hh",
            "ee",
            "  ",
            "fs",
            "ie",
            "rc",
            "so",
            "tn",
            " d",
            "l ",
            "il",
            "ni",
            "en",
            ".e",
            " .",
        ]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_mixed_line_length(self):
        lines = ["The longest line.", "A long line.", "A longer line.", "A line."]
        expected = [
            "TAAA",
            "h   ",
            "elll",
            " ooi",
            "lnnn",
            "ogge",
            "n e.",
            "glr",
            "ei ",
            "snl",
            "tei",
            " .n",
            "l e",
            "i .",
            "n",
            "e",
            ".",
        ]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_square(self):
        lines = ["HEART", "EMBER", "ABUSE", "RESIN", "TREND"]
        expected = ["HEART", "EMBER", "ABUSE", "RESIN", "TREND"]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_rectangle(self):
        lines = ["FRACTURE", "OUTLINED", "BLOOMING", "SEPTETTE"]
        expected = ["FOBS", "RULE", "ATOP", "CLOT", "TIME", "UNIT", "RENT", "EDGE"]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_triangle(self):
        lines = ["T", "EE", "AAA", "SSSS", "EEEEE", "RRRRRR"]
        expected = ["TEASER", " EASER", "  ASER", "   SER", "    ER", "     R"]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))

    def test_jagged_triangle(self):
        lines = ["11", "2", "3333", "444", "555555", "66666"]
        expected = ["123456", "1 3456", "  3456", "  3 56", "    56", "    5"]
        self.assertEqual(transpose("\n".join(lines)), "\n".join(expected))
