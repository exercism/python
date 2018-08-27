import unittest

from word_search import WordSearch, Point


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.1

class WordSearchTest(unittest.TestCase):

    def test_initial_game_grid(self):
        puzzle = ['jefblpepre']
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertIsNone(searchAnswer)

    def test_left_to_right_word(self):
        puzzle = ['clojurermt']
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertEqual(searchAnswer, (Point(0, 0), Point(6, 0)))

    def test_left_to_right_word_different_position(self):
        puzzle = ['mtclojurer']
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertEqual(searchAnswer, (Point(2, 0), Point(8, 0)))

    def test_different_left_to_right_word(self):
        puzzle = ['coffeelplx']
        searchAnswer = WordSearch(puzzle).search('coffee')
        self.assertEqual(searchAnswer, (Point(0, 0), Point(5, 0)))

    def test_different_left_to_right_word_different_position(self):
        puzzle = ['xcoffeezlp']
        searchAnswer = WordSearch(puzzle).search('coffee')
        self.assertEqual(searchAnswer, (Point(1, 0), Point(6, 0)))

    def test_left_to_right_word_two_lines(self):
        puzzle = ['jefblpepre',
                  'tclojurerm']
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertEqual(searchAnswer, (Point(1, 1), Point(7, 1)))

    def test_left_to_right_word_three_lines(self):
        puzzle = ['camdcimgtc',
                  'jefblpepre',
                  'clojurermt']
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertEqual(searchAnswer, (Point(0, 2), Point(6, 2)))

    def test_left_to_right_word_ten_lines(self):
        puzzle = ['jefblpepre',
                  'camdcimgtc',
                  'oivokprjsm',
                  'pbwasqroua',
                  'rixilelhrs',
                  'wolcqlirpc',
                  'screeaumgr',
                  'alxhpburyi',
                  'jalaycalmp',
                  'clojurermt']
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertEqual(searchAnswer, (Point(0, 9), Point(6, 9)))

    def test_left_to_right_word_ten_lines_different_position(self):
        puzzle = ['jefblpepre',
                  'camdcimgtc',
                  'oivokprjsm',
                  'pbwasqroua',
                  'rixilelhrs',
                  'wolcqlirpc',
                  'screeaumgr',
                  'alxhpburyi',
                  'clojurermt',
                  'jalaycalmp']
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertEqual(searchAnswer, (Point(0, 8), Point(6, 8)))

    def test_different_left_to_right_word_ten_lines(self):
        puzzle = ['jefblpepre',
                  'camdcimgtc',
                  'oivokprjsm',
                  'pbwasqroua',
                  'rixilelhrs',
                  'wolcqlirpc',
                  'fortranftw',
                  'alxhpburyi',
                  'clojurermt',
                  'jalaycalmp']
        searchAnswer = WordSearch(puzzle).search('fortran')
        self.assertEqual(searchAnswer, (Point(0, 6), Point(6, 6)))

    def test_multiple_words(self):
        puzzle = ['jefblpepre',
                  'camdcimgtc',
                  'oivokprjsm',
                  'pbwasqroua',
                  'rixilelhrs',
                  'wolcqlirpc',
                  'fortranftw',
                  'alxhpburyi',
                  'jalaycalmp',
                  'clojurermt']
        searchAnswer = WordSearch(puzzle).search('fortran')
        self.assertEqual(searchAnswer, (Point(0, 6), Point(6, 6)))
        searchAnswer = WordSearch(puzzle).search('clojure')
        self.assertEqual(searchAnswer, (Point(0, 9), Point(6, 9)))

    def test_single_word_right_to_left(self):
        puzzle = ['rixilelhrs']
        searchAnswer = WordSearch(puzzle).search('elixir')
        self.assertEqual(searchAnswer, (Point(5, 0), Point(0, 0)))

    @classmethod
    def setUpClass(cls):
        puzzle = ['jefblpepre',
                  'camdcimgtc',
                  'oivokprjsm',
                  'pbwasqroua',
                  'rixilelhrs',
                  'wolcqlirpc',
                  'screeaumgr',
                  'alxhpburyi',
                  'jalaycalmp',
                  'clojurermt']
        cls.example = WordSearch(puzzle)

    def test_horizontal_words_different_directions(self):
        self.assertEqual(
            self.example.search('clojure'),
            (Point(0, 9), Point(6, 9))
        )
        self.assertEqual(
            self.example.search('elixir'),
            (Point(5, 4), Point(0, 4))
        )

    def test_vertical_words_top_to_bottom(self):
        self.assertEqual(
            self.example.search('ecmascript'),
            (Point(9, 0), Point(9, 9))
        )

    def test_vertical_words_bottom_to_top(self):
        self.assertEqual(
            self.example.search('rust'),
            (Point(8, 4), Point(8, 1))
        )

    def test_diagonal_words_top_left_to_bottom_right(self):
        self.assertEqual(
            self.example.search('java'),
            (Point(0, 0), Point(3, 3))
        )

    def test_diagonal_upper_bottom_right_to_top_left(self):
        self.assertEqual(
            self.example.search('lua'),
            (Point(7, 8), Point(5, 6))
        )

    def test_diagonal_upper_bottom_left_to_top_right(self):
        self.assertEqual(
            self.example.search('lisp'),
            (Point(2, 5), Point(5, 2))
        )

    def test_diagonal_upper_top_right_to_bottom_left(self):
        self.assertEqual(
            self.example.search('ruby'),
            (Point(7, 5), Point(4, 8))
        )

    def test_words_that_are_not_in_the_puzzle(self):
        self.assertIsNone(self.example.search('haskell'))


if __name__ == '__main__':
    unittest.main()
