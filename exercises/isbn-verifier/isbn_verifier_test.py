import unittest

from isbn_verifier import verify


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.7.0

class IsbnVerifierTest(unittest.TestCase):

    def test_valid_isbn_number(self):
        self.assertIs(verify('3-598-21508-8'), True)

    def test_invalid_check_digit(self):
        self.assertIs(verify('3-598-21508-9'), False)

    def test_valid_with_X_check_digit(self):
        self.assertIs(verify('3-598-21507-X'), True)

    def test_invalid_check_digit_other_than_X(self):
        self.assertIs(verify('3-598-21507-A'), False)

    def test_invalid_character_in_isbn(self):
        self.assertIs(verify('3-598-P1581-X'), False)

    def test_invalid_X_other_than_check_digit(self):
        self.assertIs(verify('3-598-2X507-9'), False)

    def test_valid_isbn_without_separating_dashes(self):
        self.assertIs(verify('3598215088'), True)

    def test_valid_isbn_without_separating_dashes_with_X_check_digit(self):
        self.assertIs(verify('359821507X'), True)

    def test_invalid_isbn_without_check_digit_and_dashes(self):
        self.assertIs(verify('359821507'), False)

    def test_invalid_too_long_isbn_with_no_dashes(self):
        self.assertIs(verify('3598215078X'), False)

    def test_invalid_too_short_isbn(self):
        self.assertIs(verify('00'), False)

    def test_invalid_isbn_without_check_digit(self):
        self.assertIs(verify('3-598-21507'), False)

    def test_invalid_check_digit_X_used_for_0(self):
        self.assertIs(verify('3-598-21515-X'), False)

    def test_valid_empty_isbn(self):
        self.assertIs(verify(''), False)

    def test_input_is_nine_characters(self):
        self.assertIs(verify('134456729'), False)

    def test_invalid_characters_are_not_ignored(self):
        self.assertIs(verify('3132P34035'), False)

    def test_input_is_too_long_but_contains_a_valid_isbn(self):
        self.assertIs(verify('98245726788'), False)


if __name__ == '__main__':
    unittest.main()
