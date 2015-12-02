"""Tests for the binary exercise

Implementation note:
If the argument to parse_binary isn't a valid binary number the
function should raise a ValueError with a meaningful error message.
"""
import unittest

from binary import parse_binary


class BinaryTests(unittest.TestCase):

    def test_binary_1_is_decimal_1(self):
        self.assertEqual(1, parse_binary("1"))

    def test_binary_10_is_decimal_2(self):
        self.assertEqual(2, parse_binary("10"))

    def test_binary_11_is_decimal_3(self):
        self.assertEqual(3, parse_binary("11"))

    def test_binary_100_is_decimal_4(self):
        self.assertEqual(4, parse_binary("100"))

    def test_binary_1001_is_decimal_9(self):
        self.assertEqual(9, parse_binary("1001"))

    def test_binary_11010_is_decimal_26(self):
        self.assertEqual(26, parse_binary("11010"))

    def test_binary_10001101000_is_decimal_1128(self):
        self.assertEqual(1128, parse_binary("10001101000"))

    def test_invalid_binary_text_only(self):
        self.assertRaises(ValueError, parse_binary, "carrot")

    def test_invalid_binary_number_not_base2(self):
        self.assertRaises(ValueError, parse_binary, "102011")

    def test_invalid_binary_numbers_with_text(self):
        self.assertRaises(ValueError, parse_binary, "10nope")

    def test_invalid_binary_text_with_numbers(self):
        self.assertRaises(ValueError, parse_binary, "nope10")

if __name__ == '__main__':
    unittest.main()
