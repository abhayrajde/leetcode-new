class Solution(object):
    def rob(self, nums):

        dp = [-1]*len(nums)
        def rec(n):
            if (n == 0):
                return nums[n]
                
            if (n < 0):
                return 0

            if (dp[n] > -1):
                return dp[n]

            pick = nums[n] + rec(n-2)
            non_pick = 0 + rec(n-1)

            dp[n] = max(pick, non_pick)
            return (dp[n])

        return(rec(len(nums)-1))
        """
        :type nums: List[int]
        :rtype: int
        """
        
