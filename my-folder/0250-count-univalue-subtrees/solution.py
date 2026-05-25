# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.counter = 0
        def dfs(node):
            if not node:
                return True

            left_is_uni_value = dfs(node.left)
            right_is_uni_value = dfs(node.right)

            if left_is_uni_value and right_is_uni_value:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                
                self.counter += 1
                return True
            return False
        dfs(root)
        return self.counter


        dfs(root)
        return self.counter

