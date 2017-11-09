import unittest

from binary_search_tree import BinarySearchTree


class BinarySearchTreeTests(unittest.TestCase):

    def test_add_integer_numbers(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(8)
        bst.add(3)
        bst.add(5)
        bst.add(2)
        self.assertEqual(list(bst.list()), [1, 2, 3, 5, 8])

    def test_add_float_numbers(self):
        bst = BinarySearchTree()
        bst.add(7.5)
        bst.add(5.3)
        bst.add(5.5)
        bst.add(6.0)
        bst.add(7.7)
        self.assertEqual(list(bst.list()), [5.3, 5.5, 6.0, 7.5, 7.7])

    def test_add_mixed_numbers(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(8)
        bst.add(7.5)
        bst.add(5.3)
        self.assertEqual(list(bst.list()), [1, 5.3, 7.5, 8])

    def test_add_duplicated_numbers(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(1)
        bst.add(7.5)
        bst.add(5.3)
        self.assertEqual(list(bst.list()), [1, 1, 5.3, 7.5])

    def test_search_existent_numbers(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(7.5)
        self.assertEqual(bst.search(1).value, 1)
        self.assertEqual(bst.search(7.5).value, 7.5)

    def test_search_nonexistent_numbers(self):
        bst = BinarySearchTree()
        bst.add(1)
        bst.add(7.5)
        self.assertIs(bst.search(6), None)
        self.assertIs(bst.search(8.8), None)


if __name__ == '__main__':
    unittest.main()
