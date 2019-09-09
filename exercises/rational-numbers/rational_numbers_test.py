from __future__ import division

import unittest

from rational_numbers import Rational


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class RationalNumbersTest(unittest.TestCase):

    # Test addition
    def test_add_two_positive(self):
        self.assertEqual(Rational(1, 2) + Rational(2, 3), Rational(7, 6))

    def test_add_positive_and_negative(self):
        self.assertEqual(Rational(1, 2) + Rational(-2, 3), Rational(-1, 6))

    def test_add_two_negative(self):
        self.assertEqual(Rational(-1, 2) + Rational(-2, 3), Rational(-7, 6))

    def test_add_opposite(self):
        self.assertEqual(Rational(1, 2) + Rational(-1, 2), Rational(0, 1))

    # Test subtraction
    def test_subtract_two_positive(self):
        self.assertEqual(Rational(1, 2) - Rational(2, 3), Rational(-1, 6))

    def test_subtract_positive_and_negative(self):
        self.assertEqual(Rational(1, 2) - Rational(-2, 3), Rational(7, 6))

    def test_subtract_two_negative(self):
        self.assertEqual(Rational(-1, 2) - Rational(-2, 3), Rational(1, 6))

    def test_subtract_from_self(self):
        self.assertEqual(Rational(1, 2) - Rational(1, 2), Rational(0, 1))

    # Test multiplication
    def test_multiply_two_positive(self):
        self.assertEqual(Rational(1, 2) * Rational(2, 3), Rational(1, 3))

    def test_multiply_negative_by_positive(self):
        self.assertEqual(Rational(-1, 2) * Rational(2, 3), Rational(-1, 3))

    def test_multiply_two_negative(self):
        self.assertEqual(Rational(-1, 2) * Rational(-2, 3), Rational(1, 3))

    def test_multiply_reciprocal(self):
        self.assertEqual(Rational(1, 2) * Rational(2, 1), Rational(1, 1))

    def test_multiply_by_one(self):
        self.assertEqual(Rational(1, 2) * Rational(1, 1), Rational(1, 2))

    def test_multiply_by_zero(self):
        self.assertEqual(Rational(1, 2) * Rational(0, 1), Rational(0, 1))

    # Test division
    def test_divide_two_positive(self):
        self.assertEqual(Rational(1, 2) / Rational(2, 3), Rational(3, 4))

    def test_divide_positive_by_negative(self):
        self.assertEqual(Rational(1, 2) / Rational(-2, 3), Rational(-3, 4))

    def test_divide_two_negative(self):
        self.assertEqual(Rational(-1, 2) / Rational(-2, 3), Rational(3, 4))

    def test_divide_by_one(self):
        self.assertEqual(Rational(1, 2) / Rational(1, 1), Rational(1, 2))

    # Test absolute value
    def test_absolute_value_of_positive(self):
        self.assertEqual(abs(Rational(1, 2)), Rational(1, 2))

    def test_absolute_value_of_positive_negative_numerator_denominator(self):
        self.assertEqual(abs(Rational(-1, -2)), Rational(1, 2))

    def test_absolute_value_of_negative(self):
        self.assertEqual(abs(Rational(-1, 2)), Rational(1, 2))

    def test_absolute_value_of_negative_with_negative_denominator(self):
        self.assertEqual(abs(Rational(1, -2)), Rational(1, 2))

    def test_absolute_value_of_zero(self):
        self.assertEqual(abs(Rational(0, 1)), Rational(0, 1))

    # Test exponentiation of a rational number
    def test_raise_a_positive_rational_to_a_positive_integer_power(self):
        self.assertEqual(Rational(1, 2) ** 3, Rational(1, 8))

    def test_raise_a_negative_rational_to_a_positive_integer_power(self):
        self.assertEqual(Rational(-1, 2) ** 3, Rational(-1, 8))

    def test_raise_zero_to_an_integer_power(self):
        self.assertEqual(Rational(0, 1) ** 5, Rational(0, 1))

    def test_raise_one_to_an_integer_power(self):
        self.assertEqual(Rational(1, 1) ** 4, Rational(1, 1))

    def test_raise_a_positive_rational_to_the_power_of_zero(self):
        self.assertEqual(Rational(1, 2) ** 0, Rational(1, 1))

    def test_raise_a_negative_rational_to_the_power_of_zero(self):
        self.assertEqual(Rational(-1, 2) ** 0, Rational(1, 1))

    # Test exponentiation of a real number to a rational number
    def test_raise_a_real_number_to_a_positive_rational(self):
        self.assertAlmostEqual(8 ** Rational(4, 3), 16.0, places=8)

    def test_raise_a_real_number_to_a_negative_rational(self):
        self.assertAlmostEqual(
            9 ** Rational(-1, 2), 0.3333333333333333, places=8
        )

    def test_raise_a_real_number_to_a_zero_rational(self):
        self.assertAlmostEqual(2 ** Rational(0, 1), 1.0, places=8)

    # Test reduction to lowest terms
    def test_reduce_positive(self):
        self.assertEqual(Rational(2, 4), Rational(1, 2))

    def test_reduce_negative(self):
        self.assertEqual(Rational(-4, 6), Rational(-2, 3))

    def test_reduce_rational_with_negative_denominator(self):
        self.assertEqual(Rational(3, -9), Rational(-1, 3))

    def test_reduce_zero(self):
        self.assertEqual(Rational(0, 6), Rational(0, 1))

    def test_reduce_integer(self):
        self.assertEqual(Rational(-14, 7), Rational(-2, 1))

    def test_reduce_one(self):
        self.assertEqual(Rational(13, 13), Rational(1, 1))


if __name__ == '__main__':
    unittest.main()
