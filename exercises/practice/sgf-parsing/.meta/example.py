class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False

        for key, value in self.properties.items():
            if key not in other.properties:
                return False

            if other.properties[key] != value:
                return False

        for key in other.properties.keys():
            if key not in self.properties:
                return False

        if len(self.children) != len(other.children):
            return False

        for child, other_child in zip(self.children, other.children):
            if not child == other_child:
                return False
        return True

    def __repr__(self):
        """Ironically, encoding to SGF is much easier."""
        rep = '(;'
        for key, property_value in self.properties.items():
            rep += key
            for value in property_value:
                rep += '[{}]'.format(value)
        if self.children:
            if len(self.children) > 1:
                rep += '('
            for child in self.children:
                rep += repr(child)[1:-1]
            if len(self.children) > 1:
                rep += ')'
        return rep + ')'


def parse(input_string):
    root = None
    current = None
    stack = list(input_string)

    if input_string == '()':
        raise ValueError('tree with no nodes')

    if not stack:
        raise ValueError('tree missing')

    def pop():
        if stack[0] == '\\':
            stack.pop(0)
        characters = stack.pop(0)
        return ' ' if characters in ['\t'] else characters

    def pop_until(delimiter):
        try:
            value = ''
            while stack[0] != delimiter:
                value += pop()
            return value
        except IndexError as error:
            raise ValueError('properties without delimiter') from error

    while stack:
        if pop() == '(' and stack[0] == ';':
            while pop() == ';':
                properties = {}
                while stack[0].isupper():
                    key = pop_until('[')
                    if not key.isupper():
                        raise ValueError('property must be in uppercase')
                    values = []
                    while stack[0] == '[':
                        pop()
                        values.append(pop_until(']'))
                        pop()
                    properties[key] = values

                if stack[0].isalpha():
                    if not stack[0].isupper():
                        raise ValueError('property must be in uppercase')

                if root is None:
                    current = root = SgfTree(properties)

                else:
                    current = SgfTree(properties)
                    root.children.append(current)

                while stack[0] == '(':
                    child_input = pop() + pop_until(')') + pop()
                    current.children.append(parse(child_input))

        elif root is None and current is None:
            raise ValueError('tree missing')

    return root
