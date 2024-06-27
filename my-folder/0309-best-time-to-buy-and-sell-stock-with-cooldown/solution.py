class Solution(object):
    def maxProfit(self, prices):

        def dpmem(ind,canBuy):
            # Base Cases
            if(ind >= len(prices)):
                return 0
            if(dp[ind][canBuy] != -1):
                return dp[ind][canBuy]

            if(canBuy):
                buy = -prices[ind] + dpmem(ind+1, False)
                notBuy = 0 + dpmem(ind+1, True)
                dp[ind][canBuy] = max(buy, notBuy)
            else:
                sell = prices[ind] + dpmem(ind+2, True)
                notSell = 0 + dpmem(ind+1, False)
                dp[ind][canBuy] = max(sell, notSell)
            
            return dp[ind][canBuy]
        #Driver's Code
        dp = [[-1 for i in range(2)] for j in range(len(prices))]
        return(dpmem(0,1))
        """
        :type prices: List[int]
        :rtype: int
        """
        
