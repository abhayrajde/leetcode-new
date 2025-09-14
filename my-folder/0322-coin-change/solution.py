class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dpmem(ind, target):
            if target == 0: return 0
            if ind == len(coins) or target < 0: return float('inf')

            if (ind, target) in dp: return dp[(ind, target)]

            pick = 1 + dpmem(ind, target - coins[ind])
            notPick = dpmem(ind + 1, target)

            dp[(ind, target)] = min(pick, notPick)
            return dp[(ind, target)]
            
        totCoins = dpmem(0, amount)
        return totCoins if totCoins != float('inf') else -1



        # DP: memoization 
        dp = [[-1] * (amount + 1) for i in range(len(coins))]
        def dpmem(ind, target): # returns -> number of coins  
            # Base Case
            if ind == 0:
                if target % coins[ind] == 0:
                    return target // coins[ind]
                return float('inf')
            
            if dp[ind][target] != -1:
                return dp[ind][target]

            notTake = 0 + dpmem(ind - 1, target)
            
            take = float('inf')
            if coins[ind] <= target:
                take = 1 + dpmem(ind, target - coins[ind])
            
            dp[ind][target] = min(notTake, take)
            
            return dp[ind][target]
        cns = dpmem(len(coins) -1, amount)
        return cns if cns != float('inf') else -1


        # Recursion
        def recursion(ind, target): # returns -> number of coins  
            # Base Case
            if ind == 0:
                if target % coins[ind] == 0:
                    return target // coins[ind]
                return float('inf')

            notTake = 0 + recursion(ind - 1, target)
            
            take = float('inf')
            if coins[ind] <= target:
                take = 1 + recursion(ind, target - coins[ind])
            
            return min(notTake, take)
        # cns = recursion(len(coins) -1, amount)
        # return cns if cns != float('inf') else -1





