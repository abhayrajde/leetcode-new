# This can be done using MaxHeap - TODO
#https://www.youtube.com/watch?v=_HptwlLP8sI

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        hm = {}

        for i in range(len(difficulty)):
            if(difficulty[i] in hm):
                hm[difficulty[i]] = max(hm[difficulty[i]],profit[i])
            else:
                hm[difficulty[i]] = profit[i]
        difficulty = sorted(difficulty)

        #Pre-Processing of Profit
        for i in range(1,len(difficulty)):
            hm[difficulty[i]] = max(hm[difficulty[i]],hm[difficulty[i-1]])

        # hm = sorted(hm)
        totalProfit = 0
        for i in worker:
            left = 0
            right = len(difficulty) - 1
            maxProfit = 0
            while(left <= right):
                mid = (left + right)//2
                if(difficulty[mid] <= i):
                    maxProfit = max(maxProfit, hm[difficulty[mid]])
                    left = mid + 1
                else:
                    right = mid - 1
            totalProfit += maxProfit
        return totalProfit

        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        
