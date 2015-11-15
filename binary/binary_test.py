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

    @unittest.skip('not yet implemented')
    def test_binary_10_is_decimal_2(self):
        self.assertEqual(2, parse_binary("10"))

    @unittest.skip('not yet implemented')
    def test_binary_11_is_decimal_3(self):
        self.assertEqual(3, parse_binary("11"))

    @unittest.skip('not yet implemented')
    def test_binary_100_is_decimal_4(self):
        self.assertEqual(4, parse_binary("100"))

    @unittest.skip('not yet implemented')
    def test_binary_1001_is_decimal_9(self):
        self.assertEqual(9, parse_binary("1001"))

    @unittest.skip('not yet implemented')
    def test_binary_11010_is_decimal_26(self):
        self.assertEqual(26, parse_binary("11010"))

    @unittest.skip('not yet implemented')
    def test_binary_10001101000_is_decimal_1128(self):
        self.assertEqual(1128, parse_binary("10001101000"))

    @unittest.skip('not yet implemented')
    def test_invalid_binary_raises_error(self):
        self.assertRaises(ValueError, parse_binary, "carrot")

    @unittest.skip('not yet implemented')
    def test_invalid_binary_raises_error_2(self):
        self.assertRaises(ValueError, parse_binary, "102011")

if __name__ == '__main__':
    unittest.main()
