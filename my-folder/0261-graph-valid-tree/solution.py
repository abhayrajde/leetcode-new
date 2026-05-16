class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        cycle = set() # elements in curr cycle
        def dfs(curr, prev):
            if curr in cycle:
                return False
            
            cycle.add(curr)
            for nei in graph[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True
        
        # Driver Code
        return dfs(0, -1) and n == len(cycle)

