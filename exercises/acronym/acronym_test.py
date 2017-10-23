import unittest

from acronym import abbreviate


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class AcronymTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(abbreviate('Portable Network Graphics'), 'PNG')

    def test_lowercase_words(self):
        self.assertEqual(abbreviate('Ruby on Rails'), 'ROR')

    def test_punctuation(self):
        self.assertEqual(abbreviate('First In, First Out'), 'FIFO')

    def test_all_caps_words(self):
        self.assertEqual(abbreviate('PHP: Hypertext Preprocessor'), 'PHP')

    def test_non_acronym_all_caps_word(self):
        self.assertEqual(abbreviate('GNU Image Manipulation Program'), 'GIMP')

    def test_hyphenated(self):
        self.assertEqual(
            abbreviate('Complementary metal-oxide semiconductor'), 'CMOS')


if __name__ == '__main__':
    unittest.main()
