# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return
        
        q = deque([root])
        hm = {}

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                hm[curr.val] = curr
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
        keys = hm.keys()
        keys = sorted(keys)
        for i in range(len(keys)):
            if (p.val == keys[i]):
                if(i+1 < len(keys)):
                    return hm[keys[i+1]]
        return
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
