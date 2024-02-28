# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/reverse-string/canonical-data.json
# File last updated on 2024-02-28

import unittest

from reverse_string import (
    reverse,
)


class ReverseStringTest(unittest.TestCase):
    def test_an_empty_string(self):
        self.assertEqual(reverse(""), "")

    def test_a_word(self):
        self.assertEqual(reverse("robot"), "tobor")

    def test_a_capitalized_word(self):
        self.assertEqual(reverse("Ramen"), "nemaR")

    def test_a_sentence_with_punctuation(self):
        self.assertEqual(reverse("I'm hungry!"), "!yrgnuh m'I")

    def test_a_palindrome(self):
        self.assertEqual(reverse("racecar"), "racecar")

    def test_an_even_sized_word(self):
        self.assertEqual(reverse("drawer"), "reward")

    def test_wide_characters(self):
        self.assertEqual(reverse("子猫"), "猫子")
