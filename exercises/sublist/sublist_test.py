import unittest

from sublist import check_lists, SUBLIST, SUPERLIST, EQUAL, UNEQUAL


class SublistTest(unittest.TestCase):
    def test_unique_return_vals(self):
        self.assertEqual(4, len(set([SUBLIST, SUPERLIST, EQUAL, UNEQUAL])))

    def test_empty_lists(self):
        self.assertEqual(EQUAL, check_lists([], []))

    def test_empty_list_within(self):
        self.assertEqual(SUBLIST, check_lists([], [1, 2, 3]))

    def test_within_empty_list(self):
        self.assertEqual(SUPERLIST, check_lists([1], []))

    def test_equal_lists(self):
        l1 = [0, 1, 2]
        l2 = [0, 1, 2]
        self.assertEqual(EQUAL, check_lists(l1, l2))

    def test_different_lists(self):
        l1 = list(range(1000000))
        l2 = list(range(1, 1000001))
        self.assertEqual(UNEQUAL, check_lists(l1, l2))

    def test_false_start(self):
        l1 = [1, 2, 5]
        l2 = [0, 1, 2, 3, 1, 2, 5, 6]
        self.assertEqual(SUBLIST, check_lists(l1, l2))

    def test_consecutive(self):
        l1 = [1, 1, 2]
        l2 = [0, 1, 1, 1, 2, 1, 2]
        self.assertEqual(SUBLIST, check_lists(l1, l2))

    def test_sublist_at_start(self):
        l1 = [0, 1, 2]
        l2 = [0, 1, 2, 3, 4, 5]
        self.assertEqual(SUBLIST, check_lists(l1, l2))

    def test_sublist_in_middle(self):
        l1 = [2, 3, 4]
        l2 = [0, 1, 2, 3, 4, 5]
        self.assertEqual(SUBLIST, check_lists(l1, l2))

    def test_sublist_at_end(self):
        l1 = [3, 4, 5]
        l2 = [0, 1, 2, 3, 4, 5]
        self.assertEqual(SUBLIST, check_lists(l1, l2))

    def test_at_start_of_superlist(self):
        l1 = [0, 1, 2, 3, 4, 5]
        l2 = [0, 1, 2]
        self.assertEqual(SUPERLIST, check_lists(l1, l2))

    def test_in_middle_of_superlist(self):
        l1 = [0, 1, 2, 3, 4, 5]
        l2 = [2, 3]
        self.assertEqual(SUPERLIST, check_lists(l1, l2))

    def test_at_end_of_superlist(self):
        l1 = [0, 1, 2, 3, 4, 5]
        l2 = [3, 4, 5]
        self.assertEqual(SUPERLIST, check_lists(l1, l2))

    def test_large_lists(self):
        l1 = list(range(1000)) * 1000 + list(range(1000, 1100))
        l2 = list(range(900, 1050))
        self.assertEqual(SUPERLIST, check_lists(l1, l2))

    def test_spread_sublist(self):
        multiples_of_3 = list(range(3, 200, 3))
        multiples_of_15 = list(range(15, 200, 15))
        self.assertEqual(UNEQUAL,
                         check_lists(multiples_of_15, multiples_of_3))

    def test_avoid_sets(self):
        self.assertEqual(UNEQUAL, check_lists([1, 3], [1, 2, 3]))
        self.assertEqual(UNEQUAL, check_lists([1, 2, 3], [1, 3]))
        self.assertEqual(UNEQUAL, check_lists([1, 2, 3], [3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
