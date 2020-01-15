import unittest

from book_store import total

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0


class BookStoreTest(unittest.TestCase):
    def test_only_a_single_book(self):
        results = [1]
        table = 800
        self.assertEqual(total(results), table)

    def test_two_of_the_same_book(self):
        results = [2, 2]
        table = 1600
        self.assertEqual(total(results), table)

    def test_empty_basket(self):
        results = []
        table = 0
        self.assertEqual(total(results), table)

    def test_two_different_books(self):
        results = [1, 2]
        table = 1520
        self.assertEqual(total(results), table)

    def test_three_different_books(self):
        results = [1, 2, 3]
        table = 2160
        self.assertEqual(total(results), table)

    def test_four_different_books(self):
        results = [1, 2, 3, 4]
        table = 2560
        self.assertEqual(total(results), table)

    def test_five_different_books(self):
        results = [1, 2, 3, 4, 5]
        table = 3000
        self.assertEqual(total(results), table)

    def test_two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three(self):
        results = [1, 1, 2, 2, 3, 3, 4, 5]
        table = 5120
        self.assertEqual(total(results), table)

    def test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three(self):
        results = [1, 1, 2, 3, 4, 4, 5, 5]
        table = 5120
        self.assertEqual(total(results), table)

    def test_group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three(self):
        results = [1, 1, 2, 2, 3, 4]
        table = 4080
        self.assertEqual(total(results), table)

    def test_two_each_of_first_4_books_and_1_copy_each_of_rest(self):
        results = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        table = 5560
        self.assertEqual(total(results), table)

    def test_two_copies_of_each_book(self):
        results = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        table = 6000
        self.assertEqual(total(results), table)

    def test_three_copies_of_first_book_and_2_each_of_remaining(self):
        results = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
        table = 6800
        self.assertEqual(total(results), table)

    def test_three_each_of_first_2_books_and_2_each_of_remaining_books(self):
        results = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2]
        table = 7520
        self.assertEqual(total(results), table)

    def test_four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three(
        self
    ):
        results = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
        table = 10240
        self.assertEqual(total(results), table)


if __name__ == "__main__":
    unittest.main()
