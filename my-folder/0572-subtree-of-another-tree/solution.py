# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def dfs(node):
            if not node:
                return False

            if self.isSameTree(node, subRoot):
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            return left or right

        return dfs(root)



    def isSameTree(self, node1, node2):
        if not node1 and not node2: return True

        if not node1 or not node2 or node1.val != node2.val:
            return False
        
        left = self.isSameTree(node1.left, node2.left)
        right = self.isSameTree(node1.right, node2.right)

        return left and right
    
