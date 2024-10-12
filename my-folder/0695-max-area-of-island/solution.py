class Solution(object):
    def maxAreaOfIsland(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxArea = [0]

        if not grid:
            return 0
        
        def dfs(r,c,area):
            while(r >= 0 and r < ROWS and c>= 0 and c < COLS 
                and (r,c) not in visited and grid[r][c] == 1):
                visited.add((r,c))
                area = (dfs(r+1,c,area+1) + dfs(r-1,c,area+1) + dfs(r,c+1,area+1) + dfs(r,c-1,area+1))
                return area + 1
            return 0
                # maxArea[0] = max(maxArea[0],area)


        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 1 and (r,c) not in visited):
                    area = dfs(r,c,1)
                    maxArea[0] = max(maxArea[0], area)
        return maxArea[0]
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
