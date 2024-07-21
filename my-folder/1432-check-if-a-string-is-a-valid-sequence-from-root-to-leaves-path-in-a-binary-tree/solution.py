# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        def dfs(node, ind):
            if not node or ind >= len(arr):
                return False
            if arr[ind] != node.val:
                return False
            if ind == len(arr)-1 and not node.left and not node.right:
                return True
            left = dfs(node.left, ind+1)
            right = dfs(node.right, ind+1)
            return left or right
        return dfs(root,0)

            
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        
