import unittest

from yacht import score

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0
import yacht


class YachtTest(unittest.TestCase):
    def test_yacht(self):
        input_dice = [5, 5, 5, 5, 5]
        expected = 50
        self.assertEqual(score(input_dice, yacht.YACHT), expected)

    def test_not_yacht(self):
        input_dice = [1, 3, 3, 2, 5]
        expected = 0
        self.assertEqual(score(input_dice, yacht.YACHT), expected)

    def test_ones(self):
        input_dice = [1, 1, 1, 3, 5]
        expected = 3
        self.assertEqual(score(input_dice, yacht.ONES), expected)

    def test_ones_out_of_order(self):
        input_dice = [3, 1, 1, 5, 1]
        expected = 3
        self.assertEqual(score(input_dice, yacht.ONES), expected)

    def test_no_ones(self):
        input_dice = [4, 3, 6, 5, 5]
        expected = 0
        self.assertEqual(score(input_dice, yacht.ONES), expected)

    def test_twos(self):
        input_dice = [2, 3, 4, 5, 6]
        expected = 2
        self.assertEqual(score(input_dice, yacht.TWOS), expected)

    def test_fours(self):
        input_dice = [1, 4, 1, 4, 1]
        expected = 8
        self.assertEqual(score(input_dice, yacht.FOURS), expected)

    def test_yacht_counted_as_threes(self):
        input_dice = [3, 3, 3, 3, 3]
        expected = 15
        self.assertEqual(score(input_dice, yacht.THREES), expected)

    def test_yacht_of_3s_counted_as_fives(self):
        input_dice = [3, 3, 3, 3, 3]
        expected = 0
        self.assertEqual(score(input_dice, yacht.FIVES), expected)

    def test_sixes(self):
        input_dice = [2, 3, 4, 5, 6]
        expected = 6
        self.assertEqual(score(input_dice, yacht.SIXES), expected)

    def test_full_house_two_small_three_big(self):
        input_dice = [2, 2, 4, 4, 4]
        expected = 16
        self.assertEqual(score(input_dice, yacht.FULL_HOUSE), expected)

    def test_full_house_three_small_two_big(self):
        input_dice = [5, 3, 3, 5, 3]
        expected = 19
        self.assertEqual(score(input_dice, yacht.FULL_HOUSE), expected)

    def test_two_pair_is_not_a_full_house(self):
        input_dice = [2, 2, 4, 4, 5]
        expected = 0
        self.assertEqual(score(input_dice, yacht.FULL_HOUSE), expected)

    def test_four_of_a_kind_is_not_a_full_house(self):
        input_dice = [1, 4, 4, 4, 4]
        expected = 0
        self.assertEqual(score(input_dice, yacht.FULL_HOUSE), expected)

    def test_yacht_is_not_a_full_house(self):
        input_dice = [2, 2, 2, 2, 2]
        expected = 0
        self.assertEqual(score(input_dice, yacht.FULL_HOUSE), expected)

    def test_four_of_a_kind(self):
        input_dice = [6, 6, 4, 6, 6]
        expected = 24
        self.assertEqual(score(input_dice, yacht.FOUR_OF_A_KIND), expected)

    def test_yacht_can_be_scored_as_four_of_a_kind(self):
        input_dice = [3, 3, 3, 3, 3]
        expected = 12
        self.assertEqual(score(input_dice, yacht.FOUR_OF_A_KIND), expected)

    def test_full_house_is_not_four_of_a_kind(self):
        input_dice = [3, 3, 3, 5, 5]
        expected = 0
        self.assertEqual(score(input_dice, yacht.FOUR_OF_A_KIND), expected)

    def test_little_straight(self):
        input_dice = [3, 5, 4, 1, 2]
        expected = 30
        self.assertEqual(score(input_dice, yacht.LITTLE_STRAIGHT), expected)

    def test_little_straight_as_big_straight(self):
        input_dice = [1, 2, 3, 4, 5]
        expected = 0
        self.assertEqual(score(input_dice, yacht.BIG_STRAIGHT), expected)

    def test_four_in_order_but_not_a_little_straight(self):
        input_dice = [1, 1, 2, 3, 4]
        expected = 0
        self.assertEqual(score(input_dice, yacht.LITTLE_STRAIGHT), expected)

    def test_no_pairs_but_not_a_little_straight(self):
        input_dice = [1, 2, 3, 4, 6]
        expected = 0
        self.assertEqual(score(input_dice, yacht.LITTLE_STRAIGHT), expected)

    def test_minimum_is_1_maximum_is_5_but_not_a_little_straight(self):
        input_dice = [1, 1, 3, 4, 5]
        expected = 0
        self.assertEqual(score(input_dice, yacht.LITTLE_STRAIGHT), expected)

    def test_big_straight(self):
        input_dice = [4, 6, 2, 5, 3]
        expected = 30
        self.assertEqual(score(input_dice, yacht.BIG_STRAIGHT), expected)

    def test_big_straight_as_little_straight(self):
        input_dice = [6, 5, 4, 3, 2]
        expected = 0
        self.assertEqual(score(input_dice, yacht.LITTLE_STRAIGHT), expected)

    def test_no_pairs_but_not_a_big_straight(self):
        input_dice = [6, 5, 4, 3, 1]
        expected = 0
        self.assertEqual(score(input_dice, yacht.BIG_STRAIGHT), expected)

    def test_choice(self):
        input_dice = [3, 3, 5, 6, 6]
        expected = 23
        self.assertEqual(score(input_dice, yacht.CHOICE), expected)

    def test_yacht_as_choice(self):
        input_dice = [2, 2, 2, 2, 2]
        expected = 10
        self.assertEqual(score(input_dice, yacht.CHOICE), expected)


if __name__ == "__main__":
    unittest.main()
