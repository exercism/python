import unittest

from acronym import abbreviate


class AcronymTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual('PNG', abbreviate('Portable Network Graphics'))

    def test_lowercase_words(self):
        self.assertEqual('ROR', abbreviate('Ruby on Rails'))

    def test_camelcase(self):
        self.assertEqual('HTML', abbreviate('HyperText Markup Language'))

    def test_punctuation(self):
        self.assertEqual('FIFO', abbreviate('First In, First Out'))

    def test_all_caps_words(self):
        self.assertEqual('PHP', abbreviate('PHP: Hypertext Preprocessor'))

    def test_hyphenated(self):
        self.assertEqual('CMOS', abbreviate('Complementary metal-oxide semiconductor'))


if __name__ == '__main__':
    unittest.main()
