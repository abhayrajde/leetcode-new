class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node): # finding the root parent
            res = node
            while res != par[res]:
                par[node] = par[par[node]]
                res = par[node]
            return res


        def union(n1, n2): # mapping to root parent of both nodes
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]


        
