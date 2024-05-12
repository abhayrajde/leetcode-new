class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # DP: Tabulation Approach
        dp = [[0]*n for i in range(m)]
        def dptab():
            for i in range(m):
                for j in range(n):
                    # Base Cases
                    if (obstacleGrid[i][j] == 1):
                        dp[i][j] = 0
                    elif (i == 0 and j == 0):
                        dp[i][j] = 1
                    else:
                        up = left = 0
                        if (i > 0):
                            up = dp[i-1][j]
                        if(j > 0):
                            left = dp[i][j-1]
                        dp[i][j] = up + left
            return(dp[m-1][n-1])
        return(dptab())

        # DP: Memoization Approach
        # dp = [[-1]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        def dpmem(i,j):
            # Step 1: Base Case
            if (obstacleGrid[i][j] == 1):
                return 0

            if(i == 0 and j == 0 ):
                return 1

            if(i < 0 or j < 0):
                return 0
            
            if(dp[i][j] != -1):
                return dp[i][j]
            
            # Step 2: Explore|Do Stuff
            up = dpmem(i-1,j)
            left = dpmem(i,j-1)

            dp[i][j] = up + left
            return(dp[i][j])
        # return(dpmem(m-1,n-1))

        # Recursion Solution
        def recursion(i,j):
            # Step 1: Base Case
            if (i >= 0 and j >= 0 and obstacleGrid[i][j] == 1):
                return 0

            if(i == 0 and j == 0 ):
                return 1

            if(i < 0 or j < 0):
                return 0
            
            # Step 2: Explore|Do Stuff
            up = recursion(i-1,j)
            left = recursion(i,j-1)

            return(up + left)
        # return(recursion(m-1,n-1))

        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
