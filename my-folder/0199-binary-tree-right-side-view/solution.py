# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        q = deque([root])
        while(q):
            qsize = len(q)
            for i in range(len(q)):
                curr = q.popleft()
                if(i == qsize-1):
                    res.append(curr.val)
                
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
        return res     

        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
