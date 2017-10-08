import unittest

from binary_search_tree import BinarySearchTree

class BinarySearchTreeTests(unittest.TestCase):
    bst = BinarySearchTree()

    def test_add_integer_number(self):
        self.assertTrue(self.bst.add(7))

    def test_add_float_number(self):
        self.assertTrue(self.bst.add(7.5))

    def test_search_valid_number(self):
        self.assertEqual(self.bst.search(7), 7)
    
    def test_search_invalid_number(self):
        self.assertFalse(self.bst.search(8), 8)


if __name__ == '__main__':
    unittest.main()