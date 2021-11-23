class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError('row not positive')
        if not 0 <= row <= 7:
            raise ValueError('row not on board')
        if column < 0:
            raise ValueError('column not positive')
        if not 0 <= column <= 7:
            raise ValueError('column not on board')
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        idx = abs(self.row - another_queen.row)
        edx = abs(self.column - another_queen.column)
        if idx == edx == 0:
            raise ValueError('Invalid queen position: both queens in the same square')
        elif idx == edx or idx == 0 or edx == 0:
            return True
        else:
            return False
