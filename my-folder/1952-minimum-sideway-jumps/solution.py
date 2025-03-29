class Solution(object):
    def minSideJumps(self, obstacles):
        dp = [[-1 for i in range(len(obstacles))] for j in range(4)]

        # Memoization
        def recursionMem(currPos, currLane):
            # Base Case
            if currPos == len(obstacles)-1:
                return 0

            if dp[currLane][currPos] != -1:
                return dp[currLane][currPos]

            if obstacles[currPos+1] != currLane:
                return recursionMem(currPos + 1, currLane)
            else:
                minJumps = float('inf')
                for i in range(1,4):
                    if currLane != i and obstacles[currPos] != i:
                        minJumps = min(minJumps, recursionMem(currPos, i) + 1)

                dp[currLane][currPos] = minJumps
                return dp[currLane][currPos]
        
        def recursionTab():
            n = len(obstacles) - 1
            for lane in range(4):
                dp[lane][n] = 0

            for currPos in range(n-1, -1, -1):
                for currLane in range(1, 4):
                    if obstacles[currPos + 1] != currLane:
                        dp[currLane][currPos] = dp[currLane][currPos+1]
                    else:
                        ans = float('inf')
                        for i in range(1,4):
                            if(currLane != i and obstacles[currPos] != i):
                                ans = min(ans, 1 + dp[i][currPos+1])
                        dp[currLane][currPos] = ans
            return min(dp[2][0], min(dp[1][0]+1, dp[3][0]+1))

        return recursionTab()
        # return recursionMem(0,2)
        """
        :type obstacles: List[int]
        :rtype: int
        """
        
