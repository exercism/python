import unittest

from book_store import total


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

class BookStoreTest(unittest.TestCase):
    def test_only_a_single_book(self):
        self.assertEqual(total([1]), 800)

    def test_two_of_the_same_book(self):
        self.assertEqual(total([2, 2]), 1600)

    def test_empty_basket(self):
        self.assertEqual(total([]), 0)

    def test_two_different_books(self):
        self.assertEqual(total([1, 2]), 1520)

    def test_three_different_books(self):
        self.assertEqual(total([1, 2, 3]), 2160)

    def test_four_different_books(self):
        self.assertEqual(total([1, 2, 3, 4]), 2560)

    def test_five_different_books(self):
        self.assertEqual(total([1, 2, 3, 4, 5]), 3000)

    def test_two_groups_of_4_is_cheaper_than_group_of_5_plus_group_of_3(self):
        self.assertEqual(total([1, 1, 2, 2, 3, 3, 4, 5]), 5120)

    def test_two_groups_of_4_is_cheaper_than_groups_of_5_and_3(self):
        self.assertEqual(total([1, 1, 2, 3, 4, 4, 5, 5]), 5120)

    def test_group_of_4_plus_group_of_2_is_cheaper_than_2_groups_of_3(self):
        self.assertEqual(total([1, 1, 2, 2, 3, 4]), 4080)

    def test_two_each_of_first_4_books_and_1_copy_each_of_rest(self):
        self.assertEqual(total([1, 1, 2, 2, 3, 3, 4, 4, 5]), 5560)

    def test_two_copies_of_each_book(self):
        self.assertEqual(total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 6000)

    def test_three_copies_of_first_book_and_2_each_of_remaining(self):
        self.assertEqual(
            total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]), 6800)

    def test_three_each_of_first_2_books_and_2_each_of_remaining_books(self):
        self.assertEqual(
            total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2]), 7520)

    def test_four_groups_of_4_are_cheaper_than_2_groups_each_of_5_and_3(self):
        self.assertEqual(
            total([1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]),
            10240)


if __name__ == '__main__':
    unittest.main()
