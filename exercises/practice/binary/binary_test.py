"""Tests for the binary exercise

Implementation note:
If the argument to parse_binary isn't a valid binary number the
function should raise a ValueError with a meaningful error message.
"""
import unittest

from binary import parse_binary


class BinaryTest(unittest.TestCase):
    def test_binary_1_is_decimal_1(self):
        self.assertEqual(parse_binary("1"), 1)

    def test_binary_10_is_decimal_2(self):
        self.assertEqual(parse_binary("10"), 2)

    def test_binary_11_is_decimal_3(self):
        self.assertEqual(parse_binary("11"), 3)

    def test_binary_100_is_decimal_4(self):
        self.assertEqual(parse_binary("100"), 4)

    def test_binary_1001_is_decimal_9(self):
        self.assertEqual(parse_binary("1001"), 9)

    def test_binary_11010_is_decimal_26(self):
        self.assertEqual(parse_binary("11010"), 26)

    def test_binary_10001101000_is_decimal_1128(self):
        self.assertEqual(parse_binary("10001101000"), 1128)

    def test_invalid_binary_text_only(self):
        with self.assertRaises(ValueError) as err:
            parse_binary("carrot")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid binary literal: carrot")

    def test_invalid_binary_number_not_base2(self):
        with self.assertRaises(ValueError) as err:
            parse_binary("102011")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid binary literal: 102011")

    def test_invalid_binary_numbers_with_text(self):
        with self.assertRaises(ValueError) as err:
            parse_binary("10nope")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid binary literal: 10nope")

    def test_invalid_binary_text_with_numbers(self):
        with self.assertRaises(ValueError) as err:
            parse_binary("nope10")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid binary literal: nope10")

if __name__ == '__main__':
    unittest.main()
