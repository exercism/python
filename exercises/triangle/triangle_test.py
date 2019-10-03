import unittest

from triangle import equilateral, isosceles, scalene

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.1


class EquilateralTriangleTest(unittest.TestCase):
    def test_all_sides_are_equal(self):
        input = [2, 2, 2]
        expected = True
        self.assertEqual(equilateral(input), expected)

    def test_any_side_is_unequal(self):
        input = [2, 3, 2]
        expected = False
        self.assertEqual(equilateral(input), expected)

    def test_no_sides_are_equal(self):
        input = [5, 4, 6]
        expected = False
        self.assertEqual(equilateral(input), expected)

    def test_all_zero_sides_is_not_a_triangle(self):
        input = [0, 0, 0]
        expected = False
        self.assertEqual(equilateral(input), expected)

    def test_sides_may_be_floats(self):
        input = [0.5, 0.5, 0.5]
        expected = True
        self.assertEqual(equilateral(input), expected)


class IsoscelesTriangleTest(unittest.TestCase):
    def test_last_two_sides_are_equal(self):
        input = [3, 4, 4]
        expected = True
        self.assertEqual(isosceles(input), expected)

    def test_first_two_sides_are_equal(self):
        input = [4, 4, 3]
        expected = True
        self.assertEqual(isosceles(input), expected)

    def test_first_and_last_sides_are_equal(self):
        input = [4, 3, 4]
        expected = True
        self.assertEqual(isosceles(input), expected)

    def test_equilateral_triangles_are_also_isosceles(self):
        input = [4, 4, 4]
        expected = True
        self.assertEqual(isosceles(input), expected)

    def test_no_sides_are_equal(self):
        input = [2, 3, 4]
        expected = False
        self.assertEqual(isosceles(input), expected)

    def test_first_triangle_inequality_violation(self):
        input = [1, 1, 3]
        expected = False
        self.assertEqual(isosceles(input), expected)

    def test_second_triangle_inequality_violation(self):
        input = [1, 3, 1]
        expected = False
        self.assertEqual(isosceles(input), expected)

    def test_third_triangle_inequality_violation(self):
        input = [3, 1, 1]
        expected = False
        self.assertEqual(isosceles(input), expected)

    def test_sides_may_be_floats(self):
        input = [0.5, 0.4, 0.5]
        expected = True
        self.assertEqual(isosceles(input), expected)


class ScaleneTriangleTest(unittest.TestCase):
    def test_no_sides_are_equal(self):
        input = [5, 4, 6]
        expected = True
        self.assertEqual(scalene(input), expected)

    def test_all_sides_are_equal(self):
        input = [4, 4, 4]
        expected = False
        self.assertEqual(scalene(input), expected)

    def test_two_sides_are_equal(self):
        input = [4, 4, 3]
        expected = False
        self.assertEqual(scalene(input), expected)

    def test_may_not_violate_triangle_inequality(self):
        input = [7, 3, 2]
        expected = False
        self.assertEqual(scalene(input), expected)

    def test_sides_may_be_floats(self):
        input = [0.5, 0.4, 0.6]
        expected = True
        self.assertEqual(scalene(input), expected)


if __name__ == "__main__":
    unittest.main()
