import unittest

from bowling import BowlingGame


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.1

class BowlingTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll(self, rolls):
        [self.game.roll(roll) for roll in rolls]

    def roll_and_score(self, rolls):
        self.roll(rolls)
        return self.game.score()

    def test_should_be_able_to_score_a_game_with_all_zeros(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 0)

    def test_should_be_able_to_score_a_game_with_no_strikes_or_spares(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 90)

    def test_a_spare_follow_by_zeros_is_worth_ten_points(self):
        rolls = [6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 10)

    def test_points_scored_in_the_roll_after_a_spare_are_counted_twice(self):
        rolls = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 16)

    def test_consecutive_spares_each_get_a_one_roll_bonus(self):
        rolls = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 31)

    def test_last_frame_spare_gets_bonus_roll_that_is_counted_twice(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 17)

    def test_a_strike_earns_ten_points_in_a_frame_with_a_single_roll(self):
        rolls = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 10)

    def test_two_rolls_points_after_strike_are_counted_twice(self):
        rolls = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 26)

    def test_consecutive_stikes_each_get_the_two_roll_bonus(self):
        rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 81)

    def test_strike_in_last_frame_gets_two_roll_bonus_counted_once(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 10, 7, 1]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 18)

    def test_rolling_spare_with_bonus_roll_does_not_get_bonus(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 10, 7, 3]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 20)

    def test_strikes_with_the_two_bonus_rolls_do_not_get_bonus_rolls(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 10, 10]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 30)

    def test_strike_with_bonus_after_spare_in_last_frame_gets_no_bonus(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
                 3, 10]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 20)

    def test_all_strikes_is_a_perfect_game(self):
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 300)

    def test_rolls_cannot_score_negative_points(self):

        self.assertRaises(ValueError, self.game.roll, -11)

    def test_a_roll_cannot_score_more_than_10_points(self):

        self.assertRaises(ValueError, self.game.roll, 11)

    def test_two_rolls_in_a_frame_cannot_score_more_than_10_points(self):
        self.game.roll(5)

        self.assertRaises(ValueError, self.game.roll, 6)

    def test_bonus_after_strike_in_last_frame_cannot_score_more_than_10(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]

        self.roll(rolls)

        self.assertRaises(ValueError, self.game.roll, 11)

    def test_bonus_aft_last_frame_strk_can_be_more_than_10_if_1_is_strk(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 10, 6]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 26)

    def test_bonus_aft_last_frame_strk_cnt_be_strk_if_first_is_not_strk(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6]

        self.roll(rolls)

        self.assertRaises(ValueError, self.game.roll, 10)

    def test_an_incomplete_game_cannot_be_scored(self):
        rolls = [0, 0]

        self.roll(rolls)

        self.assertRaises(IndexError, self.game.score)

    def test_cannot_roll_if_there_are_already_ten_frames(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.roll(rolls)

        self.assertRaises(IndexError, self.game.roll, 0)

    def test_bonus_rolls_for_strike_must_be_rolled_before_score_is_calc(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]

        self.roll(rolls)

        self.assertRaises(IndexError, self.game.score)

    def test_both_bonuses_for_strike_must_be_rolled_before_score(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10]

        self.roll(rolls)

        self.assertRaises(IndexError, self.game.score)

    def test_bonus_rolls_for_spare_must_be_rolled_before_score_is_calc(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3]

        self.roll(rolls)

        self.assertRaises(IndexError, self.game.score)


if __name__ == '__main__':
    unittest.main()
