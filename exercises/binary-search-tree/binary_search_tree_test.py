import unittest

from binary_search_tree import BST

class BSTTests(unittest.TestCase):
    def setUp(self):
        self.tree = BST(4)

    def test_insert(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(5)
        self.assertEqual(True, self.tree.search(2))
        self.assertEqual(True, self.tree.search(1))
        self.assertEqual(True, self.tree.search(3))
        self.assertEqual(True, self.tree.search(5))

    def test_search(self):
        self.assertEqual(True, self.tree.search(2))
        self.assertEqual(True, self.tree.search(1))
        self.assertEqual(False, self.tree.search(9))
        self.assertEqual(False, self.tree.search(20))

if __name__ == '__main__':
    unittest.main()
