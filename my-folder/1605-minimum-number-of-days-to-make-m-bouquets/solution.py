# Striver Youtube Link: https://www.youtube.com/watch?v=TXAuxeYBTdg&t=1187s
class Solution(object):
    def minDays(self, bloomDay, m, k):
        def possibility(day):
            count = 0 
            noOfBoquets = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    noOfBoquets += (count/k)
                    count = 0
            noOfBoquets += (count/k)
            if(noOfBoquets >= m):
                return True
            else:
                return False

        # Base Case
        # Return -1 if m * k < len(bloomDay)
        if(m * k > len(bloomDay)):
            return -1
        left = min(bloomDay)
        right = ans = max(bloomDay)
        while(left <= right):
            mid = (left + right) // 2
            if (possibility(mid)):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
                


        

        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        
