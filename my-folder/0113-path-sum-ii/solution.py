# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, currSum, currPath):

            if not node:
                return
             
            if not node.left and not node.right and currSum + node.val == targetSum:
                res.append(currPath + [node.val])
                return
            
            left = dfs(node.left, currSum + node.val, currPath + [node.val])
            right = dfs(node.right, currSum + node.val, currPath + [node.val])
        dfs(root, 0, [])
        return res

