class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, rooms = 0, 0 
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                rooms += 1
            else:
                e += 1
                rooms -= 1
            res = max(res, rooms)
        return res 
        # Wrong, failing 1 test case
        # intervals.sort()

        # rooms = 1
        # prevEnd = intervals[0][1]
        # for start, end in intervals[1:]:
        #     if start < prevEnd:
        #         rooms += 1
        #         prevEnd = min(prevEnd, end)
        #     else:
        #         prevEnd = end
        # return rooms
