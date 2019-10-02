import unittest

from wordy import answer

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0


class WordyTest(unittest.TestCase):
    def test_just_a_number(self):
        value = "What is 5?"
        expected = 5
        self.assertEqual(answer(value), expected)

    def test_addition(self):
        value = "What is 1 plus 1?"
        expected = 2
        self.assertEqual(answer(value), expected)

    def test_more_addition(self):
        value = "What is 53 plus 2?"
        expected = 55
        self.assertEqual(answer(value), expected)

    def test_addition_with_negative_numbers(self):
        value = "What is -1 plus -10?"
        expected = -11
        self.assertEqual(answer(value), expected)

    def test_large_addition(self):
        value = "What is 123 plus 45678?"
        expected = 45801
        self.assertEqual(answer(value), expected)

    def test_subtraction(self):
        value = "What is 4 minus -12?"
        expected = 16
        self.assertEqual(answer(value), expected)

    def test_multiplication(self):
        value = "What is -3 multiplied by 25?"
        expected = -75
        self.assertEqual(answer(value), expected)

    def test_division(self):
        value = "What is 33 divided by -3?"
        expected = -11
        self.assertEqual(answer(value), expected)

    def test_multiple_additions(self):
        value = "What is 1 plus 1 plus 1?"
        expected = 3
        self.assertEqual(answer(value), expected)

    def test_addition_and_subtraction(self):
        value = "What is 1 plus 5 minus -2?"
        expected = 8
        self.assertEqual(answer(value), expected)

    def test_multiple_subtraction(self):
        value = "What is 20 minus 4 minus 13?"
        expected = 3
        self.assertEqual(answer(value), expected)

    def test_subtraction_then_addition(self):
        value = "What is 17 minus 6 plus 3?"
        expected = 14
        self.assertEqual(answer(value), expected)

    def test_multiple_multiplication(self):
        value = "What is 2 multiplied by -2 multiplied by 3?"
        expected = -12
        self.assertEqual(answer(value), expected)

    def test_addition_and_multiplication(self):
        value = "What is -3 plus 7 multiplied by -2?"
        expected = -8
        self.assertEqual(answer(value), expected)

    def test_multiple_division(self):
        value = "What is -12 divided by 2 divided by -3?"
        expected = 2
        self.assertEqual(answer(value), expected)

    def test_unknown_operation(self):
        value = "What is 52 cubed?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    def test_non_math_question(self):
        value = "Who is the President of the United States?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    def test_reject_problem_missing_an_operand(self):
        value = "What is 1 plus?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    def test_reject_problem_with_no_operands_or_operators(self):
        value = "What is?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    def test_reject_two_operations_in_a_row(self):
        value = "What is 1 plus plus 2?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    def test_reject_two_numbers_in_a_row(self):
        value = "What is 1 plus 2 1?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    def test_reject_postfix_notation(self):
        value = "What is 1 2 plus?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    def test_reject_prefix_notation(self):
        value = "What is plus 1 2?"
        with self.assertRaisesWithMessage(ValueError):
            answer(value)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
