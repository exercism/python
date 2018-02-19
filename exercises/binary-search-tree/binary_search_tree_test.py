import unittest

from binary_search_tree import BinarySearchTree, TreeNode


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class BinarySearchTreeTests(unittest.TestCase):

    def test_data_is_retained(self):
        expected = TreeNode('4', None, None)
        self.assertTreeEqual(BinarySearchTree(['4']).data(), expected)

    # Test inserting data at proper node
    def test_smaller_data_at_left_node(self):
        expected = TreeNode('4', TreeNode('2', None, None), None)
        self.assertTreeEqual(BinarySearchTree(['4', '2']).data(), expected)

    def test_same_number_at_left_node(self):
        expected = TreeNode('4', TreeNode('4', None, None), None)
        self.assertTreeEqual(BinarySearchTree(['4', '4']).data(), expected)

    def test_greater_number_at_right_node(self):
        expected = TreeNode('4', None, TreeNode('5', None, None))
        self.assertTreeEqual(BinarySearchTree(['4', '5']).data(), expected)

    def test_can_create_complex_tree(self):
        expected = TreeNode(
            '4',
            TreeNode(
                '2',
                TreeNode('1', None, None),
                TreeNode('3', None, None)
            ),
            TreeNode(
                '6',
                TreeNode('5', None, None),
                TreeNode('7', None, None)
            )
        )
        self.assertTreeEqual(
            BinarySearchTree(['4', '2', '6', '1', '3', '5', '7']).data(),
            expected
        )

    # Test can sort data
    def test_can_sort_single_number(self):
        self.assertEqual(BinarySearchTree(['2']).sorted_data(), ['2'])

    def test_can_sort_if_second_number_is_smaller_than_first(self):
        self.assertEqual(
            BinarySearchTree(['2', '1']).sorted_data(), ['1', '2']
        )

    def test_can_sort_if_second_number_is_same_as_first(self):
        self.assertEqual(
            BinarySearchTree(['2', '2']).sorted_data(), ['2', '2']
        )

    def test_can_sort_if_second_number_is_greater_than_first(self):
        self.assertEqual(
            BinarySearchTree(['2', '3']).sorted_data(), ['2', '3']
        )

    def test_can_sort_complex_tree(self):
        self.assertEqual(
            BinarySearchTree(['2', '1', '3', '6', '7', '5']).sorted_data(),
            ['1', '2', '3', '5', '6', '7']
        )

    # Utilities
    def assertTreeEqual(self, tree_one, tree_two):
        try:
            self.compare_tree(tree_one, tree_two)
        except AssertionError:
            raise AssertionError("{} != {}".format(tree_one, tree_two))

    def compare_tree(self, tree_one, tree_two):
        self.assertEqual(tree_one.data, tree_two.data)

        # Compare left tree nodes
        if tree_one.left and tree_two.left:
            self.compare_tree(tree_one.left, tree_two.left)
        elif tree_one.left is None and tree_two.left is None:
            pass
        else:
            raise AssertionError

        # Compare right tree nodes
        if tree_one.right and tree_two.right:
            self.compare_tree(tree_one.right, tree_two.right)
        elif tree_one.right is None and tree_two.right is None:
            pass
        else:
            raise AssertionError


if __name__ == '__main__':
    unittest.main()
