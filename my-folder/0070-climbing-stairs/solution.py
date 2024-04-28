class Solution(object):
    def climbStairs(self, n):
        dp = [-1]*(n+1)
        # Dp: Tabulation - Bottom Up Approach
        def dptab(n):
            dp[0] = dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return(dp[n])

        # DP: Memoization - Top Down Approach
        def dpmem(n):
            if(n <= 1):
                return 1

            if(dp[n] != -1):
                return dp[n]

            dp[n] = dpmem(n-1) + dpmem(n-2)
            return(dp[n])

        # Recursion solution
        def recursion(n):
            if(n <= 1):
                return 1
            return(recursion(n-1)+recursion(n-2))

        return(dptab(n))
        """
        :type n: int
        :rtype: int
        """
        
