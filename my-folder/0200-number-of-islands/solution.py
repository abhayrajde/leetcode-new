class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        visited = set()
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])


        def dfs(r,c):
            while(r >= 0 and r < ROWS and c >= 0 and c < COLS and 
                (r,c) not in visited and grid[r][c] == "1"):
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)


        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == "1" and (r,c) not in visited):
                    dfs(r,c)
                    islands += 1
        return islands


                    
                    

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
