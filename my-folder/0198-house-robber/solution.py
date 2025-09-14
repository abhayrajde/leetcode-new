class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP - Tabulation - Space Optimized
        prev, prev2 = nums[0], 0
        for i in range(1, len(nums)):

            pick = nums[i] + prev2
            notPick = prev
            
            curr = max(pick, notPick)
            
            prev2 = prev
            prev = curr
        return prev

        # DP - Tabulation
        # TC - O(N) | SC - O(N)
        # Here O(N) stack space is removed
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            pick = nums[i]
            if i > 1: 
                pick += dp[i - 2]
            notPick = dp[i - 1]
            dp[i] = max(pick, notPick)
        return dp[-1]

        # DP - Memoization
        # TC - O(N) | SC - O(N) + O(N) - [1 O(N) is a stack space]
        dp = [-1] * len(nums)
        def dpmem(ind):
            # Base Conditions
            if ind == 0: return nums[ind]
            if ind < 0: return 0
            if dp[ind] != -1: return dp[ind]
            
            pick = nums[ind] + dpmem(ind - 2)
            notPick = dpmem(ind - 1)

            dp[ind] = max(pick, notPick)
            return dp[ind]
        return dpmem(len(nums) - 1)

        # Brute Force
        def recursion(ind):
            # Base Conditions
            if ind == 0: return nums[ind]
            if ind < 0: return 0
            
            pick = nums[ind] + recursion(ind - 2)
            notPick = recursion(ind - 1)

            return max(pick, notPick)
        return recursion(len(nums) - 1)
