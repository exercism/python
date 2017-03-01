import unittest

from word_search import search


class WordSearchTests(unittest.TestCase):

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

    def test_horizontal_words_left_to_right(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'clojure'), ((9, 0), (9, 6)))

    def test_horizontal_words_right_to_left(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'elixir'), ((4, 5), (4, 0)))

    def test_vertical_words_top_to_bottom(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'ecmascript'), ((0, 9), (9, 9)))

    def test_vertical_words_bottom_to_top(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'rust'), ((4, 8), (1, 8)))

    def test_diagonal_top_left_to_bottom_right(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'java'), ((0, 0), (3, 3)))

    def test_diagonal_bottom_right_to_top_left(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'lua'), ((8, 7), (6, 5)))

    def test_diagonal_bottom_left_to_top_right(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'lisp'), ((5, 2), (2, 5)))

    def test_diagonal_top_right_to_bottom_left(self):
        self.assertEqual(search(WordSearchTests.puzzle, 'ruby'), ((5, 7), (8, 4)))

    def test_words_that_are_not_in_the_puzzle(self):
        self.assertIsNone(search(WordSearchTests.puzzle, 'haskell'))

    def test_search_differently_sized_puzzles(self):
        puzzle = ['qwertyuiopz',
                  'luamsicrexe',
                  'abcdefghijk']
        self.assertEqual(search(puzzle, 'exercism'), ((1, 10), (1, 3)))


if __name__ == '__main__':
    unittest.main()
