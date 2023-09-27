# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/grains/canonical-data.json
# File last updated on 2023-09-27

import unittest

from grains import (
    square,
    total,
)


class GrainsTest(unittest.TestCase):
    def test_grains_on_square_1(self):
        self.assertEqual(square(1), 1)

    def test_grains_on_square_2(self):
        self.assertEqual(square(2), 2)

    def test_grains_on_square_3(self):
        self.assertEqual(square(3), 4)

    def test_grains_on_square_4(self):
        self.assertEqual(square(4), 8)

    def test_grains_on_square_16(self):
        self.assertEqual(square(16), 32768)

    def test_grains_on_square_32(self):
        self.assertEqual(square(32), 2147483648)

    def test_grains_on_square_64(self):
        self.assertEqual(square(64), 9223372036854775808)

    def test_square_0_is_invalid(self):
        with self.assertRaises(ValueError) as err:
            square(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "square must be between 1 and 64")

    def test_negative_square_is_invalid(self):
        with self.assertRaises(ValueError) as err:
            square(-1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "square must be between 1 and 64")

    def test_square_greater_than_64_is_invalid(self):
        with self.assertRaises(ValueError) as err:
            square(65)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "square must be between 1 and 64")

    def test_returns_the_total_number_of_grains_on_the_board(self):
        self.assertEqual(total(), 18446744073709551615)
