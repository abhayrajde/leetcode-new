import sys
class Solution(object):
    def minPathSum(self, grid):

        # Recursion Solution
        def recursion(i,j):
            # Step 1: Base Cases
            if (i == 0 and j == 0):
                return grid[i][j]
            if (i < 0 or j < 0):
                return sys.maxsize
            
            # Step 2: Explore all paths and find minimum
            cost = 0
            up = grid[i][j] + recursion(i-1,j)
            left = grid[i][j] + recursion(i,j-1)

            # Step 3: Return minimum Path
            cost += min(up,left)

            return(cost)
        # return(recursion(len(grid)-1, len(grid[0])-1))

        # DP: Memoization Approach
        dp = [[sys.maxsize]*len(grid[0]) for i in range(len(grid))]
        def dpmem(i,j):
            # Step 1: Base Cases
            if (i == 0 and j == 0):
                return grid[i][j]
            if (i < 0 or j < 0):
                return sys.maxsize
            if(dp[i][j] != sys.maxsize):
                return dp[i][j]
            
            # Step 2: Explore all paths and find minimum
            up = grid[i][j] + dpmem(i-1,j)
            left = grid[i][j] + dpmem(i,j-1)

            # Step 3: Return minimum Path
            dp[i][j] = min(up,left)

            return(dp[i][j])
        # return(dpmem(len(grid)-1, len(grid[0])-1))

        #DP: Tabulation Approach
        dp = [[0]*len(grid[0]) for i in range(len(grid))]
        def dptab():
            # Base Cases
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if (i == 0 and j == 0):
                        dp[i][j] = grid[i][j]
                    else:
                        up = left = sys.maxsize
                        if(i > 0):
                            up = grid[i][j] + dp[i-1][j]
                        if(j > 0):
                            left = grid[i][j] + dp[i][j-1]
                        dp[i][j] = min(up,left)
            return(dp[len(grid)-1][len(grid[0])-1])
        return(dptab())

            
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
