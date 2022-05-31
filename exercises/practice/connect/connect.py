
class ConnectGame:
    def __init__(self, board):
        self.board = [i.strip().split() for i in board.split("\n")] #generate list from string
        self.checked = []
        self.O_X = "O" # player O will be checked first
    def check_diag(self): # test illegal diagonal
        if len(self.board) >= len(self.board[0]):
            diag_length = len(self.board)
        else:
            diag_length = len(self.board[0])
        main_diag = [[i,i] for i in range(diag_length)]
        diag_list =[[item for item in main_diag[::] if 0<=item[0]<len(self.board) and 0<=item[1]<len(self.board[0])]]
        for diag in range(1,diag_length):
            diag_left = []
            diag_right = []
            for item in range(diag_length):
                if 0<=main_diag[::][item][0]<len(self.board) and 0<=main_diag[::][item][1]-diag<len(self.board[0]):
                    diag_left.append([main_diag[::][item][0], main_diag[::][item][1]-diag])
                if 0<=main_diag[::][item][0]<len(self.board) and 0<=main_diag[::][item][1]+diag<len(self.board[0]):
                    diag_right.append([main_diag[::][item][0], main_diag[::][item][1]+diag])
            diag_list.append(diag_left)
            diag_list.append(diag_right)
        diag_list = [[self.board[item[0]][item[1]] for item in diag] for diag in diag_list]
        result = [i for i in diag_list if len(i)>2 and len(set(i))==1]
        return result
        
    def recurs_search(self,x,y): #recursive function, check if every adjacent cell is on bottom
        fields = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y+1), (x+1,y+1), (x+1,y), (x+1,y-1), (x,y-1)]
        if 0<=x<len(self.board) and 0<=y<len(self.board[0]) and self.board[x][y] == self.O_X and ([x,y] not in self.checked):
            self.checked.append([x,y])
            return "w" if x == len(self.board)-1 else [self.recurs_search(i[0],i[1]) for i in fields]
    def try_get_win(self): # check if the player O (or X) is the winner
        for i, j in enumerate(self.board[0]):
            if j == self.O_X:
                if str(self.recurs_search(0,i)).find("w") != -1:
                    return "w"
    def get_winner(self): #check player 0, then X, if neither win output ""
        if self.check_diag():
            return ""
        elif self.try_get_win():
            return "O"
        self.board = [list(i) for i in zip(*self.board[::-1])] # transpose the board, X to be from top to down
        self.checked = []
        self.O_X = "X"
        return "X" if self.try_get_win() else ""
