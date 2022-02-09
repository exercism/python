import unittest

from largest_series_product import (
    largest_product,
)

# Tests adapted from `problem-specifications//canonical-data.json`


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
        with self.assertRaises(ValueError) as err:
            largest_product("123", 4)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "span must be smaller than string length"
        )

    def test_reports_1_for_empty_string_and_empty_product_0_span(self):
        self.assertEqual(largest_product("", 0), 1)

    def test_reports_1_for_nonempty_string_and_empty_product_0_span(self):
        self.assertEqual(largest_product("123", 0), 1)

    def test_rejects_empty_string_and_nonzero_span(self):
        with self.assertRaises(ValueError) as err:
            largest_product("", 1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "span must be smaller than string length"
        )

    def test_rejects_invalid_character_in_digits(self):
        with self.assertRaises(ValueError) as err:
            largest_product("1234a5", 2)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "digits input must only contain digits")

    def test_rejects_negative_span(self):
        with self.assertRaises(ValueError) as err:
            largest_product("12345", -1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "span must not be negative")

    # Additional tests for this track
    def test_euler_big_number(self):
        self.assertEqual(
            largest_product(
                "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450",
                13,
            ),
            23514624000,
        )
