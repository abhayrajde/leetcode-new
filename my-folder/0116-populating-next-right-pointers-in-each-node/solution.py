"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if not root:
            return None
        
        q = deque([root])
        while(q):
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                if(i+1 < length):
                    curr.next = q[0]
                else:
                    curr.next = None
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
        return root
        """
        :type root: Node
        :rtype: Node
        """
        
