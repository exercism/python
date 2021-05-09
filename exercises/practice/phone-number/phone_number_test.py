import unittest

from phone_number import (
    PhoneNumber,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class PhoneNumberTest(unittest.TestCase):

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
