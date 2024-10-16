# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traverse(node, r, c):
            nonlocal cache
            if not node:
                return
            if c in cache:
                cache[c].append((r, node.val))
            else:
                cache[c] = [(r, node.val)]
            traverse(node.left, r+1, c-1)
            traverse(node.right, r+1, c+1)

        cache = {}
        traverse(root, 0, 0)
        output = []
        for c in sorted(cache.keys()):
            sec = []
            for a, b in sorted(cache[c], key=lambda x:(x[0], x[1])):
                sec.append(b)
            output.append(sec)
        return output
