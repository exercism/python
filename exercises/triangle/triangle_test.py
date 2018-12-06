import unittest

from triangle import is_equilateral, is_isosceles, is_scalene


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class is_equilateralTests(unittest.TestCase):
    def test_true_if_all_sides_are_equal(self):
        self.assertIs(is_equilateral([2, 2, 2]), True)

    def test_false_if_any_side_is_unequal(self):
        self.assertIs(is_equilateral([2, 3, 2]), False)

    def test_false_if_no_sides_are_equal(self):
        self.assertIs(is_equilateral([5, 4, 6]), False)

    def test_false_if_all_sides_are_zero(self):
        self.assertIs(is_equilateral([0, 0, 0]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(is_equilateral([0.5, 0.5, 0.5]), True)


class is_isoscelesTests(unittest.TestCase):
    def test_true_if_last_two_sides_are_equal(self):
        self.assertIs(is_isosceles([3, 4, 4]), True)

    def test_true_if_first_two_sides_are_equal(self):
        self.assertIs(is_isosceles([4, 4, 3]), True)

    def test_true_if_first_and_last_sides_are_equal(self):
        self.assertIs(is_isosceles([4, 3, 4]), True)

    def test_is_equilateral_triangles_are_also_is_isosceles(self):
        self.assertIs(is_isosceles([4, 4, 4]), True)

    def test_false_if_no_sides_are_equal(self):
        self.assertIs(is_isosceles([2, 3, 4]), False)

    def test_violation_of_triangle_inequality_is_not_isosceles_1(self):
        self.assertIs(is_isosceles([1, 1, 3]), False)

    def test_violation_of_triangle_inequality_is_not_isosceles_2(self):
        self.assertIs(is_isosceles([1, 3, 1]), False)

    def test_violation_of_triangle_inequality_is_not_isosceles_3(self):
        self.assertIs(is_isosceles([3, 1, 1]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(is_isosceles([0.5, 0.4, 0.5]), True)


class is_scaleneTests(unittest.TestCase):
    def test_true_if_no_sides_are_equal(self):
        self.assertIs(is_scalene([5, 4, 6]), True)

    def test_false_if_all_sides_are_equal(self):
        self.assertIs(is_scalene([4, 4, 4]), False)

    def test_false_if_two_sides_are_equal(self):
        self.assertIs(is_scalene([4, 4, 3]), False)

    def test_violation_of_triangle_inequality_not_is_scalene(self):
        self.assertIs(is_scalene([7, 3, 2]), False)

    def test_sides_may_be_floats(self):
        self.assertIs(is_scalene([0.5, 0.4, 0.6]), True)


if __name__ == '__main__':
    unittest.main()
