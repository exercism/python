import unittest

from word_search import WordSearch, Point

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.1


class WordSearchTest(unittest.TestCase):
    def test_should_accept_an_initial_game_grid_and_a_target_search_word(self):
        puzzle = ["jefblpepre"]
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertIsNone(search_answer)

    def test_should_locate_one_word_written_left_to_right(self):
        puzzle = ["clojurermt"]
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 0), Point(6, 0)))

    def test_should_locate_the_same_word_written_left_to_right_in_a_different_position(
        self
    ):
        puzzle = ["mtclojurer"]
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(2, 0), Point(8, 0)))

    def test_should_locate_a_different_left_to_right_word(self):
        puzzle = ["coffeelplx"]
        search_answer = WordSearch(puzzle).search("coffee")
        self.assertEqual(search_answer, (Point(0, 0), Point(5, 0)))

    def test_should_locate_that_different_left_to_right_word_in_a_different_position(
        self
    ):
        puzzle = ["xcoffeezlp"]
        search_answer = WordSearch(puzzle).search("coffee")
        self.assertEqual(search_answer, (Point(1, 0), Point(6, 0)))

    def test_should_locate_a_left_to_right_word_in_two_line_grid(self):
        puzzle = ["jefblpepre", "tclojurerm"]
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(1, 1), Point(7, 1)))

    def test_should_locate_a_left_to_right_word_in_three_line_grid(self):
        puzzle = ["camdcimgtc", "jefblpepre", "clojurermt"]
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 2), Point(6, 2)))

    def test_should_locate_a_left_to_right_word_in_ten_line_grid(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))

    def test_should_locate_that_left_to_right_word_in_a_different_position_in_a_ten_line_grid(
        self
    ):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 8), Point(6, 8)))

    def test_should_locate_a_different_left_to_right_word_in_a_ten_line_grid(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("fortran")
        self.assertEqual(search_answer, (Point(0, 6), Point(6, 6)))

    def test_should_locate_multiple_words(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("fortran")
        self.assertEqual(search_answer, (Point(0, 6), Point(6, 6)))
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))

    def test_should_locate_a_single_word_written_right_to_left(self):
        puzzle = ["rixilelhrs"]
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 0), Point(0, 0)))

    def test_should_locate_multiple_words_written_in_different_horizontal_directions(
        self
    ):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))

    def test_should_locate_words_written_top_to_bottom(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("ecmascript")
        self.assertEqual(search_answer, (Point(9, 0), Point(9, 9)))

    def test_should_locate_words_written_bottom_to_top(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("ecmascript")
        self.assertEqual(search_answer, (Point(9, 0), Point(9, 9)))
        search_answer = WordSearch(puzzle).search("rust")
        self.assertEqual(search_answer, (Point(8, 4), Point(8, 1)))

    def test_should_locate_words_written_top_left_to_bottom_right(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("ecmascript")
        self.assertEqual(search_answer, (Point(9, 0), Point(9, 9)))
        search_answer = WordSearch(puzzle).search("rust")
        self.assertEqual(search_answer, (Point(8, 4), Point(8, 1)))
        search_answer = WordSearch(puzzle).search("java")
        self.assertEqual(search_answer, (Point(0, 0), Point(3, 3)))

    def test_should_locate_words_written_bottom_right_to_top_left(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("ecmascript")
        self.assertEqual(search_answer, (Point(9, 0), Point(9, 9)))
        search_answer = WordSearch(puzzle).search("rust")
        self.assertEqual(search_answer, (Point(8, 4), Point(8, 1)))
        search_answer = WordSearch(puzzle).search("java")
        self.assertEqual(search_answer, (Point(0, 0), Point(3, 3)))
        search_answer = WordSearch(puzzle).search("lua")
        self.assertEqual(search_answer, (Point(7, 8), Point(5, 6)))

    def test_should_locate_words_written_bottom_left_to_top_right(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("ecmascript")
        self.assertEqual(search_answer, (Point(9, 0), Point(9, 9)))
        search_answer = WordSearch(puzzle).search("rust")
        self.assertEqual(search_answer, (Point(8, 4), Point(8, 1)))
        search_answer = WordSearch(puzzle).search("java")
        self.assertEqual(search_answer, (Point(0, 0), Point(3, 3)))
        search_answer = WordSearch(puzzle).search("lua")
        self.assertEqual(search_answer, (Point(7, 8), Point(5, 6)))
        search_answer = WordSearch(puzzle).search("lisp")
        self.assertEqual(search_answer, (Point(2, 5), Point(5, 2)))

    def test_should_locate_words_written_top_right_to_bottom_left(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("ecmascript")
        self.assertEqual(search_answer, (Point(9, 0), Point(9, 9)))
        search_answer = WordSearch(puzzle).search("rust")
        self.assertEqual(search_answer, (Point(8, 4), Point(8, 1)))
        search_answer = WordSearch(puzzle).search("java")
        self.assertEqual(search_answer, (Point(0, 0), Point(3, 3)))
        search_answer = WordSearch(puzzle).search("lua")
        self.assertEqual(search_answer, (Point(7, 8), Point(5, 6)))
        search_answer = WordSearch(puzzle).search("lisp")
        self.assertEqual(search_answer, (Point(2, 5), Point(5, 2)))
        search_answer = WordSearch(puzzle).search("ruby")
        self.assertEqual(search_answer, (Point(7, 5), Point(4, 8)))

    def test_should_fail_to_locate_a_word_that_is_not_in_the_puzzle(self):
        puzzle = [
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
        search_answer = WordSearch(puzzle).search("clojure")
        self.assertEqual(search_answer, (Point(0, 9), Point(6, 9)))
        search_answer = WordSearch(puzzle).search("elixir")
        self.assertEqual(search_answer, (Point(5, 4), Point(0, 4)))
        search_answer = WordSearch(puzzle).search("ecmascript")
        self.assertEqual(search_answer, (Point(9, 0), Point(9, 9)))
        search_answer = WordSearch(puzzle).search("rust")
        self.assertEqual(search_answer, (Point(8, 4), Point(8, 1)))
        search_answer = WordSearch(puzzle).search("java")
        self.assertEqual(search_answer, (Point(0, 0), Point(3, 3)))
        search_answer = WordSearch(puzzle).search("lua")
        self.assertEqual(search_answer, (Point(7, 8), Point(5, 6)))
        search_answer = WordSearch(puzzle).search("lisp")
        self.assertEqual(search_answer, (Point(2, 5), Point(5, 2)))
        search_answer = WordSearch(puzzle).search("ruby")
        self.assertEqual(search_answer, (Point(7, 5), Point(4, 8)))
        search_answer = WordSearch(puzzle).search("haskell")
        self.assertIsNone(search_answer)


if __name__ == "__main__":
    unittest.main()
