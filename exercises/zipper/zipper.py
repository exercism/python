class Zipper(object):
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def __init__(self, root, parent=None):
        self.root = dict(root)
        self.parent = None if parent is None else dict(parent)

    def value(self):
        return self.root['value']

    def set_value(self):
        pass

    def left(self):
        pass

    def set_left(self):
        pass

    def right(self):
        pass

    def set_right(self):
        pass

    def up(self):
        pass

    def to_tree(self):
        pass
