# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # normal DFS and keep total if val in range
        def traverse(node):
            nonlocal total
            if not node: return

            if node.val >= low and node.val <= high:
                total += node.val
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        total = 0
        traverse(root)
        return total
            
