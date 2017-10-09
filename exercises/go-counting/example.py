
class GoCounting:

    none = ""
    white = "W"
    black = "B"
    stones = [black, white]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, board):
        self.board = board.splitlines()
        self.width = len(self.board[0])
        self.height = len(self.board)

    def valid(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def walk_board(self, x, y,
                   visited_territory=[],
                   visited_coords=[],
                   visited_stones=[]):
        if not (x, y) in visited_coords and self.valid(x, y):
            s = self.board[y][x]
            if s in self.stones:
                if s not in visited_stones:
                    return (visited_territory, visited_stones + [s])
            else:  # s is empty
                for d in self.directions:
                    visited = self.walk_board(x + d[0], y + d[1],
                                              visited_territory + [(x, y)],
                                              visited_coords + [(x, y)],
                                              visited_stones)
                    visited_territory = visited[0]
                    visited_stones = visited[1]

        return (visited_territory, visited_stones)

    def territoryFor(self, coord):
        assert len(coord) == 2
        x, y = coord[0], coord[1]
        if not self.valid(x, y) or self.board[y][x] in self.stones:
            return (self.none, set())

        visited_territory, visited_stones = self.walk_board(x, y)
        result = set(visited_territory)

        if len(visited_stones) == 1:
            return (visited_stones[0], result)
        return (self.none, result)

    def territories(self):
        owners = self.stones + [self.none]
        result = dict([(owner, set()) for owner in owners])
        visited = set()
        for y in range(self.height):
            for x in range(self.width):
                if not (x, y) in visited:
                    owner, owned_territories = self.territoryFor((x, y))
                    result[owner].update(owned_territories)
                    visited.update(owned_territories)

        return result
