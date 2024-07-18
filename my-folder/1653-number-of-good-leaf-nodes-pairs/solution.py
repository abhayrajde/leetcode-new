# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        pairs = [0]
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        pairs[0] += 1

            all_dist = left_dist + right_dist
            return [d+1 for d in all_dist]

        dfs(root)
        return pairs[0]
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        
