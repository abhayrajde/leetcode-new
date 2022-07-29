class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1] *(amount+1)
        dp[amount] = 0
        for i in range(amount-1,-1,-1):
            for j in range(len(coins)):
                if(i + coins[j] <=amount):
                    dp[i] = min(dp[i],1+dp[i+coins[j]])
        if(dp[0]>amount):
            return(-1)
        else:
            return(dp[0])
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
