# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        res = [0]
        def dfs(node, s):
            if not node:
                return
            if not node.left and not node.right:
                res[0] += int(s+str(node.val))
            dfs(node.left, s+str(node.val))
            dfs(node.right, s+str(node.val))
        dfs(root,"")
        return res[0]
            

        """
        :type root: TreeNode
        :rtype: int
        """
        
