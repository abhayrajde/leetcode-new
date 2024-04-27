class Solution(object):
    def fib(self, n):
        # DP - Tabulation Solution - Bottom Up Approach
        # TC - O(N), SC = O(N) 
        if (n <= 1):
            return n
        
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # # DP - Memoization Solution - Top Down Approach
        # # TC - O(N), SC - O(2N) 
        # # Step 1
        # dp = [-1]*(n+1)
        # print(dp)

        # def fibonacci(n):
        #     if (n <= 1):
        #         return n

        #     # Step 2
        #     if(dp[n] != -1):
        #         return dp[n]

        #     #Step 3
        #     dp[n] = (fibonacci(n-1) + fibonacci(n-2))
        #     return dp[n]
        # return(fibonacci(n))


        # # Recursive Solution
        # def fibonacci(n):
        #     if (n <= 1):
        #         return n
        #     return(fibonacci(n-1) + fibonacci(n-2))
        # return(fibonacci(n))
        """
        :type n: int
        :rtype: int
        """
        
