import unittest

from example import binary_search, list_sorted


class BinarySearchTests(unittest.TestCase):

    def test_list_sorted(self):
        self.assertEqual(False, list_sorted([3,1,4,5,6]))

    def test_raises_value_error_if_not_sorted(self):
        self.assertEqual('The list must be sorted', binary_search([44,5,2,1,4], 6))

    def test_list_item_not_found(self):
        self.assertEqual("Item not found", binary_search([1,2,3,4,5,6], 23))


if __name__ == '__main__':
    unittest.main()
