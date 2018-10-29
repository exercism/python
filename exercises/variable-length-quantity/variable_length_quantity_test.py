import unittest

from variable_length_quantity import encode, decode


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class VariableLengthQuantityTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(encode([0x0]), [0x0])

    def test_arbitrary_single_byte(self):
        self.assertEqual(encode([0x40]), [0x40])

    def test_largest_single_byte(self):
        self.assertEqual(encode([0x7f]), [0x7f])

    def test_smallest_double_byte(self):
        self.assertEqual(encode([0x80]), [0x81, 0x0])

    def test_arbitrary_double_byte(self):
        self.assertEqual(encode([0x2000]), [0xc0, 0x0])

    def test_largest_double_byte(self):
        self.assertEqual(encode([0x3fff]), [0xff, 0x7f])

    def test_smallest_triple_byte(self):
        self.assertEqual(encode([0x4000]), [0x81, 0x80, 0x0])

    def test_arbitrary_triple_byte(self):
        self.assertEqual(encode([0x100000]), [0xc0, 0x80, 0x0])

    def test_largest_triple_byte(self):
        self.assertEqual(encode([0x1fffff]), [0xff, 0xff, 0x7f])

    def test_smallest_quadruple_byte(self):
        self.assertEqual(encode([0x200000]), [0x81, 0x80, 0x80, 0x0])

    def test_arbitrary_quadruple_byte(self):
        self.assertEqual(encode([0x8000000]), [0xc0, 0x80, 0x80, 0x0])

    def test_largest_quadruple_byte(self):
        self.assertEqual(encode([0xfffffff]), [0xff, 0xff, 0xff, 0x7f])

    def test_smallest_quintuple_byte(self):
        self.assertEqual(encode([0x10000000]), [0x81, 0x80, 0x80, 0x80, 0x0])

    def test_arbitrary_quintuple_byte(self):
        self.assertEqual(encode([0xff000000]), [0x8f, 0xf8, 0x80, 0x80, 0x0])

    def test_maximum_32_bit_integer_input(self):
        self.assertEqual(encode([0xffffffff]), [0x8f, 0xff, 0xff, 0xff, 0x7f])

    def test_two_single_byte_values(self):
        self.assertEqual(encode([0x40, 0x7f]), [0x40, 0x7f])

    def test_two_multi_byte_values(self):
        self.assertEqual(
            encode([0x4000, 0x123456]), [0x81, 0x80, 0x0, 0xc8, 0xe8, 0x56])

    def test_many_multi_byte_values(self):
        self.assertEqual(
            encode([0x2000, 0x123456, 0xfffffff, 0x0, 0x3fff, 0x4000]),
            [0xc0, 0x0, 0xc8, 0xe8, 0x56, 0xff, 0xff, 0xff, 0x7f, 0x0, 0xff,
             0x7f, 0x81, 0x80, 0x0]
        )

    def test_one_byte(self):
        self.assertEqual(decode([0x7f]), [0x7f])

    def test_two_bytes(self):
        self.assertEqual(decode([0xc0, 0x0]), [0x2000])

    def test_three_bytes(self):
        self.assertEqual(decode([0xff, 0xff, 0x7f]), [0x1fffff])

    def test_four_bytes(self):
        self.assertEqual(decode([0x81, 0x80, 0x80, 0x0]), [0x200000])

    def test_maximum_32_bit_integer(self):
        self.assertEqual(decode([0x8f, 0xff, 0xff, 0xff, 0x7f]), [0xffffffff])

    def test_incomplete_sequence_causes_error(self):
        with self.assertRaisesWithMessage(ValueError):
            decode([0xff])

    def test_incomplete_sequence_causes_error_even_if_value_is_zero(self):
        with self.assertRaisesWithMessage(ValueError):
            decode([0x80])

    def test_multiple_values(self):
        self.assertEqual(
            decode([0xc0, 0x0, 0xc8, 0xe8, 0x56, 0xff, 0xff, 0xff, 0x7f,
                    0x0, 0xff, 0x7f, 0x81, 0x80, 0x0]),
            [0x2000, 0x123456, 0xfffffff, 0x0, 0x3fff, 0x4000]
        )

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
