class Solution(object):
    def uniquePaths(self, m, n):
        # DP: Tabulation Approach
        dp = [[0]*n for i in range (m)]
        def dptab():
            for i in range(m):
                for j in range(n):
                    # Base Case
                    if (i == 0 and j == 0):
                        dp[i][j] = 1
                    else:
                        up = left = 0
                        if (j > 0):
                            up = dp[i][j-1]
                        if (i > 0):
                            left = dp[i-1][j]
                        dp[i][j] = up + left
            return(dp[m-1][n-1])    
        return dptab()

        # DP: Memoization Approach
        # dp = [[-1]*n for i in range(m)]
        def dpmem(i,j):
            # i -> row, j -> column
            # Step 1: Base Cases
            if (i == 0 and j == 0):
                return 1
            if(i < 0 or j < 0):
                return 0
            if(dp[i][j] != -1):
                return(dp[i][j])

            # Step 2: Explore by the rules
            up = dpmem(i-1,j)
            left = dpmem(i,j-1)

            #Step 3: Add all the solutions
            dp[i][j] = up + left
            return (dp[i][j])
        # return dpmem(m-1,n-1)

        # Recursion Solution
        def recursion(i,j):
            # i -> row, j -> column
            # Step 1: Base Cases
            if (i == 0 and j == 0):
                return 1
            if(i < 0 or j < 0):
                return 0

            # Step 2: Explore by the rules
            up = recursion(i-1,j)
            left = recursion(i,j-1)

            #Step 3: Add all the solutions
            return (up + left)
        # return (recursion(m-1,n-1))


        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
