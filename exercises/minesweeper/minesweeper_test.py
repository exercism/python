""" Tests for the minesweeper exercise

Implementation note:
The board function must validate its input and raise a
ValueError with a meaningfull error message if the
input turns out to be malformed.
"""

import unittest

from minesweeper import board


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class MinesweeperTest(unittest.TestCase):

    def test_no_rows(self):
        self.assertEqual(board([]), [])

    def test_no_columns(self):
        self.assertEqual(board([""]), [""])

    def test_no_mines(self):
        inp = ["   ",
               "   ",
               "   "]
        out = ["   ",
               "   ",
               "   "]
        self.assertEqual(board(inp), out)

    def test_board_with_only_mines(self):
        inp = ["***",
               "***",
               "***"]
        out = ["***",
               "***",
               "***"]
        self.assertEqual(board(inp), out)

    def test_mine_surrounded_by_spaces(self):
        inp = ["   ",
               " * ",
               "   "]
        out = ["111",
               "1*1",
               "111"]
        self.assertEqual(board(inp), out)

    def test_space_surrounded_by_mines(self):
        inp = ["***",
               "* *",
               "***"]
        out = ["***",
               "*8*",
               "***"]
        self.assertEqual(board(inp), out)

    def test_horizontal_line(self):
        inp = [" * * "]
        out = ["1*2*1"]
        self.assertEqual(board(inp), out)

    def test_horizontal_line_mines_at_edges(self):
        inp = ["*   *"]
        out = ["*1 1*"]
        self.assertEqual(board(inp), out)

    def test_vertical_line(self):
        inp = [" ",
               "*",
               " ",
               "*",
               " "]
        out = ["1",
               "*",
               "2",
               "*",
               "1"]
        self.assertEqual(board(inp), out)

    def test_vertical_line_mines_at_edges(self):
        inp = ["*",
               " ",
               " ",
               " ",
               "*"]
        out = ["*",
               "1",
               " ",
               "1",
               "*"]
        self.assertEqual(board(inp), out)

    def test_cross(self):
        inp = ["  *  ",
               "  *  ",
               "*****",
               "  *  ",
               "  *  "]
        out = [" 2*2 ",
               "25*52",
               "*****",
               "25*52",
               " 2*2 "]
        self.assertEqual(board(inp), out)

    def test_large_board(self):
        inp = [" *  * ",
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
        self.assertEqual(board(inp), out)

    # Additional test for this track
    def test_board9(self):
        inp = ["     ",
               "   * ",
               "     ",
               "     ",
               " *   "]
        out = ["  111",
               "  1*1",
               "  111",
               "111  ",
               "1*1  "]
        self.assertEqual(board(inp), out)

    def test_different_len(self):
        inp = [" ",
               "*  ",
               "  "]
        with self.assertRaisesWithMessage(ValueError):
            board(inp)

    def test_invalid_char(self):
        inp = ["X  * "]
        with self.assertRaisesWithMessage(ValueError):
            board(inp)

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
