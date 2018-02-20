import unittest
from ddt import ddt, idata, unpack

from acronym import abbreviate


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

def create_case(name, *args):
    class AnnotatedCase(dict):
        pass
    case_args = ('phrase', 'expected')
    case = AnnotatedCase()
    setattr(case, '__name__', name)
    for k, v in zip(case_args, args):
        case[k] = v
    return case


def annotated_data(**kwargs):
    def dec(function):
        @idata(create_case(k, *v) for k, v in kwargs.items())
        def wrapper(*args, **kwargs):
            function(args[0], **args[1])
        return wrapper
    return dec


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
