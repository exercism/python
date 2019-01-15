# -*- coding: utf-8 -*-

import unittest

from luhn import Luhn


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

class LuhnTest(unittest.TestCase):
    def test_single_digit_strings_can_not_be_valid(self):
        self.assertIs(Luhn("1").is_valid(), False)

    def test_a_single_zero_is_invalid(self):
        self.assertIs(Luhn("0").is_valid(), False)

    def test_a_simple_valid_SIN_that_remains_valid_if_reversed(self):
        self.assertIs(Luhn("059").is_valid(), True)

    def test_a_simple_valid_SIN_that_becomes_invalid_if_reversed(self):
        self.assertIs(Luhn("59").is_valid(), True)

    def test_a_valid_Canadian_SIN(self):
        self.assertIs(Luhn("055 444 285").is_valid(), True)

    def test_invalid_Canadian_SIN(self):
        self.assertIs(Luhn("055 444 286").is_valid(), False)

    def test_invalid_credit_card(self):
        self.assertIs(Luhn("8273 1232 7352 0569").is_valid(), False)

    def test_valid_number_with_an_even_number_of_digits(self):
        self.assertIs(Luhn("095 245 88").is_valid(), True)

    def test_valid_strings_with_a_non_digit_included_become_invalid(self):
        self.assertIs(Luhn("055a 444 285").is_valid(), False)

    def test_valid_strings_with_non_digit_added_at_end_become_invalid(self):
        self.assertIs(Luhn("059a").is_valid(), False)

    def test_valid_strings_with_punctuation_included_become_invalid(self):
        self.assertIs(Luhn("055-444-285").is_valid(), False)

    def test_valid_strings_with_symbols_included_become_invalid(self):
        self.assertIs(Luhn("055£ 444$ 285").is_valid(), False)

    def test_single_zero_with_space_is_invalid(self):
        self.assertIs(Luhn(" 0").is_valid(), False)

    def test_more_than_a_single_zero_is_valid(self):
        self.assertIs(Luhn("0000 0").is_valid(), True)

    def test_input_digit_9_is_correctly_converted_to_output_digit_9(self):
        self.assertIs(Luhn("091").is_valid(), True)

    def test_strings_with_non_digits_is_invalid(self):
        self.assertIs(Luhn(":9").is_valid(), False)

    def test_is_valid_can_be_called_repeatedly(self):
        # Additional track specific test case
        # This test was added, because we saw many implementations
        # in which the first call to is_valid() worked, but the
        # second call failed().
        number = Luhn("055 444 285")
        self.assertIs(number.is_valid(), True)
        self.assertIs(number.is_valid(), True)


if __name__ == '__main__':
    unittest.main()
