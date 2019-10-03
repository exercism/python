import unittest

from armstrong_numbers import is_armstrong_number

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class ArmstrongNumbersTest(unittest.TestCase):
    def test_zero_is_an_armstrong_number(self):
        input = 0
        expected = True
        self.assertEqual(is_armstrong_number(input), expected)

    def test_single_digit_numbers_are_armstrong_numbers(self):
        input = 5
        expected = True
        self.assertEqual(is_armstrong_number(input), expected)

    def test_there_are_no_2_digit_armstrong_numbers(self):
        input = 10
        expected = False
        self.assertEqual(is_armstrong_number(input), expected)

    def test_three_digit_number_that_is_an_armstrong_number(self):
        input = 153
        expected = True
        self.assertEqual(is_armstrong_number(input), expected)

    def test_three_digit_number_that_is_not_an_armstrong_number(self):
        input = 100
        expected = False
        self.assertEqual(is_armstrong_number(input), expected)

    def test_four_digit_number_that_is_an_armstrong_number(self):
        input = 9474
        expected = True
        self.assertEqual(is_armstrong_number(input), expected)

    def test_four_digit_number_that_is_not_an_armstrong_number(self):
        input = 9475
        expected = False
        self.assertEqual(is_armstrong_number(input), expected)

    def test_seven_digit_number_that_is_an_armstrong_number(self):
        input = 9926315
        expected = True
        self.assertEqual(is_armstrong_number(input), expected)

    def test_seven_digit_number_that_is_not_an_armstrong_number(self):
        input = 9926314
        expected = False
        self.assertEqual(is_armstrong_number(input), expected)


if __name__ == "__main__":
    unittest.main()
