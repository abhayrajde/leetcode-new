class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        return res
        # BRUTE FORCE - N^2
        # for i in range(len(gas)):
        #     j = i+1
        #     currFuel = gas[i] - cost[i]
        #     while j != i:
        #         # Base Case
        #         if currFuel < 0:
        #             break

        #         # circular logic
        #         if j == len(gas):
        #             j = 0
        #             if j == i:
        #                 break
                    
        #         currFuel = currFuel + gas[j] - cost[j]
        #         j += 1

        #     if currFuel >= 0:
        #         return i 
        # return -1

        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
