class Solution(object):
    def minFallingPathSum(self, matrix):
        # Recursion Solution
        def recursion(i,j):
            # Step 1: Base Cases
            if (j < 0 or j >= len(matrix[0])):
                return sys.maxsize
            if (i == 0):
                return matrix[0][j]
            
            # Step 2: Explore all paths
            up = matrix[i][j] + recursion(i-1,j)
            leftDiagonal = matrix[i][j] + recursion(i-1,j-1)
            rightDiagonal = matrix[i][j] + recursion(i-1,j+1)

            # Step 3: Return Minimum Solution
            return min(up, leftDiagonal, rightDiagonal)

        # COMMON DRIVER CODE
        #  cost = sys.maxsize
        # i = len(matrix)-1
        # for j in range(len(matrix[0])):
        #     cost = min(cost, recursion(i,j))
        # return cost

        # DP: Memoization Approach
        # dp = [[sys.maxsize]*len(matrix[0]) for i in range(len(matrix))]
        def dpmem(i,j):
            # Step 1: Base Cases
            if (j < 0 or j >= len(matrix[0])):
                return sys.maxsize
            if (i == 0):
                return matrix[0][j]
            if(dp[i][j] != sys.maxsize):
                return dp[i][j]
            
            # Step 2: Explore all paths
            up = matrix[i][j] + dpmem(i-1,j)
            leftDiagonal = matrix[i][j] + dpmem(i-1,j-1)
            rightDiagonal = matrix[i][j] + dpmem(i-1,j+1)

            dp[i][j] = min(up, leftDiagonal, rightDiagonal)
            return(dp[i][j])
        
        # COMMON DRIVER CODE
        # cost = sys.maxsize
        # i = len(matrix)-1
        # for j in range(len(matrix[0])):
        #     cost = min(cost, dpmem(i,j))
        # return cost

        # DP: Tabulation Approach
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
        def dptab():
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    # Step 1: Base Cases
                    if(i == 0):
                        dp[i][j] = matrix[i][j]
                    else:
                        leftDiagonal = rightDiagonal = sys.maxsize
                        up = matrix[i][j] + dp[i-1][j]
                        if(j-1 >= 0):
                            leftDiagonal = matrix[i][j] + dp[i-1][j-1]
                        if(j+1 < len(matrix[0])):
                            rightDiagonal = matrix[i][j] + dp[i-1][j+1]
                        dp[i][j] = min(up,leftDiagonal,rightDiagonal)
            return min(dp[len(matrix)-1])
        return(dptab())

        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
