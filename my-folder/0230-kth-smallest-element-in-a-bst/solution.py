# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        res = [root.val]
        def dfs(node):
            if not node:return 
            
            dfs(node.left)
            self.k -= 1
            if (self.k == 0):
                res[0] = node.val
            dfs(node.right)
        dfs(root)
        return res[0]
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
