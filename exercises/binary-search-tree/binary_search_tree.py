class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = None
        self.left = None
        self.right = None

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        pass

    def data(self):
        pass

    def sorted_data(self):
        pass
