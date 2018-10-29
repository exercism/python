import unittest

from change import find_minimum_coins


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

class ChangeTest(unittest.TestCase):
    def test_single_coin_change(self):
        self.assertEqual(find_minimum_coins(25, [1, 5, 10, 25, 100]), [25])

    def test_multiple_coin_change(self):
        self.assertEqual(find_minimum_coins(15, [1, 5, 10, 25, 100]), [5, 10])

    def test_change_with_Lilliputian_Coins(self):
        self.assertEqual(find_minimum_coins(23, [1, 4, 15, 20, 50]),
                         [4, 4, 15])

    def test_change_with_Lower_Elbonia_Coins(self):
        self.assertEqual(find_minimum_coins(63, [1, 5, 10, 21, 25]),
                         [21, 21, 21])

    def test_large_target_values(self):
        self.assertEqual(find_minimum_coins(999, [1, 2, 5, 10, 20, 50, 100]),
                         [2, 2, 5, 20, 20, 50, 100, 100, 100,
                          100, 100, 100, 100, 100, 100])

    def test_possible_change_without_unit_coins_available(self):
        self.assertEqual(find_minimum_coins(21, [2, 5, 10, 20, 50]),
                         [2, 2, 2, 5, 10])

    def test_another_possible_change_without_unit_coins_available(self):
        self.assertEqual(find_minimum_coins(27, [4, 5]),
                         [4, 4, 4, 5, 5, 5])

    def test_no_coins_make_0_change(self):
        self.assertEqual(find_minimum_coins(0, [1, 5, 10, 21, 25]), [])

    def test_error_testing_for_change_smaller_than_smallest_coin(self):
        with self.assertRaisesWithMessage(ValueError):
            find_minimum_coins(3, [5, 10])

    def test_error_if_no_combination_can_add_up_to_target(self):
        with self.assertRaisesWithMessage(ValueError):
            find_minimum_coins(94, [5, 10])

    def test_cannot_find_negative_change_values(self):
        with self.assertRaisesWithMessage(ValueError):
            find_minimum_coins(-5, [1, 2, 5])

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
