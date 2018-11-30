"""
You can make the following assumptions about the inputs to the
'sum_of_multiples' function:
    * All input numbers are non-negative 'int's, i.e. natural numbers
      including zero.
    * A list of factors must be given, and its elements are unique
      and sorted in ascending order.
"""

import unittest

from sum_of_multiples import sum_of_multiples


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0

class SumOfMultiplesTest(unittest.TestCase):
    def test_multiples_with_no_factors_in_limit(self):
        self.assertEqual(sum_of_multiples(1, [3, 5]), 0)

    def test_multiples_of_one_factor_within_limit(self):
        self.assertEqual(sum_of_multiples(4, [3, 5]), 3)

    def test_various_multiples_in_limit(self):
        self.assertEqual(sum_of_multiples(7, [3]), 9)

    def test_various_factors_with_multiples_in_limit(self):
        self.assertEqual(sum_of_multiples(10, [3, 5]), 23)

    def test_multiples_counted_only_once(self):
        self.assertEqual(sum_of_multiples(100, [3, 5]), 2318)

    def test_multiples_with_large_limit(self):
        self.assertEqual(sum_of_multiples(1000, [3, 5]), 233168)

    def test_multiples_with_three_factors(self):
        self.assertEqual(sum_of_multiples(20, [7, 13, 17]), 51)

    def test_multiples_with_factors_not_prime(self):
        self.assertEqual(sum_of_multiples(15, [4, 6]), 30)

    def test_multiples_with_factors_prime_and_not(self):
        self.assertEqual(sum_of_multiples(150, [5, 6, 8]), 4419)

    def test_multiples_with_similar_factors(self):
        self.assertEqual(sum_of_multiples(51, [5, 25]), 275)

    def test_multiples_with_large_factors(self):
        self.assertEqual(sum_of_multiples(10000, [43, 47]), 2203160)

    def test_multiples_of_one_will_be_all(self):
        self.assertEqual(sum_of_multiples(100, [1]), 4950)

    def test_multiples_of_an_empty_list(self):
        self.assertEqual(sum_of_multiples(10000, []), 0)

    def test_multiples_of_zero_will_be_none(self):
        self.assertEqual(sum_of_multiples(1, [0]), 0)

    def test_multiples_with_a_zero_factor(self):
        self.assertEqual(sum_of_multiples(4, [0, 3]), 3)

    def test_multiples_of_several_factors(self):
        self.assertEqual(sum_of_multiples(10000,
                         [2, 3, 5, 7, 11]), 39614537)


if __name__ == '__main__':
    unittest.main()
