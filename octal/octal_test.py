"""Tests for the octal exercise

Implementation note:
If an instance of the Octal class is initialized with an invalid string,
it must raise a ValueError with a meaningful error message.
"""
import unittest

from octal import Octal


class OctalTest(unittest.TestCase):
    def test_octal_1_is_decimal_1(self):
        self.assertEqual(1, Octal("1").to_decimal())

    def test_octal_10_is_decimal_8(self):
        self.assertEqual(8, Octal("10").to_decimal())

    def test_octal_17_is_decimal_15(self):
        self.assertEqual(15, Octal("17").to_decimal())

    def test_octal_130_is_decimal_88(self):
        self.assertEqual(88, Octal("130").to_decimal())

    def test_octal_2047_is_decimal_1063(self):
        self.assertEqual(1063, Octal("2047").to_decimal())

    def test_octal_1234567_is_decimal_342391(self):
        self.assertEqual(342391, Octal("1234567").to_decimal())

    def test_8_is_seen_as_invalid(self):
        self.assertRaises(ValueError, Octal, "8")

    def test_invalid_octal_is_recognized(self):
        self.assertRaises(ValueError, Octal, "carrot")

    def test_6789_is_seen_as_invalid(self):
        self.assertRaises(ValueError, Octal, "6789")

    def test_valid_octal_formatted_string_011_is_decimal_9(self):
        self.assertEqual(9, Octal("011").to_decimal())


if __name__ == '__main__':
    unittest.main()
