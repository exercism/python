import unittest

from queen_attack import board, can_attack


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class QueenAttackTest(unittest.TestCase):

    def test_queen_valid_position(self):
        try:
            board((1, 1), (2, 2))
        except ValueError:
            self.fail("Unexpected Exception")

    def test_queen_negative_row(self):
        with self.assertRaisesWithMessage(ValueError):
            board((1, 1), (-2, 2))

    def test_queen_invalid_row(self):
        with self.assertRaisesWithMessage(ValueError):
            board((1, 1), (8, 4))

    def test_queen_negative_column(self):
        with self.assertRaisesWithMessage(ValueError):
            board((1, 1), (2, -2))

    def test_queen_invalid_column(self):
        with self.assertRaisesWithMessage(ValueError):
            board((1, 1), (4, 8))

    def test_attack_false(self):
        self.assertIs(can_attack((2, 4), (6, 6)), False)

    def test_attack_same_row(self):
        self.assertIs(can_attack((2, 4), (2, 6)), True)

    def test_attack_same_column(self):
        self.assertIs(can_attack((4, 5), (2, 5)), True)

    def test_attack_diagonal1(self):
        self.assertIs(can_attack((2, 2), (0, 4)), True)

    def test_attack_diagonal2(self):
        self.assertIs(can_attack((2, 2), (3, 1)), True)

    def test_attack_diagonal3(self):
        self.assertIs(can_attack((2, 2), (1, 1)), True)

    def test_attack_diagonal4(self):
        self.assertIs(can_attack((2, 2), (5, 5)), True)

    # Tests beyond this point are not part of the canonical data.

    # If either board or can_attack are called with an invalid board position
    # they should raise a ValueError with a meaningful error message.
    def test_invalid_position_can_attack(self):
        with self.assertRaisesWithMessage(ValueError):
            can_attack((0, 0), (7, 8))

    def test_queens_same_position_board(self):
        with self.assertRaisesWithMessage(ValueError):
            board((2, 2), (2, 2))

    def test_queens_same_position_can_attack(self):
        with self.assertRaisesWithMessage(ValueError):
            can_attack((2, 2), (2, 2))

    def test_board1(self):
        ans = ['________',
               '________',
               '___W____',
               '________',
               '________',
               '______B_',
               '________',
               '________']
        self.assertEqual(board((2, 3), (5, 6)), ans)

    def test_board2(self):
        ans = ['______W_',
               '_______B',
               '________',
               '________',
               '________',
               '________',
               '________',
               '________']
        self.assertEqual(board((0, 6), (1, 7)), ans)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
