class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        atl, pac = set(), set()

        res = []

        def dfs(r, c, visited, prevHeight):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight or (r,c) in visited:
                return
            
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, -float('inf'))
            dfs(ROWS - 1, c, atl, -float('inf'))

        for r in range(ROWS):
            dfs(r, 0, pac, -float('inf'))
            dfs(r, COLS - 1, atl, -float('inf'))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

