class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if not (a == b):
                return False
        return True

    def __repr__(self):
        """Ironically, encoding to SGF is much easier"""
        rep = '(;'
        for k, vs in self.properties.items():
            rep += k
            for v in vs:
                rep += '[{}]'.format(v)
        if self.children:
            if len(self.children) > 1:
                rep += '('
            for c in self.children:
                rep += repr(c)[1:-1]
            if len(self.children) > 1:
                rep += ')'
        return rep + ')'


def is_upper(s):
    a, z = map(ord, 'AZ')
    return all(
        a <= o and o <= z
        for o in map(ord, s)
    )


def parse(input_string):
    root = None
    current = None
    stack = list(input_string)

    def assert_that(condition):
        if not condition:
            raise ValueError(
                'invalid format at {}:{}: {}'.format(
                    repr(input_string),
                    len(input_string) - len(stack),
                    repr(''.join(stack))
                )
            )
    assert_that(stack)

    def pop():
        if stack[0] == '\\':
            stack.pop(0)
        ch = stack.pop(0)
        return ' ' if ch in ['\t'] else ch

    def peek():
        return stack[0]

    def pop_until(ch):
        try:
            v = ''
            while peek() != ch:
                v += pop()
            return v
        except IndexError:
            raise ValueError('Unable to find {}'.format(ch))
    while stack:
        assert_that(pop() == '(' and peek() == ';')
        while pop() == ';':
            properties = {}
            while is_upper(peek()):
                key = pop_until('[')
                assert_that(is_upper(key))
                values = []
                while peek() == '[':
                    pop()
                    values.append(pop_until(']'))
                    pop()
                properties[key] = values
            if root is None:
                current = root = SgfTree(properties)
            else:
                current = SgfTree(properties)
                root.children.append(current)
            while peek() == '(':
                child_input = pop() + pop_until(')') + pop()
                current.children.append(parse(child_input))
    return root
