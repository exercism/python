import unittest
import gocounting

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
        board = gocounting.GoCounting(board5x5)
        stone, territory = board.territoryFor((0, 1))
        self.assertEqual(stone, board.black)
        self.assertEqual(territory, set([(0, 0), (0, 1), (1, 0)]))

    def test_5x5_for_white(self):
        board = gocounting.GoCounting(board5x5)
        stone, territory = board.territoryFor((2, 3))
        self.assertEqual(stone, board.white)
        self.assertEqual(territory, set([(2, 3)]))

    def test_5x5_for_open_territory(self):
        board = gocounting.GoCounting(board5x5)
        stone, territory = board.territoryFor((1, 4))
        self.assertEqual(stone, board.none)
        self.assertEqual(territory, set([(0, 3), (0, 4), (1, 4)]))

    def test_5x5_for_non_territory(self):
        board = gocounting.GoCounting(board5x5)
        stone, territory = board.territoryFor((1, 1))
        self.assertEqual(stone, board.none)
        self.assertEqual(territory, set())

    def test_5x5_for_valid_coordinate(self):
        board = gocounting.GoCounting(board5x5)
        stone, territory = board.territoryFor((-1, 1))
        self.assertEqual(stone, board.none)
        self.assertEqual(territory, set())

    def test_5x5_for_valid_coordinate2(self):
        board = gocounting.GoCounting(board5x5)
        stone, territory = board.territoryFor((1, 5))
        self.assertEqual(stone, board.none)
        self.assertEqual(territory, set())

    def test_one_territory_whole_board(self):
        board = gocounting.GoCounting(" ")
        territories = board.territories()
        self.assertEqual(territories[board.black], set())
        self.assertEqual(territories[board.white], set())
        self.assertEqual(territories[board.none], set([(0, 0)]))

    def test_two_territories_rectangular_board(self):
        input_board = "\n".join([
            " BW ",
            " BW "
        ])
        board = gocounting.GoCounting(input_board)
        territories = board.territories()
        self.assertEqual(territories[board.black], set([(0, 0), (0, 1)]))
        self.assertEqual(territories[board.white], set([(3, 0), (3, 1)]))
        self.assertEqual(territories[board.none], set())

    def test_9x9_for_open_territory(self):
        board = gocounting.GoCounting(board9x9)
        stone, territory = board.territoryFor((0, 8))
        self.assertEqual(stone, board.none)
        self.assertEqual(territory,
                         set([(2, 7), (2, 8), (1, 8), (0, 8), (0, 7)]))


if __name__ == '__main__':
    unittest.main()
