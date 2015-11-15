import unittest

from rectangles import count


class WordTest(unittest.TestCase):
    def test_zero_area_1(self):
        assert 0 == count()

    @unittest.skip('not yet implemented')
    def test_zero_area_2(self):
        lines = ""
        assert 0 == count(lines)

    @unittest.skip('not yet implemented')
    def test_empty_area(self):
        lines = " "
        assert 0 == count(lines)

    @unittest.skip('not yet implemented')
    def test_one_rectangle(self):
        lines = ["+-+",
                 "| |",
                 "+-+",
                 ]
        assert 1 == count(lines)

    @unittest.skip('not yet implemented')
    def test_two_rectangles_no_shared_parts(self):
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| |  ",
                 "+-+  "
                 ]
        assert 2 == count(lines)

    @unittest.skip('not yet implemented')
    def test_five_rectangles_three_regions(self):
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| | |",
                 "+-+-+"
                 ]
        assert 5 == count(lines)

    @unittest.skip('not yet implemented')
    def test_incomplete_rectangles(self):
        lines = ["  +-+",
                 "    |",
                 "+-+-+",
                 "| | -",
                 "+-+-+"
                 ]
        assert 1 == count(lines)

    @unittest.skip('not yet implemented')
    def test_complicated(self):
        lines = ["+------+----+",
                 "|      |    |",
                 "+---+--+    |",
                 "|   |       |",
                 "+---+-------+"
                 ]
        assert 3 == count(lines)

    @unittest.skip('not yet implemented')
    def test_not_so_complicated(self):
        lines = ["+------+----+",
                 "|      |    |",
                 "+------+    |",
                 "|   |       |",
                 "+---+-------+"
                 ]
        assert 2 == count(lines)

if __name__ == '__main__':
    unittest.main()
