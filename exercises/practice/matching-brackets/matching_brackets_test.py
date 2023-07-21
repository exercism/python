# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/matching-brackets/canonical-data.json
# File last updated on 2023-07-19

import unittest

from matching_brackets import (
    is_paired,
)


class MatchingBracketsTest(unittest.TestCase):
    def test_paired_square_brackets(self):
        self.assertEqual(is_paired("[]"), True)

    def test_empty_string(self):
        self.assertEqual(is_paired(""), True)

    def test_unpaired_brackets(self):
        self.assertEqual(is_paired("[["), False)

    def test_wrong_ordered_brackets(self):
        self.assertEqual(is_paired("}{"), False)

    def test_wrong_closing_bracket(self):
        self.assertEqual(is_paired("{]"), False)

    def test_paired_with_whitespace(self):
        self.assertEqual(is_paired("{ }"), True)

    def test_partially_paired_brackets(self):
        self.assertEqual(is_paired("{[])"), False)

    def test_simple_nested_brackets(self):
        self.assertEqual(is_paired("{[]}"), True)

    def test_several_paired_brackets(self):
        self.assertEqual(is_paired("{}[]"), True)

    def test_paired_and_nested_brackets(self):
        self.assertEqual(is_paired("([{}({}[])])"), True)

    def test_unopened_closing_brackets(self):
        self.assertEqual(is_paired("{[)][]}"), False)

    def test_unpaired_and_nested_brackets(self):
        self.assertEqual(is_paired("([{])"), False)

    def test_paired_and_wrong_nested_brackets(self):
        self.assertEqual(is_paired("[({]})"), False)

    def test_paired_and_wrong_nested_brackets_but_innermost_are_correct(self):
        self.assertEqual(is_paired("[({}])"), False)

    def test_paired_and_incomplete_brackets(self):
        self.assertEqual(is_paired("{}["), False)

    def test_too_many_closing_brackets(self):
        self.assertEqual(is_paired("[]]"), False)

    def test_early_unexpected_brackets(self):
        self.assertEqual(is_paired(")()"), False)

    def test_early_mismatched_brackets(self):
        self.assertEqual(is_paired("{)()"), False)

    def test_math_expression(self):
        self.assertEqual(is_paired("(((185 + 223.85) * 15) - 543)/2"), True)

    def test_complex_latex_expression(self):
        self.assertEqual(
            is_paired(
                "\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{x} &... x^2 \\end{array}\\right)"
            ),
            True,
        )
