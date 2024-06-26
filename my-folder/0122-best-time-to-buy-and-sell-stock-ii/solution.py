class Solution(object):
    def maxProfit(self, prices):
        # DP: Memoization: Top Down Approach
        def dpmem(ind, canBuy):
            #Base Case
            if(ind == len(prices)):
                return 0
            if(dp[ind][canBuy] != -1):
                return dp[ind][canBuy]

            if(canBuy):
                buy = -prices[ind] + dpmem(ind+1,False)
                notBuy = 0 + dpmem(ind+1, True)
                profit = max(buy, notBuy)
                # dp[ind][canBuy] = max(buy, notBuy)
                # return dp[ind][canBuy]
            else:
                sell = prices[ind] + dpmem(ind+1, True)
                notSell = 0 + dpmem(ind+1, False)
                profit = max(sell, notSell)
                # dp[ind][canBuy] = max(sell, notSell)
                # return dp[ind][canBuy]
            dp[ind][canBuy] = profit
            return dp[ind][canBuy]

        #Driver's Code:
        dp = [[-1 for i in range(2)] for j in range(len(prices))]
        return(dpmem(0,True))

        # Recursion solution:
        def recursion(ind, canBuy):
            #Base Case
            if(ind == len(prices)):
                return 0
            if(canBuy):
                buy = -prices[ind] + recursion(ind+1,False)
                notBuy = 0 + recursion(ind+1, True)
                return max(buy, notBuy)
            else:
                sell = prices[ind] + recursion(ind+1, True)
                notSell = 0 + recursion(ind+1, False)
                return max(sell, notSell)
        # return(recursion(0,True))


        # total_profit = 0
        # buy = prices[0]
        # for i in range(1,len(prices)):
        #     profit = prices[i]-buy
        #     if (profit > 0):
        #         total_profit+=profit
        #         buy = prices[i]
        #     else:
        #         buy = prices[i]
        # return total_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        
