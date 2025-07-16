# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected) 
#         par = [i for i in range(n)] # maintaining root parents of each node
#         rank = [1] * n # maintaining no.of childs of root parent(rank)

#         def find(n1): # Finding root parent
#             res = n1
#             while res != par[res]:
#                 par[res] = par[par[res]] # Path compression
#                 res = par[res]
#             return res
        
#         def union(n1, n2): # mapping to root parent of both nodes
#             p1, p2 = find(n1), find(n2)

#             if p1 == p2:
#                 return 0
            
#             if rank[p2] < rank[p1]:
#                 par[p1] = p2
#                 rank[p2] += 1
#             else:
#                 par[p2] = p1
#                 rank[p1] += 1
#             return 1

#         for i in range(n):
#             for j in range(i+1, n): # Avoid redundant checks (matrix is symmetric)
#                 if isConnected[i][j] == 1:
#                     union(i,j)

#         # Count how many unique routes exist          
#         # provinces = sum(1 for i in range(n) if find(i) == i)
#         provinces = sum(1 for i in range(n) if par[i] == i)
#         return provinces
                
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])
        visited = set()

        adj = {i:[] for i in range(ROWS)}
        for r in range(ROWS):
            for c in range(COLS):
                if isConnected[r][c] == 1:
                    adj[r].append(c)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
        res = 0
        for n in range(ROWS):
            if n not in visited:
                dfs(n)
                res += 1
        return res

                        

