
BLACK = 'B'
WHITE = 'W'
NONE = ''
STONES = [BLACK, WHITE]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Board:
    def __init__(self, board):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)

    def valid(self, width, height):
        return self.width > width >= 0 and self.height > height >= 0

    def walk(self, width, height, visited_territory=None, visited_coords=None, visited_stones=None):
        # Pylint gives W0102 warning if list used as default argument, because list is mutable.
        visited_territory = [] if visited_territory is None else visited_territory
        visited_coords = [] if visited_coords is None else visited_coords
        visited_stones = [] if visited_stones is None else visited_stones

        if (width, height) not in visited_coords and self.valid(width, height):
            stone = self.board[height][width]
            if stone in STONES:
                if stone not in visited_stones:
                    return (visited_territory, visited_stones + [stone])
            else:  # s is empty
                for direction in DIRECTIONS:
                    visited = self.walk(width + direction[0], height + direction[1],
                                        visited_territory + [(width, height)],
                                        visited_coords + [(width, height)],
                                        visited_stones)
                    visited_territory = visited[0]
                    visited_stones = visited[1]

        return (visited_territory, visited_stones)

    def territory(self, x, y):
        if not self.valid(x, y):
            raise ValueError('Invalid coordinate')
        if self.board[y][x] in STONES:
            return (NONE, set())

        visited_territory, visited_stones = self.walk(x, y)
        result = set(visited_territory)

        if len(visited_stones) == 1:
            return (visited_stones[0], result)
        return (NONE, result)

    def territories(self):
        owners = STONES + [NONE]
        result = {owner:set() for owner in owners}
        visited = set()
        for row in range(self.height):
            for column in range(self.width):
                if not (column, row) in visited:
                    owner, owned_territories = self.territory(column, row)
                    result[owner].update(owned_territories)
                    visited.update(owned_territories)

        return result
