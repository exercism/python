import unittest

from example import BowlingGame


class BowlingTests(unittest.TestCase):
	def should_be_able_to_score_a_game_with_all_zeros(self):
		input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	
		self.game = BowlingGame()
		
		while (i <= len(input)):
			self.game.roll(input[i])
			
		score = self.score()
		print("here")
		self.assertEqual(score ,0)

if __name__ == '__main__':
    unittest.main()

