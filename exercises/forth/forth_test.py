import unittest

from forth import evaluate, StackUnderflowError


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.7.0

class ForthUtilities(unittest.TestCase):
    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


class ForthParsingTest(ForthUtilities):
    def test_numbers_just_get_pushed_to_stack(self):
        input_data = ["1 2 3 4 5"]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(evaluate(input_data), expected)


class ForthAdditionTest(ForthUtilities):
    def test_can_add_two_numbers(self):
        input_data = ["1 2 +"]
        expected = [3]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["+"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 +"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthSubtractionTest(ForthUtilities):
    def test_can_subtract_two_numbers(self):
        input_data = ["3 4 -"]
        expected = [-1]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["-"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 -"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthMultiplicationTest(ForthUtilities):
    def test_can_multiply_two_numbers(self):
        input_data = ["2 4 *"]
        expected = [8]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["*"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 *"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthDivisionTest(ForthUtilities):
    def test_can_divide_two_numbers(self):
        input_data = ["12 3 /"]
        expected = [4]
        self.assertEqual(evaluate(input_data), expected)

    def test_performs_integer_division(self):
        input_data = ["8 3 /"]
        expected = [2]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_dividing_by_zero(self):
        input_data = ["4 0 /"]
        with self.assertRaisesWithMessage(ZeroDivisionError):
            evaluate(input_data)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["/"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 /"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthCombinedArithmeticTest(ForthUtilities):
    def test_addition_and_subtraction(self):
        input_data = ["1 2 + 4 -"]
        expected = [-1]
        self.assertEqual(evaluate(input_data), expected)

    def test_multiplication_and_division(self):
        input_data = ["2 4 * 3 /"]
        expected = [2]
        self.assertEqual(evaluate(input_data), expected)


class ForthDupTest(ForthUtilities):
    def test_copies_a_value_on_the_stack(self):
        input_data = ["1 dup"]
        expected = [1, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_copies_the_top_value_on_the_stack(self):
        input_data = ["1 2 dup"]
        expected = [1, 2, 2]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["dup"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthDropTest(ForthUtilities):
    def test_removes_the_top_value_on_the_stack_if_it_is_the_only_one(self):
        input_data = ["1 drop"]
        expected = []
        self.assertEqual(evaluate(input_data), expected)

    def test_removes_the_top_value_on_the_stack_if_it_not_the_only_one(self):
        input_data = ["3 4 drop"]
        expected = [3]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["drop"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthSwapTest(ForthUtilities):
    def test_swaps_only_two_values_on_stack(self):
        input_data = ["1 2 swap"]
        expected = [2, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_swaps_two_two_values_on_stack(self):
        input_data = ["1 2 3 swap"]
        expected = [1, 3, 2]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["swap"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 swap"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthOverTest(ForthUtilities):
    def test_copies_the_second_element_if_there_are_only_two(self):
        input_data = ["1 2 over"]
        expected = [1, 2, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_copies_the_second_element_if_there_are_more_than_two(self):
        input_data = ["1 2 3 over"]
        expected = [1, 2, 3, 2]
        self.assertEqual(evaluate(input_data), expected)

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["over"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 over"]
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(input_data)


class ForthUserDefinedWordsTest(ForthUtilities):
    def test_can_consist_of_built_in_words(self):
        input_data = [
            ": dup-twice dup dup ;",
            "1 dup-twice"
        ]
        expected = [1, 1, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_execute_in_the_right_order(self):
        input_data = [
            ": countup 1 2 3 ;",
            "countup"
        ]
        expected = [1, 2, 3]
        self.assertEqual(evaluate(input_data), expected)

    def test_can_override_other_user_defined_words(self):
        input_data = [
            ": foo dup ;",
            ": foo dup dup ;",
            "1 foo"
        ]
        expected = [1, 1, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_can_override_built_in_words(self):
        input_data = [
            ": swap dup ;",
            "1 swap"
        ]
        expected = [1, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_can_override_built_in_operators(self):
        input_data = [
            ": + * ;",
            "3 4 +"
        ]
        expected = [12]
        self.assertEqual(evaluate(input_data), expected)

    def test_can_use_different_words_with_same_name(self):
        input_data = [
            ": foo 5 ;",
            ": bar foo ;",
            ": foo 6 ;",
            "bar foo"
        ]
        expected = [5, 6]
        self.assertEqual(evaluate(input_data), expected)

    def test_can_define_word_that_uses_word_with_same_name(self):
        input_data = [
            ": foo 10 ;",
            ": foo foo 1 + ;",
            "foo"
        ]
        expected = [11]
        self.assertEqual(evaluate(input_data), expected)

    def test_cannot_redefine_numbers(self):
        input_data = [": 1 2 ;"]
        with self.assertRaisesWithMessage(ValueError):
            evaluate(input_data)

    def test_errors_if_executing_a_non_existent_word(self):
        input_data = ["foo"]
        with self.assertRaisesWithMessage(ValueError):
            evaluate(input_data)


class ForthCaseInsensitivityTest(ForthUtilities):
    def test_dup_is_case_insensitive(self):
        input_data = ["1 DUP Dup dup"]
        expected = [1, 1, 1, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_drop_is_case_insensitive(self):
        input_data = ["1 2 3 4 DROP Drop drop"]
        expected = [1]
        self.assertEqual(evaluate(input_data), expected)

    def test_swap_is_case_insensitive(self):
        input_data = ["1 2 SWAP 3 Swap 4 swap"]
        expected = [2, 3, 4, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_over_is_case_insensitive(self):
        input_data = ["1 2 OVER Over over"]
        expected = [1, 2, 1, 2, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_user_defined_words_are_case_insensitive(self):
        input_data = [
            ": foo dup ;",
            "1 FOO Foo foo"
        ]
        expected = [1, 1, 1, 1]
        self.assertEqual(evaluate(input_data), expected)

    def test_definitions_are_case_insensitive(self):
        input_data = [
            ": SWAP DUP Dup dup ;",
            "1 swap"
        ]
        expected = [1, 1, 1, 1]
        self.assertEqual(evaluate(input_data), expected)


if __name__ == '__main__':
    unittest.main()
