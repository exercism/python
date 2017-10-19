class Node:
    def __init__(self):
        self.children = [None, None]
        self.num = None


class BinarySearchTree:
    def __init__(self):
        self.__size = 0
        self.__root = Node()

    def __base_function(self, num):
        node = self.__root
        while (node.num is not None):
            if node.num > num:
                if node.children[0] is None:
                    node.children[0] = Node()
                node = node.children[0]
            elif node.num < num:
                if node.children[1] is None:
                    node.children[1] = Node()
                node = node.children[1]
            else:
                break
        return node

    def __replace_node(self, node):
        node.num = None
        pos = -1

        for i in range(len(node.children)):
            if not (node.children[i] is None or node.children[i].num is None):
                pos = i

        if not pos == -1:
            child_node = node.children[pos]
            n_pos = (pos + 1) % 2
            while not (child_node.children[n_pos] is None
                       or child_node.children[n_pos].num is None):
                child_node = child_node.children[n_pos]
            node.num = child_node.num
            self.__replace_node(child_node)

    def contains(self, num):
        node = self.__base_function(num)
        if node.num is None:
            return False
        else:
            return True

    def add(self, num):
        node = self.__base_function(num)
        if node.num is None:
            node.num = num
            self.__size += 1
            return True
        return False

    def remove(self, num):
        node = self.__base_function(num)
        if not node.num is None:
            self.__replace_node(node)
            self.__size -= 1
            return True
        return False

    def size(self):
        return self.__size
