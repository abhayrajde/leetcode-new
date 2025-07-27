class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start of each interval
        # from index 1 to end, 
        # if current's start <= prev's end, prev[1] = max(curr's last, prev's last)
        # append prev at the very end
        res = []
        intervals.sort()
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res


