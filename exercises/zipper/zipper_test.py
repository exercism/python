import unittest

from zipper import Zipper


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class ZipperTest(unittest.TestCase):
    def bt(self, value, left, right):
        return {
            'value': value,
            'left': left,
            'right': right
        }

    def leaf(self, value):
        return self.bt(value, None, None)

    def create_trees(self):
        t1 = self.bt(1, self.bt(2, None, self.leaf(3)), self.leaf(4))
        t2 = self.bt(1, self.bt(5, None, self.leaf(3)), self.leaf(4))
        t3 = self.bt(1, self.bt(2, self.leaf(5), self.leaf(3)), self.leaf(4))
        t4 = self.bt(1, self.leaf(2), self.leaf(4))
        return (t1, t2, t3, t4)

    def test_data_is_retained(self):
        t1, _, _, _ = self.create_trees()
        zipper = Zipper.from_tree(t1)
        tree = zipper.to_tree()
        self.assertEqual(tree, t1)

    def test_left_and_right_value(self):
        t1, _, _, _ = self.create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertEqual(zipper.left().right().value(), 3)

    def test_dead_end(self):
        t1, _, _, _ = self.create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertIsNone(zipper.left().left())

    def test_tree_from_deep_focus(self):
        t1, _, _, _ = self.create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertEqual(zipper.left().right().to_tree(), t1)

    def test_set_value(self):
        t1, t2, _, _ = self.create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_value(5)
        tree = updatedZipper.to_tree()
        self.assertEqual(tree, t2)

    def test_set_left_with_value(self):
        t1, _, t3, _ = self.create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_left(self.leaf(5))
        tree = updatedZipper.to_tree()
        self.assertEqual(tree, t3)

    def test_set_right_to_none(self):
        t1, _, _, t4 = self.create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_right(None)
        tree = updatedZipper.to_tree()
        self.assertEqual(tree, t4)

    def test_different_paths_to_same_zipper(self):
        t1, _, _, _ = self.create_trees()
        zipper = Zipper.from_tree(t1)
        self.assertEqual(zipper.left().up().right().to_tree(),
                         zipper.right().to_tree())


if __name__ == '__main__':
    unittest.main()
