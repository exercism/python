import unittest

from phone_number import PhoneNumber

# Tests adapted from `problem-specifications//canonical-data.json`


class PhoneNumberTest(unittest.TestCase):
    def test_cleans_the_number(self):
        number = PhoneNumber("(223) 456-7890").number
        self.assertEqual(number, "2234567890")

    def test_cleans_numbers_with_dots(self):
        number = PhoneNumber("223.456.7890").number
        self.assertEqual(number, "2234567890")

    def test_cleans_numbers_with_multiple_spaces(self):
        number = PhoneNumber("223 456   7890   ").number
        self.assertEqual(number, "2234567890")

    def test_invalid_when_9_digits(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("123456789")

    def test_invalid_when_11_digits_does_not_start_with_a_1(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("22234567890")

    def test_valid_when_11_digits_and_starting_with_1(self):
        number = PhoneNumber("12234567890").number
        self.assertEqual(number, "2234567890")

    def test_valid_when_11_digits_and_starting_with_1_even_with_punctuation(self):
        number = PhoneNumber("+1 (223) 456-7890").number
        self.assertEqual(number, "2234567890")

    def test_invalid_when_more_than_11_digits(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("321234567890")

    def test_invalid_with_letters(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("123-abc-7890")

    def test_invalid_with_punctuations(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("123-@:!-7890")

    def test_invalid_if_area_code_starts_with_0(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("(023) 456-7890")

    def test_invalid_if_area_code_starts_with_1(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("(123) 456-7890")

    def test_invalid_if_exchange_code_starts_with_0(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("(223) 056-7890")

    def test_invalid_if_exchange_code_starts_with_1(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("(223) 156-7890")

    def test_invalid_if_area_code_starts_with_0_on_valid_11_digit_number(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("1 (023) 456-7890")

    def test_invalid_if_area_code_starts_with_1_on_valid_11_digit_number(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("1 (123) 456-7890")

    def test_invalid_if_exchange_code_starts_with_0_on_valid_11_digit_number(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("1 (223) 056-7890")

    def test_invalid_if_exchange_code_starts_with_1_on_valid_11_digit_number(self):
        with self.assertRaisesWithMessage(ValueError):
            PhoneNumber("1 (223) 156-7890")

    # Additional tests for this track
    def test_area_code(self):
        number = PhoneNumber("2234567890")
        self.assertEqual(number.area_code, "223")

    def test_pretty_print(self):
        number = PhoneNumber("2234567890")
        self.assertEqual(number.pretty(), "(223)-456-7890")

    def test_pretty_print_with_full_us_phone_number(self):
        number = PhoneNumber("12234567890")
        self.assertEqual(number.pretty(), "(223)-456-7890")

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
