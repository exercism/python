import unittest
import operator

import list_ops


class ListOpsTest(unittest.TestCase):

    # tests for map
    def test_map_square(self):
        self.assertEqual(
            list_ops.map_clone(lambda x: x**2,
                               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_map_cube(self):
        self.assertEqual(
            list_ops.map_clone(lambda x: x**3,
                               [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]),
            [-1, 8, -27, 64, -125, 216, -343, 512, -729, 1000])

    def test_map_absolute(self):
        self.assertEqual(
            list_ops.map_clone(lambda x: abs(x),
                               [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_map_empty(self):
        self.assertEqual(list_ops.map_clone(operator.index, []), [])

    # tests for length
    def test_pos_leng(self):
        self.assertEqual(
            list_ops.length([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]), 10)

    def test_empty_len(self):
        self.assertEqual(list_ops.length([]), 0)

    # tests for filter
    def test_filter_odd(self):
        self.assertEqual(
            list_ops.filter_clone(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6]),
            [1, 3, 5])

    def test_filter_even(self):
        self.assertEqual(
            list_ops.filter_clone(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]),
            [2, 4, 6])

    # tests for reverse
    def test_reverse_small(self):
        self.assertEqual(list_ops.reverse([3, 2, 1]), [1, 2, 3])

    def test_reverse_mixed_types(self):
        self.assertEqual(
            list_ops.reverse(["xyz", 4.0, "cat", 1]), [1, "cat", 4.0, "xyz"])

    def test_reverse_empty(self):
        self.assertEqual(list_ops.reverse([]), [])

    # tests for append
    def test_append_tuple(self):
        self.assertEqual(
            list_ops.append(["10", "python"], "hello"),
            ["10", "python", "hello"])

    def test_append_range(self):
        self.assertEqual(
            list_ops.append([100], range(1000)), [100, range(1000)])

    def test_append_to_empty(self):
        self.assertEqual(list_ops.append([], 42), [42])

    # tests for foldl
    def test_foldl_sum(self):
        self.assertEqual(
            list_ops.foldl(operator.add, [1, 2, 3, 4, 5, 6], 0), 21)

    def test_foldl_product(self):
        self.assertEqual(
            list_ops.foldl(operator.mul, [1, 2, 3, 4, 5, 6], 1), 720)

    def test_foldl_div(self):
        self.assertEqual(
            list_ops.foldl(operator.floordiv, [1, 2, 3, 4, 5, 6], 1), 0)

    def test_foldl_sub(self):
        self.assertEqual(list_ops.foldl(operator.sub, [1, 2, 3, 4, 5], 0), -15)

    # tests for foldr
    def test_foldr_sub(self):
        self.assertEqual(list_ops.foldr(operator.sub, [1, 2, 3, 4, 5], 0), 3)

    def test_foldr_add_str(self):
        self.assertEqual(
            list_ops.foldr(operator.add,
                           ["e", "x", "e", "r", "c", "i", "s", "m"], "!"),
            "exercism!")

    # tests for flatten
    def test_flatten_nested(self):
        self.assertEqual(list_ops.flat([[[1, 2], [3]], [[4]]]), [1, 2, 3, 4])

    def test_flatten_once(self):
        self.assertEqual(list_ops.flat([["x", "y", "z"]]), ["x", "y", "z"])

    def test_flatten_empty(self):
        self.assertEqual(list_ops.flat([]), [])

    # tests for concat
    def test_concat_two(self):
        self.assertEqual(
            list_ops.concat([1, 3, 5, 8], [9, 4, 5, 6]),
            [1, 3, 5, 8, 9, 4, 5, 6])

    def test_concat_nothing(self):
        self.assertEqual(
            list_ops.concat(['orange', 'apple', 'banana'], None),
            ["orange", "apple", "banana"])

    def test_concat_empty(self):
        self.assertEqual(list_ops.concat([], []), [])


if __name__ == '__main__':
    unittest.main()
