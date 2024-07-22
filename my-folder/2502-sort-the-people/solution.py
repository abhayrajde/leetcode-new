class Solution(object):
    def sortPeople(self, names, heights):
        hAndInd = []
        for i,hei in enumerate(heights):
            hAndInd.append((hei,i))
        hAndInd = sorted(hAndInd, key = lambda x: x[0], reverse = True)
        res = []
        for i in hAndInd:
            res.append(names[i[1]])
        return res
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
