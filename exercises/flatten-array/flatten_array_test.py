import unittest

from flatten_array import flatten


class FlattenArrayTests(unittest.TestCase):

    def test_no_nesting(self):
        self.assertEqual(flatten([0, 1, 2]), [0, 1, 2])

    def test_one_level_nesting(self):
        self.assertEqual(flatten([0, [1], 2]), [0, 1, 2])

    def test_two_level_nesting(self):
        self.assertEqual(flatten([0, [1, [2, 3]], [4]]), [0, 1, 2, 3, 4])

    def test_empty_nested_lists(self):
        self.assertEqual(flatten([[()]]), [])

    def test_with_none_values(self):
        inputs = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
        expected = [0, 2, 2, 3, 8, 100, -2]
        self.assertEqual(flatten(inputs), expected)

    def test_six_level_nesting(self):
        inputs = [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(inputs), expected)

    def test_all_values_are_none(self):
        inputs = [None, [[[None]]], None, None, [[None, None], None], None]
        expected = []
        self.assertEqual(flatten(inputs), expected)

    def test_strings(self):
        self.assertEqual(flatten(['0', ['1', '2']]), ['0', '1', '2'])


if __name__ == '__main__':
    unittest.main()
