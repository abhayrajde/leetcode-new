class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        lastPeakIndex = len(heights) - 1
        output = [lastPeakIndex]
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            if h > heights[lastPeakIndex]:
                lastPeakIndex = i
                output.append(i)
        
        return output[::-1]

