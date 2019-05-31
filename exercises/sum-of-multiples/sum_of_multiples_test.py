"""
You can make the following assumptions about the inputs to the
'sum' function:
    * All input numbers are non-negative 'int's, i.e. natural numbers
      including zero.
    * A list of factors must be given, and its elements are unique
      and sorted in ascending order.
"""

import unittest

from sum_of_multiples import sum


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0

class SumOfMultiplesTest(unittest.TestCase):
    def test_no_multiples_within_limit(self):
        self.assertEqual(sum([3, 5], 1), 0)

    def test_one_factor_has_multiples_within_limit(self):
        self.assertEqual(sum([3, 5], 4), 3)

    def test_more_than_one_multiple_within_limit(self):
        self.assertEqual(sum([3], 7), 9)

    def test_various_factors_with_multiples_in_limit(self):
        self.assertEqual(sum([3, 5], 10), 23)

    def test_each_multiple_is_only_counted_once(self):
        self.assertEqual(sum([3, 5], 100), 2318)

    def test_a_much_larger_limit(self):
        self.assertEqual(sum([3, 5], 1000), 233168)

    def test_three_factors(self):
        self.assertEqual(sum([7, 13, 17], 20), 51)

    def test_factors_not_relatively_prime(self):
        self.assertEqual(sum([4, 6], 15), 30)

    def test_some_pairs_of_factors_relatively_prime_and_some_not(self):
        self.assertEqual(sum([5, 6, 8], 150), 4419)

    def test_one_factor_is_a_multiple_of_another(self):
        self.assertEqual(sum([5, 25], 51), 275)

    def test_much_larger_factors(self):
        self.assertEqual(sum([43, 47], 10000), 2203160)

    def test_all_numbers_are_multiples_of_1(self):
        self.assertEqual(sum([1], 100), 4950)

    def test_no_factors_means_an_empty_sum(self):
        self.assertEqual(sum([], 10000), 0)

    def test_the_only_multiple_of_0_is_0(self):
        self.assertEqual(sum([0], 1), 0)

    def test_the_factor_0_does_not_affect_the_sum_of_other_factors(self):
        self.assertEqual(sum([3, 0], 4), 3)

    def test_solutions_must_extend_to_cardinality_greater_than_3(self):
        self.assertEqual(sum([2, 3, 5, 7, 11], 10000), 39614537)


if __name__ == '__main__':
    unittest.main()
