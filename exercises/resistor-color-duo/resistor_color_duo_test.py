import unittest

from resistor_color_duo import value


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class ResistorColorDuoTest(unittest.TestCase):
    def test_brown_and_black(self):
        self.assertEqual(value(['brown', 'black']), 10)

    def test_blue_and_grey(self):
        self.assertEqual(value(['blue', 'grey']), 68)

    def test_yellow_and_violet(self):
        self.assertEqual(value(['yellow', 'violet']), 47)

    def test_orange_and_orange(self):
        self.assertEqual(value(['orange', 'orange']), 33)


if __name__ == '__main__':
    unittest.main()
