import unittest

from minesweeper import annotate

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class MinesweeperTest(unittest.TestCase):
    def test_no_rows(self):
        minefield = []
        expected = []
        self.assertEqual(annotate(minefield), expected)

    def test_no_columns(self):
        minefield = [""]
        expected = [""]
        self.assertEqual(annotate(minefield), expected)

    def test_no_mines(self):
        minefield = ["   ", "   ", "   "]
        expected = ["   ", "   ", "   "]
        self.assertEqual(annotate(minefield), expected)

    def test_minefield_with_only_mines(self):
        minefield = ["***", "***", "***"]
        expected = ["***", "***", "***"]
        self.assertEqual(annotate(minefield), expected)

    def test_mine_surrounded_by_spaces(self):
        minefield = ["   ", " * ", "   "]
        expected = ["111", "1*1", "111"]
        self.assertEqual(annotate(minefield), expected)

    def test_space_surrounded_by_mines(self):
        minefield = ["***", "* *", "***"]
        expected = ["***", "*8*", "***"]
        self.assertEqual(annotate(minefield), expected)

    def test_horizontal_line(self):
        minefield = [" * * "]
        expected = ["1*2*1"]
        self.assertEqual(annotate(minefield), expected)

    def test_horizontal_line_mines_at_edges(self):
        minefield = ["*   *"]
        expected = ["*1 1*"]
        self.assertEqual(annotate(minefield), expected)

    def test_vertical_line(self):
        minefield = [" ", "*", " ", "*", " "]
        expected = ["1", "*", "2", "*", "1"]
        self.assertEqual(annotate(minefield), expected)

    def test_vertical_line_mines_at_edges(self):
        minefield = ["*", " ", " ", " ", "*"]
        expected = ["*", "1", " ", "1", "*"]
        self.assertEqual(annotate(minefield), expected)

    def test_cross(self):
        minefield = ["  *  ", "  *  ", "*****", "  *  ", "  *  "]
        expected = [" 2*2 ", "25*52", "*****", "25*52", " 2*2 "]
        self.assertEqual(annotate(minefield), expected)

    def test_large_minefield(self):
        minefield = [" *  * ", "  *   ", "    * ", "   * *", " *  * ", "      "]
        expected = ["1*22*1", "12*322", " 123*2", "112*4*", "1*22*2", "111111"]
        self.assertEqual(annotate(minefield), expected)


if __name__ == "__main__":
    unittest.main()
