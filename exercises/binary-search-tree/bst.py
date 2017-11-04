# A binary search tree implementation


class Node:

    def __init__(self, data=0, left=None, right=None):
        # initialize node data
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        # initialize the root node
        self.root = None

    def add_node(self, data):
        # Returns a new node initialized with data
        return Node(data)

    def insert(self, root, data):

        if root is None:    # Tree is empty
            return self.add_node(data)
        else:
            # Modifying the tree
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root

    def search(self, root, target):

        if root is None:
            return 0
        else:
            if target == root.data:
                return 1
            else:
                if target < root.data:
                    return self.search(root.left, target)
                else:
                    return self.search(root.right, target)

    def min_value(self, root):
        while root.left is not None:
            root = root.left
        return root.data

    def max_value(self, root):
        while root.right is not None:
            root = root.right
        return root.data

    def size(self, root):
        if root is None:
            return 0
        else:
            return self.size(root.left) + self.size(root.right) + 1
