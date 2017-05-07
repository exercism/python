import unittest

from sublist import check_lists, SUBLIST, SUPERLIST, EQUAL, UNEQUAL


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class SublistTest(unittest.TestCase):
    def test_unique_return_values(self):
        self.assertEqual(len(set([SUBLIST, SUPERLIST, EQUAL, UNEQUAL])), 4)

    def test_empty_lists(self):
        self.assertEqual(
            check_lists([], []),
            EQUAL
        )

    def test_empty_list_within_non_empty_list(self):
        self.assertEqual(
            check_lists([], [1, 2, 3]),
            SUBLIST
        )

    def test_non_empty_list_contains_empty_list(self):
        self.assertEqual(
            check_lists([1, 2, 3], []),
            SUPERLIST
        )

    def test_list_equals_itself(self):
        self.assertEqual(
            check_lists([1, 2, 3], [1, 2, 3]),
            EQUAL
        )

    def test_different_lists(self):
        self.assertEqual(
            check_lists([1, 2, 3], [2, 3, 4]),
            UNEQUAL
        )

    def test_false_start(self):
        self.assertEqual(
            check_lists([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]),
            SUBLIST
        )

    def test_consecutive(self):
        self.assertEqual(
            check_lists([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]),
            SUBLIST
        )

    def test_sublist_at_start(self):
        self.assertEqual(
            check_lists([0, 1, 2], [0, 1, 2, 3, 4, 5]),
            SUBLIST
        )

    def test_sublist_in_middle(self):
        self.assertEqual(
            check_lists([2, 3, 4], [0, 1, 2, 3, 4, 5]),
            SUBLIST
        )

    def test_sublist_at_end(self):
        self.assertEqual(
            check_lists([3, 4, 5], [0, 1, 2, 3, 4, 5]),
            SUBLIST
        )

    def test_at_start_of_superlist(self):
        self.assertEqual(
            check_lists([0, 1, 2, 3, 4, 5], [0, 1, 2]),
            SUPERLIST
        )

    def test_in_middle_of_superlist(self):
        self.assertEqual(
            check_lists([0, 1, 2, 3, 4, 5], [2, 3]),
            SUPERLIST
        )

    def test_at_end_of_superlist(self):
        self.assertEqual(
            check_lists([0, 1, 2, 3, 4, 5], [3, 4, 5]),
            SUPERLIST
        )

    def test_first_list_missing_element_from_second_list(self):
        self.assertEqual(
            check_lists([1, 3], [1, 2, 3]),
            UNEQUAL
        )

    def test_second_list_missing_element_from_first_list(self):
        self.assertEqual(
            check_lists([1, 2, 3], [1, 3]),
            UNEQUAL
        )

    def test_order_matters_to_a_list(self):
        self.assertEqual(
            check_lists([1, 2, 3], [3, 2, 1]),
            UNEQUAL
        )

    def test_same_digits_but_different_numbers(self):
        self.assertEqual(
            check_lists([1, 0, 1], [10, 1]),
            UNEQUAL
        )

    # additional track specific test
    def test_inner_spaces(self):
        self.assertEqual(
            check_lists(['a c'], ['a', 'c']),
            UNEQUAL
        )

    # additional track specific test
    def test_large_lists(self):
        l1 = list(range(1000)) * 1000 + list(range(1000, 1100))
        l2 = list(range(900, 1050))
        self.assertEqual(check_lists(l1, l2), SUPERLIST)

    # additional track specific test
    def test_spread_sublist(self):
        multiples_of_3 = list(range(3, 200, 3))
        multiples_of_15 = list(range(15, 200, 15))
        self.assertEqual(check_lists(multiples_of_15, multiples_of_3), UNEQUAL)


if __name__ == '__main__':
    unittest.main()
