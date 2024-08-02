class Solution(object):
    def minSwaps(self, nums):
        
        total_ones = nums.count(1)
        window_ones, max_window_ones = 0,0
        l = 0
        for r in range(2 * len(nums)):
            if(nums[r % len(nums)] == 1):
                window_ones += 1

            if(r - l + 1 > total_ones):
                window_ones -= nums[l % len(nums)]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)
        return total_ones - max_window_ones
        """
        :type nums: List[int]
        :rtype: int
        """
        
