
class ConnectGame:

    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
    WHITE = 'O'
    BLACK = 'X'

    def __init__(self, lines):
        self.board = ConnectGame.make_board(lines)
        assert len(self.board) > 0

        self.width = len(self.board[0])
        self.height = len(self.board)
        assert self.width > 0 and self.height > 0

        for line in self.board:
            assert len(line) == self.width

    def valid(self, width, height):
        return 0 <= width < self.width and 0 <= height < self.height

    @staticmethod
    def make_board(lines):
        return [''.join(cur_line.split()) for cur_line in lines.splitlines()]

    def player_reach_dest(self, player, width, height):
        if player == self.BLACK:
            return width == self.width - 1
        if player == self.WHITE:
            return height == self.height - 1
        return None

    def walk_board(self, player, width, height, visited=None):
        if not visited:
            visited = []
        if (width, height) in visited:
            return False

        if (not self.valid(width, height)) or self.board[height][width] != player:
            return False

        if self.player_reach_dest(player, width, height):
            return True

        for vector in self.DIRECTIONS:
            if self.walk_board(player, width + vector[0], height + vector[1], visited + [(width, height)]):
                return True
        return None

    def check_player_is_winner(self, player):
        if player == self.BLACK:
            for height in range(self.height):
                if self.walk_board(player, 0, height):
                    return True
        if player == self.WHITE:
            for width in range(self.width):
                if self.walk_board(player, width, 0):
                    return True
        return None

    def get_winner(self):
        if self.check_player_is_winner(self.BLACK):
            return self.BLACK
        if self.check_player_is_winner(self.WHITE):
            return self.WHITE
        return ''
