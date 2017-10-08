import unittest

from binary_search_tree import BinarySearchTree

class BinarySearchTreeTests(unittest.TestCase):
    bst = BinarySearchTree()

    def test_add_integer_number1(self):
        self.assertTrue(self.bst.add(7))
    
    def test_add_integer_number2(self):
        self.assertTrue(self.bst.add(1))

    def test_add_integer_number3(self):
        self.assertTrue(self.bst.add(6))

    def test_add_integer_number4(self):
        self.assertTrue(self.bst.add(5))

    def test_add_float_number(self):
        self.assertTrue(self.bst.add(7.5))

    def test_search_valid_number1(self):
        self.assertEqual(self.bst.search(7).value, 7)

    def test_search_valid_number2(self):
        self.assertEqual(self.bst.search(7.5).value, 7.5)

    def test_search_valid_number3(self):
        self.assertEqual(self.bst.search(1).value, 1)
    

if __name__ == '__main__':
    unittest.main()