class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]

        highest = 0

        for pr in prices[1:]:
            if pr >= buy:
                highest = max(highest, pr - buy)
            else:
                buy = pr
        return highest











        buy = prices[0]
        sell = -1
        highest = 0

        for price in prices[1:]:
            if price < buy:
                sell = -1
                buy = price
            else:
                sell = max(sell, price)
                highest = max(sell - buy, highest)
        return highest
