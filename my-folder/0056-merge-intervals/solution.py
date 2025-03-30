class Solution(object):
    def merge(self, intervals):
        result = []
        intervals = sorted(intervals, key = lambda x:x[0])

        prev = intervals[0]
        
        for i in range(1,len(intervals)):
            curr = intervals[i]
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                result.append(prev)
                prev = curr
        result.append(prev)
        return result

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
