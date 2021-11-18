class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
            self.add(data)

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return
        inserted = False
        cur_node = self.root

        while not inserted:
            if data <= cur_node.data:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = TreeNode(data)
                    inserted = True
            elif data > cur_node.data:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = TreeNode(data)
                    inserted = True

    def _inorder_traverse(self, node, elements):
        if node is not None:
            self._inorder_traverse(node.left, elements)
            elements.append(node.data)
            self._inorder_traverse(node.right, elements)

    def data(self):
        return self.root

    def sorted_data(self):
        elements = []
        self._inorder_traverse(self.root, elements)
        return elements
