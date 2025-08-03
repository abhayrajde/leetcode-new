# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        freq = {0:1}
        self.res = 0
        def dfs(node, prevSum):
            if not node:
                return 
            
            currSum = prevSum + node.val
            x = currSum - targetSum
            
            if x in freq:
                self.res += freq[x]
            freq[currSum] = 1 + freq.get(currSum, 0)
            
            left = dfs(node.left, currSum)
            right = dfs(node.right, currSum)
            freq[currSum] -= 1
        dfs(root, 0)
        return self.res


