def gamestate(board):
    def check_if_won(player):
        # Rows
        for row in board:
            if all(cell == player for cell in row):
                return True

        # Cols
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        # top left to bottom right
        if all(board[i][i] == player for i in range(3)):
            return True

        # top right to bottom left
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False

    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    x_won = check_if_won("X")
    o_won = check_if_won("O")

    if x_won and o_won:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_won:
        if x_count == o_count:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"

    if o_won:
        if x_count > o_count:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"

    if x_count + o_count == 9:
        return "draw"

    return "ongoing"
