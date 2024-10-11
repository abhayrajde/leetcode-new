# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        if root.left == None and root.right == None:
            return [[root.val]]
        def traverse(node, track, level, vLevel):
            if node.left == None and node.right == None:
                if level in track:
                    track[level].append((node.val, vLevel))
                else:
                    track[level] = [(node.val, vLevel)]
                return track
            if node.left:
                track = traverse(node.left, track, level - 1, vLevel + 1)
            if level in track:
                track[level].append((node.val, vLevel))
            else:
                track[level] = [(node.val, vLevel)]
            if node.right:
                track = traverse(node.right, track, level + 1, vLevel + 1)
            return track
        track = {}
        traverse(root, track, 0, 0)
        output = []
        for key in sorted(dict(track.items())):
            value = track[key]
            output.append([x[0] for x in sorted(value, key=lambda x: x[1])])
        return output
        
            
        
        
