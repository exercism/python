import unittest

from binary_search_tree import BST


class BSTTests(unittest.TestCase):
    def setUp(self):
        self.tree = BST(4)

    def test_insert(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.assertTrue(self.tree.search(2))
        self.assertTrue(self.tree.search(1))

    def test_search(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.assertTrue(self.tree.search(2))
        self.assertTrue(self.tree.search(1))
        self.assertFalse(self.tree.search(9))
        self.assertFalse(self.tree.search(20))

if __name__ == '__main__':
    unittest.main()
