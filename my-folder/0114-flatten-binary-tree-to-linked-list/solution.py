class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node) -> Optional[TreeNode]:
            if not node:
                return None
            
            # Base case: a leaf node is its own tail
            if not node.left and not node.right:
                return node
            
            # Recursively flatten left and right subtrees and get their tails
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            
            # If there is a left subtree, we need to weave it into the right side
            if left_tail:
                # Save the original right child
                temp_right = node.right
                
                # Move the left subtree to the right
                node.right = node.left
                node.left = None
                
                # Connect the tail of the old left subtree to the old right subtree
                left_tail.right = temp_right
            
            # Return the correct tail of this entire flattened subtree
            # Priority: right_tail -> left_tail -> current node
            return right_tail if right_tail else left_tail

        dfs(root)
