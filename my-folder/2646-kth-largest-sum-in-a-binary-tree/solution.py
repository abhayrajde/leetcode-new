# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        max_heap = []
        q = deque([root])
        while q:
            tot = 0
            for _ in range(len(q)):
                curr = q.popleft()
                tot += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            heapq.heappush(max_heap,-tot)
        res = 0
        if k > len(max_heap):
            return -1
        for i in range(k):
            res = heapq.heappop(max_heap)
        return -res
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
