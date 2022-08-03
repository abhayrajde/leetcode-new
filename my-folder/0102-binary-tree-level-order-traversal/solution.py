# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        q = deque([root])
        res = []
        while(q):
            level_values = []
            for i in range(len(q)):
                cur = q.popleft()
                level_values.append(cur.val)
                if(cur.left):
                    q.append(cur.left)
                if(cur.right):
                    q.append(cur.right)
            if(level_values):
                res.append(level_values)
        return(res)
        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
