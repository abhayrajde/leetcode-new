class Solution(object):
    def rob(self, nums):

        # Recursion Solution
        def rec(ind, numList):
            # Base Cases
            if(ind == 0):
                return numList[0]
            
            if(ind < 0):
                return 0
            
            pick = numList[ind] + rec(ind-2, numList)
            non_pick = 0 + rec(ind-1, numList)

            return max(pick, non_pick)

        # DP: Memoization Approach (Top-Down Approach)
        def dpmem(ind,numList):
            # Base Cases
            if(ind == 0):
                return numList[0]

            if(ind < 0):
                return 0

            if(dp[ind] != -1):
                return dp[ind]

            pick = numList[ind] + dpmem(ind - 2, numList)
            notPick = 0 + dpmem(ind - 1, numList)

            dp[ind] = max(pick,notPick)
            return dp[ind]

        # DP: Tabulation Approach (Bottom-Up Approach)
        def dptab(ind, numList):
            # Base Case
            dp[0] = numList[0]
            neg = 0

            for i in range(1, len(numList)):
                pick = numList[i]
                if(i-2 > -1):
                    pick += dp[i-2]
                notPick = 0 + dp[i-1]
                dp[i] = max(pick, notPick)
            return dp[ind]

        # DP: Tabulation Approach -> Space Optimization (Bottom-Up Approach)
        def dptabso(ind, numList):
            # Base Case
            prev = numList[0]
            prev2 = 0

            for i in range(1, len(numList)):
                pick = numList[i]
                if(i-2 > -1):
                    pick += prev2
                notPick = 0 + prev
                curi = max(pick, notPick)
                prev2 = prev
                prev = curi
            return prev

        # Driver Code
        ind = len(nums)-2
        if(ind < 0):
            return nums[0]

        dp = [-1]*(len(nums)-1)
        excludeFirst = dptabso(ind,nums[1:])
        
        dp = [-1]*(len(nums)-1)
        excludeLast = dptabso(ind,nums[:len(nums)-1])
        
        return max(excludeFirst, excludeLast)
        """
        :type nums: List[int]
        :rtype: int
        """
        
