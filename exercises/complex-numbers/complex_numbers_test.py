from __future__ import division
import math

import unittest

from complex_numbers import ComplexNumber

# Tests adapted from `problem-specifications//canonical-data.json`


class ComplexNumbersTest(unittest.TestCase):

    # Real part

    def test_real_part_of_a_purely_real_number(self):
        self.assertEqual(ComplexNumber(1, 0).real, 1)

    def test_real_part_of_a_purely_imaginary_number(self):
        self.assertEqual(ComplexNumber(0, 1).real, 0)

    def test_real_part_of_a_number_with_real_and_imaginary_part(self):
        self.assertEqual(ComplexNumber(1, 2).real, 1)

    # Imaginary part

    def test_imaginary_part_of_a_purely_real_number(self):
        self.assertEqual(ComplexNumber(1, 0).imaginary, 0)

    def test_imaginary_part_of_a_purely_imaginary_number(self):
        self.assertEqual(ComplexNumber(0, 1).imaginary, 1)

    def test_imaginary_part_of_a_number_with_real_and_imaginary_part(self):
        self.assertEqual(ComplexNumber(1, 2).imaginary, 2)

    def test_imaginary_unit(self):
        self.assertEqual(
            ComplexNumber(0, 1) * ComplexNumber(0, 1), ComplexNumber(-1, 0)
        )

    # Arithmetic

    # Addition

    def test_add_purely_real_numbers(self):
        self.assertEqual(ComplexNumber(1, 0) + ComplexNumber(2, 0), ComplexNumber(3, 0))

    def test_add_purely_imaginary_numbers(self):
        self.assertEqual(ComplexNumber(0, 1) + ComplexNumber(0, 2), ComplexNumber(0, 3))

    def test_add_numbers_with_real_and_imaginary_part(self):
        self.assertEqual(ComplexNumber(1, 2) + ComplexNumber(3, 4), ComplexNumber(4, 6))

    # Subtraction

    def test_subtract_purely_real_numbers(self):
        self.assertEqual(
            ComplexNumber(1, 0) - ComplexNumber(2, 0), ComplexNumber(-1, 0)
        )

    def test_subtract_purely_imaginary_numbers(self):
        self.assertEqual(
            ComplexNumber(0, 1) - ComplexNumber(0, 2), ComplexNumber(0, -1)
        )

    def test_subtract_numbers_with_real_and_imaginary_part(self):
        self.assertEqual(
            ComplexNumber(1, 2) - ComplexNumber(3, 4), ComplexNumber(-2, -2)
        )

    # Multiplication

    def test_multiply_purely_real_numbers(self):
        self.assertEqual(ComplexNumber(1, 0) * ComplexNumber(2, 0), ComplexNumber(2, 0))

    def test_multiply_purely_imaginary_numbers(self):
        self.assertEqual(
            ComplexNumber(0, 1) * ComplexNumber(0, 2), ComplexNumber(-2, 0)
        )

    def test_multiply_numbers_with_real_and_imaginary_part(self):
        self.assertEqual(
            ComplexNumber(1, 2) * ComplexNumber(3, 4), ComplexNumber(-5, 10)
        )

    # Division

    def test_divide_purely_real_numbers(self):
        self.assertAlmostEqual(
            ComplexNumber(1, 0) / ComplexNumber(2, 0), ComplexNumber(0.5, 0)
        )

    def test_divide_purely_imaginary_numbers(self):
        self.assertAlmostEqual(
            ComplexNumber(0, 1) / ComplexNumber(0, 2), ComplexNumber(0.5, 0)
        )

    def test_divide_numbers_with_real_and_imaginary_part(self):
        self.assertAlmostEqual(
            ComplexNumber(1, 2) / ComplexNumber(3, 4), ComplexNumber(0.44, 0.08)
        )

    # Absolute value

    def test_absolute_value_of_a_positive_purely_real_number(self):
        self.assertEqual(abs(ComplexNumber(5, 0)), 5)

    def test_absolute_value_of_a_negative_purely_real_number(self):
        self.assertEqual(abs(ComplexNumber(-5, 0)), 5)

    def test_absolute_value_of_a_purely_imaginary_number_with_positive_imaginary_part(
        self
    ):
        self.assertEqual(abs(ComplexNumber(0, 5)), 5)

    def test_absolute_value_of_a_purely_imaginary_number_with_negative_imaginary_part(
        self
    ):
        self.assertEqual(abs(ComplexNumber(0, -5)), 5)

    def test_absolute_value_of_a_number_with_real_and_imaginary_part(self):
        self.assertEqual(abs(ComplexNumber(3, 4)), 5)

    # Complex conjugate

    def test_conjugate_a_purely_real_number(self):
        self.assertEqual(ComplexNumber(5, 0).conjugate(), ComplexNumber(5, 0))

    def test_conjugate_a_purely_imaginary_number(self):
        self.assertEqual(ComplexNumber(0, 5).conjugate(), ComplexNumber(0, -5))

    def test_conjugate_a_number_with_real_and_imaginary_part(self):
        self.assertEqual(ComplexNumber(1, 1).conjugate(), ComplexNumber(1, -1))

    # Complex exponential function

    def test_euler_s_identity_formula(self):
        self.assertAlmostEqual(ComplexNumber(0, math.pi).exp(), ComplexNumber(-1, 0))

    def test_exponential_of_0(self):
        self.assertAlmostEqual(ComplexNumber(0, 0).exp(), ComplexNumber(1, 0))

    def test_exponential_of_a_purely_real_number(self):
        self.assertAlmostEqual(ComplexNumber(1, 0).exp(), ComplexNumber(math.e, 0))

    def test_exponential_of_a_number_with_real_and_imaginary_part(self):
        self.assertAlmostEqual(
            ComplexNumber(math.log(2), math.pi).exp(), ComplexNumber(-2, 0)
        )

    # Additional tests for this track

    def test_equality_of_complex_numbers(self):
        self.assertEqual(ComplexNumber(1, 2), ComplexNumber(1, 2))

    def test_inequality_of_real_part(self):
        self.assertNotEqual(ComplexNumber(1, 2), ComplexNumber(2, 2))

    def test_inequality_of_imaginary_part(self):
        self.assertNotEqual(ComplexNumber(1, 2), ComplexNumber(1, 1))


if __name__ == "__main__":
    unittest.main()
