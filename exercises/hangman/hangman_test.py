import unittest

from example import Hangman

class HangmanTests(unittest.TestCase):
	def test_initially_9_failures_are_allowed(self):
		game = Hangman('foo')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 9)

	def test_initially_no_letters_are_guessed(self):
		game = Hangman('foo')

		self.assertEqual(game.get_masked_word(), '___')

	def test_after_10_failures_the_game_is_over(self):
		game = Hangman('foo')

		for i in range(10):
			game.guess('x')

		self.assertEqual(game.get_status(), 'lose')

	def test_feeding_a_correct_letter_removes_underscores(self):
		game = Hangman('foobar')

		game.guess('b')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 9)
		self.assertEqual(game.get_masked_word(),'___b__')

		game.guess('o')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 9)
		self.assertEqual(game.get_masked_word(),'_oob__')

	def test_feeding_a_correct_letter_twice_counts_as_a_failure(self):
		game = Hangman('foobar')

		game.guess('b')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 9)
		self.assertEqual(game.get_masked_word(),'___b__')

		game.guess('b')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 8)
		self.assertEqual(game.get_masked_word(),'___b__')

	def test_getting_all_the_letters_right_makes_for_a_win(self):
		game = Hangman('hello')

		game.guess('b')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 8)
		self.assertEqual(game.get_masked_word(),'_____')

		game.guess('e')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 8)
		self.assertEqual(game.get_masked_word(),'_e___')

		game.guess('l')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 8)
		self.assertEqual(game.get_masked_word(),'_ell_')

		game.guess('o')
		self.assertEqual(game.get_status(), 'busy')
		self.assertEqual(game.remainingGuesses, 8)
		self.assertEqual(game.get_masked_word(),'_ello')

		game.guess('h')
		self.assertEqual(game.get_status(), 'win')
		self.assertEqual(game.get_masked_word(), 'hello')


if __name__ == '__main__':
	unittest.main()