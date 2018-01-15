import unittest
from transpose import transpose


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class TransposeTests(unittest.TestCase):
    def test_empty_string(self):
        input_line = ""
        expected = ""
        self.assertEqual(
            transpose(input_line),
            expected
        )

    def test_two_characters_in_a_row(self):
        input_line = "A1"
        expected = [
            "A",
            "1"
        ]
        self.assertEqual(
            transpose(input_line),
            "\n".join(expected)
        )

    def test_two_characters_in_a_column(self):
        input_line = [
            "A",
            "1"
        ]
        expected = "A1"
        self.assertEqual(
            transpose("\n".join(input_line)),
            expected
        )

    def test_simple(self):
        input_line = [
            "ABC",
            "123"
        ]
        expected = [
            "A1",
            "B2",
            "C3"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_single_line(self):
        input_line = ["Single line."]
        expected = [
            "S",
            "i",
            "n",
            "g",
            "l",
            "e",
            " ",
            "l",
            "i",
            "n",
            "e",
            "."
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_first_line_longer_than_second_line(self):
        input_line = [
            "The fourth line.",
            "The fifth line."
        ]
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
            "."
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_second_line_longer_than_first_line(self):
        input_line = [
            "The first line.",
            "The second line."
        ]
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
            " ."
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_square(self):
        input_line = [
            "HEART",
            "EMBER",
            "ABUSE",
            "RESIN",
            "TREND"
        ]
        expected = [
            "HEART",
            "EMBER",
            "ABUSE",
            "RESIN",
            "TREND"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_rectangle(self):
        input_line = [
            "FRACTURE",
            "OUTLINED",
            "BLOOMING",
            "SEPTETTE"
        ]
        expected = [
            "FOBS",
            "RULE",
            "ATOP",
            "CLOT",
            "TIME",
            "UNIT",
            "RENT",
            "EDGE"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_triangle(self):
        input_line = [
            "T",
            "EE",
            "AAA",
            "SSSS",
            "EEEEE",
            "RRRRRR"
        ]
        expected = [
            "TEASER",
            " EASER",
            "  ASER",
            "   SER",
            "    ER",
            "     R"
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )

    def test_mixed_line_length(self):
        input_line = [
            "The longest line.",
            "A long line.",
            "A longer line.",
            "A line."
        ]
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
            "."
        ]
        self.assertEqual(
            transpose("\n".join(input_line)),
            "\n".join(expected)
        )


if __name__ == '__main__':
    unittest.main()
