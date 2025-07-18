class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP: Memoizatation
        dp = [-1] * len(nums)
        def dpmem(ind):
            if ind < 0:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + dpmem(ind - 2)
            notPick = dpmem(ind - 1)

            dp[ind] = max(pick, notPick)

            return dp[ind]

        # Recursion
        def recursion(ind):
            if ind < 0:
                return 0
            
            pick = nums[ind] + recursion(ind - 2)
            notPick = recursion(ind - 1)

            return max(pick, notPick)
        return dpmem(len(nums) - 1)
