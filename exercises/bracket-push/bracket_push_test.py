import unittest

from bracket_push import check_brackets


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class BracketPushTests(unittest.TestCase):
    def test_paired_square_brackets(self):
        self.assertEqual(check_brackets("[]"), True)

    def test_empty_string(self):
        self.assertEqual(check_brackets(""), True)

    def test_unpaired_brackets(self):
        self.assertEqual(check_brackets("[["), False)

    def test_wrong_ordered_brackets(self):
        self.assertEqual(check_brackets("}{"), False)

    def test_paired_with_whitespace(self):
        self.assertEqual(check_brackets("{ }"), True)

    def test_simple_nested_brackets(self):
        self.assertEqual(check_brackets("{[]}"), True)

    def test_several_paired_brackets(self):
        self.assertEqual(check_brackets("{}[]"), True)

    def test_paired_and_nested_brackets(self):
        self.assertEqual(check_brackets("([{}({}[])])"), True)

    def test_unopened_closing_brackets(self):
        self.assertEqual(check_brackets("{[)][]}"), False)

    def test_unpaired_and_nested_brackets(self):
        self.assertEqual(check_brackets("([{])"), False)

    def test_paired_and_wrong_nested_brackets(self):
        self.assertEqual(check_brackets("[({]})"), False)

    def test_math_expression(self):
        self.assertEqual(
            check_brackets("(((185 + 223.85) * 15) - 543)/2"), True)

    def test_complex_latex_expression(self):
        self.assertEqual(
            check_brackets(
                ("\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{"
                 "x} &... x^2 \\end{array}\\right)")), True)


if __name__ == '__main__':
    unittest.main()
