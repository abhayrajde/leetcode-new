# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        res = [0]
        def dfs(node, strNum):
            if not node:
                return
            temp = strNum + str(node.val)
            if not node.right and not node.left:
                res[0] += int(temp)
            left = dfs(node.left, temp)
            right = dfs(node.right, temp)
        dfs(root,"")
        return res[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        
