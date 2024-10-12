class Solution(object):
    def minGroups(self, intervals):
        dict1 = defaultdict(list)
        closeTime = [] # (closeTIme, GroupNumber)
        intervals = sorted(intervals)
        groupNumber = 1
        for st,end in intervals:
            if closeTime and closeTime[0][0] < st:
                temp = heapq.heappop(closeTime)
                dict1[temp[1]].append([st,end])
                heapq.heappush(closeTime, (end, temp[1]))
            else:
                dict1[groupNumber].append([st,end])
                heapq.heappush(closeTime, (end, groupNumber))
                groupNumber += 1
        return len(dict1.keys())



        
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

