# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/wordy/canonical-data.json
# File last updated on 2025-06-20

import unittest

from wordy import (
    answer,
)


class WordyTest(unittest.TestCase):
    def test_just_a_number(self):
        self.assertEqual(answer("What is 5?"), 5)

    def test_just_a_zero(self):
        self.assertEqual(answer("What is 0?"), 0)

    def test_just_a_negative_number(self):
        self.assertEqual(answer("What is -123?"), -123)

    def test_addition(self):
        self.assertEqual(answer("What is 1 plus 1?"), 2)

    def test_addition_with_a_left_hand_zero(self):
        self.assertEqual(answer("What is 0 plus 2?"), 2)

    def test_addition_with_a_right_hand_zero(self):
        self.assertEqual(answer("What is 3 plus 0?"), 3)

    def test_more_addition(self):
        self.assertEqual(answer("What is 53 plus 2?"), 55)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(answer("What is -1 plus -10?"), -11)

    def test_large_addition(self):
        self.assertEqual(answer("What is 123 plus 45678?"), 45801)

    def test_subtraction(self):
        self.assertEqual(answer("What is 4 minus -12?"), 16)

    def test_multiplication(self):
        self.assertEqual(answer("What is -3 multiplied by 25?"), -75)

    def test_division(self):
        self.assertEqual(answer("What is 33 divided by -3?"), -11)

    def test_multiple_additions(self):
        self.assertEqual(answer("What is 1 plus 1 plus 1?"), 3)

    def test_addition_and_subtraction(self):
        self.assertEqual(answer("What is 1 plus 5 minus -2?"), 8)

    def test_multiple_subtraction(self):
        self.assertEqual(answer("What is 20 minus 4 minus 13?"), 3)

    def test_subtraction_then_addition(self):
        self.assertEqual(answer("What is 17 minus 6 plus 3?"), 14)

    def test_multiple_multiplication(self):
        self.assertEqual(answer("What is 2 multiplied by -2 multiplied by 3?"), -12)

    def test_addition_and_multiplication(self):
        self.assertEqual(answer("What is -3 plus 7 multiplied by -2?"), -8)

    def test_multiple_division(self):
        self.assertEqual(answer("What is -12 divided by 2 divided by -3?"), 2)

    def test_unknown_operation(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 52 cubed?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "unknown operation")

    def test_reject_problem_missing_an_operand(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 1 plus?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")

    def test_reject_problem_with_no_operands_or_operators(self):
        with self.assertRaises(ValueError) as err:
            answer("What is?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")

    def test_reject_two_operations_in_a_row(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 1 plus plus 2?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")

    def test_reject_two_numbers_in_a_row(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 1 plus 2 1?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")

    def test_reject_postfix_notation(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 1 2 plus?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")

    def test_reject_prefix_notation(self):
        with self.assertRaises(ValueError) as err:
            answer("What is plus 1 2?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")

    # Additional tests for this track

    def test_missing_operation(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 2 2 minus 3?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")

    def test_missing_number(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 7 plus multiplied by -2?")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "syntax error")
