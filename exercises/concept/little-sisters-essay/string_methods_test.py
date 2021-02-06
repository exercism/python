import unittest
from string_methods import *


class TestStringMethods(unittest.TestCase):
    def test_capitalize_word(self):
        self.assertEqual(capitalize_title("canopy"), "Canopy")

    def test_capitalize_title(self):
        self.assertEqual(capitalize_title("fish are cold blooded"),
                         "Fish Are Cold Blooded")

    def test_sentence_ending(self):
        self.assertEqual(check_sentence_ending("Snails can sleep for 3 years."), True)

    def test_sentence_ending_without_period(self):
        self.assertEqual(check_sentence_ending("Fittonia are nice"), False)

    def remove_extra_spaces_only_start(self):
        self.assertEqual(remove_extra_spaces("  A rolling stone gathers no moss"),
                        "A rolling stone gathers no moss")

    def remove_extra_spaces(self):
        self.assertEqual(remove_extra_spaces("  Elephants can't jump.  "),
                        "Elephants can't jump.")

    def test_replace_word_choice(self):
        self.assertEqual(replace_word_choice("Animals are cool.", "cool", "awesome"),
                        "Animals are awesome.")

    def test_replace_word_not_exist(self):
        self.assertEqual(replace_word_choice("Animals are cool.", "small", "tiny"),
                        "Animals are cool.")
