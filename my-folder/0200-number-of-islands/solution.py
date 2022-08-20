class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row,col = q.popleft()
                #LEFT
                if((row-1>=0) and (grid[row-1][col] == "1") and ((row-1,col) not in visited)):
                    visited.add((row-1,col))
                    q.append((row-1,col))
                
                #RIGHT
                if((row+1<rows) and (grid[row+1][col] == "1") and ((row+1,col) not in visited)):
                    visited.add((row+1,col))
                    q.append((row+1,col))
                
                #UP
                if((col-1>=0) and (grid[row][col-1] == "1") and ((row,col-1) not in visited)):
                    visited.add((row,col-1))
                    q.append((row,col-1))
                    
                #DOWN
                if((col+1<cols) and (grid[row][col+1] == "1") and ((row,col+1) not in visited)):
                    visited.add((row,col+1))
                    q.append((row,col+1))
                    
        for r in range(rows):
            for c in range(cols):
                if((grid[r][c] == "1") and ((r,c) not in visited)):
                    bfs(r,c)
                    islands+=1
                    print(islands)
        return islands
                    
                    
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
