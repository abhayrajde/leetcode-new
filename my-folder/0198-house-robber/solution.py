class Solution(object):
    def rob(self, nums):

        # Recursion Solution

        def rec(n):
            if (n == 0):
                return nums[n]
                
            if (n < 0):
                return 0

            pick = nums[n] + rec(n-2)
            non_pick = 0 + rec(n-1)

            return(max(pick, non_pick))


        # DP: Memoization Approach (Top-Down Approach)
        # dp = [-1]*len(nums)
        def dpmem(n):
            if (n == 0):
                return nums[n]
                
            if (n < 0):
                return 0

            if (dp[n] > -1):
                return dp[n]

            pick = nums[n] + dpmem(n-2)
            non_pick = 0 + dpmem(n-1)

            dp[n] = max(pick, non_pick)
            return (dp[n])

        # DP: Tabulation Approach (Bottom-Up Approach)
        dp = [-1]*len(nums)
        def dptab(n):
            dp[0] = nums[0]
            neg = 0
            for i in range(1,n+1):
                pick = nums[i]
                if (i > 1):
                    pick += dp[i-2]
                
                non_pick = 0 + dp[i-1]

                dp[i] = max(pick, non_pick)
            return dp[n]

        # DP: Tabulation Approach -> Space Optimization
        # 1,     2,      3,  4,5,6,7
        # ^      ^       ^
        # |      |       |
        #prev2  prev    curr
        def dptabso(n):
            prev = nums[0]
            prev2 = 0
            for i in range(1,n+1):
                pick = nums[i]
                if (i > 1):
                    pick += prev2
                
                non_pick = 0 + prev

                curr = max(pick, non_pick)
                prev2 = prev
                prev = curr
            return prev

        return(dptabso(len(nums)-1))
        """
        :type nums: List[int]
        :rtype: int
        """
        
