"""Tests for the largest-series-product exercise

Implementation note:
In case of invalid inputs to the 'largest_product' function
your program should raise a ValueError with a meaningful error message.

Feel free to reuse your code from the 'series' exercise!
"""
import unittest

from largest_series_product import largest_product


class SeriesTest(unittest.TestCase):
    def test_largest_product_of_2(self):
        self.assertEqual(72, largest_product("0123456789", 2))

    def test_largest_product_of_2_unordered(self):
        self.assertEqual(48, largest_product("576802143", 2))

    def test__largest_product_span_equals_length(self):
        self.assertEqual(18, largest_product("29", 2))

    def test_largest_product_of_3(self):
        self.assertEqual(504, largest_product("0123456789", 3))

    def test_largest_product_of_3_unordered(self):
        self.assertEqual(270, largest_product("1027839564", 3))

    def test_largest_product_of_5(self):
        self.assertEqual(15120, largest_product("0123456789", 5))

    def test_big_number(self):
        series = "73167176531330624919225119674426574742355349194934"
        self.assertEqual(23520, largest_product(series, 6))

    def test_another_big_number(self):
        series = "52677741234314237566414902593461595376319419139427"
        self.assertEqual(28350, largest_product(series, 6))

    def test_project_euler_big_number(self):
        series = (
            "731671765313306249192251196744265747423553491949349698352031277450632623957"
            "831801698480186947885184385861560789112949495459501737958331952853208805511"
            "125406987471585238630507156932909632952274430435576689664895044524452316173"
            "185640309871112172238311362229893423380308135336276614282806444486645238749"
            "303589072962904915604407723907138105158593079608667017242712188399879790879"
            "227492190169972088809377665727333001053367881220235421809751254540594752243"
            "525849077116705560136048395864467063244157221553975369781797784617406495514"
            "929086256932197846862248283972241375657056057490261407972968652414535100474"
            "821663704844031998900088952434506585412275886668811642717147992444292823086"
            "346567481391912316282458617866458359124566529476545682848912883142607690042"
            "242190226710556263211111093705442175069416589604080719840385096245544436298"
            "123098787992724428490918884580156166097919133875499200524063689912560717606"
            "058861164671094050775410022569831552000559357297257163626956188267042825248"
            "3600823257530420752963450"
        )
        self.assertEqual(23514624000, largest_product(series, 13))

    def test_all_digits_zero(self):
        self.assertEqual(0, largest_product("0000", 2))

    def test_all_spans_contain_zero(self):
        self.assertEqual(0, largest_product("99099", 3))

    def test_identity_with_empty_string(self):
        self.assertEqual(1, largest_product("", 0))

    def test_identity_with_nonempty_string(self):
        self.assertEqual(1, largest_product("123", 0))

    def test_span_long_than_number(self):
        with self.assertRaises(ValueError):
            largest_product("123", 4)

    def test_nonzero_span_and_empty_string(self):
        with self.assertRaises(ValueError):
            largest_product("", 1)

    def test_digits_with_invalid_character(self):
        with self.assertRaises(ValueError):
            largest_product("1234a5", 2)

    def test_negative_span(self):
        with self.assertRaises(ValueError):
            largest_product("12345", -1)


if __name__ == '__main__':
    unittest.main()
