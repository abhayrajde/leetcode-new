# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, curr_sum):
            if(not node):
                return False
            sum1 = curr_sum + node.val
            if(sum1 == targetSum and not node.left and not node.right):
                print curr_sum
                return True
            
            return(dfs(node.left, curr_sum+node.val) or dfs(node.right, curr_sum+node.val))
        return(dfs(root,0))
        
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
