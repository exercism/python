import unittest

from resistor_color_trio import (
    label,
)

# Tests adapted from `problem-specifications//canonical-data.json`


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
