import unittest

from bracket_push import check_brackets


class BracketPushTests(unittest.TestCase):
    def test_input_empty(self):
        self.assertEqual(check_brackets(""), True)

    def test_simple_curly(self):
        self.assertEqual(check_brackets("{}"), True)

    def test_simple_square(self):
        self.assertEqual(check_brackets("[]"), True)

    def test_curly_only_open(self):
        self.assertEqual(check_brackets("{{"), False)

    def test_parenthesis_switched(self):
        self.assertEqual(check_brackets(")("), False)

    def test_simple_square_with_numbers(self):
        self.assertEqual(check_brackets("[42]"), True)

    def test_mixed_not_nested(self):
        self.assertEqual(check_brackets("{}[]"), True)

    def test_nested(self):
        self.assertEqual(check_brackets("{[]}"), True)

    def test_crossed(self):
        self.assertEqual(check_brackets("{[}]"), False)

    def test_round_single(self):
        self.assertEqual(check_brackets("{[])[]}"), False)

    def test_nested_ensemble(self):
        self.assertEqual(check_brackets("{[]([()])}"), True)

    def test_with_different_chars(self):
        self.assertEqual(check_brackets(" {[<](x [(42)]) }"), True)


if __name__ == '__main__':
    unittest.main()
