# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        level_sum = [] # collect sum of all the elements on particular level
        q = deque([root])
        #BFS run 1: collect level sum
        while q:
            sum1 = 0
            for _ in range(len(q)):
                curr = q.popleft()
                sum1 += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level_sum.append(sum1)
        
        #BFS run 2: update the cousin value
        q = deque([(root, root.val)])
        level = 0
        while q:
            for _ in range(len(q)):
                curr, child_sum = q.popleft()
                curr.val = level_sum[level] - child_sum

                child_sum = 0
                if curr.left:
                    child_sum += curr.left.val
                if curr.right:
                    child_sum += curr.right.val
                if curr.left:
                    q.append((curr.left, child_sum))
                if curr.right:
                    q.append((curr.right, child_sum))
            level += 1
        return root


        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
