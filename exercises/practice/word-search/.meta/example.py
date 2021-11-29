import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}:{self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other


DIRECTIONS = (Point(1, 0), Point(1, -1), Point(1, 1), Point(-1, -1),
              Point(0, -1), Point(0, 1), Point(-1, 1), Point(-1, 0))


class WordSearch:
    def __init__(self, puzzle):
        self.rows = puzzle
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    def find_char(self, coordinate):
        if coordinate.x < 0 or coordinate.x >= self.width:
            return None
        if coordinate.y < 0 or coordinate.y >= self.height:
            return None
        return self.rows[coordinate.y][coordinate.x]

    def find(self, word, position, direction):
        current = copy.copy(position)
        for letter in word:
            if self.find_char(current) != letter:
                return None
            current += direction
        return position, current - direction

    def search(self, word):
        positions = (Point(idx, edx)
                     for idx in range(self.width) for edx in range(self.height))
        for position in positions:
            for direction in DIRECTIONS:
                result = self.find(word, position, direction)
                if result:
                    return result
        return None
