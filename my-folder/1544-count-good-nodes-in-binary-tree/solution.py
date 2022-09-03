# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        if not root:return -1
        # maxval = [root.val]
        goodcount = [0]
        def dfs(node,maxval):
            if not node:
                return
            
            if(node.val >= maxval):
                goodcount[0]+=1
                maxval = max(maxval,node.val)
            
            dfs(node.left,maxval)
            dfs(node.right,maxval)
            
        dfs(root,root.val)
        return goodcount[0]
            
            
        """
        :type root: TreeNode
        :rtype: int
        """
        
