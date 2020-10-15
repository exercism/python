import unittest

from queen_attack import Queen

# Tests adapted from `problem-specifications//canonical-data.json`


class QueenAttackTest(unittest.TestCase):
    # Test creation of Queens with valid and invalid positions
    def test_queen_with_a_valid_position(self):
        Queen(2, 2)

    def test_queen_must_have_positive_row(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(-2, 2)

    def test_queen_must_have_row_on_board(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(8, 4)

    def test_queen_must_have_positive_column(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(2, -2)

    def test_queen_must_have_column_on_board(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(4, 8)

    # Test the ability of one queen to attack another
    def test_can_not_attack(self):
        self.assertIs(Queen(2, 4).can_attack(Queen(6, 6)), False)

    def test_can_attack_on_same_row(self):
        self.assertIs(Queen(2, 4).can_attack(Queen(2, 6)), True)

    def test_can_attack_on_same_column(self):
        self.assertIs(Queen(4, 5).can_attack(Queen(2, 5)), True)

    def test_can_attack_on_first_diagonal(self):
        self.assertIs(Queen(2, 2).can_attack(Queen(0, 4)), True)

    def test_can_attack_on_second_diagonal(self):
        self.assertIs(Queen(2, 2).can_attack(Queen(3, 1)), True)

    def test_can_attack_on_third_diagonal(self):
        self.assertIs(Queen(2, 2).can_attack(Queen(1, 1)), True)

    def test_can_attack_on_fourth_diagonal(self):
        self.assertIs(Queen(1, 7).can_attack(Queen(0, 6)), True)

    # Track-specific tests
    def test_queens_same_position_can_attack(self):
        with self.assertRaisesWithMessage(ValueError):
            Queen(2, 2).can_attack(Queen(2, 2))

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
