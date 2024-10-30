class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start of each interval
        # from index 1 to end, 
        # if current's start <= prev's end, prev[1] = max(curr's last, prev's last)
        # append prev at the very end
        output = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                output.append(prev)
                prev = interval
        output.append(prev)
        return output
