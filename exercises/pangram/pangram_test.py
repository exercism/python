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

    def test_mixedcase_and_punctuation(self):
        self.assertTrue(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))

    def test_unchecked_german_umlaute(self):
        self.assertTrue(is_pangram('Victor jagt zwölf Boxkämpfer quer über den'
                                   ' großen Sylter Deich.'))


if __name__ == '__main__':
    unittest.main()
