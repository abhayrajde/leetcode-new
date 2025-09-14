# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lowestStack = []
        highestStack = []
        
        def populateLowest(node):
            if not node: return

            lowestStack.append(node)
            populateLowest(node.left)
            
        def populateHighest(node):
            if not node: return

            highestStack.append(node)
            populateHighest(node.right)
        
        populateLowest(root)
        populateHighest(root)

        def getLowest():
            leftNode = lowestStack.pop()
            if leftNode.right:
                populateLowest(leftNode.right)
            return leftNode

        def getHighest():
            rightNode = highestStack.pop()
            if rightNode.left:
                populateHighest(rightNode.left)
            return rightNode
        
        def findTarget(leftNode, rightNode):
            if leftNode == rightNode: return False

            if leftNode.val + rightNode.val == k:
                return True
            
            elif leftNode.val + rightNode.val < k:
                leftNode = getLowest()
            else:
                rightNode = getHighest()
            return findTarget(leftNode, rightNode)

        leftNode = getLowest()
        rightNode = getHighest()

        return findTarget(leftNode, rightNode)

        # HOW IS THIS EASY????
        


