import unittest

from series import (
    slices,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class SeriesTest(unittest.TestCase):
    def test_slices_of_one_from_one(self):
        self.assertEqual(slices("1", 1), ["1"])

    def test_slices_of_one_from_two(self):
        self.assertEqual(slices("12", 1), ["1", "2"])

    def test_slices_of_two(self):
        self.assertEqual(slices("35", 2), ["35"])

    def test_slices_of_two_overlap(self):
        self.assertEqual(slices("9142", 2), ["91", "14", "42"])

    def test_slices_can_include_duplicates(self):
        self.assertEqual(slices("777777", 3), ["777", "777", "777", "777"])

    def test_slices_of_a_long_series(self):
        self.assertEqual(
            slices("918493904243", 5),
            ["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"],
        )

    def test_slice_length_is_too_large(self):
        with self.assertRaises(ValueError) as err:
            slices("12345", 6)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "slice length cannot be greater than series length"
        )

    def test_slice_length_cannot_be_zero(self):
        with self.assertRaises(ValueError) as err:
            slices("12345", 0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "slice length cannot be zero")

    def test_slice_length_cannot_be_negative(self):
        with self.assertRaises(ValueError) as err:
            slices("123", -1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "slice length cannot be negative")

    def test_empty_series_is_invalid(self):
        with self.assertRaises(ValueError) as err:
            slices("", 1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "series cannot be empty")
