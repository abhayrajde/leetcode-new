class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
        return max_profit

        """
        :type prices: List[int]
        :rtype: int
        """
        
