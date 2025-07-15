class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        self.maxArea = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))

            area = 1
            area += (dfs(r+1, c) +
            dfs(r-1, c) +
            dfs(r, c+1) +
            dfs(r, c-1)) 
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    self.maxArea = max(self.maxArea, dfs(r,c))
        return self.maxArea

        
