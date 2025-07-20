class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # Case 1: add new interval - no overlapping, and return res
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # Case 2: add interval and continue - no overlapping
                res.append(intervals[i])
            else: # Overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)
        return res

        # n = len(intervals)
        # i = 0
        # output = []

        # while i < n and intervals[i][1] < newInterval[0]:
        #     output.append(intervals[i])
        #     i += 1
        
        # while i < n and newInterval[1] >= intervals[i][0]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # output.append(newInterval)

        # while i < n:
        #     output.append(intervals[i])
        #     i += 1
        # return output
