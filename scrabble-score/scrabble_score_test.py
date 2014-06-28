import unittest

from scrabble import score


class WordTest(unittest.TestCase):
    def test_empty_word_scores_zero(self):
        self.assertEqual(0, score(""))

    def test_whitespace_scores_zero(self):
        self.assertEqual(0, score(" \t\n"))

    def test_scores_very_short_word(self):
        self.assertEqual(1, score('a'))

    def test_scores_other_very_short_word(self):
        self.assertEqual(4, score('f'))

    def test_simple_word_scores_the_number_of_letters(self):
        self.assertEqual(6, score("street"))

    def test_complicated_word_scores_more(self):
        self.assertEqual(22, score("quirky"))

    def test_scores_are_case_insensitive(self):
        self.assertEqual(20, score("MULTIBILLIONAIRE"))

if __name__ == '__main__':
    unittest.main()
