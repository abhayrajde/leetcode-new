class Solution(object):
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        if fresh == 0:
            return time

        while(q and fresh > 0):
            for _ in range(len(q)):
                r, c = q.popleft()
                if( r>= 0 and r < rows and c >= 0 and c < cols and (r,c) not in visited and grid[r][c] != 0):
                    visited.add((r,c))
                    q.append((r+1,c))
                    q.append((r-1,c))
                    q.append((r,c+1))
                    q.append((r,c-1))

                    if grid[r][c] == 1:
                        fresh -= 1
            time += 1
        if(fresh == 0):
            return time - 1
        return -1

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
