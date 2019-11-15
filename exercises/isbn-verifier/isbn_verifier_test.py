import unittest

from isbn_verifier import is_valid

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.7.0


class IsbnVerifierTest(unittest.TestCase):
    def test_valid_isbn_number(self):
        self.assertIs(is_valid("3-598-21508-8"), True)

    def test_invalid_isbn_check_digit(self):
        self.assertIs(is_valid("3-598-21508-9"), False)

    def test_valid_isbn_number_with_a_check_digit_of_10(self):
        self.assertIs(is_valid("3-598-21507-X"), True)

    def test_check_digit_is_a_character_other_than_x(self):
        self.assertIs(is_valid("3-598-21507-A"), False)

    def test_invalid_character_in_isbn(self):
        self.assertIs(is_valid("3-598-P1581-X"), False)

    def test_x_is_only_valid_as_a_check_digit(self):
        self.assertIs(is_valid("3-598-2X507-9"), False)

    def test_valid_isbn_without_separating_dashes(self):
        self.assertIs(is_valid("3598215088"), True)

    def test_isbn_without_separating_dashes_and_x_as_check_digit(self):
        self.assertIs(is_valid("359821507X"), True)

    def test_isbn_without_check_digit_and_dashes(self):
        self.assertIs(is_valid("359821507"), False)

    def test_too_long_isbn_and_no_dashes(self):
        self.assertIs(is_valid("3598215078X"), False)

    def test_too_short_isbn(self):
        self.assertIs(is_valid("00"), False)

    def test_isbn_without_check_digit(self):
        self.assertIs(is_valid("3-598-21507"), False)

    def test_check_digit_of_x_should_not_be_used_for_0(self):
        self.assertIs(is_valid("3-598-21515-X"), False)

    def test_empty_isbn(self):
        self.assertIs(is_valid(""), False)

    def test_input_is_9_characters(self):
        self.assertIs(is_valid("134456729"), False)

    def test_invalid_characters_are_not_ignored(self):
        self.assertIs(is_valid("3132P34035"), False)

    def test_input_is_too_long_but_contains_a_valid_isbn(self):
        self.assertIs(is_valid("98245726788"), False)


if __name__ == "__main__":
    unittest.main()
