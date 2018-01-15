from collections import deque


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if(self.root is None):
            self.root = TreeNode(value)
        else:
            inserted = False
            cur_node = self.root

            while not inserted:
                if(value <= cur_node.value):
                    if(cur_node.left_node):
                        cur_node = cur_node.left_node
                    else:
                        cur_node.left_node = TreeNode(value)
                        inserted = True
                elif(value > cur_node.value):
                    if(cur_node.right_node):
                        cur_node = cur_node.right_node
                    else:
                        cur_node.right_node = TreeNode(value)
                        inserted = True

    def search(self, value):
        cur_node = self.root
        found = False
        while not found:
            if(cur_node is None):
                return None
            elif(value < cur_node.value):
                cur_node = cur_node.left_node
            elif(value > cur_node.value):
                cur_node = cur_node.right_node
            elif(value == cur_node.value):
                return cur_node

    def list(self):
        elements = deque()
        self.trav_inorder(self.root, elements)
        return elements

    def trav_inorder(self, node, elements):
        if(node is not None):
            self.trav_inorder(node.left_node, elements)
            elements.append(node.value)
            self.trav_inorder(node.right_node, elements)
