"""Diamond inheritance problem exmaple."""


class ClassA:
    sequence = ""
    def __init__(self):
        self.name = 'A'
        self.sequence += self.name

class ClassMixin:
    def sequence_as_tuple(self):
        return tuple(self.sequence)

class ClassB(ClassA, ClassMixin):
    def __init__(self):
        super().__init__()
        self.name = 'B'
        self.sequence += self.name

class ClassC(ClassA, ClassMixin):
    def __init__(self):
        super().__init__()
        self.name = 'C'
        self.sequence += self.name

class ClassD(ClassA, ClassMixin):
    def __init__(self):
        super().__init__()
        self.name = 'D'
        self.sequence += self.name

class ClassE(ClassC, ClassB, ClassD):
    def __init__(self):
        super().__init__()
        self.name = 'E'
        self.sequence += self.name
