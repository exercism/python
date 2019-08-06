import unittest
import operator

import list_ops


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.4.0

class ListOpsTest(unittest.TestCase):

    # test for append
    def test_append_empty_lists(self):
        self.assertEqual(list_ops.append([], []), [])

    def test_append_empty_list_to_list(self):
        self.assertEqual(list_ops.append([], [1, 2, 3, 4]), [1, 2, 3, 4])

    def test_append_nonempty_lists(self):
        self.assertEqual(list_ops.append([1, 2], [2, 3, 4, 5]),
                         [1, 2, 2, 3, 4, 5])

    # tests for concat
    def test_concat_empty_list(self):
        self.assertEqual(list_ops.concat([]), [])

    def test_concat_list_of_lists(self):
        self.assertEqual(list_ops.concat([[1, 2], [3], [], [4, 5, 6]]),
                         [1, 2, 3, 4, 5, 6])

    def test_concat_list_of_nested_lists(self):
        self.assertEqual(
            list_ops.concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]),
            [[1], [2], [3], [], [4, 5, 6]])

    # tests for filter
    def test_filter_empty_list(self):
        self.assertEqual(list_ops.filter(lambda x: x % 2 == 1, []), [])

    def test_filter_nonempty_list(self):
        self.assertEqual(
            list_ops.filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5]),
            [1, 3, 5])

    # tests for length
    def test_length_empty_list(self):
        self.assertEqual(list_ops.length([]), 0)

    def test_length_nonempty_list(self):
        self.assertEqual(list_ops.length([1, 2, 3, 4]), 4)

    # tests for map
    def test_map_empty_list(self):
        self.assertEqual(list_ops.map(lambda x: x + 1, []), [])

    def test_map_nonempty_list(self):
        self.assertEqual(list_ops.map(lambda x: x + 1, [1, 3, 5, 7]),
                         [2, 4, 6, 8])

    # tests for foldl
    def test_foldl_empty_list(self):
        self.assertEqual(list_ops.foldl(operator.mul, [], 2), 2)

    def test_foldl_nonempty_list_addition(self):
        self.assertEqual(list_ops.foldl(operator.add, [1, 2, 3, 4], 5), 15)

    def test_foldl_nonempty_list_floordiv(self):
        self.assertEqual(list_ops.foldl(operator.floordiv, [2, 5], 5), 0)

    # tests for foldr
    def test_foldr_empty_list(self):
        self.assertEqual(list_ops.foldr(operator.mul, [], 2), 2)

    def test_foldr_nonempty_list_addition(self):
        self.assertEqual(list_ops.foldr(operator.add, [1, 2, 3, 4], 5), 15)

    def test_foldr_nonempty_list_floordiv(self):
        self.assertEqual(list_ops.foldr(operator.floordiv, [2, 5], 5), 2)

    # additional test for foldr
    def test_foldr_add_str(self):
        self.assertEqual(
            list_ops.foldr(operator.add,
                           ["e", "x", "e", "r", "c", "i", "s", "m"], "!"),
            "exercism!")

    # tests for reverse
    def test_reverse_empty_list(self):
        self.assertEqual(list_ops.reverse([]), [])

    def test_reverse_nonempty_list(self):
        self.assertEqual(list_ops.reverse([1, 3, 5, 7]), [7, 5, 3, 1])

    def test_reverse_list_of_lists_not_flattened(self):
        self.assertEqual(list_ops.reverse([[1, 2], [3], [], [4, 5, 6]]),
                         [[4, 5, 6], [], [3], [1, 2]])

    # additional test for reverse
    def test_reverse_mixed_types(self):
        self.assertEqual(
            list_ops.reverse(["xyz", 4.0, "cat", 1]), [1, "cat", 4.0, "xyz"])


if __name__ == '__main__':
    unittest.main()
