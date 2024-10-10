class Solution(object):
    def minSwaps(self, s):
        openingCount, closingCount = 0, 0
        l = 0
        r = len(s) - 1
        swapCount = 0
        while(l < r):
            if s[l] == '[':
                openingCount += 1 
                l += 1
            else:
                if closingCount < openingCount:
                    l += 1
                    closingCount += 1
                else:
                    while(s[r] != "["):
                        r -= 1
                    swapCount += 1
                    l += 1
                    r -= 1
                    openingCount += 1
        return swapCount


        """
        :type s: str
        :rtype: int
        """
