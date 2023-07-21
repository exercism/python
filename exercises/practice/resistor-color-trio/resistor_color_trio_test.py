# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/resistor-color-trio/canonical-data.json
# File last updated on 2023-07-19

import unittest

from resistor_color_trio import (
    label,
)


class ResistorColorTrioTest(unittest.TestCase):
    def test_orange_and_orange_and_black(self):
        self.assertEqual(label(["orange", "orange", "black"]), "33 ohms")

    def test_blue_and_grey_and_brown(self):
        self.assertEqual(label(["blue", "grey", "brown"]), "680 ohms")

    def test_red_and_black_and_red(self):
        self.assertEqual(label(["red", "black", "red"]), "2 kiloohms")

    def test_green_and_brown_and_orange(self):
        self.assertEqual(label(["green", "brown", "orange"]), "51 kiloohms")

    def test_yellow_and_violet_and_yellow(self):
        self.assertEqual(label(["yellow", "violet", "yellow"]), "470 kiloohms")

    def test_blue_and_violet_and_blue(self):
        self.assertEqual(label(["blue", "violet", "blue"]), "67 megaohms")

    def test_minimum_possible_value(self):
        self.assertEqual(label(["black", "black", "black"]), "0 ohms")

    def test_maximum_possible_value(self):
        self.assertEqual(label(["white", "white", "white"]), "99 gigaohms")

    def test_first_two_colors_make_an_invalid_octal_number(self):
        self.assertEqual(label(["black", "grey", "black"]), "8 ohms")

    def test_ignore_extra_colors(self):
        self.assertEqual(label(["blue", "green", "yellow", "orange"]), "650 kiloohms")
