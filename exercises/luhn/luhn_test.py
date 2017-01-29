import unittest

from luhn import Luhn


class LuhnTests(unittest.TestCase):
    def test_single_digit_strings_can_not_be_valid(self):
        self.assertFalse(Luhn("1").is_valid())

    def test_a_single_zero_is_invalid(self):
        self.assertFalse(Luhn("0").is_valid())

    def test_valid_Canadian_SIN(self):
        self.assertTrue(Luhn("046 454 286").is_valid())

    def test_invalid_Canadian_SIN(self):
        self.assertFalse(Luhn("046 454 287").is_valid())

    def test_invalid_credit_card(self):
        self.assertFalse(Luhn("8273 1232 7352 0569").is_valid())

    def test_valid_strings_with_a_non_digit_added_become_invalid(self):
        self.assertFalse(Luhn("046a 454 286").is_valid())


if __name__ == '__main__':
    unittest.main()
