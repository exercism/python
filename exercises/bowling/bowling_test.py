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

if __name__ == '__main__':
    unittest.main()
