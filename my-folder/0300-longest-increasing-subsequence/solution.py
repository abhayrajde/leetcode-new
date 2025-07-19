class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP: Memoization
        dp = [[-1] * (len(nums)+1) for _ in range(len(nums)+1)]

        def dpmem(ind, prevInd):
            if ind >= len(nums):
                return 0
            if dp[ind][prevInd] != -1:
                return dp[ind][prevInd]

            notTake = dpmem(ind + 1, prevInd)
            take = 0
            if prevInd == -1 or nums[ind] > nums[prevInd]:
                take = 1 + dpmem(ind + 1, ind)
            dp[ind][prevInd] = max(take, notTake)
            return dp[ind][prevInd]

        # def dpmem(ind, prevInd): #Return -> count of elements
        #     if ind < 0:
        #         return 0
            
        #     if dp[ind][prevInd] != -1:
        #         return dp[ind][prevInd]

        #     notTake = 0 + dpmem(ind - 1, prevInd)
        #     take = -float("inf")
        #     if nums[ind] < nums[prevInd]:
        #         take = 1 + dpmem(ind - 1, ind)

        #     dp[ind][prevInd] = max(take, notTake)
        #     return dp[ind][prevInd]
        
        return dpmem(0, -1)

        # Recursion
        def recursion(ind, prevEl): #Return -> count of elements
            if ind < 0:
                return 0

            notTake = 0 + recursion(ind - 1, prevEl)
            take = -float("inf")
            if nums[ind] < prevEl:
                take = 1 + recursion(ind - 1, nums[ind])
            return max(take, notTake)

        # return recursion(len(nums)-1, float('inf'))

