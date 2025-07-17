class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Dijkstra's algo - bfs + minheap
        N = len(grid)
        visited = set()
        minH = [(grid[0][0], 0, 0)]
        directions = [[0, 1], [0, -1], [1,0], [-1, 0]]

        visited.add((0,0))
        while minH:
            time, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return time
            for dr, dc in directions:
                neiR, neiC = dr + r, dc + c
                if neiR < 0 or neiC < 0 or neiR >= N or neiC >= N or (neiR, neiC) in visited:
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minH, (max(time,grid[neiR][neiC]), neiR, neiC))
