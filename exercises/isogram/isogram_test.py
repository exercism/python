import unittest

from isogram import is_isogram


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

class TestIsogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertIs(is_isogram(""), True)

    def test_isogram_with_only_lower_case_characters(self):
        self.assertIs(is_isogram("isogram"), True)

    def test_word_with_one_duplicated_character(self):
        self.assertIs(is_isogram("eleven"), False)

    def test_longest_reported_english_isogram(self):
        self.assertIs(is_isogram("subdermatoglyphic"), True)

    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertIs(is_isogram("Alphabet"), False)

    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertIs(is_isogram("thumbscrew-japingly"), True)

    def test_isogram_with_duplicated_non_letter_character(self):
        self.assertIs(is_isogram("Hjelmqvist-Gryb-Zock-Pfund-Wax"), True)

    def test_made_up_name_that_is_an_isogram(self):
        self.assertIs(is_isogram("Emily Jung Schwartzkopf"), True)

    def test_duplicated_character_in_the_middle(self):
        self.assertIs(is_isogram("accentor"), False)

    def test_isogram_with_duplicated_letter_and_nonletter_character(self):
        self.assertIs(is_isogram("Aleph Bot Chap"), False)


if __name__ == '__main__':
    unittest.main()
