import unittest

from word_search import WordSearch, Point


class WordSearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        puzzle = ('jefblpepre\n'
                  'camdcimgtc\n'
                  'oivokprjsm\n'
                  'pbwasqroua\n'
                  'rixilelhrs\n'
                  'wolcqlirpc\n'
                  'screeaumgr\n'
                  'alxhpburyi\n'
                  'jalaycalmp\n'
                  'clojurermt')
        self.example = WordSearch(puzzle)

    def test_horizontal_words_left_to_right(self):
        self.assertEqual(
            self.example.search('clojure'),
            (Point(0, 9), Point(6, 9))
        )

    def test_horizontal_words_right_to_left(self):
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

    def test_search_differently_sized_puzzles(self):
        puzzle = ('qwertyuiopz\n'
                  'luamsicrexe\n'
                  'abcdefghijk')
        self.assertEqual(
            WordSearch(puzzle).search('exercism'),
            (Point(10, 1), Point(3, 1))
        )


if __name__ == '__main__':
    unittest.main()
