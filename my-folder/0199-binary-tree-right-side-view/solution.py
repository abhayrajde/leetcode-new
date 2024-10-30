# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do BFS and create map of row and nodes
        # return last node of each row from the map
        if not root:
            return []
        cache = {}
        q = [(root, 0)]

        while q:
            node, row = q.pop(0)
            if row in cache:
                cache[row].append(node)
            else:
                cache[row] = [node]
            if node.left:
                q.append((node.left, row + 1))
            if node.right:
                q.append((node.right, row + 1))
        
        output = []
        for row in cache:
            nodes = cache[row]
            output.append(nodes[-1].val)

        return output

