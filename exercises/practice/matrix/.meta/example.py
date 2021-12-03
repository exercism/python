class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(number) for number in row.split()]
                     for row in matrix_string.split('\n')]
        self.columns = [list(tup) for tup in zip(*self.rows)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
