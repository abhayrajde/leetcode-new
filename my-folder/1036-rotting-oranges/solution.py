class Solution(object):
    def orangesRotting(self, grid):
        q = deque()
        
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 2):
                    q.append((r,c))
                if(grid[r][c] == 1):
                    fresh+=1
        
        visited = set()
        mins = 0
        while(q and fresh > 0):
            print(q)
            for i in range(len(q)):
                r,c = q.popleft()
                
                # Down
                if(r+1 < rows and ((r+1,c) not in visited) and (grid[r+1][c]==1)):
                    q.append((r+1,c))
                    visited.add((r+1,c))
                    grid[r+1][c] = 2
                    fresh-=1
                
                # Up
                if(r-1 >= 0 and ((r-1,c) not in visited) and (grid[r-1][c]==1)):
                    q.append((r-1,c))
                    visited.add((r-1,c))
                    grid[r-1][c] = 2
                    fresh-=1
                
                # Left
                if(c-1 >= 0 and ((r,c-1) not in visited) and (grid[r][c-1]==1)):
                    q.append((r,c-1))
                    visited.add((r,c-1))
                    grid[r][c-1] = 2
                    fresh-=1
                
                # Right
                if(c+1 < cols and ((r,c+1) not in visited) and (grid[r][c+1]==1)):
                    q.append((r,c+1))
                    visited.add((r,c+1))
                    grid[r][c+1] = 2
                    fresh -= 1
            mins+=1
        if(fresh == 0):
            return(mins)
        return(-1)
                
                
                
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
