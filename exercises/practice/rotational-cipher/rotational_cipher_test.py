# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/rotational-cipher/canonical-data.json
# File last updated on 2023-07-19

import unittest

from rotational_cipher import (
    rotate,
)


class RotationalCipherTest(unittest.TestCase):
    def test_rotate_a_by_0_same_output_as_input(self):
        self.assertEqual(rotate("a", 0), "a")

    def test_rotate_a_by_1(self):
        self.assertEqual(rotate("a", 1), "b")

    def test_rotate_a_by_26_same_output_as_input(self):
        self.assertEqual(rotate("a", 26), "a")

    def test_rotate_m_by_13(self):
        self.assertEqual(rotate("m", 13), "z")

    def test_rotate_n_by_13_with_wrap_around_alphabet(self):
        self.assertEqual(rotate("n", 13), "a")

    def test_rotate_capital_letters(self):
        self.assertEqual(rotate("OMG", 5), "TRL")

    def test_rotate_spaces(self):
        self.assertEqual(rotate("O M G", 5), "T R L")

    def test_rotate_numbers(self):
        self.assertEqual(rotate("Testing 1 2 3 testing", 4), "Xiwxmrk 1 2 3 xiwxmrk")

    def test_rotate_punctuation(self):
        self.assertEqual(rotate("Let's eat, Grandma!", 21), "Gzo'n zvo, Bmviyhv!")

    def test_rotate_all_letters(self):
        self.assertEqual(
            rotate("The quick brown fox jumps over the lazy dog.", 13),
            "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
        )
