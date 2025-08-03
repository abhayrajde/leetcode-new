# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)

        # dfs function will help to generate the adj dict
        def dfs(node):
            if not node:
                return
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)

            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        mins = 0
        q = deque([start])
        visited = set()
        
        while q:
            mins += 1
            for _ in range(len(q)):
                curr = q.popleft()
                visited.add(curr)
                for nei in adj[curr]:
                    if nei not in visited:
                        q.append(nei)
        return mins - 1
                

        
