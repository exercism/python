import unittest

from book_store import calculate_total


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.1

class BookStoreTests(unittest.TestCase):
    def test_only_a_single_book(self):
        self.assertAlmostEqual(calculate_total([1]), 8.00,
                               places=2)

    def test_two_of_the_same_book(self):
        self.assertAlmostEqual(calculate_total([2, 2]), 16.00,
                               places=2)

    def test_empty_basket(self):
        self.assertAlmostEqual(calculate_total([]), 0.00,
                               places=2)

    def test_two_different_books(self):
        self.assertAlmostEqual(calculate_total([1, 2]), 15.20,
                               places=2)

    def test_three_different_books(self):
        self.assertAlmostEqual(calculate_total([1, 2, 3]), 21.60,
                               places=2)

    def test_four_different_books(self):
        self.assertAlmostEqual(calculate_total([1, 2, 3, 4]), 25.60,
                               places=2)

    def test_five_different_books(self):
        self.assertAlmostEqual(
            calculate_total([1, 2, 3, 4, 5]), 30.00,
            places=2)

    def test_two_groups_of_4_is_cheaper_than_group_of_5_plus_group_of_3(self):
        self.assertAlmostEqual(
            calculate_total([1, 1, 2, 2, 3, 3, 4, 5]), 51.20,
            places=2)

    def test_group_of_4_plus_group_of_2_is_cheaper_than_2_groups_of_3(self):
        self.assertAlmostEqual(
            calculate_total([1, 1, 2, 2, 3, 4]), 40.80,
            places=2)

    def test_two_each_of_first_4_books_and_1_copy_each_of_rest(self):
        self.assertAlmostEqual(
            calculate_total([1, 1, 2, 2, 3, 3, 4, 4, 5]), 55.60,
            places=2)

    def test_two_copies_of_each_book(self):
        self.assertAlmostEqual(
            calculate_total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 60.00,
            places=2)

    def test_three_copies_of_first_book_and_2_each_of_remaining(self):
        self.assertAlmostEqual(
            calculate_total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]),
            68.00,
            places=2)

    def test_three_each_of_first_2_books_and_2_each_of_remaining_books(self):
        self.assertAlmostEqual(
            calculate_total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2]),
            75.20,
            places=2)


if __name__ == '__main__':
    unittest.main()
