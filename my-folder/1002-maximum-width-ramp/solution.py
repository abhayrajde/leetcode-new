class Solution(object):
    def maxWidthRamp(self, nums):
        maxRightList = [nums[-1]] 
        for i in range(len(nums)-2, -1, -1):
            maxRightList.insert(0, max(nums[i], maxRightList[0]))
        
        # [8,8,8,5,5,5]
        l = 0
        r = 0
        res = 0
        while (r < len(nums)):
            if(l == r):
                r += 1
            else:
                if(nums[l] > maxRightList[r]):
                    l += 1
                else:
                    res = max(res, r-l)
                    r += 1
        return res



            
        """
        :type nums: List[int]
        :rtype: int
        """
        
