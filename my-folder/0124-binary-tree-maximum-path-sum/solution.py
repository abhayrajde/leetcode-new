# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        if not root: return 0
        res = [float("-inf")]
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            
            res[0] = max(res[0],(node.val + left + right))
            
            return (node.val + max(left,right))
        dfs(root)
        return res[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        
