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
            largest_product("73167176531330624919225119674426574742355349194934", 6),
            23520,
        )

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

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
