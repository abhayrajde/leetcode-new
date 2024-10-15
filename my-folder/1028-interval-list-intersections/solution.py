class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i, j = 0, 0
        res = []
        while(i < len(firstList) and j < len(secondList)):
            a = firstList[i]
            b = secondList[j]

            start = max(a[0],b[0])
            end = min(a[1], b[1])

            if start <= end:
                res.append([start, end])

            if a[1] < b[1]:
                i += 1
            else:
                j += 1
        return res



        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
