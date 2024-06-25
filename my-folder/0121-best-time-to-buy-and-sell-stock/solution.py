class Solution(object):
    def maxProfit(self, prices):
        minBuy = prices[0]

        maxProfit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - minBuy
            maxProfit = max(profit, maxProfit)

            minBuy = min(minBuy, prices[i])
        return maxProfit
        """
        :type prices: List[int]
        :rtype: int
        """
        
