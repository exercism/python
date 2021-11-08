import unittest

from variable_length_quantity import (
    decode,
    encode,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class VariableLengthQuantityTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(encode([0x0]), [0x0])

    def test_arbitrary_single_byte(self):
        self.assertEqual(encode([0x40]), [0x40])

    def test_largest_single_byte(self):
        self.assertEqual(encode([0x7F]), [0x7F])

    def test_smallest_double_byte(self):
        self.assertEqual(encode([0x80]), [0x81, 0x0])

    def test_arbitrary_double_byte(self):
        self.assertEqual(encode([0x2000]), [0xC0, 0x0])

    def test_largest_double_byte(self):
        self.assertEqual(encode([0x3FFF]), [0xFF, 0x7F])

    def test_smallest_triple_byte(self):
        self.assertEqual(encode([0x4000]), [0x81, 0x80, 0x0])

    def test_arbitrary_triple_byte(self):
        self.assertEqual(encode([0x100000]), [0xC0, 0x80, 0x0])

    def test_largest_triple_byte(self):
        self.assertEqual(encode([0x1FFFFF]), [0xFF, 0xFF, 0x7F])

    def test_smallest_quadruple_byte(self):
        self.assertEqual(encode([0x200000]), [0x81, 0x80, 0x80, 0x0])

    def test_arbitrary_quadruple_byte(self):
        self.assertEqual(encode([0x8000000]), [0xC0, 0x80, 0x80, 0x0])

    def test_largest_quadruple_byte(self):
        self.assertEqual(encode([0xFFFFFFF]), [0xFF, 0xFF, 0xFF, 0x7F])

    def test_smallest_quintuple_byte(self):
        self.assertEqual(encode([0x10000000]), [0x81, 0x80, 0x80, 0x80, 0x0])

    def test_arbitrary_quintuple_byte(self):
        self.assertEqual(encode([0xFF000000]), [0x8F, 0xF8, 0x80, 0x80, 0x0])

    def test_maximum_32_bit_integer_input(self):
        self.assertEqual(encode([0xFFFFFFFF]), [0x8F, 0xFF, 0xFF, 0xFF, 0x7F])

    def test_two_single_byte_values(self):
        self.assertEqual(encode([0x40, 0x7F]), [0x40, 0x7F])

    def test_two_multi_byte_values(self):
        self.assertEqual(
            encode([0x4000, 0x123456]), [0x81, 0x80, 0x0, 0xC8, 0xE8, 0x56]
        )

    def test_many_multi_byte_values(self):
        self.assertEqual(
            encode([0x2000, 0x123456, 0xFFFFFFF, 0x0, 0x3FFF, 0x4000]),
            [
                0xC0,
                0x0,
                0xC8,
                0xE8,
                0x56,
                0xFF,
                0xFF,
                0xFF,
                0x7F,
                0x0,
                0xFF,
                0x7F,
                0x81,
                0x80,
                0x0,
            ],
        )

    def test_one_byte(self):
        self.assertEqual(decode([0x7F]), [0x7F])

    def test_two_bytes(self):
        self.assertEqual(decode([0xC0, 0x0]), [0x2000])

    def test_three_bytes(self):
        self.assertEqual(decode([0xFF, 0xFF, 0x7F]), [0x1FFFFF])

    def test_four_bytes(self):
        self.assertEqual(decode([0x81, 0x80, 0x80, 0x0]), [0x200000])

    def test_maximum_32_bit_integer(self):
        self.assertEqual(decode([0x8F, 0xFF, 0xFF, 0xFF, 0x7F]), [0xFFFFFFFF])

    def test_incomplete_sequence_causes_error(self):
        with self.assertRaises(ValueError) as err:
            decode([0xFF])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "incomplete sequence")

    def test_incomplete_sequence_causes_error_even_if_value_is_zero(self):
        with self.assertRaises(ValueError) as err:
            decode([0x80])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "incomplete sequence")

    def test_multiple_values(self):
        self.assertEqual(
            decode(
                [
                    0xC0,
                    0x0,
                    0xC8,
                    0xE8,
                    0x56,
                    0xFF,
                    0xFF,
                    0xFF,
                    0x7F,
                    0x0,
                    0xFF,
                    0x7F,
                    0x81,
                    0x80,
                    0x0,
                ]
            ),
            [0x2000, 0x123456, 0xFFFFFFF, 0x0, 0x3FFF, 0x4000],
        )
