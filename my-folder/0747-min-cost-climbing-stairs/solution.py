class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #DP: Memoization
        dp = [-1] * (len(cost) + 1) 
        def dpmem(ind):
            if ind < 0: 
                return 0

            if dp[ind] != -1:
                return dp[ind]

            currCost = 0 if ind == len(cost) else cost[ind]
            dp[ind] = currCost + min(dpmem(ind - 1), dpmem(ind - 2))
            return dp[ind]


        # Recursion
        def recursion(ind):
            if ind < 0:
                return 0

            currCost = 0 if ind == len(cost) else cost[ind]
            
            option1 = currCost + recursion(ind - 1)
            option2 = currCost + recursion(ind - 2)           
            return min(option1, option2)
        
        return min(dpmem(len(cost)), dpmem(len(cost)-1)) 
        
        
