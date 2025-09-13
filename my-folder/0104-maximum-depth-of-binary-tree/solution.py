# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node, currDepth):
            if not node:
                return 
            
            self.res = max(self.res, currDepth + 1)

            left = dfs(node.left, currDepth + 1)
            right = dfs(node.right, currDepth + 1)
        dfs(root,0)
        return self.res


            
