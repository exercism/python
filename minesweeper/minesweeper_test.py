try:
    from minesweeper import board
except ImportError:
    raise SystemExit('Could not find minesweeper.py. Does it exist?')

import unittest

class MinesweeperTest(unittest.TestCase):
    def test_board1(self):
        inp = ["+------+", "| *  * |", "|  *   |", "|    * |", "|   * *|",
               "| *  * |", "|      |", "+------+"]
        out = ["+------+", "|1*22*1|", "|12*322|", "| 123*2|", "|112*4*|",
               "|1*22*2|", "|111111|", "+------+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board2(self):
        inp = ["+-----+", "| * * |", "|     |", "|   * |", "|  * *|",
               "| * * |", "+-----+"]
        out = ["+-----+", "|1*2*1|", "|11322|", "| 12*2|", "|12*4*|",
               "|1*3*2|", "+-----+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board3(self):
        inp = ["+-----+", "| * * |", "+-----+"]
        out = ["+-----+", "|1*2*1|", "+-----+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board4(self):
        inp = ["+-+", "|*|", "| |", "|*|", "| |", "| |", "+-+"]
        out = ["+-+", "|*|", "|2|", "|*|", "|1|", "| |", "+-+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board5(self):
        inp = ["+-+", "|*|", "+-+"]
        out = ["+-+", "|*|", "+-+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board6(self):
        inp = ["+--+", "|**|", "|**|", "+--+"]
        out = ["+--+", "|**|", "|**|", "+--+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board7(self):
        inp = ["+--+", "|**|", "|**|", "+--+"]
        out = ["+--+", "|**|", "|**|", "+--+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board8(self):
        inp = ["+---+", "|***|", "|* *|", "|***|", "+---+"]
        out = ["+---+", "|***|", "|*8*|", "|***|", "+---+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_board9(self):
        inp = ["+-----+", "|     |", "|   * |", "|     |", "|     |",
               "| *   |", "+-----+"]
        out = ["+-----+", "|  111|", "|  1*1|", "|  111|", "|111  |",
               "|1*1  |", "+-----+"]
        self.assertEqual(out, board(inp))

    @unittest.skip("Not implemented yet")
    def test_different_len(self):
        inp = ["+-+", "| |", "|*  |", "|  |", "+-+"]
        self.assertRaisesRegex(ValueError, "^Invalid board", board, inp)

    @unittest.skip("Not implemented yet")
    def test_faulty_border(self):
        inp = ["+-----+", "*   * |", "+-- --+"]
        self.assertRaisesRegex(ValueError, "^Invalid board", board, inp)

    @unittest.skip("Not implemented yet")
    def test_invalid_char(self):
        inp = ["+-----+", "|X  * |", "+-----+"]
        self.assertRaisesRegex(ValueError, "^Invalid board", board, inp)

if __name__ == '__main__':
    unittest.main()
