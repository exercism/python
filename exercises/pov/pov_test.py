import unittest

from pov import Tree


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class PovTest(unittest.TestCase):

    def test_singleton_returns_same_tree(self):
        tree = Tree('x')
        self.assertTreeEquals(tree.from_pov('x'), tree)

    def test_can_reroot_tree_with_parent_and_one_sibling(self):
        tree = Tree('parent', [
            Tree('x'),
            Tree('sibling')
        ])
        expected = Tree('x', [
            Tree('parent', [
                Tree('sibling')
            ])
        ])
        self.assertTreeEquals(tree.from_pov('x'), expected)

    def test_can_reroot_tree_with_parent_and_many_siblings(self):
        tree = Tree('parent', [
            Tree('a'),
            Tree('x'),
            Tree('b'),
            Tree('c')
        ])
        expected = Tree('x', [
            Tree('parent', [
                Tree('a'),
                Tree('b'),
                Tree('c')
            ])
        ])
        self.assertTreeEquals(tree.from_pov('x'), expected)

    def test_can_reroot_a_tree_with_new_root_deeply_nested(self):
        tree = Tree('level-0', [
            Tree('level-1', [
                Tree('level-2', [
                    Tree('level-3', [
                        Tree('x')
                    ])
                ])
            ])
        ])
        expected = Tree('x', [
            Tree('level-3', [
                Tree('level-2', [
                    Tree('level-1', [
                        Tree('level-0')
                    ])
                ])
            ])
        ])
        self.assertTreeEquals(tree.from_pov('x'), expected)

    def test_moves_children_of_new_root_to_same_level_as_former_parent(self):
        tree = Tree('parent', [
            Tree('x', [
                Tree('kid-0'),
                Tree('kid-1')
            ])
        ])
        expected = Tree('x', [
            Tree('parent'),
            Tree('kid-0'),
            Tree('kid-1')
        ])
        self.assertTreeEquals(tree.from_pov('x'), expected)

    def test_can_reroot_complex_tree_with_cousins(self):
        tree = Tree('grandparent', [
            Tree('parent', [
                Tree('x', [
                    Tree('kid-0'),
                    Tree('kid-1')
                ]),
                Tree('sibling-0'),
                Tree('sibling-1')
            ]),
            Tree('uncle', [
                Tree('cousin-0'),
                Tree('cousin-1')
            ])
        ])
        expected = Tree('x', [
            Tree('kid-0'),
            Tree('kid-1'),
            Tree('parent', [
                Tree('sibling-0'),
                Tree('sibling-1'),
                Tree('grandparent', [
                    Tree('uncle', [
                        Tree('cousin-0'),
                        Tree('cousin-1')
                    ])
                ])
            ])
        ])
        self.assertTreeEquals(tree.from_pov('x'), expected)

    def test_errors_if_target_does_not_exist_in_singleton_tree(self):
        tree = Tree('x')
        with self.assertRaisesWithMessage(ValueError):
            tree.from_pov('nonexistent')

    def test_errors_if_target_does_not_exist_in_large_tree(self):
        tree = Tree('parent', [
            Tree('x', [
                Tree('kid-0'),
                Tree('kid-1')
            ]),
            Tree('sibling-0'),
            Tree('sibling-1')
        ])
        with self.assertRaisesWithMessage(ValueError):
            tree.from_pov('nonexistent')

    def test_find_path_between_two_nodes(self):
        tree = Tree('parent', [
            Tree('x'),
            Tree('sibling')
        ])
        expected = ['x', 'parent']
        self.assertEqual(tree.path_to('x', 'parent'), expected)

    def test_can_find_path_to_sibling(self):
        tree = Tree('parent', [
            Tree('a'),
            Tree('x'),
            Tree('b'),
            Tree('c')
        ])
        expected = ['x', 'parent', 'b']
        self.assertEqual(tree.path_to('x', 'b'), expected)

    def test_can_find_path_to_cousin(self):
        tree = Tree('grandparent', [
            Tree('parent', [
                Tree('x', [
                    Tree('kid-0'),
                    Tree('kid-1')
                ]),
                Tree('sibling-0'),
                Tree('sibling-1')
            ]),
            Tree('uncle', [
                Tree('cousin-0'),
                Tree('cousin-1')
            ])
        ])
        expected = ['x', 'parent', 'grandparent', 'uncle', 'cousin-1']
        self.assertEqual(tree.path_to('x', 'cousin-1'), expected)

    def test_can_find_path_from_nodes_other_than_x(self):
        tree = Tree('parent', [
            Tree('a'),
            Tree('x'),
            Tree('b'),
            Tree('c')
        ])
        expected = ['a', 'parent', 'c']
        self.assertEqual(tree.path_to('a', 'c'), expected)

    def test_errors_if_destination_does_not_exist(self):
        tree = Tree('parent', [
            Tree('x', [
                Tree('kid-0'),
                Tree('kid-1')
            ]),
            Tree('sibling-0'),
            Tree('sibling-1')
        ])
        with self.assertRaisesWithMessage(ValueError):
            tree.path_to('x', 'nonexistent')

    def test_errors_if_source_does_not_exist(self):
        tree = Tree('parent', [
            Tree('x', [
                Tree('kid-0'),
                Tree('kid-1')
            ]),
            Tree('sibling-0'),
            Tree('sibling-1')
        ])
        with self.assertRaisesWithMessage(ValueError):
            tree.path_to('nonexistent', 'x')

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def assertTreeEquals(self, result, expected):
        self.assertEqual(result, expected,
                         '{} != {}'.format(result, expected))


if __name__ == '__main__':
    unittest.main()
