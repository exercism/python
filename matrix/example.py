class Matrix(object):
    def __init__(self, s):
        self.rows = [[int(n) for n in row.split()]
                     for row in s.split('\n')]

    @property
    def columns(self):
        return map(list, zip(*self.rows))
