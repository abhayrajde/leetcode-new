class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        start = (-1,-1)
        visited = set()

        # Find the starting point
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '*':
                    start = (r,c)
                    visited.add(start)
        
        # Run BFS and find nearest food
        q = deque([start])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 0
        while q:
            count += 1
            for _ in range(len(q)):
                currR, currC = q.popleft()
                for dr, dc in directions:
                    newR, newC = currR + dr, currC + dc
                    if newR < 0 or newC < 0 or newR >= ROWS or newC >= COLS or (newR, newC) in visited or grid[newR][newC] == 'X':
                        continue
                    if grid[newR][newC] == '#':
                        return count
                    visited.add((newR,newC))
                    q.append((newR,newC))
        return -1



        
