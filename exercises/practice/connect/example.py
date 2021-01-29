
class ConnectGame:

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
    white = "O"
    black = "X"
    none = ""

    def __init__(self, lines):
        self.board = ConnectGame.make_board(lines)
        assert len(self.board) > 0

        self.width = len(self.board[0])
        self.height = len(self.board)
        assert self.width > 0 and self.height > 0

        for l in self.board:
            assert len(l) == self.width

    def valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    @staticmethod
    def make_board(lines):
        return ["".join(l.split()) for l in lines.splitlines()]

    def player_reach_dest(self, player, x, y):
        if player == self.black:
            return x == self.width - 1
        if player == self.white:
            return y == self.height - 1

    def walk_board(self, player, x, y, visited=[]):
        if (x, y) in visited:
            return False

        if (not self.valid(x, y)) or self.board[y][x] != player:
            return False

        if self.player_reach_dest(player, x, y):
            return True

        for d in self.directions:
            if self.walk_board(player, x + d[0], y + d[1], visited + [(x, y)]):
                return True

    def check_player_is_winner(self, player):
        if player == self.black:
            for y in range(self.height):
                if self.walk_board(player, 0, y):
                    return True
        if player == self.white:
            for x in range(self.width):
                if self.walk_board(player, x, 0):
                    return True

    def get_winner(self):
        if self.check_player_is_winner(self.black):
            return self.black
        if self.check_player_is_winner(self.white):
            return self.white
        return self.none
