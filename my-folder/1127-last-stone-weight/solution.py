class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for st in stones:
            heapq.heappush(maxHeap, -st)
        
        while len(maxHeap) > 1:
            y = - heapq.heappop(maxHeap)
            x = - heapq.heappop(maxHeap)
            if y > x:
                heapq.heappush(maxHeap, -(y - x))
        return -maxHeap[0] if maxHeap else 0
            

