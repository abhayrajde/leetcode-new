# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        q = deque([root])
        hm = {}

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                hm[curr.val] = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        keys = sorted(hm.keys())
        for i in range(len(keys)):
            if p.val == keys[i] and i + 1 < len(keys):
                return hm[keys[i+1]]
        return

