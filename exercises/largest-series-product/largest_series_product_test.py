"""Tests for the largest-series-product exercise

Implementation note:
In case of invalid inputs to the 'largest_product' function
your program should raise a ValueError with a meaningful error message.

Feel free to reuse your code from the 'series' exercise!
"""
import unittest

from largest_series_product import largest_product


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class LargestSeriesProductTest(unittest.TestCase):
    def test_finds_the_largest_product_if_span_equals_length(self):
        self.assertEqual(largest_product("29", 2), 18)

    def test_can_find_the_largest_product_of_2_with_numbers_in_order(self):
        self.assertEqual(largest_product("0123456789", 2), 72)

    def test_can_find_the_largest_product_of_2(self):
        self.assertEqual(largest_product("576802143", 2), 48)

    def test_can_find_the_largest_product_of_3_with_numbers_in_order(self):
        self.assertEqual(largest_product("0123456789", 3), 504)

    def test_can_find_the_largest_product_of_3(self):
        self.assertEqual(largest_product("1027839564", 3), 270)

    def test_can_find_the_largest_product_of_5_with_numbers_in_order(self):
        self.assertEqual(largest_product("0123456789", 5), 15120)

    def test_can_get_the_largest_product_of_a_big_number(self):
        self.assertEqual(
            largest_product(
                "73167176531330624919225119674426574742355349194934", 6),
            23520)

    def test_reports_zero_if_the_only_digits_are_zero(self):
        self.assertEqual(largest_product("0000", 2), 0)

    def test_reports_zero_if_all_spans_include_zero(self):
        self.assertEqual(largest_product("99099", 3), 0)

    def test_rejects_span_longer_than_string_length(self):
        with self.assertRaisesWithMessage(ValueError):
            largest_product("123", 4)

    def test_reports_1_for_empty_string_and_empty_product_0_span(self):
        self.assertEqual(largest_product("", 0), 1)

    def test_reports_1_for_nonempty_string_and_empty_product_0_span(self):
        self.assertEqual(largest_product("123", 0), 1)

    def test_rejects_empty_string_and_nonzero_span(self):
        with self.assertRaisesWithMessage(ValueError):
            largest_product("", 1)

    def test_rejects_invalid_character_in_digits(self):
        with self.assertRaisesWithMessage(ValueError):
            largest_product("1234a5", 2)

    def test_rejects_negative_span(self):
        with self.assertRaisesWithMessage(ValueError):
            largest_product("12345", -1)

    @unittest.skip("extra-credit")
    def test_project_euler_big_number(self):
        series = (
            "73167176531330624919225119674426574742355349194934969835203127745"
            "06326239578318016984801869478851843858615607891129494954595017379"
            "58331952853208805511125406987471585238630507156932909632952274430"
            "43557668966489504452445231617318564030987111217223831136222989342"
            "33803081353362766142828064444866452387493035890729629049156044077"
            "23907138105158593079608667017242712188399879790879227492190169972"
            "08880937766572733300105336788122023542180975125454059475224352584"
            "90771167055601360483958644670632441572215539753697817977846174064"
            "95514929086256932197846862248283972241375657056057490261407972968"
            "65241453510047482166370484403199890008895243450658541227588666881"
            "16427171479924442928230863465674813919123162824586178664583591245"
            "66529476545682848912883142607690042242190226710556263211111093705"
            "44217506941658960408071984038509624554443629812309878799272442849"
            "09188845801561660979191338754992005240636899125607176060588611646"
            "71094050775410022569831552000559357297257163626956188267042825248"
            "3600823257530420752963450")
        self.assertEqual(largest_product(series, 13), 23514624000)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
