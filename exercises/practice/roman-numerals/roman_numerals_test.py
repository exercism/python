import unittest

from roman_numerals import (
    roman,
)

# Tests adapted from `problem-specifications//canonical-data.json`
class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_i(self):
        self.assertEqual(roman(1), "I")

    def test_2_is_ii(self):
        self.assertEqual(roman(2), "II")

    def test_3_is_iii(self):
        self.assertEqual(roman(3), "III")

    def test_4_is_iv(self):
        self.assertEqual(roman(4), "IV")

    def test_5_is_v(self):
        self.assertEqual(roman(5), "V")

    def test_6_is_vi(self):
        self.assertEqual(roman(6), "VI")

    def test_9_is_ix(self):
        self.assertEqual(roman(9), "IX")

    def test_27_is_xxvii(self):
        self.assertEqual(roman(27), "XXVII")

    def test_48_is_xlviii(self):
        self.assertEqual(roman(48), "XLVIII")

    def test_49_is_xlix(self):
        self.assertEqual(roman(49), "XLIX")

    def test_59_is_lix(self):
        self.assertEqual(roman(59), "LIX")

    def test_93_is_xciii(self):
        self.assertEqual(roman(93), "XCIII")

    def test_141_is_cxli(self):
        self.assertEqual(roman(141), "CXLI")

    def test_163_is_clxiii(self):
        self.assertEqual(roman(163), "CLXIII")

    def test_402_is_cdii(self):
        self.assertEqual(roman(402), "CDII")

    def test_575_is_dlxxv(self):
        self.assertEqual(roman(575), "DLXXV")

    def test_911_is_cmxi(self):
        self.assertEqual(roman(911), "CMXI")

    def test_1024_is_mxxiv(self):
        self.assertEqual(roman(1024), "MXXIV")

    def test_3000_is_mmm(self):
        self.assertEqual(roman(3000), "MMM")

    def test_16_is_xvi(self):
        self.assertEqual(roman(16), "XVI")

    def test_66_is_lxvi(self):
        self.assertEqual(roman(66), "LXVI")

    def test_166_is_clxvi(self):
        self.assertEqual(roman(166), "CLXVI")

    def test_666_is_dclxvi(self):
        self.assertEqual(roman(666), "DCLXVI")

    def test_1666_is_mdclxvi(self):
        self.assertEqual(roman(1666), "MDCLXVI")
