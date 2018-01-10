import unittest

from example import equilateral, isosceles, scalene


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class EquilateralTests(unittest.TestCase):
    def test_true_if_all_sides_are_equal(self):
        self.assertIs(equilateral([2, 2, 2]), True)

    def test_false_if_any_side_is_unequal(self):
        self.assertIs(equilateral([2, 3, 2]), False)

    def test_false_if_no_sides_are_equal(self):
        self.assertIs(equilateral([5, 4, 6]), False)

    def test_false_if_all_sides_are_zero(self):
        self.assertIs(equilateral([0, 0, 0]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(equilateral([0.5, 0.5, 0.5]), True)


class IsoscelesTests(unittest.TestCase):
    def test_true_if_last_two_sides_are_equal(self):
        self.assertIs(isosceles([3, 4, 4]), True)

    def test_true_if_first_two_sides_are_equal(self):
        self.assertIs(isosceles([4, 4, 3]), True)

    def test_true_if_first_and_last_sides_are_equal(self):
        self.assertIs(isosceles([4, 3, 4]), True)

    def test_equilateral_triangles_are_also_isosceles(self):
        self.assertIs(isosceles([4, 4, 4]), True)

    def test_false_if_no_sides_are_equal(self):
        self.assertIs(isosceles([2, 3, 4]), False)

    def test_violation_of_triangle_inequality_not_isosceles(self):
        self.assertIs(isosceles([1, 1, 3]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(isosceles([0.5, 0.4, 0.5]), True)


class ScaleneTests(unittest.TestCase):
    def test_true_if_no_sides_are_equal(self):
        self.assertIs(scalene([5, 4, 6]), True)

    def test_false_if_all_sides_are_equal(self):
        self.assertIs(scalene([4, 4, 4]), False)

    def test_false_if_two_sides_are_equal(self):
        self.assertIs(scalene([4, 4, 3]), False)

    def test_violation_of_triangle_inequality_not_scalene(self):
        self.assertIs(scalene([7, 3, 2]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(scalene([0.5, 0.4, 0.6]), True)


if __name__ == '__main__':
    unittest.main()
