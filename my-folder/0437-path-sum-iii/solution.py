# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        hm = defaultdict(int)
        hm[0]=1
        self.count = 0
        def dfs(node, currsum,hm):
            # exit condition
            if not node:
                return 0

            currsum += node.val

            self.count += hm.get((currsum-targetSum),0)

            hm[currsum] += 1

            dfs(node.left,currsum,hm)
            dfs(node.right,currsum,hm)
            
            hm[currsum] -= 1
        dfs(root,0,hm)
        return(self.count)

        
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        
