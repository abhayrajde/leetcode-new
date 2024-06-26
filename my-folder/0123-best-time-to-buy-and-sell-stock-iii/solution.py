class Solution(object):
    def maxProfit(self, prices):
        def dpmem(ind, canBuy, k):
            #Base Cases
            if(ind == len(prices)):
                return 0
            if(k == 0):
                return 0
            
            if(dp[ind][canBuy][k] != -1):
                return dp[ind][canBuy][k]

            if(canBuy):
                buy = -prices[ind] + dpmem(ind+1, False, k)
                notBuy = 0 + dpmem(ind+1, True, k)
                dp[ind][canBuy][k] = max(buy, notBuy)

            else:
                sell = prices[ind] + dpmem(ind+1, True, k-1)
                notSell = 0 + dpmem(ind+1, False, k)
                dp[ind][canBuy][k] = max(sell, notSell)

            return dp[ind][canBuy][k]

        dp = [[[-1 for i in range(3)] for j in range(2)] for x in range(len(prices))]
        return dpmem(0,1,2)
        # maxProfit = 0
        # for i in range(2):
        #     profit = dpmem(0, True, i)
        #     maxProfit = max(maxProfit, profit)
        # return maxProfit

        """
        :type prices: List[int]
        :rtype: int
        """
        
