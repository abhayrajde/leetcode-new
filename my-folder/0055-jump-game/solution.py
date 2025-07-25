class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy solution
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

        # #DP: Memoization - TLE
        # dp = defaultdict(bool)
        # def recursion(ind): 
        #     if ind == len(nums)-1:
        #         return True
        #     if ind > len(nums)-1 or nums[ind] == 0:
        #         return False

        #     if ind in dp:
        #         return dp[ind]

        #     for i in range(1, nums[ind] + 1):
        #         if recursion(ind + i):
        #             dp[ind] = True
        #             return dp[ind]
        #     dp[ind] = False
        #     return dp[ind]

        # return recursion(0)

        # GOOD, BAD, UNKNOWN = 1, 0, -1
        # memo = [UNKNOWN] * len(nums)
        # memo[-1] = GOOD
        # for i in range(len(nums) - 2, -1, -1):
        #     furthest_jump = min(i + nums[i], len(nums) - 1)
        #     for j in range(i + 1, furthest_jump + 1):
        #         if memo[j] == GOOD:
        #             memo[i] = GOOD
        #             break
        # return memo[0] == GOOD
