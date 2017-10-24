import unittest

from pov import fromPov, pathTo

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.1


class PovTest(unittest.TestCase):
    def test_singleton_returns_same_tree(self):
        tree = {'x': {}}
        self.assertEqual(fromPov(tree, 'x'), tree)

    def test_can_reroot_tree_with_parent_and_one_sibling(self):
        tree = {
            'parent': {
                'x': {},
                'sibling': {}
            }
        }
        expected = {
            'x': {
                'parent': {
                    'sibling': {}
                }
            }
        }
        self.assertEqual(fromPov(tree, 'x'), expected)

    def test_can_reroot_tree_with_parent_and_many_siblings(self):
        tree = {
            'parent': {
                'a': {},
                'x': {},
                'b': {},
                'c': {}
            }
        }
        expected = {
            'x': {
                'parent': {
                    'a': {},
                    'b': {},
                    'c': {},
                }
            }
        }
        self.assertEqual(fromPov(tree, 'x'), expected)

    def test_can_reroot_a_tree_with_new_root_deeply_nested(self):
        tree = {
            'level-0': {
                'level-1': {
                    'level-2': {
                        'level-3': {
                            'x': {}
                        }
                    }
                }
            }
        }
        expected = {
            'x': {
                'level-3': {
                    'level-2': {
                        'level-1': {
                            'level-0': {}
                        }
                    }
                }
            }
        }
        self.assertEqual(fromPov(tree, 'x'), expected)

    def test_moves_children_of_new_root_to_same_level_as_former_parent(self):
        tree = {
            'parent': {
                'x': {
                    'kid-0': {},
                    'kid-1': {}
                }
            }
        }
        expected = {
            'x': {
                'parent': {},
                'kid-0': {},
                'kid-1': {}
            }
        }
        self.assertEqual(fromPov(tree, 'x'), expected)

    def test_can_reroot_complex_tree_with_cousins(self):
        tree = {
            'grandparent': {
                'parent': {
                    'x': {
                        'kid-0': {},
                        'kid-1': {}
                    },
                    'sibling-0': {},
                    'sibling-1': {}
                },
                'uncle': {
                    'cousin-0': {},
                    'cousin-1': {}
                }
            }
        }
        expected = {
            'x': {
                'kid-0': {},
                'kid-1': {},
                'parent': {
                    'sibling-0': {},
                    'sibling-1': {},
                    'grandparent': {
                        'uncle': {
                            'cousin-0': {},
                            'cousin-1': {}
                        }
                    }
                }
            }
        }
        self.assertEqual(fromPov(tree, 'x'), expected)

    def test_errors_if_target_does_not_exist_in_singleton_tree(self):
        tree = {'x': {}}
        with self.assertRaises(ValueError):
            fromPov(tree, 'nonexistent')

    def test_errors_if_target_does_not_exist_in_large_tree(self):
        tree = {
            'parent': {
                'x': {
                    'kid-0': {},
                    'kid-1': {}
                },
                'sibling-0': {},
                'sibling-1': {}
            }
        }
        with self.assertRaises(ValueError):
            fromPov(tree, 'nonexistent')

    def test_find_path_between_two_nodes(self):
        tree = {
            'parent': {
                'x': {},
                'sibling': {}
            }
        }
        expected = ['x', 'parent']
        self.assertEqual(pathTo(tree, 'x', 'parent'), expected)

    def test_can_find_path_to_sibling(self):
        tree = {
            'parent': {
                'a': {},
                'x': {},
                'b': {},
                'c': {}
            }
        }
        expected = ['x', 'parent', 'b']
        self.assertEqual(pathTo(tree, 'x', 'b'), expected)

    def test_can_find_path_to_cousin(self):
        tree = {
            'grandparent': {
                'parent': {
                    'x': {
                        'kid-0': {},
                        'kid-1': {}
                    },
                    'sibling-0': {},
                    'sibling-1': {}
                },
                'uncle': {
                    'cousin-0': {},
                    'cousin-1': {}
                }
            }
        }
        expected = ['x', 'parent', 'grandparent', 'uncle', 'cousin-1']
        self.assertEqual(pathTo(tree, 'x', 'cousin-1'), expected)

    def test_can_find_path_from_nodes_other_than_x(self):
        tree = {
            'parent': {
                'a': {},
                'x': {},
                'b': {},
                'c': {}
            }
        }
        expected = ['a', 'parent', 'c']
        self.assertEqual(pathTo(tree, 'a', 'c'), expected)

    def test_errors_if_destination_does_not_exist(self):
        tree = {
            'parent': {
                'x': {
                    'kid-0': {},
                    'kid-1': {}
                },
                'sibling-0': {},
                'sibling-1': {}
            }
        }
        with self.assertRaises(ValueError):
            pathTo(tree, 'x', 'nonexistent')

    def test_errors_if_source_does_not_exist(self):
        tree = {
            'parent': {
                'x': {
                    'kid-0': {},
                    'kid-1': {}
                },
                'sibling-0': {},
                'sibling-1': {}
            }
        }
        with self.assertRaises(ValueError):
            pathTo(tree, 'nonexistent', 'x')


if __name__ == '__main__':
    unittest.main()
