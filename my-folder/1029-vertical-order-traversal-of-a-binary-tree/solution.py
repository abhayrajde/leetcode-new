# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = defaultdict(list)
        def dfs(node, r, c):
            if not node:
                return 
            
            left = dfs(node.left, r + 1, c - 1)
            right = dfs(node.right, r + 1, c + 1)
            hm[c].append((r, node.val))
        dfs(root, 0, 0)
        res = []
        for c in sorted(hm.keys()):
            colEl = []
            hm[c].sort()
            for r, val in hm[c]:
                colEl.append(val)
            res.append(colEl)
        return res


