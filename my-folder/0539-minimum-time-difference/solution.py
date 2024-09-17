class Solution(object):
    def findMinDifference(self, timePoints):
        timePoints = sorted(timePoints)
        result = float('inf')
        # sortedTimePoints.append(timePoints[0])
        for i in range(len(timePoints)-1):
            a = timePoints[i]
            b = timePoints[i+1]
            # if (i == len(timePoints) - 1):
            #     a,b = b,a
            #Edge Case
            if(i == 0):
                c = timePoints[-1]
                hrdiff = int(c[:2]) - int(a[:2])
                mindiff = int(c[3:]) - int(a[3:])
                totdiff = (hrdiff * 60) + mindiff
                edgeCaseVal = 1440 - totdiff
                result = min(result,edgeCaseVal)
            hrdiff = int(b[:2]) - int(a[:2])
            mindiff = int(b[3:]) - int(a[3:])
            totdiff = (hrdiff * 60) + mindiff
            result = min(result, totdiff)
        return result
            
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
