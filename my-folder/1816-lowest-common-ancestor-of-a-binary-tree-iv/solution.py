# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        nodes = set(nodes)
        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node in nodes:
                return node

            if left and right:
                return node
            
            if left:
                return left
            
            if right:
                return right
            return
        return dfs(root)
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        
