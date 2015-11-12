import unittest

from bracket_push import check_brackets


class BracketPushTests(unittest.TestCase):

    def test_input_empty(self):
        self.assertEqual(check_brackets(""), True)

    def test_single(self):
        self.assertEqual(check_brackets("{}"), True)

    def test_unclosed(self):
        self.assertEqual(check_brackets("{{"), False)

    def test_wrong_order(self):
        self.assertEqual(check_brackets("}{"), False)

    def test_mixed_not_nested(self):
        self.assertEqual(check_brackets("{}[]"), True)

    def test_mixed_nested(self):
        self.assertEqual(check_brackets("{[]}"), True)

    def test_improperly_nested(self):
        self.assertEqual(check_brackets("{[}]"), False)

    def test_not_opened_nested(self):
        self.assertEqual(check_brackets("{[)][]}"), False)

    def test_nested_ensemble(self):
        self.assertEqual(check_brackets("{[]([()])}"), True)


if __name__ == '__main__':
    unittest.main()
