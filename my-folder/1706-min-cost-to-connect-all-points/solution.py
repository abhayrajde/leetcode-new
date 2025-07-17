class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = { i:[] for i in range(N) }

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        #Prim's Algo
        res = 0
        minH = [(0,0)]
        visited = set()
        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            visited.add(i)
            res += cost
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, (neiCost, nei))
        return res
