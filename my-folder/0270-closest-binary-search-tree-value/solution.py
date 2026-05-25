# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.min_diff = float('inf')
        self.result = root.val

        def dfs(node):
            if not node:
                return
            diff = abs(node.val - target)

            if diff < self.min_diff:
                self.min_diff = diff
                self.result = node.val
                
            elif diff == self.min_diff:
                self.result = min(self.result, node.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.result


