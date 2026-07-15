# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/raindrops/canonical-data.json
# File last updated on 2023-07-19

import unittest

from raindrops import (
    convert,
)


class RaindropsTest(unittest.TestCase):
    def test_01_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1")

    def test_02_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling")

    def test_03_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang")

    def test_04_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong")

    def test_05_the_sound_for_6_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(6), "Pling")

    def test_06_2_to_the_power_3_does_not_make_a_raindrop_sound_as_3_is_the_exponent_not_the_base(
        self,
    ):
        self.assertEqual(convert(8), "8")

    def test_07_the_sound_for_9_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(9), "Pling")

    def test_08_the_sound_for_10_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(10), "Plang")

    def test_09_the_sound_for_14_is_plong_as_it_has_a_factor_of_7(self):
        self.assertEqual(convert(14), "Plong")

    def test_10_the_sound_for_15_is_pling_plang_as_it_has_factors_3_and_5(self):
        self.assertEqual(convert(15), "PlingPlang")

    def test_11_the_sound_for_21_is_pling_plong_as_it_has_factors_3_and_7(self):
        self.assertEqual(convert(21), "PlingPlong")

    def test_12_the_sound_for_25_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(25), "Plang")

    def test_13_the_sound_for_27_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(27), "Pling")

    def test_14_the_sound_for_35_is_plang_plong_as_it_has_factors_5_and_7(self):
        self.assertEqual(convert(35), "PlangPlong")

    def test_15_the_sound_for_49_is_plong_as_it_has_a_factor_7(self):
        self.assertEqual(convert(49), "Plong")

    def test_16_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52")

    def test_17_the_sound_for_105_is_pling_plang_plong_as_it_has_factors_3_5_and_7(self):
        self.assertEqual(convert(105), "PlingPlangPlong")

    def test_18_the_sound_for_3125_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(3125), "Plang")
