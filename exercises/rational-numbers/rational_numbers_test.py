import unittest

from rational_numbers import abs, add, div, exprational, expreal, mul, reduce, sub

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class RationalNumbersTest(unittest.TestCase):

    # Tests of type: Arithmetic

    # Addition

    def test_add_two_positive_rational_numbers(self):
        pass

    def test_add_a_positive_rational_number_and_a_negative_rational_number(self):
        pass

    def test_add_two_negative_rational_numbers(self):
        pass

    def test_add_a_rational_number_to_its_additive_inverse(self):
        pass

    # Subtraction

    def test_subtract_two_positive_rational_numbers(self):
        pass

    def test_subtract_a_positive_rational_number_and_a_negative_rational_number(self):
        pass

    def test_subtract_two_negative_rational_numbers(self):
        pass

    def test_subtract_a_rational_number_from_itself(self):
        pass

    # Multiplication

    def test_multiply_two_positive_rational_numbers(self):
        pass

    def test_multiply_a_negative_rational_number_by_a_positive_rational_number(self):
        pass

    def test_multiply_two_negative_rational_numbers(self):
        pass

    def test_multiply_a_rational_number_by_its_reciprocal(self):
        pass

    def test_multiply_a_rational_number_by_1(self):
        pass

    def test_multiply_a_rational_number_by_0(self):
        pass

    # Division

    def test_divide_two_positive_rational_numbers(self):
        pass

    def test_divide_a_positive_rational_number_by_a_negative_rational_number(self):
        pass

    def test_divide_two_negative_rational_numbers(self):
        pass

    def test_divide_a_rational_number_by_1(self):
        pass

    # Tests of type: Absolute value

    # Absolute value of a positive rational number

    # Absolute value of a positive rational number with negative numerator and denominator

    # Absolute value of a negative rational number

    # Absolute value of a negative rational number with negative denominator

    # Absolute value of zero

    # Tests of type: Exponentiation of a rational number

    # Raise a positive rational number to a positive integer power

    # Raise a negative rational number to a positive integer power

    # Raise zero to an integer power

    # Raise one to an integer power

    # Raise a positive rational number to the power of zero

    # Raise a negative rational number to the power of zero

    # Tests of type: Exponentiation of a real number to a rational number

    # Raise a real number to a positive rational number

    # Raise a real number to a negative rational number

    # Raise a real number to a zero rational number

    # Tests of type: Reduction to lowest terms

    # Reduce a positive rational number to lowest terms

    # Reduce a negative rational number to lowest terms

    # Reduce a rational number with a negative denominator to lowest terms

    # Reduce zero to lowest terms

    # Reduce an integer to lowest terms

    # Reduce one to lowest terms


if __name__ == "__main__":
    unittest.main()
