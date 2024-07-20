# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, currSum):
            if not node:
                return False
            sum1 = currSum + node.val
            if(sum1 == targetSum and not node.left and not node.right):
                return True
            left = dfs(node.left, sum1)
            right = dfs(node.right, sum1)
            return left or right
        return dfs(root, 0)
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
