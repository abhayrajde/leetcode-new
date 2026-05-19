class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for src, dest, wei in times:
            graph[src].append((dest, wei))

        print(graph)

        minheap = [(0,k)]
        visited = set()
        maxTime = 0

        while minheap:
            wei, src = heapq.heappop(minheap)
            if src in visited:
                continue
            visited.add(src)
            maxTime = max(maxTime, wei)
            for dest, nextWei in graph[src]:
                if dest not in visited: 
                    heapq.heappush(minheap, (wei + nextWei, dest))
        return maxTime if len(visited) == n else -1



