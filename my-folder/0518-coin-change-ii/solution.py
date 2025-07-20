class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #DP Memoization - Top Down Approach
        #TC: O(N*K) | 
        dp = [[-1]*(amount+1) for i in range(len(coins))]
        def dpmem(ind, target):
            # Base Case
            if target == 0:
                return 1
            if ind >= len(coins) or target < 0:
                return 0
            
            if dp[ind][target] != -1:
                return dp[ind][target]

            notPick = dpmem(ind + 1, target)
            pick = dpmem(ind, target - coins[ind])

            dp[ind][target] = pick + notPick
            return dp[ind][target]
        return dpmem(0, amount)
        
        def recursion(ind, target):
            # Base Case
            if target == 0:
                return 1
            if ind >= len(coins) or target < 0:
                return 0

            notPick = recursion(ind + 1, target)
            pick = recursion(ind, target - coins[ind])

            return pick + notPick
        # return recursion(0, amount)

