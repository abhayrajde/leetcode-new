class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = {}
        # self.maxJumps = -1

        def dfs(ind):
            if ind == N - 1:
                return 0
            
            if ind in dp:
                return dp[ind]

            maxJumps = float('-inf')
            for j in range(ind + 1, N):
                if abs(nums[j] - nums[ind]) <= target:
                    maxJumps = max(maxJumps, 1 + dfs(j))

            dp[ind] = maxJumps
            return maxJumps
        
        result = dfs(0)
        return result if result != float('-inf') else -1
        # return selfmaxJumps

# class Solution:
#     def maximumJumps(self, nums: List[int], target: int) -> int:
#         N = len(nums)
#         memo = {}
        
#         def dfs(ind):
#             if ind == N - 1:
#                 return 0
#             if ind in memo:
#                 return memo[ind]
            
#             max_jumps = float('-inf')
#             for j in range(ind + 1, N):
#                 if abs(nums[j] - nums[ind]) <= target:
#                     max_jumps = max(max_jumps, 1 + dfs(j))
            
#             memo[ind] = max_jumps
#             return memo[ind]
        
#         result = dfs(0)
#         return result if result != float('-inf') else -1

