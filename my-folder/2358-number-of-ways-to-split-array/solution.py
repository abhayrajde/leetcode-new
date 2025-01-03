class Solution(object):
    def waysToSplitArray(self, nums):
        tot = sum(nums)
        curr = 0 
        count = 0
        for i in range(len(nums)-1):
            curr += nums[i]
            if curr >= (tot - curr):
                count += 1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        
