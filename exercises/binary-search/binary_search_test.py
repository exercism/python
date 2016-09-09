import unittest

from binary_search import binary_search


class BinarySearchTests(unittest.TestCase):

    def test_finds_value_in_array_with_one_element(self):
        self.assertEqual(0, binary_search([6], 6))

    def test_finds_value_in_middle_of_array(self):
        self.assertEqual(3, binary_search([1, 3, 4, 6, 8, 9, 11], 6))

    def test_finds_value_at_beginning_of_array(self):
        self.assertEqual(0, binary_search([1, 3, 4, 6, 8, 9, 11], 1))

    def test_finds_value_at_end_of_array(self):
        self.assertEqual(6, binary_search([1, 3, 4, 6, 8, 9, 11], 11))

    def test_finds_value_in_array_of_odd_length(self):
        self.assertEqual(9, binary_search(
            [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144))

    def test_finds_value_in_array_of_even_length(self):
        self.assertEqual(5, binary_search(
            [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21))

    def test_identifies_value_missing(self):
        self.assertRaises(ValueError, binary_search, [1, 3, 4, 6, 8, 9, 11], 7)

    def test_value_smaller_than_arrays_minimum(self):
        self.assertRaises(ValueError, binary_search, [1, 3, 4, 6, 8, 9, 11], 0)

    def test_value_larger_than_arrays_maximum(self):
        self.assertRaises(ValueError, binary_search, [1, 3, 4, 6, 8, 9, 11], 13)

    def test_empty_array(self):
        self.assertRaises(ValueError, binary_search, [], 1)

if __name__ == '__main__':
    unittest.main()
