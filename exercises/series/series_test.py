"""Tests for the series exercise

Implementation note:
The slices function should raise a ValueError with a meaningful error
message if its length argument doesn't fit the series.
"""
import unittest

from series import slices


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class SeriesTest(unittest.TestCase):
    def test_slices_of_one(self):
        self.assertEqual(
            slices("01234", 1),
            ["0", "1", "2", "3", "4"]
        )

    def test_slices_of_two(self):
        self.assertEqual(
            slices("01234", 2),
            ["01", "12", "23", "34"]
        )

    def test_slices_of_three(self):
        self.assertEqual(
            slices("01234", 3),
            ["012", "123", "234"]
        )

    def test_slices_of_five(self):
        self.assertEqual(
            slices("01234", 5),
            ["01234"]
        )

    def test_order_preserved_with_descending_numbers(self):
        self.assertEqual(
            slices("43210", 3),
            ["432", "321", "210"]
        )

    def test_order_preserved_with_random_numbers(self):
        self.assertEqual(
            slices("83627", 3),
            ["836", "362", "627"]
        )

    def test_slices_can_include_duplicates(self):
        self.assertEqual(
            slices("123123", 3),
            ["123", "231", "312", "123"]
        )

    def test_overly_long_slice(self):
        with self.assertRaises(ValueError):
            slices("01234", 6)

    def test_overly_short_slice(self):
        with self.assertRaises(ValueError):
            slices("01234", 0)


if __name__ == '__main__':
    unittest.main()
