class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #DP Memoization - Top Down Approach
        dp = [[-1]*2 for i in range(len(prices))]

        def dpmem(ind: int, buy: bool):
            # Base Cases
            if ind >= len(prices):
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            if buy:
                purchase = -prices[ind] + dpmem(ind + 1, False)
                notPurchase = dpmem(ind + 1, True)
                dp[ind][buy] = max(purchase, notPurchase)
                return dp[ind][buy]
            else:
                sell = prices[ind] + dpmem(ind + 2, True)
                notSell = dpmem(ind + 1, False)
                dp[ind][buy] = max(sell, notSell)
                return dp[ind][buy]
        return dpmem(0,True)
        
        # Recursion
        def recursion(ind: int, buy: bool):
            # Base Cases
            if ind >= len(prices):
                return 0
            if buy:
                purchase = -prices[ind] + recursion(ind + 1, False)
                notPurchase = recursion(ind + 1, True)
                return max(purchase, notPurchase)
            else:
                sell = prices[ind] + recursion(ind + 2, True)
                notSell = recursion(ind + 1, False)
                return max(sell, notSell)
        # return recursion(0,True)
