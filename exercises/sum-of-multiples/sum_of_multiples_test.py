import unittest

from sum_of_multiples import sum_of_multiples

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.0


class SumOfMultiplesTest(unittest.TestCase):
    def test_no_multiples_within_limit(self):
        self.assertEqual(sum_of_multiples(1, [3, 5]), 0)

    def test_one_factor_has_multiples_within_limit(self):
        self.assertEqual(sum_of_multiples(4, [3, 5]), 3)

    def test_more_than_one_multiple_within_limit(self):
        self.assertEqual(sum_of_multiples(7, [3]), 9)

    def test_more_than_one_factor_with_multiples_within_limit(self):
        self.assertEqual(sum_of_multiples(10, [3, 5]), 23)

    def test_each_multiple_is_only_counted_once(self):
        self.assertEqual(sum_of_multiples(100, [3, 5]), 2318)

    def test_a_much_larger_limit(self):
        self.assertEqual(sum_of_multiples(1000, [3, 5]), 233168)

    def test_three_factors(self):
        self.assertEqual(sum_of_multiples(20, [7, 13, 17]), 51)

    def test_factors_not_relatively_prime(self):
        self.assertEqual(sum_of_multiples(15, [4, 6]), 30)

    def test_some_pairs_of_factors_relatively_prime_and_some_not(self):
        self.assertEqual(sum_of_multiples(150, [5, 6, 8]), 4419)

    def test_one_factor_is_a_multiple_of_another(self):
        self.assertEqual(sum_of_multiples(51, [5, 25]), 275)

    def test_much_larger_factors(self):
        self.assertEqual(sum_of_multiples(10000, [43, 47]), 2203160)

    def test_all_numbers_are_multiples_of_1(self):
        self.assertEqual(sum_of_multiples(100, [1]), 4950)

    def test_no_factors_means_an_empty_sum(self):
        self.assertEqual(sum_of_multiples(10000, []), 0)

    def test_the_only_multiple_of_0_is_0(self):
        self.assertEqual(sum_of_multiples(1, [0]), 0)

    def test_the_factor_0_does_not_affect_the_sum_of_multiples_of_other_factors(self):
        self.assertEqual(sum_of_multiples(4, [3, 0]), 3)

    def test_solutions_using_include_exclude_must_extend_to_cardinality_greater_than_3(
        self
    ):
        self.assertEqual(sum_of_multiples(10000, [2, 3, 5, 7, 11]), 39614537)


if __name__ == "__main__":
    unittest.main()
