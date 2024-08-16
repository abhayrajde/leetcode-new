class Solution(object):
    def maxDistance(self, arrays):
        minEl = arrays[0][0]
        maxEl = arrays[0][-1]
        res = -float("inf")
        for i in range(1, len(arrays)):
            diff1 = abs(maxEl - arrays[i][0])
            diff2 = abs(minEl - arrays[i][-1])

            res = max(res, diff1, diff2)

            minEl = min(minEl, arrays[i][0])
            maxEl = max(maxEl, arrays[i][-1])
        return res
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
