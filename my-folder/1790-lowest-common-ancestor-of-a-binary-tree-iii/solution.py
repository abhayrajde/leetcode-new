"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        ans = set()
        cur_p = p
        cur_q = q
        while cur_p or cur_q:
            if cur_p and cur_q and cur_p.val == cur_q.val:
                return cur_q
            if cur_p:
                if cur_p.val in ans:
                    return cur_p
                ans.add(cur_p.val)
                cur_p = cur_p.parent
            if cur_q:
                if cur_q.val in ans:
                    return cur_q
                ans.add(cur_q.val)
                cur_q = cur_q.parent
        """
        :type node: Node
        :rtype: Node
        """
        
