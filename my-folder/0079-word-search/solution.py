class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        
        def dfs(r, c, ind):
            # Base Cases
            if ind >= len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or word[ind] != board[r][c] or (r,c) in visited:
                return False

            visited.add((r,c))

            res = (dfs(r+1,c,ind+1) or
            dfs(r-1,c,ind+1) or
            dfs(r,c+1,ind+1) or
            dfs(r,c-1,ind+1))

            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False

        

