import unittest

from triangle import Triangle, TriangleError


class TriangleTests(unittest.TestCase):
    def test_equilateral_triangles_have_equal_sides(self):
        self.assertEqual(Triangle(2, 2, 2).kind(), "equilateral")

    def test_larger_equilateral_triangles_also_have_equal_sides(self):
        self.assertEqual(Triangle(10, 10, 10).kind(), "equilateral")

    def test_isosceles_triangles_have_last_two_sides_equal(self):
        self.assertEqual(Triangle(3, 4, 4).kind(), "isosceles")

    def test_isosceles_triangles_have_first_and_last_sides_equal(self):
        self.assertEqual(Triangle(4, 3, 4).kind(), "isosceles")

    def test_isosceles_triangles_have_two_first_sides_equal(self):
        self.assertEqual(Triangle(4, 4, 3).kind(), "isosceles")

    def test_isosceles_triangles_have_in_fact_exactly_two_sides_equal(self):
        self.assertEqual(Triangle(10, 10, 2).kind(), "isosceles")

    def test_scalene_triangles_have_no_equal_sides(self):
        self.assertEqual(Triangle(3, 4, 5).kind(), "scalene")

    def test_scalene_triangles_have_no_equal_sides_at_a_larger_scale_too(self):
        self.assertEqual(Triangle(10, 11, 12).kind(), "scalene")

        self.assertEqual(Triangle(5, 4, 2).kind(), "scalene")

    def test_very_small_triangles_are_legal(self):
        self.assertEqual(Triangle(0.4, 0.6, 0.3).kind(), "scalene")

    def test_triangles_with_no_size_are_illegal(self):
        with self.assertRaisesWithMessage(TriangleError):
            Triangle(0, 0, 0)

    def test_triangles_with_negative_sides_are_illegal(self):
        with self.assertRaisesWithMessage(TriangleError):
            Triangle(3, 4, -5)

    def test_triangles_violating_triangle_inequality_are_illegal(self):
        with self.assertRaisesWithMessage(TriangleError):
            Triangle(1, 1, 3)

    def test_triangles_violating_triangle_inequality_are_illegal_2(self):
        with self.assertRaisesWithMessage(TriangleError):
            Triangle(2, 4, 2)

    def test_triangles_violating_triangle_inequality_are_illegal_3(self):
        with self.assertRaisesWithMessage(TriangleError):
            Triangle(7, 3, 2)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
