import unittest

from isogram import is_isogram


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.7.0

class IsogramTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertIs(is_isogram(""), True)

    def test_isogram_with_only_lower_case_characters(self):
        self.assertIs(is_isogram("isogram"), True)

    def test_word_with_one_duplicated_character(self):
        self.assertIs(is_isogram("eleven"), False)

    def test_word_with_one_duplicated_character_from_end_of_alphabet(self):
        self.assertIs(is_isogram("zzyzx"), False)

    def test_longest_reported_english_isogram(self):
        self.assertIs(is_isogram("subdermatoglyphic"), True)

    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertIs(is_isogram("Alphabet"), False)

    def test_word_with_duplicated_letter_in_mixed_case_lowercase_first(self):
        self.assertIs(is_isogram("alphAbet"), False)

    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertIs(is_isogram("thumbscrew-japingly"), True)

    def test_hypothetical_word_with_duplicate_character_following_hyphen(self):
        self.assertIs(is_isogram("thumbscrew-jappingly"), False)

    def test_isogram_with_duplicated_hyphen(self):
        self.assertIs(is_isogram("six-year-old"), True)

    def test_made_up_name_that_is_an_isogram(self):
        self.assertIs(is_isogram("Emily Jung Schwartzkopf"), True)

    def test_duplicated_character_in_the_middle(self):
        self.assertIs(is_isogram("accentor"), False)

    def test_same_first_and_last_characters(self):
        self.assertIs(is_isogram("angola"), False)

    # Additional tests for this track

    def test_isogram_with_duplicated_letter_and_nonletter_character(self):
        self.assertIs(is_isogram("Aleph Bot Chap"), False)


if __name__ == '__main__':
    unittest.main()
