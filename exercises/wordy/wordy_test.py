import unittest

from wordy import answer

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0


class WordyTest(unittest.TestCase):
    def test_just_a_number(self):
        value = "What is 5?"
        self.assertEqual(answer("What is 5?"), 5)

    def test_addition(self):
        value = "What is 1 plus 1?"
        self.assertEqual(answer("What is 1 plus 1?"), 2)

    def test_more_addition(self):
        value = "What is 53 plus 2?"
        self.assertEqual(answer("What is 53 plus 2?"), 55)

    def test_addition_with_negative_numbers(self):
        value = "What is -1 plus -10?"
        self.assertEqual(answer("What is -1 plus -10?"), -11)

    def test_large_addition(self):
        value = "What is 123 plus 45678?"
        self.assertEqual(answer("What is 123 plus 45678?"), 45801)

    def test_subtraction(self):
        value = "What is 4 minus -12?"
        self.assertEqual(answer("What is 4 minus -12?"), 16)

    def test_multiplication(self):
        value = "What is -3 multiplied by 25?"
        self.assertEqual(answer("What is -3 multiplied by 25?"), -75)

    def test_division(self):
        value = "What is 33 divided by -3?"
        self.assertEqual(answer("What is 33 divided by -3?"), -11)

    def test_multiple_additions(self):
        value = "What is 1 plus 1 plus 1?"
        self.assertEqual(answer("What is 1 plus 1 plus 1?"), 3)

    def test_addition_and_subtraction(self):
        value = "What is 1 plus 5 minus -2?"
        self.assertEqual(answer("What is 1 plus 5 minus -2?"), 8)

    def test_multiple_subtraction(self):
        value = "What is 20 minus 4 minus 13?"
        self.assertEqual(answer("What is 20 minus 4 minus 13?"), 3)

    def test_subtraction_then_addition(self):
        value = "What is 17 minus 6 plus 3?"
        self.assertEqual(answer("What is 17 minus 6 plus 3?"), 14)

    def test_multiple_multiplication(self):
        value = "What is 2 multiplied by -2 multiplied by 3?"
        self.assertEqual(answer("What is 2 multiplied by -2 multiplied by 3?"), -12)

    def test_addition_and_multiplication(self):
        value = "What is -3 plus 7 multiplied by -2?"
        self.assertEqual(answer("What is -3 plus 7 multiplied by -2?"), -8)

    def test_multiple_division(self):
        value = "What is -12 divided by 2 divided by -3?"
        self.assertEqual(answer("What is -12 divided by 2 divided by -3?"), 2)

    def test_unknown_operation(self):
        value = "What is 52 cubed?"
        with self.assertRaisesWithMessage(ValueError):
            answer("What is 52 cubed?")

    def test_non_math_question(self):
        value = "Who is the President of the United States?"
        with self.assertRaisesWithMessage(ValueError):
            answer("Who is the President of the United States?")

    def test_reject_problem_missing_an_operand(self):
        value = "What is 1 plus?"
        with self.assertRaisesWithMessage(ValueError):
            answer("What is 1 plus?")

    def test_reject_problem_with_no_operands_or_operators(self):
        value = "What is?"
        with self.assertRaisesWithMessage(ValueError):
            answer("What is?")

    def test_reject_two_operations_in_a_row(self):
        value = "What is 1 plus plus 2?"
        with self.assertRaisesWithMessage(ValueError):
            answer("What is 1 plus plus 2?")

    def test_reject_two_numbers_in_a_row(self):
        value = "What is 1 plus 2 1?"
        with self.assertRaisesWithMessage(ValueError):
            answer("What is 1 plus 2 1?")

    def test_reject_postfix_notation(self):
        value = "What is 1 2 plus?"
        with self.assertRaisesWithMessage(ValueError):
            answer("What is 1 2 plus?")

    def test_reject_prefix_notation(self):
        value = "What is plus 1 2?"
        with self.assertRaisesWithMessage(ValueError):
            answer("What is plus 1 2?")

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
