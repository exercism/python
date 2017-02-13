import unittest

from rectangles import count


class WordTest(unittest.TestCase):
    def test_zero_area_1(self):
        self.assertEqual(0, count())

    def test_zero_area_2(self):
        lines = ""
        self.assertEqual(0, count(lines))

    def test_empty_area(self):
        lines = " "
        self.assertEqual(0, count(lines))

    def test_one_rectangle(self):
        lines = ["+-+",
                 "| |",
                 "+-+"]
        self.assertEqual(1, count(lines))

    def test_two_rectangles_no_shared_parts(self):
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| |  ",
                 "+-+  "]
        self.assertEqual(2, count(lines))

    def test_five_rectangles_three_regions(self):
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| | |",
                 "+-+-+"]
        self.assertEqual(5, count(lines))

    def test_incomplete_rectangles(self):
        lines = ["  +-+",
                 "    |",
                 "+-+-+",
                 "| | -",
                 "+-+-+"]
        self.assertEqual(1, count(lines))

    def test_complicated(self):
        lines = ["+------+----+",
                 "|      |    |",
                 "+---+--+    |",
                 "|   |       |",
                 "+---+-------+"]
        self.assertEqual(3, count(lines))

    def test_not_so_complicated(self):
        lines = ["+------+----+",
                 "|      |    |",
                 "+------+    |",
                 "|   |       |",
                 "+---+-------+"]
        self.assertEqual(2, count(lines))


if __name__ == '__main__':
    unittest.main()
