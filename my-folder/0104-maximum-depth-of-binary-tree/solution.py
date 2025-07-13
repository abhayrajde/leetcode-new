# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node, currDepth):
            if not node:
                return

            res[0] = max(res[0], currDepth + 1)
            dfs(node.left, currDepth + 1)
            dfs(node.right, currDepth + 1)

        dfs(root, 0)
        return res[0]


            
