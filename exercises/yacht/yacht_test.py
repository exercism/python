import unittest

import yacht

# Tests adapted from `problem-specifications//canonical-data.json`


class YachtTest(unittest.TestCase):
    def test_yacht(self):
        self.assertEqual(yacht.score([5, 5, 5, 5, 5], yacht.YACHT), 50)

    def test_not_yacht(self):
        self.assertEqual(yacht.score([1, 3, 3, 2, 5], yacht.YACHT), 0)

    def test_ones(self):
        self.assertEqual(yacht.score([1, 1, 1, 3, 5], yacht.ONES), 3)

    def test_ones_out_of_order(self):
        self.assertEqual(yacht.score([3, 1, 1, 5, 1], yacht.ONES), 3)

    def test_no_ones(self):
        self.assertEqual(yacht.score([4, 3, 6, 5, 5], yacht.ONES), 0)

    def test_twos(self):
        self.assertEqual(yacht.score([2, 3, 4, 5, 6], yacht.TWOS), 2)

    def test_fours(self):
        self.assertEqual(yacht.score([1, 4, 1, 4, 1], yacht.FOURS), 8)

    def test_yacht_counted_as_threes(self):
        self.assertEqual(yacht.score([3, 3, 3, 3, 3], yacht.THREES), 15)

    def test_yacht_of_3s_counted_as_fives(self):
        self.assertEqual(yacht.score([3, 3, 3, 3, 3], yacht.FIVES), 0)

    def test_sixes(self):
        self.assertEqual(yacht.score([2, 3, 4, 5, 6], yacht.SIXES), 6)

    def test_full_house_two_small_three_big(self):
        self.assertEqual(yacht.score([2, 2, 4, 4, 4], yacht.FULL_HOUSE), 16)

    def test_full_house_three_small_two_big(self):
        self.assertEqual(yacht.score([5, 3, 3, 5, 3], yacht.FULL_HOUSE), 19)

    def test_two_pair_is_not_a_full_house(self):
        self.assertEqual(yacht.score([2, 2, 4, 4, 5], yacht.FULL_HOUSE), 0)

    def test_four_of_a_kind_is_not_a_full_house(self):
        self.assertEqual(yacht.score([1, 4, 4, 4, 4], yacht.FULL_HOUSE), 0)

    def test_yacht_is_not_a_full_house(self):
        self.assertEqual(yacht.score([2, 2, 2, 2, 2], yacht.FULL_HOUSE), 0)

    def test_four_of_a_kind(self):
        self.assertEqual(yacht.score([6, 6, 4, 6, 6], yacht.FOUR_OF_A_KIND), 24)

    def test_yacht_can_be_scored_as_four_of_a_kind(self):
        self.assertEqual(yacht.score([3, 3, 3, 3, 3], yacht.FOUR_OF_A_KIND), 12)

    def test_full_house_is_not_four_of_a_kind(self):
        self.assertEqual(yacht.score([3, 3, 3, 5, 5], yacht.FOUR_OF_A_KIND), 0)

    def test_little_straight(self):
        self.assertEqual(yacht.score([3, 5, 4, 1, 2], yacht.LITTLE_STRAIGHT), 30)

    def test_little_straight_as_big_straight(self):
        self.assertEqual(yacht.score([1, 2, 3, 4, 5], yacht.BIG_STRAIGHT), 0)

    def test_four_in_order_but_not_a_little_straight(self):
        self.assertEqual(yacht.score([1, 1, 2, 3, 4], yacht.LITTLE_STRAIGHT), 0)

    def test_no_pairs_but_not_a_little_straight(self):
        self.assertEqual(yacht.score([1, 2, 3, 4, 6], yacht.LITTLE_STRAIGHT), 0)

    def test_minimum_is_1_maximum_is_5_but_not_a_little_straight(self):
        self.assertEqual(yacht.score([1, 1, 3, 4, 5], yacht.LITTLE_STRAIGHT), 0)

    def test_big_straight(self):
        self.assertEqual(yacht.score([4, 6, 2, 5, 3], yacht.BIG_STRAIGHT), 30)

    def test_big_straight_as_little_straight(self):
        self.assertEqual(yacht.score([6, 5, 4, 3, 2], yacht.LITTLE_STRAIGHT), 0)

    def test_no_pairs_but_not_a_big_straight(self):
        self.assertEqual(yacht.score([6, 5, 4, 3, 1], yacht.BIG_STRAIGHT), 0)

    def test_choice(self):
        self.assertEqual(yacht.score([3, 3, 5, 6, 6], yacht.CHOICE), 23)

    def test_yacht_as_choice(self):
        self.assertEqual(yacht.score([2, 2, 2, 2, 2], yacht.CHOICE), 10)


if __name__ == "__main__":
    unittest.main()
