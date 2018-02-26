import unittest
from ddt import ddt, unpack
from ddt_ext import annotated_data

from acronym import abbreviate


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

@ddt
class AcronymTest(unittest.TestCase):
    @annotated_data(
        basic=['Portable Network Graphics', 'PNG'],
        lowercase_words=['Ruby on Rails', 'ROR'],
        punctuation=['First In, First Out', 'FIFO'],
        all_caps_word=['GNU Image Manipulation Program', 'GIMP'],
        punctuation_without_whitespace=[
            'Complementary metal-oxide semiconductor',
            'CMOS'
        ],
    )
    @unpack
    def test_abbreviate(self, phrase, expected):
        self.assertEqual(abbreviate(phrase), expected)


if __name__ == '__main__':
    unittest.main()
