import unittest
from ddt import ddt, data, unpack

from all_your_base import rebase


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.3.0


class AnnotatedCase(dict):
    case_args = ('input_base', 'digits', 'output_base', 'expected')

    def __init__(self, name, *args):
        setattr(self, '__name__', name)
        for k, v in zip(AnnotatedCase.case_args, args):
            self[k] = v


@ddt
class AllYourBaseTests(unittest.TestCase):
    @data(
        AnnotatedCase('single bit to one decimal', 2, [1], 10, [1]),
        AnnotatedCase('binary to single decimal', 2, [1, 0, 1], 10, [5]),
        AnnotatedCase('single decimal to binary', 10, [5], 2, [1, 0, 1]),
        AnnotatedCase(
            'binary to multiple decimal',
            2, [1, 0, 1, 0, 1, 0], 10, [4, 2]
        ),
        AnnotatedCase('decimal to binary', 10, [4, 2], 2, [1, 0, 1, 0, 1, 0]),
        AnnotatedCase('trinary to hexadecimal', 3, [1, 1, 2, 0], 16, [2, 10]),
        AnnotatedCase('hexadecimal to trinary', 16, [2, 10], 3, [1, 1, 2, 0]),
        AnnotatedCase('15 bit integer', 97, [3, 46, 60], 73, [6, 10, 45]),
        AnnotatedCase('empty list', 2, [], 10, []),
        AnnotatedCase('single zero', 10, [0], 2, []),
        AnnotatedCase('multiple zeros', 10, [0, 0, 0], 2, []),
        AnnotatedCase('leading zeros', 7, [0, 6, 0], 10, [4, 2])
    )
    @unpack
    def test_rebase(self, input_base, digits, output_base, expected):
        self.assertEqual(
            rebase(input_base, digits, output_base),
            expected
        )

    @data(
        AnnotatedCase('base is one', 1, [0], 10),
        AnnotatedCase('base is zero', 0, [], 10),
        AnnotatedCase('base is negative', -2, [1], 10),
        AnnotatedCase('negative digit', 2, [1, -1, 1, 0, 1, 0], 10),
        AnnotatedCase('invalid positive digit', 2, [1, 2, 1, 0, 1, 0], 10),
        AnnotatedCase('output base is one', 2, [1, 0, 1, 0, 1, 0], 1),
        AnnotatedCase('output base is zero', 10, [7], 0),
        AnnotatedCase('output base is negative', 2, [1], -7),
        AnnotatedCase('bot hbase are negative', -2, [1], -7),
    )
    @unpack
    def test_rebase_error(self, input_base, digits, output_base):
        with self.assertRaisesWithMessage(ValueError):
            rebase(input_base, digits, output_base)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
