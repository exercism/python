import unittest
import connect

testcases = [
    {
        "description": "an empty board has no winner",
        "board":
        """ . . . . .
             . . . . .
              . . . . .
               . . . . .
                . . . . .""",
        "winner": ""
    },
    {
        "description": "O can win on a 1x1 board",
        "board": "O",
        "winner": "O"
    },
    {
        "description": "X can win on a 1x1 board",
        "board": "X",
        "winner": "X"
    },
    {
        "description": "only edges does not make a winner",
        "board":
            """ O O O X
                 X . . X
                  X . . X
                   X O O O""",
        "winner": ""
    },
    {
        "description": "illegal diagonal does not make a winner",
        "board":
            """ X O . .
                 O X X X
                  O X O .
                   . O X .
                    X X O O""",
        "winner": ""
    },
    {
        "description": "nobody wins crossing adjacent angles",
        "board":
            """ X . . .
                 . X O .
                  O . X O
                   . O . X
                    . . O .""",
        "winner": ""
    },
    {
        "description": "X wins crossing from left to right",
        "board":
            """ . O . .
                 O X X X
                  O X O .
                   X X O X
                    . O X .""",
        "winner": "X"
    },
    {
        "description": "X wins using a convoluted path",
        "board":
            """ . X X . .
                 X . X . X
                  . X . X .
                   . X X . .
                    O O O O O""",
        "winner": "X"
    },
    {
        "description": "O wins crossing from top to bottom",
        "board":
            """ . O . .
                 O X X X
                  O O O .
                   X X O X
                    . O X .""",
        "winner": "O"
    },
    {
        "description": "X wins using a spiral path",
        "board":
            """ O X X X X X X X X
                 O X O O O O O O O
                  O X O X X X X X O
                   O X O X O O O X O
                    O X O X X X O X O
                     O X O O O X O X O
                      O X X X X X O X O
                       O O O O O O O X O
                        X X X X X X X X O """,
        "winner": "X"
    },
]


class SieveTest(unittest.TestCase):
    def test_game(self):
        for t in testcases:
            winner = connect.play(t["board"])
            expected = t["winner"] if t["winner"] else "None"
            got = winner if winner else "None"
            self.assertEqual(winner, t["winner"],
                             "Test failed: %s, expected winner: %s, got: %s"
                             % (t["description"], expected, got))


if __name__ == '__main__':
    unittest.main()
