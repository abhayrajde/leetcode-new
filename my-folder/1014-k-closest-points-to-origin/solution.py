class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i in range(len(points)):
            x, y = points[i]
            distance = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(minHeap, (distance, points[i]))
        
        res = []
        for i in range(k):
            distance, pos = heapq.heappop(minHeap)
            res.append(pos)
        return res



        # dists = []
        # for i in range(len(points)):
        #     point = points[i]
        #     dist = (point[0]**2 + point[1]**2)**0.5
        #     dists.append((i, dist))
        
        # dists.sort(key=lambda x:x[1])
        # output = []
        # for i in range(k):
        #     index, dist = dists[i]
        #     output.append(points[index])
        # return output
        
