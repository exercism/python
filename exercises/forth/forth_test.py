import unittest

from forth import evaluate


class ForthAdditionTest(unittest.TestCase):
    def test_can_add_two_numbers(self):
        input_data = ["1 2 +"]
        expected = [3]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["+"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 +"]
        self.assertIsNone(evaluate(input_data))


class ForthSubtractionTest(unittest.TestCase):
    def test_can_subtract_two_numbers(self):
        input_data = ["3 4 -"]
        expected = [-1]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["-"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 -"]
        self.assertIsNone(evaluate(input_data))


class ForthMultiplicationTest(unittest.TestCase):
    def test_can_multiply_two_numbers(self):
        input_data = ["2 4 *"]
        expected = [8]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["*"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 *"]
        self.assertIsNone(evaluate(input_data))


class ForthDivisionTest(unittest.TestCase):
    def test_can_divide_two_numbers(self):
        input_data = ["3 4 -"]
        expected = [-1]
        self.assertEqual(expected, evaluate(input_data))

    def test_performs_integer_division(self):
        input_data = ["8 3 /"]
        expected = [2]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_dividing_by_zero(self):
        input_data = ["4 0 /"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["-"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 -"]
        self.assertIsNone(evaluate(input_data))


class ForthCombinedArithmeticTest(unittest.TestCase):
    def test_addition_and_subtraction(self):
        input_data = ["1 2 + 4 -"]
        expected = [-1]
        self.assertEqual(expected, evaluate(input_data))

    def test_multiplication_and_division(self):
        input_data = ["2 4 * 3 /"]
        expected = [2]
        self.assertEqual(expected, evaluate(input_data))


class ForthDupTest(unittest.TestCase):
    def test_copies_the_top_value_on_the_stack(self):
        input_data = ["1 DUP"]
        expected = [1, 1]
        self.assertEqual(expected, evaluate(input_data))

    def test_is_case_insensitive(self):
        input_data = ["1 2 Dup"]
        expected = [1, 2, 2]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["dup"]
        self.assertIsNone(evaluate(input_data))


class ForthDropTest(unittest.TestCase):
    def test_removes_the_top_value_on_the_stack_if_it_is_the_only_one(self):
        input_data = ["1 DROP"]
        expected = []
        self.assertEqual(expected, evaluate(input_data))

    def test_removes_the_top_value_on_the_stack_if_it_not_the_only_one(self):
        input_data = ["3 4 DROP"]
        expected = [3]
        self.assertEqual(expected, evaluate(input_data))

    def test_is_case_insensitive(self):
        input_data = ["1 2 Drop"]
        expected = [1]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["drop"]
        self.assertIsNone(evaluate(input_data))


class ForthSwapTest(unittest.TestCase):
    def test_swaps_only_two_values_on_stack(self):
        input_data = ["1 2 SWAP"]
        expected = [2, 1]
        self.assertEqual(expected, evaluate(input_data))

    def test_swaps_two_two_values_on_stack(self):
        input_data = ["1 2 3 SWAP"]
        expected = [1, 3, 2]
        self.assertEqual(expected, evaluate(input_data))

    def test_is_case_insensitive(self):
        input_data = ["3 4 Swap"]
        expected = [4, 3]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["swap"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 swap"]
        self.assertIsNone(evaluate(input_data))


class ForthOverTest(unittest.TestCase):
    def test_copies_the_second_element_if_there_are_only_two(self):
        input_data = ["1 2 OVER"]
        expected = [1, 2, 1]
        self.assertEqual(expected, evaluate(input_data))

    def test_copies_the_second_element_if_there_are_more_than_two(self):
        input_data = ["1 2 3 OVER"]
        expected = [1, 2, 3, 2]
        self.assertEqual(expected, evaluate(input_data))

    def test_is_case_insensitive(self):
        input_data = ["3 4 Over"]
        expected = [3, 4, 3]
        self.assertEqual(expected, evaluate(input_data))

    def test_errors_if_there_is_nothing_on_the_stack(self):
        input_data = ["over"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_there_is_only_one_value_on_the_stack(self):
        input_data = ["1 over"]
        self.assertIsNone(evaluate(input_data))


class ForthUserDefinedWordsTest(unittest.TestCase):
    def test_can_consist_of_built_in_words(self):
        input_data = [
            ": dup-twice dup dup ;",
            "1 dup-twice"
        ]
        expected = [1, 1, 1]
        self.assertEqual(expected, evaluate(input_data))

    def test_execute_in_the_right_order(self):
        input_data = [
            ": countup 1 2 3 ;",
            "countup"
        ]
        expected = [1, 2, 3]
        self.assertEqual(expected, evaluate(input_data))

    def test_can_override_other_user_defined_words(self):
        input_data = [
            ": foo dup ;",
            ": foo dup dup ;",
            "1 foo"
        ]
        expected = [1, 1, 1]
        self.assertEqual(expected, evaluate(input_data))

    def test_can_override_built_in_words(self):
        input_data = [
            ": swap dup ;",
            "1 swap"
        ]
        expected = [1, 1]
        self.assertEqual(expected, evaluate(input_data))

    def test_can_override_built_in_operators(self):
        input_data = [
            ": + * ;",
            "3 4 +"
        ]
        expected = [12]
        self.assertEqual(expected, evaluate(input_data))

    def test_is_case_insensitive(self):
        input_data = [
            ": foo dup ;",
            "1 FOO"
        ]
        expected = [1, 1]
        self.assertEqual(expected, evaluate(input_data))

    def test_cannot_redefine_numbers(self):
        input_data = [": 1 2 ;"]
        self.assertIsNone(evaluate(input_data))

    def test_errors_if_executing_a_non_existent_word(self):
        input_data = ["foo"]
        self.assertIsNone(evaluate(input_data))


if __name__ == '__main__':
    unittest.main()
