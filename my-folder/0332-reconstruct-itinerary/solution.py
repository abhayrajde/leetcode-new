# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adj = { src: [] for src, dest in tickets }

#         tickets.sort()

#         for src, dest in tickets:
#             adj[src].append(dest)
        
#         # for places in adj.keys():
#         #     adj[places].sort()
        
#         res = ["JFK"]

#         def dfs(src):
#             if len(res) == len(tickets) + 1:
#                 return True
#             if src not in adj:
#                 return False
            
#             temp = list(adj[src])
#             for i, dest in enumerate(temp):
#                 adj[src].pop(i)
#                 res.append(dest)
                
#                 if dfs(dest): return True
#                 # if dfs returned False - backtrack our decision
#                 adj[src].insert(i, dest)
#                 res.pop()
#             return False
#         dfs('JFK')
#         return res

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
            
        dfs('JFK')
        return res[::-1]
