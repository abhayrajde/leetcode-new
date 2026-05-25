# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.newNode = None
        def dfs(node, parent, right_sibling):
            if not node:
                return

            dfs(node.left, node, node.right)

            if not self.newNode:
                self.newNode = node

            node.left = right_sibling
            node.right = parent
            
        dfs(root, None, None)
        return self.newNode


