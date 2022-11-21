"""Diamond inheritance problem exmaple."""


class ClassA:
    sequence = ""
    def __init__(self):
        self.name = 'A'
        self.sequence += self.name

class ClassB(ClassA):
    def __init__(self):
        super().__init__()
        self.name = 'B'
        self.sequence += self.name

class ClassC(ClassA):
    def __init__(self):
        super().__init__()
        print('Init C')
        self.name = 'C'
        self.sequence += self.name

class ClassD(ClassA):
    def __init__(self):
        super().__init__()
        self.name = 'D'
        self.sequence += self.name

class ClassE(ClassC, ClassB, ClassD):
    def __init__(self):
        #ClassC.__init__(self)
        ClassB.__init__(self)
        #ClassC.__init__(self)
        #ClassD.__init__(self)
        self.name = 'E'
        self.sequence += self.name



e = ClassE()



print(e.sequence)