from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [member.__dict__() for member in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def __iter__(self):
        yield self.label
        for child in self.children:
            for grandchild in child:
                yield grandchild

    def dup(self):
        return Tree(self.label, [member.dup() for member in self.children])

    def add(self, other):
        tree = self.dup()
        tree.children.append(other)
        return tree

    def remove(self, node):
        tree = self.dup()
        for child in list(tree.children):
            tree.children.remove(child)
            if child.label == node:
                break
            tree.children.append(child.remove(node))
        return tree

    def from_pov(self, from_node):
        stack = [self]
        visited = set()

        while stack:
            tree = stack.pop(0)
            if tree.label in visited:
                continue

            visited.add(tree.label)
            if from_node == tree.label:
                return tree

            for child in tree.children:
                stack.append(child.add(tree.remove(child.label)))

        raise ValueError('Tree could not be reoriented')



    def path_to(self, from_node, to_node):
        reordered = self.from_pov(from_node)
        stack = reordered.children
        path = [from_node]

        while path[-1] != to_node:
            try:
                tree = stack.pop()
            except IndexError as error:
                raise ValueError('No path found') from error
            if to_node in tree:
                path.append(tree.label)
                stack = tree.children
        return path
