import unittest

from queen_attack import board, can_attack


class QueenAttackTest(unittest.TestCase):
    def test_board1(self):
        ans = ['________',
               '________',
               '___W____',
               '________',
               '________',
               '______B_',
               '________',
               '________']
        self.assertEqual(ans, board((2, 3), (5, 6)))

    def test_board2(self):
        ans = ['______W_',
               '_______B',
               '________',
               '________',
               '________',
               '________',
               '________',
               '________']
        self.assertEqual(ans, board((0, 6), (1, 7)))

    def test_attack_true1(self):
        self.assertEqual(True, can_attack((2, 3), (5, 6)))

    def test_attack_true2(self):
        self.assertEqual(True, can_attack((2, 6), (5, 3)))

    def test_attack_true3(self):
        self.assertEqual(True, can_attack((2, 4), (2, 7)))

    def test_attack_true4(self):
        self.assertEqual(True, can_attack((5, 4), (2, 4)))

    def test_attack_true5(self):
        self.assertEqual(True, can_attack((1, 1), (6, 6)))

    def test_attack_true6(self):
        self.assertEqual(True, can_attack((0, 6), (1, 7)))

    def test_attack_false1(self):
        self.assertEqual(False, can_attack((4, 2), (0, 5)))

    def test_attack_false2(self):
        self.assertEqual(False, can_attack((2, 3), (4, 7)))

    # If either board or can_attack are called with an invalid board position
    # they should raise a ValueError with a meaningful error message.
    def test_invalid_position_board(self):
        with self.assertRaises(ValueError):
            board((0, 0), (7, 8))

    def test_invalid_position_can_attack(self):
        with self.assertRaises(ValueError):
            can_attack((0, 0), (7, 8))

    def test_queens_same_position_board(self):
        with self.assertRaises(ValueError):
            board((2, 2), (2, 2))

    def test_queens_same_position_can_attack(self):
        with self.assertRaises(ValueError):
            can_attack((2, 2), (2, 2))


if __name__ == '__main__':
    unittest.main()
