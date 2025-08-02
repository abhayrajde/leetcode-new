# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False
            newSum = currSum + node.val
            if newSum == targetSum and not node.left and not node.right:
                return True
            
            left = dfs(node.left, newSum)
            right = dfs(node.right, newSum)
            return left or right
        return dfs(root, 0) if root else False
