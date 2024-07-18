# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        def dfs(node):
            if not node:
                return None

            if(node == p or node == q):
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if(left != None and right != None):
                return node
            
            if(left != None):
                return left
            else:
                return right
        return dfs(root)
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
