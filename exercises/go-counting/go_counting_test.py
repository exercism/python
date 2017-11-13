import unittest
import go_counting


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

board5x5 = "\n".join([
    "  B  ",
    " B B ",
    "B W B",
    " W W ",
    "  W  "
])

board9x9 = "\n".join([
    "  B   B  ",
    "B   B   B",
    "WBBBWBBBW",
    "W W W W W",
    "         ",
    " W W W W ",
    "B B   B B",
    " W BBB W ",
    "   B B   "
])


class GoCountingTest(unittest.TestCase):
    def test_5x5_for_black(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territoryFor((0, 1))
        self.assertEqual(stone, go_counting.BLACK)
        self.assertEqual(territory, set([(0, 0), (0, 1), (1, 0)]))

    def test_5x5_for_white(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territoryFor((2, 3))
        self.assertEqual(stone, go_counting.WHITE)
        self.assertEqual(territory, set([(2, 3)]))

    def test_5x5_for_open_territory(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territoryFor((1, 4))
        self.assertEqual(stone, go_counting.NONE)
        self.assertEqual(territory, set([(0, 3), (0, 4), (1, 4)]))

    def test_5x5_for_non_territory(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territoryFor((1, 1))
        self.assertEqual(stone, go_counting.NONE)
        self.assertEqual(territory, set())

    def test_5x5_for_valid_coordinate(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territoryFor((-1, 1))
        self.assertEqual(stone, go_counting.NONE)
        self.assertEqual(territory, set())

    def test_5x5_for_valid_coordinate2(self):
        board = go_counting.Board(board5x5)
        stone, territory = board.territoryFor((1, 5))
        self.assertEqual(stone, go_counting.NONE)
        self.assertEqual(territory, set())

    def test_one_territory_whole_board(self):
        board = go_counting.Board(" ")
        territories = board.territories()
        self.assertEqual(territories[go_counting.BLACK], set())
        self.assertEqual(territories[go_counting.WHITE], set())
        self.assertEqual(territories[go_counting.NONE], set([(0, 0)]))

    def test_two_territories_rectangular_board(self):
        input_board = "\n".join([
            " BW ",
            " BW "
        ])
        board = go_counting.Board(input_board)
        territories = board.territories()
        self.assertEqual(territories[go_counting.BLACK], set([(0, 0), (0, 1)]))
        self.assertEqual(territories[go_counting.WHITE], set([(3, 0), (3, 1)]))
        self.assertEqual(territories[go_counting.NONE], set())

    def test_9x9_for_open_territory(self):
        board = go_counting.Board(board9x9)
        stone, territory = board.territoryFor((0, 8))
        self.assertEqual(stone, go_counting.NONE)
        self.assertEqual(territory,
                         set([(2, 7), (2, 8), (1, 8), (0, 8), (0, 7)]))


if __name__ == '__main__':
    unittest.main()
