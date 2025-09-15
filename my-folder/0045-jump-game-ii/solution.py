class Solution:
    def jump(self, nums: List[int]) -> int:
        # GREEDY - TC: O(N)
        l, r = 0, 0
        res = 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l, r = r + 1, farthest
            res += 1
        return res

        # DP: MEMOIZATION - TOP DOWN - TC: O(N)**2
        # dp = [-1] * len(nums)
        # def dpmem(ind): # no. of jumps
        #     if ind >= len(nums) - 1:
        #         return 0
        #     if nums[ind] == 0:
        #         return float("inf")
        #     if dp[ind] != -1:
        #         return dp[ind]

        #     minJumps = float("inf")
        #     for i in range(1, nums[ind] + 1):
        #         jumps = 1 + dpmem(ind + i)
        #         minJumps = min(minJumps, jumps)
        #     dp[ind] = minJumps
        #     return dp[ind]
        # return dpmem(0)

