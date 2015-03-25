import unittest
import math

from list_ops import map_src, length_src, reduce_src


class ListOpsTest(unittest.TestCase):

    # necessary functions to test map_src
    def square(self, x):
        return x**2

    def cube(self, x):
        return x**3

    def plus_one(self, x):
        return x + 1

    def minus_one(self, x):
        return x - 1

    # tests for map
    def test_map_square(self):
        self.assertEqual([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], map_src(
            self.square, [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]))

    def test_map_cube(self):
        self.assertEqual([-
                          1, 8, -
                          27, 64, -
                          125, 216, -
                          343, 512, -
                          729, 1000], map_src(self.cube, [-
                                                          1, 2, -
                                                          3, 4, -
                                                          5, 6, -
                                                          7, 8, -
                                                          9, 10]))

    def test_map_absolute(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], map_src(
            abs, [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]))

    def test_map_increase_plus_one(self):
        self.assertEqual([0, 3, -
                          2, 5, -
                          4, 7, -
                          6, 9, -
                          8, 11], map_src(self.plus_one, [-
                                                          1, 2, -
                                                          3, 4, -
                                                          5, 6, -
                                                          7, 8, -
                                                          9, 10]))

    def test_map_decrease_minus_one(self):
        self.assertEqual([-
                          2, 1, -
                          4, 3, -
                          6, 5, -
                          8, 7, -
                          10, 9], map_src(self.minus_one, [-
                                                           1, 2, -
                                                           3, 4, -
                                                           5, 6, -
                                                           7, 8, -
                                                           9, 10]))

    # necessary functions to test reduce_src
    def product(self, x, y):
        return x * y

    def concat(self, x, y):
        return int(str(x) + str(y))

    def sum(self, x, y):
        return x + y

    # tests for reduce
    def test_reduce_sum(self):
        self.assertEqual(21, reduce_src(self.sum, [1, 2, 3, 4, 5, 6]))

    def test_reduce_product(self):
        self.assertEqual(720, reduce_src(self.product, [1, 2, 3, 4, 5, 6]))

    def test_reduce_concatenate(self):
        self.assertEqual(123456, reduce_src(self.concat, [1, 2, 3, 4, 5, 6]))

    # tests for length
    def test_length_positive(self):
        self.assertEqual(10, length_src([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]))

    def test_empty_length(self):
        self.assertEqual(0, length_src([]))


if __name__ == '__main__':
    unittest.main()
