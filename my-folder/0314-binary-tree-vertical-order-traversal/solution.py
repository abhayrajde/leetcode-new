# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        dict1 = defaultdict(list)
        h_dist, v_dist = 0, 0

        def dfs(node, h_dist, v_dist):
            if not node:
                return
            dict1[h_dist].append((node.val, v_dist))

            left = dfs(node.left, h_dist - 1, v_dist + 1)
            right = dfs(node.right, h_dist + 1, v_dist + 1)
            
        dfs(root,0,0)
        pairs = sorted(dict1.items())

        result = []
        for key, values in pairs:
            sortedValues = sorted(values, key = lambda x:x[1])
            temp = []
            for i in sortedValues:
                temp.append(i[0])
            result.append(temp)
        return result
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
