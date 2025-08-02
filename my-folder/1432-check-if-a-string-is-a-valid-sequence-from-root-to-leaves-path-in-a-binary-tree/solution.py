# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, ind):
            if not node or ind >= len(arr) or node.val != arr[ind]:
                return False
            if ind == len(arr) - 1 and not node.left and not node.right and node.val == arr[ind]:
                return True
            
            left = dfs(node.left, ind + 1)
            right = dfs(node.right, ind + 1)

            return left or right
        return dfs(root, 0)

