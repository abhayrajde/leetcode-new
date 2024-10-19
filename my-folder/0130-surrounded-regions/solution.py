class Solution(object):
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if (r >= 0 and r < rows and c >= 0 and c < cols 
                and board[r][c] != "X" and board[r][c] != "T"):
                board[r][c] = "T"
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1] == "O":
                dfs(r,cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows-1][c] == "O":
                dfs(rows-1,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"



        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
