import unittest

from binary_search import binary_search


class BinarySearchTests(unittest.TestCase):

    def test_raises_error_if_list_is_not_sorted(self):
        self.assertRaises(ValueError, binary_search, [44, 5, 2, 1, 4], 6)

    def test_raises_error_if_list_is_empty(self):
        self.assertRaises(ValueError, binary_search, [], 1)

    def test_list_item_not_found(self):
        self.assertEqual("Item not found.",
                         binary_search([1, 2, 3, 4, 5, 6], 23))

    def test_list_item_found(self):
        self.assertEqual(3, binary_search([1, 2, 3, 4, 5, 6, 7, 8], 4))

    def test_list_item_found_larger_list(self):
        self.assertEqual(7, binary_search([1,5,6,7,8,9,12,14,16,22,47,100,123],14))


if __name__ == '__main__':
    unittest.main()
