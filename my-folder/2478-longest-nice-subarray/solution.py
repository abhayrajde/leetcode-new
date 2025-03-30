class Solution(object):
    def longestNiceSubarray(self, nums):
        res = 0
        curr = 0
        l = 0
        for r in range(len(nums)):
            while curr & nums[r]:
                curr = curr ^ nums[l]
                l += 1
            curr = curr | nums[r]
            res = max(res, r-l+1)
        return res

        """
        :type nums: List[int]
        :rtype: int
        """
        
