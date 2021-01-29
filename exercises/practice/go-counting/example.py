
BLACK = "B"
WHITE = "W"
NONE = ""
STONES = [BLACK, WHITE]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Board:
    def __init__(self, board):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)

    def valid(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def walk(self, x, y,
             visited_territory=[],
             visited_coords=[],
             visited_stones=[]):
        if not (x, y) in visited_coords and self.valid(x, y):
            s = self.board[y][x]
            if s in STONES:
                if s not in visited_stones:
                    return (visited_territory, visited_stones + [s])
            else:  # s is empty
                for d in DIRECTIONS:
                    visited = self.walk(x + d[0], y + d[1],
                                        visited_territory + [(x, y)],
                                        visited_coords + [(x, y)],
                                        visited_stones)
                    visited_territory = visited[0]
                    visited_stones = visited[1]

        return (visited_territory, visited_stones)

    def territory(self, x, y):
        if not self.valid(x, y):
            raise ValueError('invalid coordinate')
        if self.board[y][x] in STONES:
            return (NONE, set())

        visited_territory, visited_stones = self.walk(x, y)
        result = set(visited_territory)

        if len(visited_stones) == 1:
            return (visited_stones[0], result)
        return (NONE, result)

    def territories(self):
        owners = STONES + [NONE]
        result = dict([(owner, set()) for owner in owners])
        visited = set()
        for y in range(self.height):
            for x in range(self.width):
                if not (x, y) in visited:
                    owner, owned_territories = self.territory(x, y)
                    result[owner].update(owned_territories)
                    visited.update(owned_territories)

        return result
