class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.d1 = 0
        self.d2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        x = 1 if player == 1 else -1
        self.row[row] += x
        self.col[col] += x
        if row == col:
            self.d1 += x
        if row == self.n - col - 1:
            self.d2 += x
        
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.d1) == self.n or abs(self.d2) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
