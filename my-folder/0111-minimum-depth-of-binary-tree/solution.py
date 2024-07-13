# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        count = 0
        q = deque([root])
        while q:
            count += 1
            for i in range(len(q)):
                curr = q.popleft()
                if(not curr.left and not curr.right):
                    return count
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
        return count

        """
        :type root: TreeNode
        :rtype: int
        """
        
