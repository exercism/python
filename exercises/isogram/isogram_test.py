import unittest

from isogram import is_isogram


# test cases adapted from `x-common//canonical-data.json` @ version: 1.1.0

class TestIsogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_isogram(""))

    @unittest.skip("remove this annotation to run this test")
    def test_isogram_with_only_lower_case_characters(self):
        self.assertTrue(is_isogram("isogram"))

    @unittest.skip("remove this annotation to run this test")
    def test_word_with_one_duplicated_character(self):
        self.assertFalse(is_isogram("eleven"))

    @unittest.skip("remove this annotation to run this test")
    def test_longest_reported_english_isogram(self):
        self.assertTrue(is_isogram("subdermatoglyphic"))

    @unittest.skip("remove this annotation to run this test")
    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertFalse(is_isogram("Alphabet"))

    @unittest.skip("remove this annotation to run this test")
    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertTrue(is_isogram("thumbscrew-japingly"))

    @unittest.skip("remove this annotation to run this test")
    def test_isogram_with_duplicated_non_letter_character(self):
        self.assertTrue(is_isogram("Hjelmqvist-Gryb-Zock-Pfund-Wax"))

    @unittest.skip("remove this annotation to run this test")
    def test_made_up_name_that_is_an_isogram(self):
        self.assertTrue(is_isogram("Emily Jung Schwartzkopf"))

    @unittest.skip("remove this annotation to run this test")
    def test_duplicated_character_in_the_middle(self):
        self.assertFalse(is_isogram("accentor"))

    @unittest.skip("remove this annotation to run this test")
    def test_isogram_with_duplicated_letter_and_nonletter_character(self):
        self.assertFalse(is_isogram("Aleph Bot Chap"))


if __name__ == '__main__':
    unittest.main()
