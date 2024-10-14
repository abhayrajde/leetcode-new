class Solution(object):
    def maxKelements(self, nums, k):
        max_heap = []
        score = 0
        for i in range(len(nums)):
            heapq.heappush(max_heap, -nums[i])
        for j in range(k):
            ele_val = heapq.heappop(max_heap)
            ele_val *= -1
            score += ele_val
            heapq.heappush(max_heap, -(ele_val)//3)
        return score

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
