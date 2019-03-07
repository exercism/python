import unittest

from tree_building import Record, BuildTree


class TreeBuildingTest(unittest.TestCase):
    """
        Record(record_id, parent_id): records given to be processed
        Node(node_id): Node in tree
        BuildTree(records): records as argument and returns tree
        BuildTree should raise ValueError if given records are invalid
    """

    def test_empty_list_input(self):
        records = []
        root = BuildTree(records)
        self.assertIsNone(root)

    def test_one_node(self):
        records = [
            Record(0, 0)
        ]
        root = BuildTree(records)

        self.assert_node_is_leaf(root, node_id=0)

    def test_three_nodes_in_order(self):
        records = [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0)
        ]
        root = BuildTree(records)

        self.assert_node_is_branch(root, node_id=0, children_count=2)
        self.assert_node_is_leaf(root.children[0], node_id=1)
        self.assert_node_is_leaf(root.children[1], node_id=2)

    def test_three_nodes_in_reverse_order(self):
        records = [
            Record(2, 0),
            Record(1, 0),
            Record(0, 0)
        ]
        root = BuildTree(records)

        self.assert_node_is_branch(root, node_id=0, children_count=2)
        self.assert_node_is_leaf(root.children[0], node_id=1)
        self.assert_node_is_leaf(root.children[1], node_id=2)

    def test_more_than_two_children(self):
        records = [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0),
            Record(3, 0)
        ]
        root = BuildTree(records)

        self.assert_node_is_branch(root, node_id=0, children_count=3)
        self.assert_node_is_leaf(root.children[0], node_id=1)
        self.assert_node_is_leaf(root.children[1], node_id=2)
        self.assert_node_is_leaf(root.children[2], node_id=3)

    def test_binary_tree(self):
        records = [
            Record(6, 2),
            Record(0, 0),
            Record(3, 1),
            Record(2, 0),
            Record(4, 1),
            Record(5, 2),
            Record(1, 0)
        ]
        root = BuildTree(records)

        self.assert_node_is_branch(root, 0, 2)
        self.assert_node_is_branch(root.children[0], 1, 2)
        self.assert_node_is_branch(root.children[1], 2, 2)
        self.assert_node_is_leaf(root.children[0].children[0], 3)
        self.assert_node_is_leaf(root.children[0].children[1], 4)
        self.assert_node_is_leaf(root.children[1].children[0], 5)
        self.assert_node_is_leaf(root.children[1].children[1], 6)

    def test_unbalanced_tree(self):
        records = [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0),
            Record(3, 1),
            Record(4, 1),
            Record(5, 1),
            Record(6, 2),
        ]
        root = BuildTree(records)

        self.assert_node_is_branch(root, 0, 2)
        self.assert_node_is_branch(root.children[0], 1, 3)
        self.assert_node_is_branch(root.children[1], 2, 1)
        self.assert_node_is_leaf(root.children[0].children[0], 3)
        self.assert_node_is_leaf(root.children[0].children[1], 4)
        self.assert_node_is_leaf(root.children[0].children[2], 5)
        self.assert_node_is_leaf(root.children[1].children[0], 6)

    def test_root_node_has_parent(self):
        records = [
            Record(0, 1),
            Record(1, 0)
        ]
        # Root parent_id should be equal to record_id(0)
        with self.assertRaisesWithMessage(ValueError):
            BuildTree(records)

    def test_no_root_node(self):
        records = [
            Record(1, 0),
            Record(2, 0)
        ]
        # Record with record_id 0 (root) is missing
        with self.assertRaisesWithMessage(ValueError):
            BuildTree(records)

    def test_non_continuous(self):
        records = [
            Record(2, 0),
            Record(4, 2),
            Record(1, 0),
            Record(0, 0)
        ]
        # Record with record_id 3 is missing
        with self.assertRaisesWithMessage(ValueError):
            BuildTree(records)

    def test_cycle_directly(self):
        records = [
            Record(5, 2),
            Record(3, 2),
            Record(2, 2),
            Record(4, 1),
            Record(1, 0),
            Record(0, 0),
            Record(6, 3)
        ]
        # Cycle caused by Record 2 with parent_id pointing to itself
        with self.assertRaisesWithMessage(ValueError):
            BuildTree(records)

    def test_cycle_indirectly(self):
        records = [
            Record(5, 2),
            Record(3, 2),
            Record(2, 6),
            Record(4, 1),
            Record(1, 0),
            Record(0, 0),
            Record(6, 3)
        ]
        # Cycle caused by Record 2 with parent_id(6) greater than record_id(2)
        with self.assertRaisesWithMessage(ValueError):
            BuildTree(records)

    def test_higher_id_parent_of_lower_id(self):
        records = [
            Record(0, 0),
            Record(2, 0),
            Record(1, 2)
        ]
        # Record 1 have parent_id(2) greater than record_id(1)
        with self.assertRaisesWithMessage(ValueError):
            BuildTree(records)

    def assert_node_is_branch(self, node, node_id, children_count):
        self.assertEqual(node.node_id, node_id)
        self.assertNotEqual(len(node.children), 0)
        self.assertEqual(len(node.children), children_count)

    def assert_node_is_leaf(self, node, node_id):
        self.assertEqual(node.node_id, node_id)
        self.assertEqual(len(node.children), 0)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
