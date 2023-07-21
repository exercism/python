# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/queen-attack/canonical-data.json
# File last updated on 2023-07-19

import unittest

from queen_attack import (
    Queen,
)


class QueenAttackTest(unittest.TestCase):
    # Test creation of Queens with valid and invalid positions
    def test_queen_with_a_valid_position(self):
        Queen(2, 2)

    def test_queen_must_have_positive_row(self):
        with self.assertRaises(ValueError) as err:
            Queen(-2, 2)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "row not positive")

    def test_queen_must_have_row_on_board(self):
        with self.assertRaises(ValueError) as err:
            Queen(8, 4)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "row not on board")

    def test_queen_must_have_positive_column(self):
        with self.assertRaises(ValueError) as err:
            Queen(2, -2)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "column not positive")

    def test_queen_must_have_column_on_board(self):
        with self.assertRaises(ValueError) as err:
            Queen(4, 8)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "column not on board")

    # Test the ability of one queen to attack another
    def test_cannot_attack(self):
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

    def test_cannot_attack_if_falling_diagonals_are_only_the_same_when_reflected_across_the_longest_falling_diagonal(
        self,
    ):
        self.assertIs(Queen(4, 1).can_attack(Queen(2, 5)), False)

    # Track-specific tests
    def test_queens_same_position_can_attack(self):
        with self.assertRaises(ValueError) as err:
            Queen(2, 2).can_attack(Queen(2, 2))
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0],
            "Invalid queen position: both queens in the same square",
        )
