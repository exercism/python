# Concepts of binary-search-tree

## Example implementation

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/binary-search-tree/example.py):

```python
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


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
```

## Concepts

- [class][class]: a general comprehension of class concept and and how it works is required, `class` statement
- [Implied Argument][implied-argument]: student needs to know how to use statement `self` in a class
- [class members][class-members]: student must know how members of a class work
- [class methods][class-methods]: student must know how methods of a class work inside and outside the class, the use and meaning of `def` statement
- [arguments][arguments]: concept over arguments of a function and how to use them is required
- [return value][return-value]: the knowledge of `return` statement could be a useful concept in this exercise
- [Dunder Methods][dunder-methods]: student needs to know when to use dunder methods `__init__` and `__str__`
- [overload][overload]: students need to overload methods and specifically dunder methods in this exercise
- [Constructor][constructor]: student needs to know how to build an object using its constructor
- [None][none]: student needs to know the meaning of `None` and how and when assign it to a variable
- [Identity][identity]: the best way to check if an element is `None` is via the _identity_ operator, `is`
- [Boolean][boolean]: concept required to solve the exercise
- [in][in]: use of the `in` statement is useful to look for an object into a list
- [for][for]: the `for ... in` concept is useful to loop over the lists
- [Loops][loops]: concept required to solve the exercise
- [Integer comparison][integer-comparison]: concept required to solve the exercise
- [Recursion][recursion]: recursion is a core concept in this exercise
- [Lists][lists]: knowledge of lists and iteration on lists is required for this exercise
- [Conditional structures][conditional-structures]: knowledge of conditional conceptis and `if...else` statements are required
- [Methods of list][methods-of-list]: the use of methods of list could be useful in this exercise. Methods like `append`, `pop`...
