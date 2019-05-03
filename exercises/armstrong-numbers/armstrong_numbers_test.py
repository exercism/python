import unittest

from armstrong_numbers import is_armstrong_number


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class ArmstrongNumbersTest(unittest.TestCase):

    def test_zero_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(0), True)

    def test_single_digit_numbers_are_armstrong_numbers(self):
        self.assertIs(is_armstrong_number(5), True)

    def test_there_are_no_two_digit_armstrong_numbers(self):
        self.assertIs(is_armstrong_number(10), False)

    def test_three_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(153), True)

    def test_three_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(100), False)

    def test_four_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(9474), True)

    def test_four_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(9475), False)

    def test_seven_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(9926315), True)

    def test_seven_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(9926314), False)


if __name__ == '__main__':
    unittest.main()
