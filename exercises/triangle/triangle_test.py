import unittest

from triangle import Triangle, TriangleError


# Tests adapted from `problem-specifications/exercises/triangle/canonical-data.json` @ v1.0.0

class TriangleTests(unittest.TestCase):
    def test_equilateral_triangles(self):
        self.assertEqual(Triangle(2, 2, 2).kind(), "equilateral")
        self.assertNotEqual(Triangle(2, 3, 2).kind(), "equilateral")
        self.assertNotEqual(Triangle(5, 4, 6).kind(), "equilateral")
        self.assertNotEqual(Triangle(0, 0, 0).kind(), "equilateral")
        self.assertEqual(Triangle(0.5, 0.5, 0.5).kind(), "equilateral")

    def test_isosceles_triangles(self):
        self.assertEqual(Triangle(3, 4, 4).kind(), "isosceles")
        self.assertEqual(Triangle(4, 3, 4).kind(), "isosceles")
        self.assertEqual(Triangle(4, 4, 3).kind(), "isosceles")
        self.assertEqual(Triangle(4, 4, 4).kind(), "isosceles")
        self.assertNotEqual(Triangle(2, 3, 4).kind(), "isosceles")
        self.assertNotEqual(Triangle(1, 1, 3).kind(), "isosceles")
        self.assertEqual(Triangle(0.5, 0.4, 0.5).kind(), "isosceles")

    def test_scalene_triangles(self):
        self.assertEqual(Triangle(5, 4, 6).kind(), "scalene")
        self.assertNotEqual(Triangle(4, 4, 4).kind(), "scalene")
        self.assertNotEqual(Triangle(4, 4, 3).kind(), "scalene")
        self.assertNotEqual(Triangle(7, 3, 2).kind(), "scalene")
        self.assertEqual(Triangle(0.5, 0.4, 0.6).kind(), "scalene")

    # Additional tests for this track

    def test_illegal_triangles(self):
        self.assertEqual(Triangle(0, 0, 0).kind(), "error")
        self.assertEqual(Triangle(3, 4, -5).kind(), "error")
        self.assertEqual(Triangle(1, 1, 3).kind(), "error")
        self.assertEqual(Triangle(2, 4, 2).kind(), "error")
        self.assertEqual(Triangle(7, 3, 2).kind(), "error")

    def test_larger_equilateral_triangles_also_have_equal_sides(self):
        self.assertEqual(Triangle(10, 10, 10).kind(), "equilateral")


if __name__ == '__main__':
    unittest.main()
