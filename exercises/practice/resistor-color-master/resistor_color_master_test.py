import unittest

from resistor_color_master import (
    label,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class ResistorColorMasterTest(unittest.TestCase):
    def test_orange_orange_black_and_red(self):
        self.assertEqual(label(["orange", "orange", "black", "red"]), "33 ohms 2%")

    def test_blue_grey_brown_and_violet(self):
        self.assertEqual(label(["blue", "grey", "brown", "violet"]), "680 ohms 0.1%")

    def test_red_black_red_and_green(self):
        self.assertEqual(label(["red", "black", "red", "green"]), "2 kiloohms 0.5%")

    def test_green_brown_orange_and_grey(self):
        self.assertEqual(
            label(["green", "brown", "orange", "grey"]), "51 kiloohms 0.05%"
        )

    def test_one_black_band(self):
        self.assertEqual(label(["black"]), "0 ohms")

    def test_orange_orange_yellow_black_and_brown(self):
        self.assertEqual(
            label(["orange", "orange", "yellow", "black", "brown"]), "334 ohms 1%"
        )

    def test_red_green_yellow_yellow_and_brown(self):
        self.assertEqual(
            label(["red", "green", "yellow", "yellow", "brown"]), "2.54 megaohms 1%"
        )

    def test_blue_grey_white_red_and_brown(self):
        self.assertEqual(
            label(["blue", "grey", "white", "brown", "brown"]), "6.89 kiloohms 1%"
        )

    def test_violet_orange_red_and_grey(self):
        self.assertEqual(
            label(["violet", "orange", "red", "grey"]), "7.3 kiloohms 0.05%"
        )

    def test_brown_red_orange_green_and_blue(self):
        self.assertEqual(
            label(["brown", "red", "orange", "green", "blue"]), "12.3 megaohms 0.25%"
        )
