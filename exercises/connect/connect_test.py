import unittest

from connect import ConnectGame

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class ConnectTest(unittest.TestCase):
    def test_an_empty_board_has_no_winner(self):
        game = ConnectGame(
            """. . . . .
                . . . . .
                 . . . . .
                  . . . . .
                   . . . . ."""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "",
            'Test failed: "%s", expected winner: %s, got: %s'
            % ("an empty board has no winner", "None", winner if winner else "None"),
        )

    def test_x_can_win_on_a_1x1_board(self):
        game = ConnectGame("""X""")
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "X",
            'Test failed: "%s", expected winner: %s, got: %s'
            % ("X can win on a 1x1 board", "X", winner if winner else "None"),
        )

    def test_o_can_win_on_a_1x1_board(self):
        game = ConnectGame("""O""")
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "O",
            'Test failed: "%s", expected winner: %s, got: %s'
            % ("O can win on a 1x1 board", "O", winner if winner else "None"),
        )

    def test_only_edges_does_not_make_a_winner(self):
        game = ConnectGame(
            """O O O X
                X . . X
                 X . . X
                  X O O O"""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "",
            'Test failed: "%s", expected winner: %s, got: %s'
            % (
                "only edges does not make a winner",
                "None",
                winner if winner else "None",
            ),
        )

    def test_illegal_diagonal_does_not_make_a_winner(self):
        game = ConnectGame(
            """X O . .
                O X X X
                 O X O .
                  . O X .
                   X X O O"""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "",
            'Test failed: "%s", expected winner: %s, got: %s'
            % (
                "illegal diagonal does not make a winner",
                "None",
                winner if winner else "None",
            ),
        )

    def test_nobody_wins_crossing_adjacent_angles(self):
        game = ConnectGame(
            """X . . .
                . X O .
                 O . X O
                  . O . X
                   . . O ."""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "",
            'Test failed: "%s", expected winner: %s, got: %s'
            % (
                "nobody wins crossing adjacent angles",
                "None",
                winner if winner else "None",
            ),
        )

    def test_x_wins_crossing_from_left_to_right(self):
        game = ConnectGame(
            """. O . .
                O X X X
                 O X O .
                  X X O X
                   . O X ."""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "X",
            'Test failed: "%s", expected winner: %s, got: %s'
            % ("X wins crossing from left to right", "X", winner if winner else "None"),
        )

    def test_o_wins_crossing_from_top_to_bottom(self):
        game = ConnectGame(
            """. O . .
                O X X X
                 O O O .
                  X X O X
                   . O X ."""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "O",
            'Test failed: "%s", expected winner: %s, got: %s'
            % ("O wins crossing from top to bottom", "O", winner if winner else "None"),
        )

    def test_x_wins_using_a_convoluted_path(self):
        game = ConnectGame(
            """. X X . .
                X . X . X
                 . X . X .
                  . X X . .
                   O O O O O"""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "X",
            'Test failed: "%s", expected winner: %s, got: %s'
            % ("X wins using a convoluted path", "X", winner if winner else "None"),
        )

    def test_x_wins_using_a_spiral_path(self):
        game = ConnectGame(
            """O X X X X X X X X
                O X O O O O O O O
                 O X O X X X X X O
                  O X O X O O O X O
                   O X O X X X O X O
                    O X O O O X O X O
                     O X X X X X O X O
                      O O O O O O O X O
                       X X X X X X X X O"""
        )
        winner = game.get_winner()
        self.assertEqual(
            winner,
            "X",
            'Test failed: "%s", expected winner: %s, got: %s'
            % ("X wins using a spiral path", "X", winner if winner else "None"),
        )


if __name__ == "__main__":
    unittest.main()
