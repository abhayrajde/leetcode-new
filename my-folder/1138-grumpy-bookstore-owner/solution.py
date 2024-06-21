#https://www.youtube.com/watch?v=kCxCE0_66vM
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        idealSatisfaction = 0
        for i in range(len(customers)):
            if(grumpy[i] == 0):
                idealSatisfaction += customers[i]
        
        bonusSatisfaction = 0
        for i in range(minutes):
            if (grumpy[i] == 1):
                bonusSatisfaction += customers[i]
        
        maxBonus = bonusSatisfaction

        i = 0
        j = minutes
        while(j<len(customers)):
            bonusSatisfaction += customers[j] * grumpy[j]  # New element in the window
            bonusSatisfaction -= customers[i] * grumpy[i]  # Rwmove/Slide first element in the window

            maxBonus = max(maxBonus, bonusSatisfaction)
 
            i += 1
            j += 1
        return idealSatisfaction + maxBonus            
                

        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        
