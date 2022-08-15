# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def dfs(node, left, right):
            if not node:
                return True
            if((left>=node.val) or (right<=node.val)):
                return False
            
            return(dfs(node.left,left,node.val) and dfs(node.right,node.val,right))
        return(dfs(root,-float("inf"),float("inf")))
            
            
        """
        :type root: TreeNode
        :rtype: bool
        """
        
