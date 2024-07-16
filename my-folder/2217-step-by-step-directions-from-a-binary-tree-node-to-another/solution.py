# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        def dfs(node, path,target):
            if not node:
                return ""
            
            if node.val == target:
                return path
            
            path.append("L")
            res = dfs(node.left,path,target)
            if res: 
                return res

            path.pop()
            path.append("R")
            res = dfs(node.right,path,target)
            if res:
                return res
            
            path.pop()
            return ""

        startPath = dfs(root,[],startValue)
        destPath = dfs(root,[],destValue)
        i = 0
        while i < min(len(startPath),len(destPath)):
            if startPath[i] != destPath[i]:
                break
            i += 1
        res = ["U"] * len(startPath[i:]) + destPath[i:]

        return "".join(res)
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
