class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}

        for src, dest, cost in times:
            adj[src].append((dest, cost))

        res = 0
        minHeap = [(0, k)]
        visited = set()
        
        while minHeap:
            cost1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)
            res = max(res, cost1)

            for node2, cost2 in adj[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (cost1 + cost2, node2))
        return res if len(visited) == n else -1 
