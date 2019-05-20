import unittest
from darts import score


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class darts_test(unittest.TestCase):
    def test_dart_lands_outside_target(self):
        self.assertEqual(score(-9, 9), 0)

    def test_dart_lands_just_in_border_of_target(self):
        self.assertEqual(score(0, 10), 1)

    def test_dart_lands_outer_circle(self):
        self.assertEqual(score(4, 4), 1)

    def test_dart_lands_border_between_outside_middle(self):
        self.assertEqual(score(5, 0), 5)

    def test_dart_lands_in_middle_circle(self):
        self.assertEqual(score(0.8, -0.8), 5)

    def test_dart_lands_border_betweeen_middle_inner(self):
        self.assertEqual(score(0, -1), 10)

    def test_dart_lands_inner_circle(self):
        self.assertEqual(score(-0.1, -0.1), 10)

    def test_dart_coord_sum_more_than_1_radius_less_than_1_is_in_inner(self):
        self.assertEqual(score(0.4, 0.8), 10)

    def test_dart_coord_sum_more_than_5_radius_less_than_5_is_in_middle(self):
        self.assertEqual(score(2, 4), 5)

    def test_dart_coord_sum_more_than_10_radius_less_than_10_is_in_outer(self):
        self.assertEqual(score(4, 8), 1)


if __name__ == '__main__':
    unittest.main()
