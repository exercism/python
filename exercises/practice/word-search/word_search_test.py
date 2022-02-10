import unittest

from word_search import (
    WordSearch,
    Point,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class WordSearchTest(unittest.TestCase):
    def test_should_accept_an_initial_game_grid_and_a_target_search_word(self):
        puzzle = WordSearch(["jefblpepre"])
        self.assertIsNone(puzzle.search("clojure"))

    def test_should_locate_one_word_written_left_to_right(self):
        puzzle = WordSearch(["clojurermt"])
        self.assertEqual(puzzle.search("clojure"), (Point(0, 0), Point(6, 0)))

    def test_should_locate_the_same_word_written_left_to_right_in_a_different_position(
        self,
    ):
        puzzle = WordSearch(["mtclojurer"])
        self.assertEqual(puzzle.search("clojure"), (Point(2, 0), Point(8, 0)))

    def test_should_locate_a_different_left_to_right_word(self):
        puzzle = WordSearch(["coffeelplx"])
        self.assertEqual(puzzle.search("coffee"), (Point(0, 0), Point(5, 0)))

    def test_should_locate_that_different_left_to_right_word_in_a_different_position(
        self,
    ):
        puzzle = WordSearch(["xcoffeezlp"])
        self.assertEqual(puzzle.search("coffee"), (Point(1, 0), Point(6, 0)))

    def test_should_locate_a_left_to_right_word_in_two_line_grid(self):
        puzzle = WordSearch(["jefblpepre", "tclojurerm"])
        self.assertEqual(puzzle.search("clojure"), (Point(1, 1), Point(7, 1)))

    def test_should_locate_a_left_to_right_word_in_three_line_grid(self):
        puzzle = WordSearch(["camdcimgtc", "jefblpepre", "clojurermt"])
        self.assertEqual(puzzle.search("clojure"), (Point(0, 2), Point(6, 2)))

    def test_should_locate_a_left_to_right_word_in_ten_line_grid(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))

    def test_should_locate_that_left_to_right_word_in_a_different_position_in_a_ten_line_grid(
        self,
    ):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "clojurermt",
                "jalaycalmp",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 8), Point(6, 8)))

    def test_should_locate_a_different_left_to_right_word_in_a_ten_line_grid(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "fortranftw",
                "alxhpburyi",
                "clojurermt",
                "jalaycalmp",
            ]
        )
        self.assertEqual(puzzle.search("fortran"), (Point(0, 6), Point(6, 6)))

    def test_should_locate_multiple_words(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "fortranftw",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("fortran"), (Point(0, 6), Point(6, 6)))
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))

    def test_should_locate_a_single_word_written_right_to_left(self):
        puzzle = WordSearch(["rixilelhrs"])
        self.assertEqual(puzzle.search("elixir"), (Point(5, 0), Point(0, 0)))

    def test_should_locate_multiple_words_written_in_different_horizontal_directions(
        self,
    ):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))

    def test_should_locate_words_written_top_to_bottom(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))

    def test_should_locate_words_written_bottom_to_top(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))
        self.assertEqual(puzzle.search("rust"), (Point(8, 4), Point(8, 1)))

    def test_should_locate_words_written_top_left_to_bottom_right(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))
        self.assertEqual(puzzle.search("rust"), (Point(8, 4), Point(8, 1)))
        self.assertEqual(puzzle.search("java"), (Point(0, 0), Point(3, 3)))

    def test_should_locate_words_written_bottom_right_to_top_left(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))
        self.assertEqual(puzzle.search("rust"), (Point(8, 4), Point(8, 1)))
        self.assertEqual(puzzle.search("java"), (Point(0, 0), Point(3, 3)))
        self.assertEqual(puzzle.search("lua"), (Point(7, 8), Point(5, 6)))

    def test_should_locate_words_written_bottom_left_to_top_right(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))
        self.assertEqual(puzzle.search("rust"), (Point(8, 4), Point(8, 1)))
        self.assertEqual(puzzle.search("java"), (Point(0, 0), Point(3, 3)))
        self.assertEqual(puzzle.search("lua"), (Point(7, 8), Point(5, 6)))
        self.assertEqual(puzzle.search("lisp"), (Point(2, 5), Point(5, 2)))

    def test_should_locate_words_written_top_right_to_bottom_left(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))
        self.assertEqual(puzzle.search("rust"), (Point(8, 4), Point(8, 1)))
        self.assertEqual(puzzle.search("java"), (Point(0, 0), Point(3, 3)))
        self.assertEqual(puzzle.search("lua"), (Point(7, 8), Point(5, 6)))
        self.assertEqual(puzzle.search("lisp"), (Point(2, 5), Point(5, 2)))
        self.assertEqual(puzzle.search("ruby"), (Point(7, 5), Point(4, 8)))

    def test_should_fail_to_locate_a_word_that_is_not_in_the_puzzle(self):
        puzzle = WordSearch(
            [
                "jefblpepre",
                "camdcimgtc",
                "oivokprjsm",
                "pbwasqroua",
                "rixilelhrs",
                "wolcqlirpc",
                "screeaumgr",
                "alxhpburyi",
                "jalaycalmp",
                "clojurermt",
            ]
        )
        self.assertEqual(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
        self.assertEqual(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
        self.assertEqual(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))
        self.assertEqual(puzzle.search("rust"), (Point(8, 4), Point(8, 1)))
        self.assertEqual(puzzle.search("java"), (Point(0, 0), Point(3, 3)))
        self.assertEqual(puzzle.search("lua"), (Point(7, 8), Point(5, 6)))
        self.assertEqual(puzzle.search("lisp"), (Point(2, 5), Point(5, 2)))
        self.assertEqual(puzzle.search("ruby"), (Point(7, 5), Point(4, 8)))
        self.assertIsNone(puzzle.search("haskell"))

    def test_should_fail_to_locate_words_that_are_not_on_horizontal_vertical_or_diagonal_lines(
        self,
    ):
        puzzle = WordSearch(["abc", "def"])
        self.assertIsNone(puzzle.search("aef"))
        self.assertIsNone(puzzle.search("ced"))
        self.assertIsNone(puzzle.search("abf"))
        self.assertIsNone(puzzle.search("cbd"))

    def test_should_not_concatenate_different_lines_to_find_a_horizontal_word(self):
        puzzle = WordSearch(["abceli", "xirdfg"])
        self.assertIsNone(puzzle.search("elixir"))

    def test_should_not_wrap_around_horizontally_to_find_a_word(self):
        puzzle = WordSearch(["silabcdefp"])
        self.assertIsNone(puzzle.search("lisp"))

    def test_should_not_wrap_around_vertically_to_find_a_word(self):
        puzzle = WordSearch(["s", "u", "r", "a", "b", "c", "t"])
        self.assertIsNone(puzzle.search("rust"))


if __name__ == "__main__":
    unittest.main()
