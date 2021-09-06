import unittest
import pytest
from string_methods import (capitalize_title,
                            check_sentence_ending,
                            clean_up_spacing,
                            replace_word_choice)


class TestStringMethods(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_capitalize_word(self):
        self.assertEqual(capitalize_title("canopy"), "Canopy")

    @pytest.mark.task(taskno=1)
    def test_capitalize_title(self):
        self.assertEqual(capitalize_title("fish are cold blooded"),
                         "Fish Are Cold Blooded")

    @pytest.mark.task(taskno=2)
    def test_sentence_ending(self):
        self.assertEqual(check_sentence_ending("Snails can sleep for 3 years."), True)

    @pytest.mark.task(taskno=2)
    def test_sentence_ending_without_period(self):
        self.assertEqual(check_sentence_ending("Fittonia are nice"), False)

    @pytest.mark.task(taskno=3)
    def test_remove_extra_spaces_only_start(self):
        self.assertEqual(clean_up_spacing("  A rolling stone gathers no moss"),
                         "A rolling stone gathers no moss")

    @pytest.mark.task(taskno=3)
    def test_remove_extra_spaces(self):
        self.assertEqual(clean_up_spacing("  Elephants can't jump.  "),
                         "Elephants can't jump.")

    @pytest.mark.task(taskno=4)
    def test_replace_word_choice(self):
        self.assertEqual(replace_word_choice("Animals are cool.", "cool", "awesome"),
                         "Animals are awesome.")

    @pytest.mark.task(taskno=4)
    def test_replace_word_not_exist(self):
        self.assertEqual(replace_word_choice("Animals are cool.", "small", "tiny"),
                         "Animals are cool.")
