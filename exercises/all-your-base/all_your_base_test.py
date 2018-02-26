import unittest
from ddt import ddt, unpack
from ddt_ext import annotated_data

from all_your_base import rebase


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.3.0


@ddt
class AllYourBaseTests(unittest.TestCase):
    @annotated_data(
        single_bit_to_one_decimal=(2, [1], 10, [1]),
        binary_to_single_decimal=(2, [1, 0, 1], 10, [5]),
        single_decimal_to_binary=(10, [5], 2, [1, 0, 1]),
        binary_to_multiple_decimal=(2, [1, 0, 1, 0, 1, 0], 10, [4, 2]),
        decimal_to_binary=(10, [4, 2], 2, [1, 0, 1, 0, 1, 0]),
        trinary_to_hexadecimal=(3, [1, 1, 2, 0], 16, [2, 10]),
        hexadecimal_to_trinary=(16, [2, 10], 3, [1, 1, 2, 0]),
        fifteen_bit_integer=(97, [3, 46, 60], 73, [6, 10, 45]),
        empty_list=(2, [], 10, []),
        single_zero=(10, [0], 2, []),
        multiple_zeros=(10, [0, 0, 0], 2, []),
        leading_zeros=(7, [0, 6, 0], 10, [4, 2]),
    )
    @unpack
    def test_rebase(self, input_base, digits, output_base, expected):
        self.assertEqual(
            rebase(input_base, digits, output_base),
            expected
        )

    @annotated_data(
        base_is_one=(1, [0], 10),
        base_is_zero=(0, [], 10),
        base_is_negative=(-2, [1], 10),
        negative_digit=(2, [1, -1, 1, 0, 1, 0], 10),
        invalid_positive_digit=(2, [1, 2, 1, 0, 1, 0], 10),
        output_base_is_one=(2, [1, 0, 1, 0, 1, 0], 1),
        output_base_is_zero=(10, [7], 0),
        output_base_is_negative=(2, [1], -7),
        both_bases_are_negative=(-2, [1], -7),
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
