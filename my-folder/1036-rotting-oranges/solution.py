class Solution(object):
    def orangesRotting(self, grid):
        visited = set()
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 2):
                    q.append((r,c))
                if(grid[r][c] == 1):
                    fresh += 1
        
        while(q and fresh>0):
            for i in range(len(q)):    
                r,c = q.popleft()

                #UP
                if(r-1>=0 and ((r-1,c) not in visited) and (grid[r-1][c] == 1)):
                    visited.add((r-1,c))
                    q.append((r-1,c))
                    fresh-=1
                    grid[r-1][c] == 2
                    
                #DOWN
                if(r+1<rows and ((r+1,c) not in visited) and (grid[r+1][c] == 1)):
                    visited.add((r+1,c))
                    q.append((r+1,c))
                    fresh-=1
                    grid[r+1][c] == 2
                    
                #LEFT
                if(c-1>=0 and ((r,c-1) not in visited) and (grid[r][c-1] == 1)):
                    visited.add((r,c-1))
                    q.append((r,c-1))
                    fresh-=1
                    grid[r][c-1] == 2
                    
                #RIGHT
                if(c+1<cols and ((r,c+1) not in visited) and (grid[r][c+1] == 1)):
                    visited.add((r,c+1))
                    q.append((r,c+1))
                    fresh-=1
                    grid[r][c+1] == 2
            time+=1
        if(fresh == 0):
            return time
        return (-1)        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
