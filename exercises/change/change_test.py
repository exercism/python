import unittest

from change import find_fewest_coins

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0


class ChangeTest(unittest.TestCase):
    def test_single_coin_change(self):
        self.assertEqual(find_fewest_coins([1, 5, 10, 25, 100], 25), [25])

    def test_multiple_coin_change(self):
        self.assertEqual(find_fewest_coins([1, 5, 10, 25, 100], 15), [5, 10])

    def test_change_with_lilliputian_coins(self):
        self.assertEqual(find_fewest_coins([1, 4, 15, 20, 50], 23), [4, 4, 15])

    def test_change_with_lower_elbonia_coins(self):
        self.assertEqual(find_fewest_coins([1, 5, 10, 21, 25], 63), [21, 21, 21])

    def test_large_target_values(self):
        self.assertEqual(
            find_fewest_coins([1, 2, 5, 10, 20, 50, 100], 999),
            [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100],
        )

    def test_possible_change_without_unit_coins_available(self):
        self.assertEqual(find_fewest_coins([2, 5, 10, 20, 50], 21), [2, 2, 2, 5, 10])

    def test_another_possible_change_without_unit_coins_available(self):
        self.assertEqual(find_fewest_coins([4, 5], 27), [4, 4, 4, 5, 5, 5])

    def test_no_coins_make_0_change(self):
        self.assertEqual(find_fewest_coins([1, 5, 10, 21, 25], 0), [])

    def test_error_testing_for_change_smaller_than_the_smallest_of_coins(self):
        with self.assertRaisesWithMessage(ValueError):
            find_fewest_coins([5, 10], 3)

    def test_error_if_no_combination_can_add_up_to_target(self):
        with self.assertRaisesWithMessage(ValueError):
            find_fewest_coins([5, 10], 94)

    def test_cannot_find_negative_change_values(self):
        with self.assertRaisesWithMessage(ValueError):
            find_fewest_coins([1, 2, 5], -5)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
