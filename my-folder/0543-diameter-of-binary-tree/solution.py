# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(node):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = max(res[0],(2+left+right))
            return (1+max(left,right))
        dfs(root)
        return res[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        
