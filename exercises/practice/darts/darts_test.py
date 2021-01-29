import unittest

from darts import score

# Tests adapted from `problem-specifications//canonical-data.json`


class DartsTest(unittest.TestCase):
    def test_missed_target(self):
        self.assertEqual(score(-9, 9), 0)

    def test_on_the_outer_circle(self):
        self.assertEqual(score(0, 10), 1)

    def test_on_the_middle_circle(self):
        self.assertEqual(score(-5, 0), 5)

    def test_on_the_inner_circle(self):
        self.assertEqual(score(0, -1), 10)

    def test_exactly_on_centre(self):
        self.assertEqual(score(0, 0), 10)

    def test_near_the_centre(self):
        self.assertEqual(score(-0.1, -0.1), 10)

    def test_just_within_the_inner_circle(self):
        self.assertEqual(score(0.7, 0.7), 10)

    def test_just_outside_the_inner_circle(self):
        self.assertEqual(score(0.8, -0.8), 5)

    def test_just_within_the_middle_circle(self):
        self.assertEqual(score(-3.5, 3.5), 5)

    def test_just_outside_the_middle_circle(self):
        self.assertEqual(score(-3.6, -3.6), 1)

    def test_just_within_the_outer_circle(self):
        self.assertEqual(score(-7.0, 7.0), 1)

    def test_just_outside_the_outer_circle(self):
        self.assertEqual(score(7.1, -7.1), 0)

    def test_asymmetric_position_between_the_inner_and_middle_circles(self):
        self.assertEqual(score(0.5, -4), 5)


if __name__ == "__main__":
    unittest.main()
