# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        def dfs(node, curr_path, curr_sum):
            # Base Case
            if not node:
                return
            sum1 = curr_sum + node.val
            if sum1 == targetSum and not node.left and not node.right:
                path1 = curr_path+[node.val]
                res.append(path1)
            
            left = dfs(node.left, curr_path+[node.val], curr_sum + node.val)
            right = dfs(node.right, curr_path+[node.val], curr_sum + node.val)
        dfs(root, [], 0)
        return res
            

        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
