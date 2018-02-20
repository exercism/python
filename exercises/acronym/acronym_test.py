import unittest
from ddt import ddt, data, unpack

from acronym import abbreviate


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

class AnnotatedCase(dict):
    case_args = ('phrase', 'expected')

    def __init__(self, name, *args):
        setattr(self, '__name__', name)
        for k, v in zip(AnnotatedCase.case_args, args):
            self[k] = v


@ddt
class AcronymTest(unittest.TestCase):
    @data(
        AnnotatedCase('basic', "Portable Network Graphics", 'PNG'),
        AnnotatedCase('lowercase words', 'Ruby on Rails', 'ROR'),
        AnnotatedCase('punctuation', 'First In, First Out', 'FIFO'),
        AnnotatedCase(
            'all caps word',
            'GNU Image Manipulation Program',
            'GIMP'
        ),
        AnnotatedCase(
            'punctuation without whitespace',
            'Complementary metal-oxide semiconductor',
            'CMOS'
        ),
    )
    @unpack
    def test_abbreviate(self, phrase, expected):
        self.assertEqual(abbreviate(phrase), expected)


if __name__ == '__main__':
    unittest.main()
