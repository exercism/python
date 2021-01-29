import unittest

from palindrome_products import largest, smallest

# Tests adapted from `problem-specifications//canonical-data.json`


class PalindromeProductsTest(unittest.TestCase):
    def test_finds_the_smallest_palindrome_from_single_digit_factors(self):
        value, factors = smallest(min_factor=1, max_factor=9)
        self.assertEqual(value, 1)
        self.assertFactorsEqual(factors, [[1, 1]])

    def test_finds_the_largest_palindrome_from_single_digit_factors(self):
        value, factors = largest(min_factor=1, max_factor=9)
        self.assertEqual(value, 9)
        self.assertFactorsEqual(factors, [[1, 9], [3, 3]])

    def test_find_the_smallest_palindrome_from_double_digit_factors(self):
        value, factors = smallest(min_factor=10, max_factor=99)
        self.assertEqual(value, 121)
        self.assertFactorsEqual(factors, [[11, 11]])

    def test_find_the_largest_palindrome_from_double_digit_factors(self):
        value, factors = largest(min_factor=10, max_factor=99)
        self.assertEqual(value, 9009)
        self.assertFactorsEqual(factors, [[91, 99]])

    def test_find_smallest_palindrome_from_triple_digit_factors(self):
        value, factors = smallest(min_factor=100, max_factor=999)
        self.assertEqual(value, 10201)
        self.assertFactorsEqual(factors, [[101, 101]])

    def test_find_the_largest_palindrome_from_triple_digit_factors(self):
        value, factors = largest(min_factor=100, max_factor=999)
        self.assertEqual(value, 906609)
        self.assertFactorsEqual(factors, [[913, 993]])

    def test_find_smallest_palindrome_from_four_digit_factors(self):
        value, factors = smallest(min_factor=1000, max_factor=9999)
        self.assertEqual(value, 1002001)
        self.assertFactorsEqual(factors, [[1001, 1001]])

    def test_find_the_largest_palindrome_from_four_digit_factors(self):
        value, factors = largest(min_factor=1000, max_factor=9999)
        self.assertEqual(value, 99000099)
        self.assertFactorsEqual(factors, [[9901, 9999]])

    def test_empty_result_for_smallest_if_no_palindrome_in_the_range(self):
        value, factors = smallest(min_factor=1002, max_factor=1003)
        self.assertIsNone(value)
        self.assertFactorsEqual(factors, [])

    def test_empty_result_for_largest_if_no_palindrome_in_the_range(self):
        value, factors = largest(min_factor=15, max_factor=15)
        self.assertIsNone(value)
        self.assertFactorsEqual(factors, [])

    def test_error_result_for_smallest_if_min_is_more_than_max(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = smallest(min_factor=10000, max_factor=1)

    def test_error_result_for_largest_if_min_is_more_than_max(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = largest(min_factor=2, max_factor=1)

    def assertFactorsEqual(self, actual, expected):
        self.assertEqual(set(map(frozenset, actual)), set(map(frozenset, expected)))

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
