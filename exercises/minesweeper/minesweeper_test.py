""" Tests for the minesweeper exercise

Implementation note:
The board function must validate its input and raise a
ValueError with a *meaningful* error message if the
input turns out to be malformed.
"""

import unittest

from minesweeper import annotate


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class MinesweeperTest(unittest.TestCase):

    def test_no_rows(self):
        self.assertEqual(annotate([]), [])

    def test_no_columns(self):
        self.assertEqual(annotate([""]), [""])

    def test_no_mines(self):
        minefield = ["   ",
                     "   ",
                     "   "]
        out = ["   ",
               "   ",
               "   "]
        self.assertEqual(annotate(minefield), out)

    def test_annotate_with_only_mines(self):
        minefield = ["***",
                     "***",
                     "***"]
        out = ["***",
               "***",
               "***"]
        self.assertEqual(annotate(minefield), out)

    def test_mine_surrounded_by_spaces(self):
        minefield = ["   ",
                     " * ",
                     "   "]
        out = ["111",
               "1*1",
               "111"]
        self.assertEqual(annotate(minefield), out)

    def test_space_surrounded_by_mines(self):
        minefield = ["***",
                     "* *",
                     "***"]
        out = ["***",
               "*8*",
               "***"]
        self.assertEqual(annotate(minefield), out)

    def test_horizontal_line(self):
        minefield = [" * * "]
        out = ["1*2*1"]
        self.assertEqual(annotate(minefield), out)

    def test_horizontal_line_mines_at_edges(self):
        minefield = ["*   *"]
        out = ["*1 1*"]
        self.assertEqual(annotate(minefield), out)

    def test_vertical_line(self):
        minefield = [" ",
                     "*",
                     " ",
                     "*",
                     " "]
        out = ["1",
               "*",
               "2",
               "*",
               "1"]
        self.assertEqual(annotate(minefield), out)

    def test_vertical_line_mines_at_edges(self):
        minefield = ["*",
                     " ",
                     " ",
                     " ",
                     "*"]
        out = ["*",
               "1",
               " ",
               "1",
               "*"]
        self.assertEqual(annotate(minefield), out)

    def test_cross(self):
        minefield = ["  *  ",
                     "  *  ",
                     "*****",
                     "  *  ",
                     "  *  "]
        out = [" 2*2 ",
               "25*52",
               "*****",
               "25*52",
               " 2*2 "]
        self.assertEqual(annotate(minefield), out)

    def test_large_annotate(self):
        minefield = [" *  * ",
                     "  *   ",
                     "    * ",
                     "   * *",
                     " *  * ",
                     "      "]
        out = ["1*22*1",
               "12*322",
               " 123*2",
               "112*4*",
               "1*22*2",
               "111111"]
        self.assertEqual(annotate(minefield), out)

    # Additional test for this track
    def test_annotate9(self):
        minefield = ["     ",
                     "   * ",
                     "     ",
                     "     ",
                     " *   "]
        out = ["  111",
               "  1*1",
               "  111",
               "111  ",
               "1*1  "]
        self.assertEqual(annotate(minefield), out)

    def test_different_len(self):
        minefield = [" ",
                     "*  ",
                     "  "]
        with self.assertRaisesWithMessage(ValueError):
            annotate(minefield)

    def test_invalid_char(self):
        minefield = ["X  * "]
        with self.assertRaisesWithMessage(ValueError):
            annotate(minefield)

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
