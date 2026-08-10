# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/state-of-tic-tac-toe/canonical-data.json
# File last updated on 2026-01-30

import unittest

from state_of_tic_tac_toe import (
    gamestate,
)


class StateOfTicTacToeTest(unittest.TestCase):
    def test_finished_game_where_x_won_via_left_column_victory(self):
        board = [
            "XOO",
            "X  ",
            "X  ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_middle_column_victory(self):
        board = [
            "OXO",
            " X ",
            " X ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_right_column_victory(self):
        board = [
            "OOX",
            "  X",
            "  X",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_left_column_victory(self):
        board = [
            "OXX",
            "OX ",
            "O  ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_middle_column_victory(self):
        board = [
            "XOX",
            " OX",
            " O ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_right_column_victory(self):
        board = [
            "XXO",
            " XO",
            "  O",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_top_row_victory(self):
        board = [
            "XXX",
            "XOO",
            "O  ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_middle_row_victory(self):
        board = [
            "O  ",
            "XXX",
            " O ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_bottom_row_victory(self):
        board = [
            " OO",
            "O X",
            "XXX",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_top_row_victory(self):
        board = [
            "OOO",
            "XXO",
            "XX ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_middle_row_victory(self):
        board = [
            "XX ",
            "OOO",
            "X  ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_bottom_row_victory(self):
        board = [
            "XOX",
            " XX",
            "OOO",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_falling_diagonal_victory(self):
        board = [
            "XOO",
            " X ",
            "  X",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_rising_diagonal_victory(self):
        board = [
            "O X",
            "OX ",
            "X  ",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_falling_diagonal_victory(self):
        board = [
            "OXX",
            "OOX",
            "X O",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_o_won_via_rising_diagonal_victory(self):
        board = [
            "  O",
            " OX",
            "OXX",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_a_row_and_a_column_victory(self):
        board = [
            "XXX",
            "XOO",
            "XOO",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_finished_game_where_x_won_via_two_diagonal_victories(self):
        board = [
            "XOX",
            "OXO",
            "XOX",
        ]
        self.assertEqual(gamestate(board), "win")

    def test_draw(self):
        board = [
            "XOX",
            "XXO",
            "OXO",
        ]
        self.assertEqual(gamestate(board), "draw")

    def test_another_draw(self):
        board = [
            "XXO",
            "OXX",
            "XOO",
        ]
        self.assertEqual(gamestate(board), "draw")

    def test_ongoing_game_one_move_in(self):
        board = [
            "   ",
            "X  ",
            "   ",
        ]
        self.assertEqual(gamestate(board), "ongoing")

    def test_ongoing_game_two_moves_in(self):
        board = [
            "O  ",
            " X ",
            "   ",
        ]
        self.assertEqual(gamestate(board), "ongoing")

    def test_ongoing_game_five_moves_in(self):
        board = [
            "X  ",
            " XO",
            "OX ",
        ]
        self.assertEqual(gamestate(board), "ongoing")

    def test_invalid_board_x_went_twice(self):
        board = [
            "XX ",
            "   ",
            "   ",
        ]
        with self.assertRaises(ValueError) as err:
            gamestate(board)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Wrong turn order: X went twice")

    def test_invalid_board_o_started(self):
        board = [
            "OOX",
            "   ",
            "   ",
        ]
        with self.assertRaises(ValueError) as err:
            gamestate(board)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Wrong turn order: O started")

    def test_invalid_board_x_won_and_o_kept_playing(self):
        board = [
            "XXX",
            "OOO",
            "   ",
        ]
        with self.assertRaises(ValueError) as err:
            gamestate(board)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0],
            "Impossible board: game should have ended after the game was won",
        )

    def test_invalid_board_players_kept_playing_after_a_win(self):
        board = [
            "XXX",
            "OOO",
            "XOX",
        ]
        with self.assertRaises(ValueError) as err:
            gamestate(board)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0],
            "Impossible board: game should have ended after the game was won",
        )
