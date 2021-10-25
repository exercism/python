import unittest

from go_counting import (
    Board,
    WHITE,
    BLACK,
    NONE,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class GoCountingTest(unittest.TestCase):
    def test_black_corner_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=0, y=1)
        self.assertEqual(stone, BLACK)
        self.assertSetEqual(territory, {(0, 0), (0, 1), (1, 0)})

    def test_white_center_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=2, y=3)
        self.assertEqual(stone, WHITE)
        self.assertSetEqual(territory, {(2, 3)})

    def test_open_corner_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=1, y=4)
        self.assertEqual(stone, NONE)
        self.assertSetEqual(territory, {(0, 3), (0, 4), (1, 4)})

    def test_a_stone_and_not_a_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=1, y=1)
        self.assertEqual(stone, NONE)
        self.assertSetEqual(territory, set())

    def test_invalid_because_x_is_too_low_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with self.assertRaises(ValueError) as err:
            board.territory(x=-1, y=1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid coordinate")

    def test_invalid_because_x_is_too_high_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with self.assertRaises(ValueError) as err:
            board.territory(x=5, y=1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid coordinate")

    def test_invalid_because_y_is_too_low_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with self.assertRaises(ValueError) as err:
            board.territory(x=1, y=-1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid coordinate")

    def test_invalid_because_y_is_too_high_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with self.assertRaises(ValueError) as err:
            board.territory(x=1, y=5)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Invalid coordinate")

    def test_one_territory_is_the_whole_board(self):
        board = Board([" "])
        territories = board.territories()
        self.assertSetEqual(territories[BLACK], set())
        self.assertSetEqual(territories[WHITE], set())
        self.assertSetEqual(territories[NONE], {(0, 0)})

    def test_two_territory_rectangular_board(self):
        board = Board([" BW ", " BW "])
        territories = board.territories()
        self.assertSetEqual(territories[BLACK], {(0, 0), (0, 1)})
        self.assertSetEqual(territories[WHITE], {(3, 0), (3, 1)})
        self.assertSetEqual(territories[NONE], set())

    def test_two_region_rectangular_board(self):
        board = Board([" B "])
        territories = board.territories()
        self.assertSetEqual(territories[BLACK], {(0, 0), (2, 0)})
        self.assertSetEqual(territories[WHITE], set())
        self.assertSetEqual(territories[NONE], set())

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
