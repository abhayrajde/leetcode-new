# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        def dfs(node, currSum, currList):
            if not node:
                return 
            sum1 = currSum + node.val
            if(sum1 == targetSum and not node.left and not node.right):
                currList.append(node.val)
                res.append(currList)
            left = dfs(node.left, sum1, currList+[node.val])
            right = dfs(node.right, sum1, currList+[node.val])
            return left or right
        dfs(root,0,[])
        return res
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
