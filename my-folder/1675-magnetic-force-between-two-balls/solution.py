#https://www.youtube.com/watch?v=CSXkcvH8V-c
class Solution(object):
    def maxDistance(self, position, m):
        def isPossible(gap, m):
            prev = position[0]
            countBalls = 1
            for i in range(1,len(position)):
                curr = position[i]

                if(abs(curr - prev) >= gap):
                    countBalls += 1
                    prev = curr
                
                if(countBalls == m):
                    break

            return countBalls == m

        position = sorted(position)
        left = 0
        right = position[-1]
        #mid = (left + right) // 2
        ans = 0

        while (left <= right):
            mid = (left + right) // 2

            if(isPossible(mid,m)):
                ans = max(ans, mid)
                left = mid + 1
            
            else:
                right = mid - 1

        return ans
        
            
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        
