class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minH = []

        res = {}
        i = 0

        for q in sorted(queries):
            # Add all possible ranges for q to minHeap
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minH, (r - l + 1, r))
                i += 1
            
            # Remove all out of range intervals for q before proceeding with answer
            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            res[q] = minH[0][0] if minH else -1
        return [res[q] for q in queries]

