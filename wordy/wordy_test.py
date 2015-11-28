import unittest

from wordy import calculate


class WordyTest(unittest.TestCase):

    def test_simple_add_1(self):
        self.assertEqual(18, calculate("What is 5 plus 13?"))

    def test_simple_add_2(self):
        self.assertEqual(-8, calculate("What is 5 plus -13?"))

    def test_simple_sub_1(self):
        self.assertEqual(6, calculate("What is 103 minus 97?"))

    def test_simple_sub_2(self):
        self.assertEqual(-6, calculate("What is 97 minus 103?"))

    def test_simple_mult(self):
        self.assertEqual(21, calculate("What is 7 multiplied by 3?"))

    def test_simple_div(self):
        self.assertEqual(9, calculate("What is 45 divided by 5?"))

    def test_add_negative_numbers(self):
        self.assertEqual(-11, calculate("What is -1 plus -10?"))

    def test_add_more_digits(self):
        self.assertEqual(45801, calculate("What is 123 plus 45678?"))

    def test_add_twice(self):
        self.assertEqual(4, calculate("What is 1 plus 2 plus 1?"))

    def test_add_then_subtract(self):
        self.assertEqual(14, calculate("What is 1 plus 5 minus -8?"))

    def test_subtract_twice(self):
        self.assertEqual(-7, calculate("What is 20 minus 14 minus 13?"))

    def test_multiply_twice(self):
        self.assertEqual(-12, calculate("What is 2 multiplied by -2 "
                                        "multiplied by 3?"))

    def test_add_then_multiply(self):
        self.assertEqual(-8, calculate("What is -3 plus 7 multiplied by -2?"))

    def test_divide_twice(self):
        self.assertEqual(
            16, calculate("What is -12000 divided by 25 divided by -30?"))

    def test_invalid_operation(self):
        self.assertRaises(ValueError, calculate, "What is 4 xor 7?")

    def test_missing_operation(self):
        self.assertRaises(ValueError, calculate, "What is 2 2 minus 3?")

    def test_missing_number(self):
        self.assertRaises(ValueError, calculate, "What is 7 plus "
                                                 "multiplied by -2?")

    def test_irrelevant_question(self):
        self.assertRaises(ValueError, calculate, "Which is greater, 3 or 2?")


if __name__ == '__main__':
    unittest.main()
