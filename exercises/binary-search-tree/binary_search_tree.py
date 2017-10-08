
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return str(self.value)

# lalal
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
                if(value < cur_node.value):
                    if(cur_node.left_node):
                        cur_node = cur_node.left_node
                    else:
                        cur_node.left_node = TreeNode(value)
                        inserted = True
                elif(value >  cur_node.value):
                    if(cur_node.right_node):
                        cur_node = cur_node.right_node
                    else:
                        cur_node.right_node = TreeNode(value)
                        inserted = True                  
