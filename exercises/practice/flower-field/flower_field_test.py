# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/flower-field/canonical-data.json
# File last updated on 2025-12-30

import unittest

from flower_field import (
    annotate,
)


class FlowerFieldTest(unittest.TestCase):
    def test_no_rows(self):
        self.assertEqual(annotate([]), [])

    def test_no_columns(self):
        self.assertEqual(annotate([""]), [""])

    def test_no_flowers(self):
        self.assertEqual(annotate(["   ", "   ", "   "]), ["   ", "   ", "   "])

    def test_garden_full_of_flowers(self):
        self.assertEqual(annotate(["***", "***", "***"]), ["***", "***", "***"])

    def test_flower_surrounded_by_spaces(self):
        self.assertEqual(annotate(["   ", " * ", "   "]), ["111", "1*1", "111"])

    def test_space_surrounded_by_flowers(self):
        self.assertEqual(annotate(["***", "* *", "***"]), ["***", "*8*", "***"])

    def test_horizontal_line(self):
        self.assertEqual(annotate([" * * "]), ["1*2*1"])

    def test_horizontal_line_flowers_at_edges(self):
        self.assertEqual(annotate(["*   *"]), ["*1 1*"])

    def test_vertical_line(self):
        self.assertEqual(annotate([" ", "*", " ", "*", " "]), ["1", "*", "2", "*", "1"])

    def test_vertical_line_flowers_at_edges(self):
        self.assertEqual(annotate(["*", " ", " ", " ", "*"]), ["*", "1", " ", "1", "*"])

    def test_cross(self):
        self.assertEqual(
            annotate(["  *  ", "  *  ", "*****", "  *  ", "  *  "]),
            [" 2*2 ", "25*52", "*****", "25*52", " 2*2 "],
        )

    def test_large_garden(self):
        self.assertEqual(
            annotate([" *  * ", "  *   ", "    * ", "   * *", " *  * ", "      "]),
            ["1*22*1", "12*322", " 123*2", "112*4*", "1*22*2", "111111"],
        )

    def test_multiple_adjacent_flowers(self):
        self.assertEqual(annotate([" ** "]), ["1**1"])

    # Additional tests for this track
    def test_annotate_9(self):
        self.assertEqual(
            annotate(["     ", "   * ", "     ", "     ", " *   "]),
            ["  111", "  1*1", "  111", "111  ", "1*1  "],
        )

    def test_different_len(self):
        with self.assertRaises(ValueError) as err:
            annotate([" ", "*  ", "  "])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "The board is invalid with current input."
        )

    def test_invalid_char(self):
        with self.assertRaises(ValueError) as err:
            annotate(["X  * "])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "The board is invalid with current input."
        )
