# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            temp = []
            for i in range(len(q)):
                curr = q.popleft()
                temp.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            res.append(temp)
        for i in range(1,len(res),2):
            res[i] = reversed(res[i])
        return res

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
