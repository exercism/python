import unittest

from perfect_numbers import (
    classify,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class PerfectNumbersTest(unittest.TestCase):
    def test_smallest_perfect_number_is_classified_correctly(self):
        self.assertIs(classify(6), "perfect")

    def test_medium_perfect_number_is_classified_correctly(self):
        self.assertIs(classify(28), "perfect")

    def test_large_perfect_number_is_classified_correctly(self):
        self.assertIs(classify(33550336), "perfect")


class AbundantNumbersTest(unittest.TestCase):
    def test_smallest_abundant_number_is_classified_correctly(self):
        self.assertIs(classify(12), "abundant")

    def test_medium_abundant_number_is_classified_correctly(self):
        self.assertIs(classify(30), "abundant")

    def test_large_abundant_number_is_classified_correctly(self):
        self.assertIs(classify(33550335), "abundant")


class DeficientNumbersTest(unittest.TestCase):
    def test_smallest_prime_deficient_number_is_classified_correctly(self):
        self.assertIs(classify(2), "deficient")

    def test_smallest_non_prime_deficient_number_is_classified_correctly(self):
        self.assertIs(classify(4), "deficient")

    def test_medium_deficient_number_is_classified_correctly(self):
        self.assertIs(classify(32), "deficient")

    def test_large_deficient_number_is_classified_correctly(self):
        self.assertIs(classify(33550337), "deficient")

    def test_edge_case_no_factors_other_than_itself_is_classified_correctly(self):
        self.assertIs(classify(1), "deficient")


class InvalidInputsTest(unittest.TestCase):
    def test_zero_is_rejected_as_it_is_not_a_positive_integer(self):
        with self.assertRaises(ValueError) as err:
            classify(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0],
            "Classification is only possible for positive integers.",
        )

    def test_negative_integer_is_rejected_as_it_is_not_a_positive_integer(self):
        with self.assertRaises(ValueError) as err:
            classify(-1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0],
            "Classification is only possible for positive integers.",
        )
