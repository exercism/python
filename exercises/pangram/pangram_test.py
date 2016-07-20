# -*- coding: utf-8 -*-

import unittest

from pangram import is_pangram


class PangramTests(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_pangram(''))

    def test_valid_pangram(self):
        self.assertTrue(
            is_pangram('the quick brown fox jumps over the lazy dog'))

    def test_missing_x(self):
        self.assertFalse(is_pangram('a quick movement of the enemy will '
                                    'jeopardize five gunboats'))

    def test_another_missing_character(self):
        self.assertFalse(
            is_pangram('the quick brown fish jumps over the lazy dog'))

    def test_pangram_with_underscores(self):
        self.assertTrue(
            is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"))

    def test_pangram_with_numbers(self):
        self.assertTrue(
            is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"))

    def test_missing_letters_replaced_by_numbers(self):
        self.assertFalse(
            is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"))

    def test_mixedcase_and_punctuation(self):
        self.assertTrue(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))

    def test_unchecked_german_umlaute(self):
        self.assertTrue(is_pangram('Victor jagt zwölf Boxkämpfer quer über den'
                                   ' großen Sylter Deich.'))


if __name__ == '__main__':
    unittest.main()
