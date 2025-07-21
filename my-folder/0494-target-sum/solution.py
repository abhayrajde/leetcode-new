class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DP TABULATION - BOTTOM UP APPROACH
        dp =  [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # (0 elements, 0 sum) -> 1 way
                     # 1 way to sum to zero with first 0 elements

        for i in range(len(nums)):
            for currSum, count in dp[i].items():
                dp[i + 1][currSum + nums[i]] += count
                dp[i + 1][currSum - nums[i]] += count
        return dp[len(nums)][target]


        # DP MEMOIZATION - TOP DOWN APPROACH
        dp = {} # (index, currSum) => num of ways

        def dpmem(ind, currSum):
            # Base Cases
            if ind >= len(nums):
                return 1 if currSum == target else 0

            if (ind, currSum) in dp:
                return dp[(ind, currSum)]

            addC = dpmem(ind + 1, currSum + nums[ind])
            subC = dpmem(ind + 1, currSum - nums[ind])

            dp[(ind, currSum)] = addC + subC
            return dp[(ind, currSum)]

        return dpmem(0,0)

        # RECURSION - BRUTE FORCE APPROACH
        def recursion(ind, currSum):
            # Base Cases
            if ind >= len(nums):
                if currSum == target:
                    return 1
                return 0

            addC = recursion(ind + 1, currSum + nums[ind])
            subC = recursion(ind + 1, currSum - nums[ind])

            return addC + subC
        # return recursion(0,0)
