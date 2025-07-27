# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return
            
            if p.val == node.val or q.val == node.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left != None and right != None:
                return node
            
            if left:
                return left
            return right
        return dfs(root)

