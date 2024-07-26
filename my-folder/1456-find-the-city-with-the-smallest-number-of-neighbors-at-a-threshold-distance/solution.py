class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        adj = defaultdict(list)
        for v1, v2, dist in edges:
            adj[v1].append((v2,dist))
            adj[v2].append((v1,dist))

        def dijkstra(src):
            heap = [(0,src)] #Total_dist, node
            visited = set()

            while(heap):
                dist, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, dist2 in adj[node]:
                    if(dist + dist2 <= distanceThreshold):
                        heapq.heappush(heap, (dist + dist2, nei))
            return len(visited)-1
        res, min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if(count <= min_count):
                res = src
                min_count = count
        return res

        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        
