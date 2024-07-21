# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        nums = [0]
        def dfs(node, currNum):
            if not node:
                return 
            temp = currNum + str(node.val)
            if(not node.left and not node.right):
                nums[0] += int(temp)
            left = dfs(node.left, temp)
            right = dfs(node.right, temp)
        dfs(root, "")
        return nums[0]

        """
        :type root: TreeNode
        :rtype: int
        """
        
