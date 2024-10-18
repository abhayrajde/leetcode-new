# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cache = {}
        q = [(root, 0, 0)]

        while q:
            node, row, col = q.pop(0)
            if row in cache:
                cache[row].append((node, col))
            else:
                cache[row] = [(node, col)]
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        
        output = []
        for row in cache:
            nodes = cache[row]
            output.append(nodes[-1][0].val)

        return output

