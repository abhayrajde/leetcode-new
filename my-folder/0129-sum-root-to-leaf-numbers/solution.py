# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
                return root.val

        def traverse(node, s):
            if node.left == None and node.right == None:
                return s + str(node.val)
            l = ''
            if node.left:
                l = traverse(node.left, s + str(node.val))
            r = ''
            if node.right:
                r = traverse(node.right, s + str(node.val))
            
            return int('0' if l == '' else l) + int('0' if r == '' else r)


        return traverse(root, '')
