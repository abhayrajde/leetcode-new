# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        # Base Case:
        if not root:
            return []
        q = deque([root])
        result = []
        
        while q:
            temp = []
            for _ in range(len(q)):
                curr = q.popleft()
                temp.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            result.append(temp[-1])
        return result

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
