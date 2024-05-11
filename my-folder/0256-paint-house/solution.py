# ** colors and its code **
# red = 0
# blue = 1
# green = 2
import sys
class Solution(object):
    def minCost(self, costs):
        dp = [[sys.maxsize]*4 for i in range (len(costs))]
        # Recursion solution
        def dpmem(h,c):
            # h, c -> house, color
            if(h == 0):
                minCost = sys.maxsize
                for i in range(3):
                    if (i != c):
                        minCost = min(minCost, costs[h][i])
                return minCost
                
            if (dp[h][c] != sys.maxsize):
                return dp[h][c]

            minCost = sys.maxsize
            for i in range(3):
                if (i != c):
                    cost = costs[h][i] + dpmem(h-1,i)
                    minCost = min(minCost, cost)

            dp[h][c] = minCost
            return minCost

        def recursion(house,lastColor):
            if (house == 0):
                minCost = sys.maxsize
                for color in range(3):
                    if (color != lastColor):
                        minCost = min(minCost, costs[0][color])
                return minCost

            if(dp[house][lastColor] != sys.maxsize):
                return dp[house][lastColor]
            
            minCost = sys.maxsize

            for color in range(3):
                if(color != lastColor):
                    cost = costs[house][color] + recursion(house-1,color)
                    minCost = min(minCost,cost)
                    
            dp[house][lastColor] = minCost
            print(dp)
            return minCost

        return dpmem(len(costs)-1, 3)


        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
