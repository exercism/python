"""
Notes regarding the implementation of smallest_palindrome and
largest:

Both functions must take two keyword arguments:
    max -- int
    min -- int, default 0

Their return value must be a tuple (value, factors) where value is the
palindrome itself, and factors is an iterable containing both factors of the
palindrome in arbitrary order.
"""

import unittest

from palindrome_products import smallest, largest


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class PalindromeProductsTest(unittest.TestCase):
    def test_smallest_palindrome_from_single_digit_factors(self):
        value, factors = smallest(min=1, max=9)
        self.assertEqual(value, 1)
        self.assertFactorsEqual(factors, [[1, 1]])

    def test_largest_palindrome_from_single_digit_factors(self):
        value, factors = largest(min=1, max=9)
        self.assertEqual(value, 9)
        self.assertFactorsEqual(factors, [[1, 9], [3, 3]])

    def test_smallest_palindrome_from_double_digit_factors(self):
        value, factors = smallest(min=10, max=99)
        self.assertEqual(value, 121)
        self.assertFactorsEqual(factors, [[11, 11]])

    def test_largest_palindrome_from_double_digit_factors(self):
        value, factors = largest(min=10, max=99)
        self.assertEqual(value, 9009)
        self.assertFactorsEqual(factors, [[91, 99]])

    def test_smallest_palindrome_from_triple_digit_factors(self):
        value, factors = smallest(min=100, max=999)
        self.assertEqual(value, 10201)
        self.assertFactorsEqual(factors, [[101, 101]])

    def test_largest_palindrome_from_triple_digit_factors(self):
        value, factors = largest(min=100, max=999)
        self.assertEqual(value, 906609)
        self.assertFactorsEqual(factors, [[913, 993]])

    def test_smallest_palindrome_from_four_digit_factors(self):
        value, factors = smallest(min=1000, max=9999)
        self.assertEqual(value, 1002001)
        self.assertFactorsEqual(factors, [[1001, 1001]])

    def test_largest_palindrome_from_four_digit_factors(self):
        value, factors = largest(min=1000, max=9999)
        self.assertEqual(value, 99000099)
        self.assertFactorsEqual(factors, [[9901, 9999]])

    def test_empty_for_smallest_palindrome_if_none_in_range(self):
        value, factors = smallest(min=1002, max=1003)
        self.assertIsNone(value)
        self.assertFactorsEqual(factors, [])

    def test_empty_for_largest_palindrome_if_none_in_range(self):
        value, factors = largest(min=15, max=15)
        self.assertIsNone(value)
        self.assertFactorsEqual(factors, [])

    def test_error_for_smallest_palindrome_if_min_is_more_than_max(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = smallest(min=10000, max=1)

    def test_error_for_largest_palindrome_if_min_is_more_than_max(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = largest(min=2, max=1)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def assertFactorsEqual(self, actual, expected):
        self.assertEqual(set(map(frozenset, actual)),
                         set(map(frozenset, expected)))


if __name__ == '__main__':
    unittest.main()
