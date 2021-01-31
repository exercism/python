import unittest

from luhn import (
    Luhn,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class LuhnTest(unittest.TestCase):
    def test_single_digit_strings_can_not_be_valid(self):
        self.assertIs(Luhn("1").valid(), False)

    def test_a_single_zero_is_invalid(self):
        self.assertIs(Luhn("0").valid(), False)

    def test_a_simple_valid_sin_that_remains_valid_if_reversed(self):
        self.assertIs(Luhn("059").valid(), True)

    def test_a_simple_valid_sin_that_becomes_invalid_if_reversed(self):
        self.assertIs(Luhn("59").valid(), True)

    def test_a_valid_canadian_sin(self):
        self.assertIs(Luhn("055 444 285").valid(), True)

    def test_invalid_canadian_sin(self):
        self.assertIs(Luhn("055 444 286").valid(), False)

    def test_invalid_credit_card(self):
        self.assertIs(Luhn("8273 1232 7352 0569").valid(), False)

    def test_invalid_long_number_with_an_even_remainder(self):
        self.assertIs(Luhn("1 2345 6789 1234 5678 9012").valid(), False)

    def test_valid_number_with_an_even_number_of_digits(self):
        self.assertIs(Luhn("095 245 88").valid(), True)

    def test_valid_number_with_an_odd_number_of_spaces(self):
        self.assertIs(Luhn("234 567 891 234").valid(), True)

    def test_valid_strings_with_a_non_digit_added_at_the_end_become_invalid(self):
        self.assertIs(Luhn("059a").valid(), False)

    def test_valid_strings_with_punctuation_included_become_invalid(self):
        self.assertIs(Luhn("055-444-285").valid(), False)

    def test_valid_strings_with_symbols_included_become_invalid(self):
        self.assertIs(Luhn("055# 444$ 285").valid(), False)

    def test_single_zero_with_space_is_invalid(self):
        self.assertIs(Luhn(" 0").valid(), False)

    def test_more_than_a_single_zero_is_valid(self):
        self.assertIs(Luhn("0000 0").valid(), True)

    def test_input_digit_9_is_correctly_converted_to_output_digit_9(self):
        self.assertIs(Luhn("091").valid(), True)

    def test_using_ascii_value_for_non_doubled_non_digit_isn_t_allowed(self):
        self.assertIs(Luhn("055b 444 285").valid(), False)

    def test_using_ascii_value_for_doubled_non_digit_isn_t_allowed(self):
        self.assertIs(Luhn(":9").valid(), False)

    # Additional tests for this track

    def test_is_valid_can_be_called_repeatedly(self):
        # This test was added, because we saw many implementations
        # in which the first call to valid() worked, but the
        # second call failed().
        number = Luhn("055 444 285")
        self.assertIs(number.valid(), True)
        self.assertIs(number.valid(), True)


if __name__ == "__main__":
    unittest.main()
