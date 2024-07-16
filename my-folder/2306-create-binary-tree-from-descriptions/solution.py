# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        if not descriptions:
            return []

        cannotBeRoot = set()
        potentialRoot = []
        for i in descriptions:
            potentialRoot.append(i[0])
        hm = {}
        for i in range(len(descriptions)):
            if(descriptions[i][0] not in hm):
                hm[descriptions[i][0]] = TreeNode(descriptions[i][0])
            if(descriptions[i][1] not in hm):
                hm[descriptions[i][1]] = TreeNode(descriptions[i][1])

            if(descriptions[i][2]):
                hm[descriptions[i][0]].left = hm[descriptions[i][1]]
            else:
                hm[descriptions[i][0]].right = hm[descriptions[i][1]]
            
            cannotBeRoot.add(descriptions[i][1])
        print(cannotBeRoot)
        for i in range(len(potentialRoot)):
            if(potentialRoot[i] not in cannotBeRoot):
                root = hm[potentialRoot[i]]
        return root

        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        
