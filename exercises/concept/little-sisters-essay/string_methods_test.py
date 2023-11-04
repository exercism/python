import unittest
import pytest
from string_methods import (capitalize_title,
                            check_sentence_ending,
                            clean_up_spacing,
                            replace_word_choice)


class LittleSistersEssayTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_capitalize_word(self):

        actual_result = capitalize_title("canopy")
        expected = "Canopy"
        error_message = (f'Called capitalize_title("canopy"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the title.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_capitalize_title(self):

        actual_result = capitalize_title("fish are cold blooded")
        expected = "Fish Are Cold Blooded"
        error_message = (f'Called capitalize_title("fish are cold blooded"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the title.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_sentence_ending(self):

        actual_result = check_sentence_ending("Snails can sleep for 3 years.")
        expected = True
        error_message = (f'Called check_sentence_ending("Snails can sleep for 3 years."). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected} for a period ending.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_sentence_ending_without_period(self):

        actual_result = check_sentence_ending("Fittonia are nice")
        expected = False
        error_message = (f'Called check_sentence_ending("Fittonia are nice"). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected} for a period ending.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_remove_extra_spaces_only_start(self):

        actual_result = clean_up_spacing("  A rolling stone gathers no moss")
        expected = "A rolling stone gathers no moss"
        error_message = (f'Called clean_up_spacing("  A rolling stone gathers no moss"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" as a cleaned string.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_remove_extra_spaces(self):

        actual_result = clean_up_spacing("  Elephants can't jump.  ")
        expected = "Elephants can't jump."
        error_message = ("Called clean_up_spacing(\"  Elephants can't jump.  \")"
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" as a cleaned string.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_replace_word_choice(self):

        actual_result = replace_word_choice("Animals are cool.", "cool", "awesome")
        expected = "Animals are awesome."
        error_message = ('Called replace_word_choice("Animals are cool.", "cool", "awesome"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" after the word replacement.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_replace_word_not_exist(self):

        actual_result = replace_word_choice("Animals are cool.", "small", "tiny")
        expected = "Animals are cool."
        error_message = ('Called replace_word_choice("Animals are cool.", "small", "tiny"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}", because the word '
                         'to be replaced is not in the sentence.')

        self.assertEqual(actual_result, expected, msg=error_message)
