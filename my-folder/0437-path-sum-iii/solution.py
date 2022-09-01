# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        prevsum = collections.defaultdict(int)
        prevsum[0] = 1
        
        res = [0]
        def dfs(node,currsum):
            
            if not node:
                return 0 
            
            currsum += node.val
            
            if (currsum - targetSum) in prevsum and prevsum[currsum-targetSum]>0:
                res[0]+=prevsum.get((currsum-targetSum),0)
                
            prevsum[currsum]+=1
            
            dfs(node.left, currsum)
            # prevsum[currsum]-=1
            # currsum-=node.val
            
            dfs(node.right, currsum)
            
            prevsum[currsum]-=1
            currsum-=node.val
            
        dfs(root, 0)
        return res[0]
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        
