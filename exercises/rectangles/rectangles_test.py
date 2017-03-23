import unittest

from rectangles import count


class WordTest(unittest.TestCase):
    def test_zero_area_1(self):
        self.assertEqual(count(), 0)

    def test_zero_area_2(self):
        lines = ""
        self.assertEqual(count(lines), 0)

    def test_empty_area(self):
        lines = " "
        self.assertEqual(count(lines), 0)

    def test_one_rectangle(self):
        lines = ["+-+",
                 "| |",
                 "+-+"]
        self.assertEqual(count(lines), 1)

    def test_two_rectangles_no_shared_parts(self):
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| |  ",
                 "+-+  "]
        self.assertEqual(count(lines), 2)

    def test_five_rectangles_three_regions(self):
        lines = ["  +-+",
                 "  | |",
                 "+-+-+",
                 "| | |",
                 "+-+-+"]
        self.assertEqual(count(lines), 5)

    def test_incomplete_rectangles(self):
        lines = ["  +-+",
                 "    |",
                 "+-+-+",
                 "| | -",
                 "+-+-+"]
        self.assertEqual(count(lines), 1)

    def test_complicated(self):
        lines = ["+------+----+",
                 "|      |    |",
                 "+---+--+    |",
                 "|   |       |",
                 "+---+-------+"]
        self.assertEqual(count(lines), 3)

    def test_not_so_complicated(self):
        lines = ["+------+----+",
                 "|      |    |",
                 "+------+    |",
                 "|   |       |",
                 "+---+-------+"]
        self.assertEqual(count(lines), 2)


if __name__ == '__main__':
    unittest.main()
