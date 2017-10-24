import unittest

from zipper import Zipper

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0


def bt(value, left, right):
    return {
        'value': value,
        'left': left,
        'right': right
        }


def leaf(value):
    return bt(value, None, None)


EMPTY_TREE = None


def create_trees():
    t1 = bt(1, bt(2, EMPTY_TREE, leaf(3)), leaf(4))
    t2 = bt(1, bt(5, EMPTY_TREE, leaf(3)), leaf(4))
    t3 = bt(1, bt(2, leaf(5), leaf(3)), leaf(4))
    t4 = bt(1, leaf(2), leaf(4))
    return (t1, t2, t3, t4)


class ZipperTest(unittest.TestCase):
    def test_data_is_retained(self):
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        tree = zipper.to_tree()
        self.assertEqual(tree, t1)

    def test_left_and_right_value(self):
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertEqual(zipper.left().right().value(), 3)

    def test_dead_end(self):
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertIsNone(zipper.left().left())

    def test_tree_from_deep_focus(self):
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertEqual(zipper.left().right().to_tree(), t1)

    def test_set_value(self):
        t1, t2, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_value(5)
        tree = updatedZipper.to_tree()
        self.assertEqual(tree, t2)

    def test_set_left_with_value(self):
        t1, _, t3, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_left(leaf(5))
        tree = updatedZipper.to_tree()
        self.assertEqual(tree, t3)

    def test_set_right_to_none(self):
        t1, _, _, t4 = create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_right(None)
        tree = updatedZipper.to_tree()
        self.assertEqual(tree, t4)

    def test_different_paths_to_same_zipper(self):
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertEqual(zipper.left().up().right().to_tree(),
                         zipper.right().to_tree())


if __name__ == '__main__':
    unittest.main()
