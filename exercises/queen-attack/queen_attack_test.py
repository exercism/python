import unittest

from queen_attack import Queen


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0

class QueenAttackTest(unittest.TestCase):

    # Test creation of Queens with valid and invalid positions
    def test_queen_valid_position(self):
        try:
            Queen(2, 2)
        except ValueError:
            self.fail("Unexpected Exception")

    def test_queen_negative_row(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(-2, 2)

    def test_queen_invalid_row(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(8, 4)

    def test_queen_negative_column(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(2, -2)

    def test_queen_invalid_column(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(4, 8)

    # Test the ability of one queen to attack another
    def test_attack_false(self):
        self.assertIs(Queen(2, 4).can_attack(Queen(6, 6)), False)

    def test_attack_same_row(self):
        self.assertIs(Queen(2, 4).can_attack(Queen(2, 6)), True)

    def test_attack_same_column(self):
        self.assertIs(Queen(4, 5).can_attack(Queen(2, 5)), True)

    def test_attack_diagonal1(self):
        self.assertIs(Queen(2, 2).can_attack(Queen(0, 4)), True)

    def test_attack_diagonal2(self):
        self.assertIs(Queen(2, 2).can_attack(Queen(3, 1)), True)

    def test_attack_diagonal3(self):
        self.assertIs(Queen(2, 2).can_attack(Queen(1, 1)), True)

    def test_attack_diagonal4(self):
        self.assertIs(Queen(2, 2).can_attack(Queen(5, 5)), True)

    # Track-specific tests
    def test_queens_same_position_can_attack(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(2, 2).can_attack(Queen(2, 2))

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
