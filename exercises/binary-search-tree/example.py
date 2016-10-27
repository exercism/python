class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if new_val > self.root.value:
            if self.root.right is None:
                self.root.right = Node(new_val)
            else:
                self.pre_insert(self.root.right, new_val)
        elif new_val < self.root.value:
            if self.root.left is None:
                self.root.left = Node(new_val)
            else:
                self.pre_insert(self.root.left, new_val)

    def pre_insert(self, node, val):
        if node.right is None and val > node.value:
            node.right = Node(val)
        elif node.left is None and val < node.value:
            node.left = Node(val)
        elif val > node.value:
            self.pre_insert(node.right, val)
        else:
            self.pre_insert(node.left, val)

    def search(self, find_val):
        current = self.root
        while current.left is not None or current.right is not None:
            if find_val == current.value:
                return True
            elif find_val > current.value:
                current = current.right
            else:
                current = current.left
        return False
