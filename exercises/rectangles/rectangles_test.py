import unittest

from rectangles import count


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class WordTest(unittest.TestCase):
    def test_no_rows(self):
        self.assertEqual(count([]), 0)

    def test_no_columns(self):
        self.assertEqual(count(['']), 0)

    def test_no_rectangles(self):
        self.assertEqual(count([' ']), 0)

    def test_one_rectangle(self):
        lines = ['+-+',
                 '| |',
                 '+-+']
        self.assertEqual(count(lines), 1)

    def test_two_rectangles_without_shared_parts(self):
        lines = ['  +-+',
                 '  | |',
                 '+-+-+',
                 '| |  ',
                 '+-+  ']
        self.assertEqual(count(lines), 2)

    def test_five_rectangles_with_shared_parts(self):
        lines = ['  +-+',
                 '  | |',
                 '+-+-+',
                 '| | |',
                 '+-+-+']
        self.assertEqual(count(lines), 5)

    def test_rectangle_of_height_1_is_counted(self):
        lines = ['+--+',
                 '+--+']
        self.assertEqual(count(lines), 1)

    def test_rectangle_of_width_1_is_counted(self):
        lines = ['++',
                 '||',
                 '++']
        self.assertEqual(count(lines), 1)

    def test_1x1_square_is_counted(self):
        lines = ['++',
                 '++']
        self.assertEqual(count(lines), 1)

    def test_only_complete_rectangles_are_counted(self):
        lines = ['  +-+',
                 '    |',
                 '+-+-+',
                 '| | -',
                 '+-+-+']
        self.assertEqual(count(lines), 1)

    def test_rectangles_can_be_of_different_sizes(self):
        lines = ['+------+----+',
                 '|      |    |',
                 '+---+--+    |',
                 '|   |       |',
                 '+---+-------+']
        self.assertEqual(count(lines), 3)

    def test_corner_is_required_for_a_rectangle_to_be_complete(self):
        lines = ['+------+----+',
                 '|      |    |',
                 '+------+    |',
                 '|   |       |',
                 '+---+-------+']
        self.assertEqual(count(lines), 2)

    def test_large_input_with_many_rectangles(self):
        lines = ['+---+--+----+',
                 '|   +--+----+',
                 '+---+--+    |',
                 '|   +--+----+',
                 '+---+--+--+-+',
                 '+---+--+--+-+',
                 '+------+  | |',
                 '          +-+']
        self.assertEqual(count(lines), 60)


if __name__ == '__main__':
    unittest.main()
