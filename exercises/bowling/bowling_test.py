import unittest

from example import BowlingGame


class BowlingTests(unittest.TestCase):
    def test_should_be_able_to_score_a_game_with_all_zeros(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 0)

    def test_should_be_able_to_score_a_game_with_no_strikes_or_spares(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 90)

    def test_a_spare_follow_by_zeros_is_worth_ten_points(self):
        rolls = [6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 10)

    def test_points_scored_in_the_roll_after_a_spare_are_counted_twice(self):
        rolls = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 16)

    def test_consecutive_spares_each_get_a_one_roll_bonus(self):
        rolls = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 31)

    def test_last_frame_spare_gets_bonus_roll_that_is_counted_twice(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 17)

    def test_a_strike_earns_ten_points_in_a_frame_with_a_single_roll(self):
        rolls = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 10)

    def test_two_rolls_points_after_strike_are_counted_twice(self):
        rolls = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 26)

    def test_consecutive_stikes_each_get_the_two_roll_bonus(self):
        rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 81)

    def test_strike_in_last_frame_gets_two_roll_bonus_counted_once(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 1]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 18)

    def test_rolling_spare_with_bonus_roll_does_not_get_bonus(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 3]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 20)

    def test_strikes_with_the_two_bonus_rolls_do_not_get_bonus_rolls(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 30)

    def test_strike_with_bonus_after_spare_in_last_frame_gets_no_bonus(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 10]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 20)

    def test_all_strikes_is_a_perfect_game(self):

        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

        self.game = BowlingGame()

        for roll in rolls:
            self.game.roll(roll)
        score = self.game.score()

        self.assertEqual(score, 300)


if __name__ == '__main__':
    unittest.main()
