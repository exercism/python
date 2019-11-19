class Matrix:
    def __init__(self, s):
        self.rows = [[int(n) for n in row.split()]
                     for row in s.split('\n')]
        self.columns = [list(tup) for tup in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
