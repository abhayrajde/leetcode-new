# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        def dfs(node, count):
            if not node or count >= len(arr):
                return False
            if node.val != arr[count]:
                return False
            if not node.left and not node.right and count == len(arr)-1:
                return True
            left = dfs(node.left, count+1)
            right = dfs(node.right, count+1)
            return left or right
        return dfs(root,0)

        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        
