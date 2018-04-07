import unittest

from yacht import score


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class YachtTests(unittest.TestCase):
    def test_yacht(self):
        self.assertEqual(score([5, 5, 5, 5, 5], "yacht"), 50)

    def test_not_yacht(self):
        self.assertEqual(score([1, 3, 3, 2, 5], "yacht"), 0)

    def test_ones(self):
        self.assertEqual(score([1, 1, 1, 3, 5], "ones"), 3)

    def test_ones_out_of_order(self):
        self.assertEqual(score([3, 1, 1, 5, 1], "ones"), 3)

    def test_no_ones(self):
        self.assertEqual(score([4, 3, 6, 5, 5], "ones"), 0)

    def test_twos(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "twos"), 2)

    def test_fours(self):
        self.assertEqual(score([1, 4, 1, 4, 1], "fours"), 8)

    def test_yacht_counted_as_threes(self):
        self.assertEqual(score([3, 3, 3, 3, 3], "threes"), 15)

    def test_yacht_of_threes_counted_as_fives(self):
        self.assertEqual(score([3, 3, 3, 3, 3], "fives"), 0)

    def test_sixes(self):
        self.assertEqual(score([2, 3, 4, 5, 6], "sixes"), 6)

    def test_full_house_two_small_three_big(self):
        self.assertEqual(score([2, 2, 4, 4, 4], "full house"), 16)

    def test_full_house_three_small_two_big(self):
        self.assertEqual(score([5, 3, 3, 5, 3], "full house"), 19)

    def test_two_pair_is_not_a_full_house(self):
        self.assertEqual(score([2, 2, 4, 4, 5], "full house"), 0)

    def test_yacht_is_not_a_full_house(self):
        self.assertEqual(score([2, 2, 2, 2, 2], "full house"), 0)

    def test_four_of_a_kind(self):
        self.assertEqual(score([6, 6, 4, 6, 6], "four of a kind"), 24)

    def test_yacht_can_be_scored_as_four_of_a_kind(self):
        self.assertEqual(score([3, 3, 3, 3, 3], "four of a kind"), 12)

    def test_full_house_is_not_four_of_a_kind(self):
        self.assertEqual(score([3, 5, 4, 1, 2], "four of a kind"), 0)

    def test_little_straight(self):
        self.assertEqual(score([3, 5, 4, 1, 2], "little straight"), 30)

    def test_little_straight_as_big_straight(self):
        self.assertEqual(score([1, 2, 3, 4, 5], "big straight"), 0)

    def test_four_in_order_but_not_a_little_straight(self):
        self.assertEqual(score([1, 1, 2, 3, 4], "little straight"), 0)

    def test_no_pairs_but_not_a_little_straight(self):
        self.assertEqual(score([1, 2, 3, 4, 6], "little straight"), 0)

    def test_min_1_max_5_but_not_a_little_straight(self):
        self.assertEqual(score([1, 1, 3, 4, 5], "little straight"), 0)

    def test_big_straight(self):
        self.assertEqual(score([4, 6, 2, 5, 3], "big straight"), 30)

    def test_big_straight_as_little_straight(self):
        self.assertEqual(score([6, 5, 4, 3, 2], "little straight"), 0)

    def test_choice(self):
        self.assertEqual(score([3, 3, 5, 6, 6], "choice"), 23)

    def test_yacht_as_choice(self):
        self.assertEqual(score([2, 2, 2, 2, 2], "choice"), 10)


if __name__ == '__main__':
    unittest.main()
