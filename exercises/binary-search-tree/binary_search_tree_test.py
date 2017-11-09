import unittest

from binary_search_tree import BinarySearchTree


class BinarySearchTreeTests(unittest.TestCase):

    def test_add_integer_numbers(self):
        bst = BinarySearchTree()
        self.assertIs(bst.add(1), True)
        self.assertIs(bst.add(8), True)
        self.assertIs(bst.add(3), True)
        self.assertIs(bst.add(5), True)
        self.assertIs(bst.add(2), True)
        self.assertEqual(list(bst.list()), [1, 2, 3, 5, 8])

    def test_add_float_numbers(self):
        bst = BinarySearchTree()
        self.assertIs(bst.add(7.5), True)
        self.assertIs(bst.add(5.3), True)
        self.assertIs(bst.add(5.5), True)
        self.assertIs(bst.add(6.0), True)
        self.assertIs(bst.add(7.7), True)
        self.assertEqual(list(bst.list()), [5.3, 5.5, 6.0, 7.5, 7.7])

    def test_add_mixed_numbers(self):
        bst = BinarySearchTree()
        self.assertIs(bst.add(1), True)
        self.assertIs(bst.add(8), True)
        self.assertIs(bst.add(7.5), True)
        self.assertIs(bst.add(5.3), True)
        self.assertEqual(list(bst.list()), [1, 5.3, 7.5, 8])

    def test_add_duplicated_numbers(self):
        bst = BinarySearchTree()
        self.assertIs(bst.add(1), True)
        self.assertIs(bst.add(1), True)
        self.assertIs(bst.add(7.5), True)
        self.assertIs(bst.add(5.3), True)
        self.assertEqual(list(bst.list()), [1, 1, 5.3, 7.5])

    def test_search_valid_numbers(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(7.5)
        self.assertEqual(bst.search(1).value, 1)
        self.assertEqual(bst.search(7.5).value, 7.5)

    def test_search_invalid_numbers(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(7.5)
        self.assertIs(bst.search(6), False)
        self.assertIs(bst.search(8.8), False)


if __name__ == '__main__':
    unittest.main()
