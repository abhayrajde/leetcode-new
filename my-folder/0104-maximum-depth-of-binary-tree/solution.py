# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        res = [0]
        def dfs(node,currLength):
            if not node:
                return
            currLength += 1
            res[0] = max(res[0],currLength)
            dfs(node.left, currLength)
            dfs(node.right, currLength)
        dfs(root,0)
        return res[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        
