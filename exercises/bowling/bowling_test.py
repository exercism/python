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

if __name__ == '__main__':
    unittest.main()
