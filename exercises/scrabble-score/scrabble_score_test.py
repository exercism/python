import unittest

from scrabble_score import score


class WordTest(unittest.TestCase):
    def test_invalid_word_scores_zero(self):
        self.assertEqual(score(''), 0)
        self.assertEqual(score(' \t\n'), 0)
        self.assertEqual(score('hous3'), 0)
        self.assertEqual(score('wo rd'), 0)

    def test_scores_very_short_word(self):
        self.assertEqual(score('a'), 1)

    def test_scores_other_very_short_word(self):
        self.assertEqual(score('f'), 4)

    def test_simple_word_scores_the_number_of_letters(self):
        self.assertEqual(score("street"), 6)

    def test_complicated_word_scores_more(self):
        self.assertEqual(score("quirky"), 22)

    def test_scores_are_case_insensitive(self):
        self.assertEqual(score("OxyphenButazone"), 41)


if __name__ == '__main__':
    unittest.main()
