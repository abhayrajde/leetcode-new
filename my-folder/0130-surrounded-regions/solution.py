class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        #1. DFS: capture unsurrounded region (O => T)
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] != 'O':
                return
            visited.add((r,c))
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        #2. Capture surrounded region (O => X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        #3. Uncapture unsurrounded region (T => O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'


        """
        Do not return anything, modify board in-place instead.
        """
        
