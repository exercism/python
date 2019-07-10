import unittest
from darts import score


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.2.0

class darts_test(unittest.TestCase):
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

    def test_just_within_the__inner_circle(self):
        self.assertEqual(score(0.7, 0.7), 10)

    def test_just_within_the_middle_circle(self):
        self.assertAlmostEqual(score(-3.5, 3.5), 5)

    def test_just_outside_the_middle_circle(self):
        self.assertAlmostEqual(score(-3.6, -3.6), 1)

    def test_just_outside_the_outer_circle(self):
        self.assertAlmostEqual(score(7.1, -7.1), 0)

    def test_asymmetric_position_between_the_inner_and_middle_circles(self):
        self.assertAlmostEqual(score(0.5, -4), 5)

    # Additional tests for this track
    def test_border_of_the_outside(self):
        self.assertEqual(score(-10, 0), 1)

    def test_border_between_outside_and_middle(self):
        self.assertEqual(score(5, 0), 5)

    def test_border_betweeen_middle_and_inner(self):
        self.assertEqual(score(0, -1), 10)

    def test_coord_sum_more_than_1_radius_less_than_1_is_in_inner(self):
        self.assertEqual(score(0.4, 0.8), 10)

    def test_coord_sum_more_than_5_radius_less_than_5_is_in_middle(self):
        self.assertEqual(score(2, 4), 5)

    def test_coord_sum_more_than_10_radius_less_than_10_is_in_outer(self):
        self.assertEqual(score(4, 8), 1)


if __name__ == '__main__':
    unittest.main()
