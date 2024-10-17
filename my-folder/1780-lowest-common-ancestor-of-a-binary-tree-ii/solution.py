# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        count = [0]
        def dfs(node):
            if not node:
                return

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                count[0] += 1
                return node
            
            if left and right:
                return node
            
            if left:
                return left

            if right:
                return right
            return
            
        traverse = dfs(root)
        if count[0] == 2:
            return traverse
        return
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
