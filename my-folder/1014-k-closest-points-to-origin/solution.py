class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for i in range(len(points)):
            point = points[i]
            dist = (point[0]**2 + point[1]**2)**0.5
            dists.append((i, dist))
        
        dists.sort(key=lambda x:x[1])
        output = []
        for i in range(k):
            index, dist = dists[i]
            output.append(points[index])
        return output
        
