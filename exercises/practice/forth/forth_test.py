import unittest

from forth import (
    evaluate,
    StackUnderflowError,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class ForthTest(unittest.TestCase):
    def test_parsing_and_numbers_numbers_just_get_pushed_onto_the_stack(self):
        self.assertEqual(evaluate(["1 2 3 4 5"]), [1, 2, 3, 4, 5])

    def test_addition_can_add_two_numbers(self):
        self.assertEqual(evaluate(["1 2 +"]), [3])

    def test_addition_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["+"])

    def test_addition_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["1 +"])

    def test_subtraction_can_subtract_two_numbers(self):
        self.assertEqual(evaluate(["3 4 -"]), [-1])

    def test_subtraction_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["-"])

    def test_subtraction_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["1 -"])

    def test_multiplication_can_multiply_two_numbers(self):
        self.assertEqual(evaluate(["2 4 *"]), [8])

    def test_multiplication_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["*"])

    def test_multiplication_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["1 *"])

    def test_division_can_divide_two_numbers(self):
        self.assertEqual(evaluate(["12 3 /"]), [4])

    def test_division_performs_integer_division(self):
        self.assertEqual(evaluate(["8 3 /"]), [2])

    def test_division_errors_if_dividing_by_zero(self):
        # divide by zero
        with self.assertRaisesWithMessage(ZeroDivisionError):
            evaluate(["4 0 /"])

    def test_division_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["/"])

    def test_division_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["1 /"])

    def test_combined_arithmetic_addition_and_subtraction(self):
        self.assertEqual(evaluate(["1 2 + 4 -"]), [-1])

    def test_combined_arithmetic_multiplication_and_division(self):
        self.assertEqual(evaluate(["2 4 * 3 /"]), [2])

    def test_dup_copies_a_value_on_the_stack(self):
        self.assertEqual(evaluate(["1 dup"]), [1, 1])

    def test_dup_copies_the_top_value_on_the_stack(self):
        self.assertEqual(evaluate(["1 2 dup"]), [1, 2, 2])

    def test_dup_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["dup"])

    def test_drop_removes_the_top_value_on_the_stack_if_it_is_the_only_one(self):
        self.assertEqual(evaluate(["1 drop"]), [])

    def test_drop_removes_the_top_value_on_the_stack_if_it_is_not_the_only_one(self):
        self.assertEqual(evaluate(["1 2 drop"]), [1])

    def test_drop_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["drop"])

    def test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_the_only_ones(self):
        self.assertEqual(evaluate(["1 2 swap"]), [2, 1])

    def test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_not_the_only_ones(
        self,
    ):
        self.assertEqual(evaluate(["1 2 3 swap"]), [1, 3, 2])

    def test_swap_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["swap"])

    def test_swap_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["1 swap"])

    def test_over_copies_the_second_element_if_there_are_only_two(self):
        self.assertEqual(evaluate(["1 2 over"]), [1, 2, 1])

    def test_over_copies_the_second_element_if_there_are_more_than_two(self):
        self.assertEqual(evaluate(["1 2 3 over"]), [1, 2, 3, 2])

    def test_over_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["over"])

    def test_over_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaisesWithMessage(StackUnderflowError):
            evaluate(["1 over"])

    def test_user_defined_words_can_consist_of_built_in_words(self):
        self.assertEqual(evaluate([": dup-twice dup dup ;", "1 dup-twice"]), [1, 1, 1])

    def test_user_defined_words_execute_in_the_right_order(self):
        self.assertEqual(evaluate([": countup 1 2 3 ;", "countup"]), [1, 2, 3])

    def test_user_defined_words_can_override_other_user_defined_words(self):
        self.assertEqual(
            evaluate([": foo dup ;", ": foo dup dup ;", "1 foo"]), [1, 1, 1]
        )

    def test_user_defined_words_can_override_built_in_words(self):
        self.assertEqual(evaluate([": swap dup ;", "1 swap"]), [1, 1])

    def test_user_defined_words_can_override_built_in_operators(self):
        self.assertEqual(evaluate([": + * ;", "3 4 +"]), [12])

    def test_user_defined_words_can_use_different_words_with_the_same_name(self):
        self.assertEqual(
            evaluate([": foo 5 ;", ": bar foo ;", ": foo 6 ;", "bar foo"]), [5, 6]
        )

    def test_user_defined_words_can_define_word_that_uses_word_with_the_same_name(self):
        self.assertEqual(evaluate([": foo 10 ;", ": foo foo 1 + ;", "foo"]), [11])

    def test_user_defined_words_cannot_redefine_non_negative_numbers(self):
        with self.assertRaisesWithMessage(ValueError):
            evaluate([": 1 2 ;"])

    def test_user_defined_words_errors_if_executing_a_non_existent_word(self):
        with self.assertRaisesWithMessage(ValueError):
            evaluate(["foo"])

    def test_case_insensitivity_dup_is_case_insensitive(self):
        self.assertEqual(evaluate(["1 DUP Dup dup"]), [1, 1, 1, 1])

    def test_case_insensitivity_drop_is_case_insensitive(self):
        self.assertEqual(evaluate(["1 2 3 4 DROP Drop drop"]), [1])

    def test_case_insensitivity_swap_is_case_insensitive(self):
        self.assertEqual(evaluate(["1 2 SWAP 3 Swap 4 swap"]), [2, 3, 4, 1])

    def test_case_insensitivity_over_is_case_insensitive(self):
        self.assertEqual(evaluate(["1 2 OVER Over over"]), [1, 2, 1, 2, 1])

    def test_case_insensitivity_user_defined_words_are_case_insensitive(self):
        self.assertEqual(evaluate([": foo dup ;", "1 FOO Foo foo"]), [1, 1, 1, 1])

    def test_case_insensitivity_definitions_are_case_insensitive(self):
        self.assertEqual(evaluate([": SWAP DUP Dup dup ;", "1 swap"]), [1, 1, 1, 1])

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
